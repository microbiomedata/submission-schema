from pathlib import Path
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import EnumDefinition, EnumDefinitionName, PermissibleValue, SchemaDefinition
import csv

repo_root = Path(__file__).resolve().parent.parent.parent.parent

# Paths to the source and target schema files
SOURCE_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"
TARGET_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"

# Paths to the TSV files
SOIL_ENV_LOCAL_PATH = repo_root / "notebooks/post_google_sheets_soil_env_local_scale.tsv"
SOIL_ENV_MEDIUM_PATH = repo_root / "notebooks/post_google_sheets_soil_env_medium_scale.tsv"
SOIL_ENV_BROAD_PATH = repo_root / "notebooks/post_google_sheets_soil_env_broad_scale.tsv"


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


def inject_terms_into_schema(env_path: Path, enum_name: str, sv: SchemaView) -> SchemaDefinition:
    """
    Inject terms from a TSV file into the schema under a specified enumeration name.

    :param env_path: Path to the TSV file containing the terms to inject.
    :param schema_yaml_path: Path to the schema YAML file to inject the terms into.
    :param enum_name: Name of the enumeration to add or update in the schema.
    :param sv: SchemaView object representing the schema.
    :return: The updated schema.
    """
    data = parse_tsv_to_dict(env_path)
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


def main():
    """
    Inject terms from multiple TSV files into the schema, each under a specified enumeration name.
    """
    # Define files and corresponding enumeration names
    file_enum_mappings = [
        (SOIL_ENV_LOCAL_PATH, "EnvLocalScaleSoilEnum"),
        (SOIL_ENV_MEDIUM_PATH, "EnvMediumScaleSoilEnum"),
        (SOIL_ENV_BROAD_PATH, "EnvBroadScaleSoilEnum")
    ]
    schemaview = SchemaView(SOURCE_SCHEMA_YAML_PATH)
    # Load, inject terms, and save the updated schema for each file
    schema = None
    for env_path, enum_name in file_enum_mappings:
        schema = inject_terms_into_schema(env_path, enum_name, schemaview)

    # Dump the updated schema to the specified output file
    with TARGET_SCHEMA_YAML_PATH.open("w", encoding="utf-8") as file:
        file.write(yaml_dumper.dumps(schema))


if __name__ == "__main__":
    main()
