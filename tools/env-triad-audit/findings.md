# Environmental-triad enum audit — findings

Audit captured against `submission-schema` branch `tools/env-triad-audit` (from `main` at the time of writing) using `audit_enums.py`. Biosample counts come from a local mirror of the NMDC runtime mongo.

## Expected policy

- `env_broad_scale` values come from the EnvO `biome` (`ENVO:00000428`) hierarchy, especially for samples not tightly associated with a host.
- `env_medium` values come from the EnvO `environmental material` (`ENVO:00010483`) hierarchy.
- For host- or plant-associated samples, some PO and UBERON terms are allowed in `env_medium`.
- For host-associated `env_broad_scale`, some "organism-associated" ENVO classes were expected to be allowed — this was **never encoded** in the schema (see Finding 1).

## Enum coverage

Only 4 of 17 DH interfaces have dedicated per-package env-triad enums:

| Interface | Has env-triad enums? |
|---|---|
| Water, Soil, Sediment, PlantAssociated | ✅ all three slots |
| Air, Biofilm, BuiltEnv, Emsl, HcrCores, HcrFluidsSwabs, **HostAssociated**, JgiMg/MgLr/Mt, MiscEnvs, WastewaterSludge | ❌ none |

## Audit output (per-enum)

```
enum                                       terms missing  is_biome is_env_mat
--------------------------------------------------------------------------------
EnvBroadScaleWaterEnum                        56       0        56          0
EnvLocalScaleWaterEnum                        86       2         0          0
EnvMediumWaterEnum                            96       1         0         95
EnvBroadScaleSoilEnum                         52       0        52          0
EnvLocalScaleSoilEnum                         83       0         0          0
EnvMediumSoilEnum                             85       0         0         85
EnvBroadScaleSedimentEnum                     15       0        15          0
EnvLocalScaleSedimentEnum                     53       0         0          0
EnvMediumSedimentEnum                         11       0         0         11
EnvBroadScalePlantAssociatedEnum              72       0        72          0
EnvLocalScalePlantAssociatedEnum              62       0         0          0
EnvMediumPlantAssociatedEnum                  45       3         4          4
```

`missing` means the CURIE isn't in the local mongo mirror of `ontology_class_set`; usually indicates a recently-added term or a prefix not loaded (e.g., CHEBI, EFO, DOID, PATO, EO, GENEPIO terms).

## Finding 1 — HostAssociated has no env-triad enums

`HostAssociatedInterface` (schema lines 23398-23949) has slot_usage for `env_broad_scale`, `env_local_scale`, `env_medium` but:

- `env_broad_scale`: **no override, no enum, no pattern** — anything goes.
- `env_local_scale`: pattern `^\S+.*\S+ \[ENVO:\d{7,8}\]$` only — ENVO-only, no UBERON/PO.
- `env_medium`: same ENVO-only pattern.

The 61 Host-associated biosamples currently storing `ENVO:01001002` "animal-associated environment" as `env_broad_scale` passed validation by omission, not by design. Host-associated samples also have no PO/UBERON permission in `env_medium` despite the tooltip on the general `env_broad_scale` slot saying UBERON/PO should be used there for anatomical context.

**Proposed fix**: add `EnvBroadScaleHostAssociatedEnum`, `EnvLocalScaleHostAssociatedEnum`, `EnvMediumHostAssociatedEnum` with an explicit enumeration of allowed values (ENVO "X-associated environment" classes for broad_scale; PO/UBERON-heavy for medium).

## Finding 2 — `EnvMediumPlantAssociatedEnum` contains 9 questionable ENVO terms

Expected: PO + UBERON + a few ENVO environmental-material terms. Actual: includes the class `biome` itself, one obsolete term, three ocean biomes, and several vegetation-layer concepts that are not environmental materials.

| CURIE | Label | Why it's questionable |
|---|---|---|
| `ENVO:00000428` | **biome** | The abstract class, listed as if it were a permissible value |
| `ENVO:00000047` | **obsolete canopy** | OBSOLETE term |
| `ENVO:00005801` | rhizosphere | Astronomical body part, not environmental material |
| `ENVO:01000033` | oceanic pelagic zone biome | Biome (not material), irrelevant to plants |
| `ENVO:01000035` | oceanic epipelagic zone biome | Same |
| `ENVO:01000228` | tropical moist broadleaf forest biome | Same |
| `ENVO:01000335` | understory | Layer concept |
| `ENVO:01000336` | shrub layer | Layer concept |
| `ENVO:01000337` | herb and fern layer | Layer concept |

**Proposed fix**: remove these 9 terms, add any legitimate environmental-material ENVO terms that plant-associated samples actually need, keep the PO + UBERON set.

## Finding 3 — `any_of: [enum, string]` string fallback defeats enum enforcement

Every `env_broad_scale` slot_usage on the existing interfaces declares `any_of: [EnvBroadScale<Package>Enum, string]`. The `string` branch makes the enum advisory — any value matching the CURIE pattern passes.

Evidence in biosample data:

| env_package | n | env_broad_scale term | is_a descendant of biome? | In any `EnvBroadScale*Enum`? |
|---|---:|---|---|---|
| Host-associated | 61 | `ENVO:01001002` animal-associated environment | No (not even via combined isa/partof) | No |
| plant-associated | 192 | `ENVO:01001442` agriculture *(stored as "agricultural biome" — label drift, see Finding 4)* | No | No |
| plant-associated | 76 | `ENVO:01001001` plant-associated environment | No | No |
| plant-associated | 16 | `ENVO:01000245` cropland biome | Yes | Yes |

**329 of 345** host/plant-associated biosamples use broad_scale values that are neither biomes nor in any per-package enum. They pass via the string fallback.

**Proposed fix** (policy question, not a simple patch): either broaden the enums to explicitly include the "organism-associated environment" ENVO classes users are actually choosing, or remove the `string` fallback and enforce the enum. Mixing the two leaves users without guardrails and leaves downstream consumers unable to rely on the enum as ground truth.

## Finding 4 — Label drift (cross-cutting, not submission-schema's bug)

`ENVO:01001442` is labeled `agriculture` in `ontology_class_set`, but 192 biosamples store `env_broad_scale.term.name` as `"agricultural biome"`. Biosample ingestion does not re-sync term labels against the current ontology mirror.

**Filed separately against the runtime/ingestion repo.**

## Running this audit

```bash
# from submission-schema repo root
python tools/env-triad-audit/audit_enums.py

# point at a remote mongo (must have ontology_class_set + ontology_relation_set)
MONGO_URI='mongodb://host:27017' python tools/env-triad-audit/audit_enums.py
```
