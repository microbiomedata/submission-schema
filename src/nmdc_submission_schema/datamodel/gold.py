import json
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import Dict, Set, Iterable, Optional

import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue, SchemaDefinition
from linkml_runtime.loaders import yaml_loader


class PathwayLevel(Enum):
    ecosystem = 'Ecosystem'
    ecosystem_category = 'EcosystemCategory'
    ecosystem_type = 'EcosystemType'
    ecosystem_subtype = 'EcosystemSubtype'
    specific_ecosystem = 'SpecificEcosystem'


class GoldTermSet:

    def __init__(self, *, schema_enum_suffix: str = '', include: Optional[Dict[PathwayLevel, Iterable[str]]] = None):
        self.schema_enum_suffix: str = schema_enum_suffix
        self.terms: Dict[PathwayLevel, Set[str]] = defaultdict(set)
        self.include: Dict[PathwayLevel, Iterable[str]] = include if include is not None else {}


def inject_gold_pathway_terms(gold_ecosystem_tree_path: Path, input_schema_path: SchemaDefinition) -> SchemaDefinition:
    """Inject gold pathway terms into the schema."""
    with open(gold_ecosystem_tree_path) as f:
        gold_ecosystem_tree = json.load(f)

    levels = list(PathwayLevel)
    all_terms = GoldTermSet()
    soil_terms = GoldTermSet(schema_enum_suffix='ForSoil', include={
        PathwayLevel.ecosystem: ['Environmental'],
        PathwayLevel.ecosystem_category: ['Terrestrial'],
        PathwayLevel.ecosystem_type: ['Soil'],
    })
    term_sets = [all_terms, soil_terms]

    def _add_term(term_set, term, level_index):
        level = levels[level_index]
        if term_set.include.get(level) and term['name'] not in term_set.include[level]:
            return
        term_set.terms[level].add(term['name'])
        for child in term.get('children', []):
            _add_term(term_set, child, level_index + 1)

    for term_set in term_sets:
        for ecosystem in gold_ecosystem_tree['children']:
            _add_term(term_set, ecosystem, level_index=0)

    schemaview = SchemaView(input_schema_path)

    for term_set in term_sets:
        for level in levels:
            pvs = [PermissibleValue(text=term) for term in sorted(term_set.terms[level])]
            schemaview.add_enum(EnumDefinition(
                name=level.value + term_set.schema_enum_suffix + 'Enum',
                permissible_values=pvs
            ))

    return schemaview.schema

@click.command()
@click.option('--gold-ecosystem-tree-path', '-g', type=click.Path(exists=True),
              help='Path to the gold ecosystem tree.')
@click.option('--input-file', '-i', type=click.File('r'), default="-")
@click.option('--output-file', '-o', type=click.File('w'), default="-")
def main(gold_ecosystem_tree_path, input_file, output_file):
    schema = yaml_loader.loads(input_file.read(), SchemaDefinition)
    output = inject_gold_pathway_terms(Path(gold_ecosystem_tree_path), schema)
    print(yaml_dumper.dumps(output), file=output_file)
