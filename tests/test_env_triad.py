from pprint import pprint

import pytest
from pathlib import Path
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import PermissibleValue
from src.nmdc_submission_schema.scripts.generate_env_triad_enums import parse_tsv_to_dict, inject_terms_into_schema, main  # Replace 'your_module' with your script filename


repo_root = Path(__file__).resolve().parent.parent

# Define the paths to the test input files
SOIL_ENV_LOCAL_PATH = repo_root / "tests/inputs/soil_env_local_test.tsv"
SOIL_ENV_MEDIUM_PATH = repo_root / "tests/inputs/soil_env_medium_test.tsv"
SOIL_ENV_BROAD_PATH = repo_root / "tests/inputs/soil_env_broad_test.tsv"
BASE_SCHEMA_PATH = repo_root / "tests/inputs/base_schema.yaml"
OUTPUT_SCHEMA_PATH = repo_root / "tests/inputs/output_schema.yaml"  # Location for output schema


@pytest.fixture
def sample_schema_view():
    # Create a SchemaView instance from the base schema file
    return SchemaView(str(BASE_SCHEMA_PATH))


def test_parse_tsv_to_dict():
    # Test parsing of a sample TSV file
    parsed_data = parse_tsv_to_dict(SOIL_ENV_LOCAL_PATH)
    expected_data = [
        {"term_id": "ENVO:00000077", "term_name": "agricultural soil"},
        {"term_id": "ENVO:00000170", "term_name": "dune soil"},
        {"term_id": "ENVO:00000111", "term_name": "forest soil"}
        # Add more expected terms if they are present in the actual file
    ]
    assert parsed_data == expected_data, "Parsed data does not match expected data"


def test_inject_terms_into_schema(sample_schema_view):
    # Inject terms into the schema with a specific enum name
    enum_name = "TestEnum"
    updated_schema = inject_terms_into_schema(SOIL_ENV_LOCAL_PATH, enum_name, sample_schema_view)

    # Check if the enumeration was added
    assert enum_name in updated_schema.enums, f"Enum '{enum_name}' not found in schema"

    # Verify the permissible values
    enum_def = updated_schema.enums[enum_name]
    expected_pvs = ["agricultural soil [ENVO:00000077]", "dune soil [ENVO:00000170]", "forest soil [ENVO:00000111]"]
    for pv in expected_pvs:
        assert pv in enum_def.permissible_values.keys()


def test_main(tmp_path):
    # Define paths to the TSV files and expected enums

    file_enum_mappings = [
        (SOIL_ENV_LOCAL_PATH, "EnvLocalScaleSoilEnum"),
        (SOIL_ENV_MEDIUM_PATH, "EnvMediumScaleSoilEnum"),
        (SOIL_ENV_BROAD_PATH, "EnvBroadScaleSoilEnum")
    ]

    # Run `main` with real file paths
    for tsv_path, enum_name in file_enum_mappings:
        main(enum_name, tsv_path, BASE_SCHEMA_PATH, BASE_SCHEMA_PATH)

    # Verify that the output schema file contains the injected enums with the correct permissible values
    output_schema_view = SchemaView(str(BASE_SCHEMA_PATH))

    # Check that each enum exists with expected permissible values
    for tsv_path, enum_name in file_enum_mappings:
        assert enum_name in output_schema_view.schema.enums, f"Enum '{enum_name}' not found in output schema"

        # Load and check permissible values
        expected_data = parse_tsv_to_dict(tsv_path)
        sorted_data = sorted(expected_data, key=lambda x: x["term_name"])
        expected_pvs = [PermissibleValue(text=f"{term['term_name']} [{term['term_id']}]") for term in sorted_data]

        enum_def = output_schema_view.schema.enums[enum_name]
        assert list(enum_def.permissible_values.values()) == expected_pvs, f"Permissible values for '{enum_name}' do not match expected data"
