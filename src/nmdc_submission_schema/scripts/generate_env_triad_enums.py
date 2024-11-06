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
import csv


def parse_tsv_to_dict(file_path):
    """
    Parse a TSV file into a dictionary.
    Assumes the first column is the key, and the rest are values.

    :param file_path: Path to the TSV file.
    :return: Dictionary with the first column as keys and rows as values.
    """
    data_dict = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row:
                # Use the first column as the key and the rest as values
                key = row[0]
                values = row[1:] if len(row) > 1 else []
                data_dict[key] = values

    return data_dict


def inject_env_local_scale_terms (env_local_path: Path, input_schema_path: SchemaDefinition) -> SchemaDefinition:
    """Inject gold pathway terms into the schema."""
    data = parse_tsv_to_dict(env_local_path)
    print(data)
    schemaview = SchemaView(input_schema_path)

    for term in data:
        pvs = [PermissibleValue(text=term_id) for term in data]
        schemaview.add_enum(EnumDefinition(
            name='EnvironmentalTriadLocalEnum',
            permissible_values=pvs
        ))

    return schemaview.schema

@click.command()
@click.option('--env-local-file', '-g', type=click.Path(exists=True))
@click.option('--schema-input-file', '-i', type=click.File('r'), default="-")
@click.option('--schema-output-file', '-o', type=click.File('w'), default="-")
def main(env_local_file, input_file, output_file):
    schema = yaml_loader.loads(input_file.read(), SchemaDefinition)
    output = inject_env_local_scale_terms(Path(env_local_file), schema)
    print(yaml_dumper.dumps(output), file=output_file)
