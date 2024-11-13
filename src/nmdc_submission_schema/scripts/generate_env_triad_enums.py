from pathlib import Path
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import EnumDefinition, EnumDefinitionName, PermissibleValue, SchemaDefinition
import csv
import click

repo_root = Path(__file__).resolve().parent.parent.parent.parent

# Paths to the source and target schema files
SOURCE_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"
TARGET_SCHEMA_YAML_PATH = repo_root / "src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"

SOIL_ENV_LOCAL_PATH = "post_google_sheets_soil_env_local_scale.tsv"
SOIL_ENV_MEDIUM_PATH = "post_google_sheets_soil_env_medium.tsv"
SOIL_ENV_BROAD_PATH = "post_google_sheets_soil_env_broad_scale.tsv"
WATER_ENV_LOCAL_PATH = "post_google_sheets_water_env_local_scale.tsv"
WATER_ENV_MEDIUM_PATH = "post_google_sheets_water_env_medium.tsv"
WATER_ENV_BROAD_PATH = "post_google_sheets_water_env_broad_scale.tsv"
SEDIMENT_ENV_LOCAL_PATH = "post_google_sheets_sediment_env_local_scale.tsv"
SEDIMENT_ENV_MEDIUM_PATH = "post_google_sheets_sediment_env_medium.tsv"
SEDIMENT_ENV_BROAD_PATH = "post_google_sheets_sediment_env_broad_scale.tsv"
PLANT_ASSOCIATED_ENV_LOCAL_PATH = "post_google_sheets_plant_associated_env_local_scale.tsv"
PLANT_ASSOCIATED_ENV_MEDIUM_PATH = "post_google_sheets_plant_associated_env_medium.tsv"
PLANT_ASSOCIATED__ENV_BROAD_PATH = "post_google_sheets_plant_associated_env_broad_scale.tsv"

enum_file_mappings = {
    SOIL_ENV_LOCAL_PATH: "EnvLocalScaleSoilEnum",
    SOIL_ENV_MEDIUM_PATH: "EnvMediumSoilEnum",
    SOIL_ENV_BROAD_PATH: "EnvBroadScaleSoilEnum",
    WATER_ENV_LOCAL_PATH: "EnvLocalScaleWaterEnum",
    WATER_ENV_MEDIUM_PATH: "EnvMediumWaterEnum",
    WATER_ENV_BROAD_PATH: "EnvBroadScaleWaterEnum",
    SEDIMENT_ENV_LOCAL_PATH: "EnvLocalScaleSedimentEnum",
    SEDIMENT_ENV_MEDIUM_PATH: "EnvMediumSedimentEnum",
    SEDIMENT_ENV_BROAD_PATH: "EnvBroadScaleSedimentEnum",
    PLANT_ASSOCIATED_ENV_LOCAL_PATH: "EnvLocalScalePlantAssociatedEnum",
    PLANT_ASSOCIATED_ENV_MEDIUM_PATH: "EnvMediumPlantAssociatedEnum",
    PLANT_ASSOCIATED__ENV_BROAD_PATH: "EnvBroadScalePlantAssociatedEnum"
}


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


def ingest(values_file_path: Path,
           source_schema_yaml_path: Path = SOURCE_SCHEMA_YAML_PATH,
           target_schema_yaml_path: Path = TARGET_SCHEMA_YAML_PATH,
           enum_name: str = None) -> None:
    """
    Inject terms from multiple TSV files into the schema, each under a specified enumeration name.

    :param values_file_path: Path to the TSV file containing the terms to replace the Enum PVs with
    :param source_schema_yaml_path: Path to the source schema YAML file.
    :param target_schema_yaml_path: Path to the target schema YAML file.
    :param enum_name: Dictionary mapping TSV file paths to enumeration names.
    """
    # Define files and corresponding enumeration names

    if enum_name is None:
        enum_name = enum_file_mappings.get(values_file_path.name)
    if enum_name is None:
        raise ValueError(f"Enumeration name not found for file: {values_file_path.name}")

    sv = SchemaView(source_schema_yaml_path)
    # Load, inject terms, and save the updated schema for each file
    schema = inject_terms_into_schema(values_file_path,
                                      enum_name,
                                      sv)

    # Dump the updated schema to the specified output file
    with target_schema_yaml_path.open("w", encoding="utf-8") as file:
        file.write(yaml_dumper.dumps(schema))


@click.command()
@click.option("-f", "--values-file-path",
              type=click.Path(path_type=Path), required=True,
              help="Path to the TSV file containing the terms to replace the Enum PVs with.")
@click.option("-i", "--source-schema-yaml-path",
              type=click.Path(exists=True, path_type=Path),
              default=SOURCE_SCHEMA_YAML_PATH,
              help="Path to the source schema YAML file.")
@click.option("-o", "--target-schema-yaml-path",
              type=click.Path(path_type=Path),
              default=TARGET_SCHEMA_YAML_PATH,
              help="Path to the target schema YAML file.")
def main(values_file_path, source_schema_yaml_path, target_schema_yaml_path):
    """CLI to inject terms from a TSV file into the schema."""

    # Check if the required files exist
    if not values_file_path.exists():
        click.echo(f"Warning: Values file '{values_file_path}' not implemented yet.")
        return

    ingest(values_file_path, source_schema_yaml_path, target_schema_yaml_path)

if __name__ == "__main__":
    main()
