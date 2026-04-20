"""
Audit every Env(BroadScale|LocalScale|Medium)*Enum defined in the
submission-schema YAML against the expected OBO ancestry:

  - env_broad_scale permissible values should be is_a descendants of
    ENVO:00000428 (biome).
  - env_medium permissible values should be is_a descendants of
    ENVO:00010483 (environmental material), except where policy allows
    PO/UBERON for host- or plant-associated samples.
  - env_local_scale has no single expected parent; values are reported
    but not checked for ancestry membership here.

Ancestry is computed by $graphLookup over `rdfs:subClassOf` edges in the
local mirror of the NMDC runtime ontology (collections:
`ontology_class_set`, `ontology_relation_set`).

Outputs two sections:
  1. Per-enum counts: terms, missing-from-mirror, is_biome, is_env_mat.
  2. For every Env(BroadScale|Medium)*Enum, lists any terms that fail
     the expected-ancestor check (so you can propose removals or argue
     for them).

Run from the submission-schema repo root or with REPO_ROOT env set:

    python tools/env-triad-audit/audit_enums.py

Dependencies:
  - Python 3.9+
  - mongosh on PATH, connected to a mongod holding the NMDC runtime
    ontology collections (defaults to the `nmdc` db on localhost).

Override the mongo connection with MONGO_URI and/or MONGO_DB:

    MONGO_URI='mongodb://host:27017' MONGO_DB=nmdc python tools/env-triad-audit/audit_enums.py
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

BIOME_ID = "ENVO:00000428"
ENV_MATERIAL_ID = "ENVO:00010483"

REPO_ROOT = Path(os.environ.get("REPO_ROOT") or Path(__file__).resolve().parents[2])
SCHEMA_PATH = REPO_ROOT / "src" / "nmdc_submission_schema" / "schema" / "nmdc_submission_schema.yaml"

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.environ.get("MONGO_DB", "nmdc")


def extract_enum_ids() -> dict[str, list[str]]:
    txt = SCHEMA_PATH.read_text()
    enum_names = re.findall(
        r"^  (Env(?:BroadScale|LocalScale|Medium)\w+Enum):", txt, re.MULTILINE
    )
    out: dict[str, list[str]] = {}
    for name in enum_names:
        block_re = re.compile(
            rf"^  {name}:\n(.*?)(?=^  [A-Z]\w+(?:Enum|Interface|Mixin):|\Z)",
            re.DOTALL | re.MULTILINE,
        )
        m = block_re.search(txt)
        block = m.group(1) if m else ""
        ids = sorted(set(re.findall(r"\[([A-Z][A-Z_]*:\d+)\]", block)))
        out[name] = ids
    return out


def resolve_ancestry(all_ids: list[str]) -> dict[str, dict]:
    """Use mongosh to compute pure-is_a ancestors for each id, via $graphLookup
    over `rdfs:subClassOf` edges. Returns {id: {name, is_biome, is_env_mat}} or
    {missing: True} if the id isn't in ontology_class_set."""

    js = f"""
const targets = {json.dumps(all_ids)};
const BIOME = {json.dumps(BIOME_ID)};
const ENV_MAT = {json.dumps(ENV_MATERIAL_ID)};
const results = {{}};
for (const id of targets) {{
  const r = db.ontology_class_set.aggregate([
    {{ $match: {{ id }} }},
    {{ $graphLookup: {{
        from: 'ontology_relation_set',
        startWith: '$id',
        connectFromField: 'object',
        connectToField: 'subject',
        as: 'anc',
        restrictSearchWithMatch: {{ predicate: 'rdfs:subClassOf' }},
        maxDepth: 25
    }} }},
    {{ $project: {{ anc: '$anc.object', name: '$name' }} }}
  ]).toArray();
  if (r.length === 0) {{ results[id] = {{ missing: true }}; continue; }}
  const anc = r[0].anc || [];
  results[id] = {{
    name: r[0].name,
    is_biome: anc.includes(BIOME) || id === BIOME,
    is_env_mat: anc.includes(ENV_MAT) || id === ENV_MAT
  }};
}}
print(JSON.stringify(results));
"""
    proc = subprocess.run(
        ["mongosh", MONGO_URI, "--quiet", MONGO_DB, "--eval", js],
        capture_output=True,
        text=True,
        check=True,
    )
    # mongosh can emit connection banners even with --quiet; isolate the JSON blob.
    out = proc.stdout.strip().splitlines()
    for line in reversed(out):
        if line.startswith("{"):
            return json.loads(line)
    raise RuntimeError(f"Could not parse mongosh output:\n{proc.stdout}\n---\n{proc.stderr}")


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"Schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 1

    enum_ids = extract_enum_ids()
    all_ids = sorted({i for v in enum_ids.values() for i in v})
    ancestry = resolve_ancestry(all_ids)

    print(
        f"{'enum':<42} {'terms':>5} {'missing':>7} {'is_biome':>9} {'is_env_mat':>10}"
    )
    print("-" * 80)
    for name, ids in enum_ids.items():
        missing = sum(1 for i in ids if ancestry.get(i, {}).get("missing"))
        n_biome = sum(1 for i in ids if ancestry.get(i, {}).get("is_biome"))
        n_em = sum(1 for i in ids if ancestry.get(i, {}).get("is_env_mat"))
        print(f"{name:<42} {len(ids):>5} {missing:>7} {n_biome:>9} {n_em:>10}")

    print("\n--- NON-biome members of every EnvBroadScale*Enum ---")
    for name, ids in enum_ids.items():
        if "BroadScale" not in name:
            continue
        non_biome = [
            i
            for i in ids
            if not ancestry.get(i, {}).get("is_biome")
            and not ancestry.get(i, {}).get("missing")
        ]
        if non_biome:
            print(f"\n{name}:")
            for i in non_biome:
                print(f"  {i}  {ancestry[i]['name']}")

    print("\n--- NON-env-material members of every EnvMedium*Enum ---")
    for name, ids in enum_ids.items():
        if "Medium" not in name:
            continue
        non_em = [
            i
            for i in ids
            if not ancestry.get(i, {}).get("is_env_mat")
            and not ancestry.get(i, {}).get("missing")
        ]
        if non_em:
            print(f"\n{name}:")
            for i in non_em:
                print(f"  {i}  {ancestry[i]['name']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
