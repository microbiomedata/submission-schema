from pathlib import Path
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import EnumDefinition, EnumDefinitionName, PermissibleValue, SchemaDefinition
import csv

repo_root = Path(__file__).resolve().parent.parent.parent.parent

# Paths to the source and target schema files
SOURCE_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"
TARGET_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"


def parse_tsv_to_dict(file_path):
    """
    Parse a TSV file into a list of dictionaries representing each row in the file.

    :param file_path: Path to the TSV file to parse.
    :return: A list of dictionaries representing each row in the file.
    """
    data_dict = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader, None)  # Skip the header
        for row in reader:
            if row:
                data_dict.append({"term_id": row[0], "term_name": row[1]})

    return data_dict

def inject_terms_into_schema(values_file_path: Path,
                             enum_name: str,
                             sv: SchemaView) -> SchemaDefinition:
    """
    Inject terms from a TSV file into the schema under a specified enumeration name.

    :param values_file_path: Path to the TSV file containing the terms to inject.
    :param enum_name: Name of the enumeration to add or update in the schema.
    :param sv: SchemaView object representing the schema.
    :return: The updated schema.
    """
    data = parse_tsv_to_dict(values_file_path)
    sorted_data = sorted(data, key=lambda x: x["term_name"])

    pvs = [PermissibleValue(text=f"{term['term_name']} [{term['term_id']}]") for term in sorted_data]

    enum_def = EnumDefinition(
        name=enum_name,
        permissible_values=pvs
    )

    # Check if the enum already exists; if so, delete it before adding the new one
    if sv.schema.enums.get(enum_name):
        sv.delete_enum(EnumDefinitionName(enum_name))

    sv.add_enum(enum_def)
    return sv.schema


def ingest(enum_name: str,
           values_file_path: Path,
           source_schema_yaml_path: Path = SOURCE_SCHEMA_YAML_PATH,
           target_schema_yaml_path: Path = TARGET_SCHEMA_YAML_PATH) -> None:
    """
    Inject terms from multiple TSV files into the schema, each under a specified enumeration name.

    :param enum_name : Name of the enumeration to add or update in the schema.
    :param values_file_path: Path to the TSV file containing the terms to replace the Enum PVs with
    :param source_schema_yaml_path: Path to the source schema YAML file.
    :param target_schema_yaml_path: Path to the target schema YAML file.
    """
    # Define files and corresponding enumeration names

    sv = SchemaView(source_schema_yaml_path)
    # Load, inject terms, and save the updated schema for each file
    schema = inject_terms_into_schema(values_file_path,
                                      enum_name,
                                      sv)

    # Dump the updated schema to the specified output file
    with target_schema_yaml_path.open("w", encoding="utf-8") as file:
        file.write(yaml_dumper.dumps(schema))

