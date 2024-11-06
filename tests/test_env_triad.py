import pytest
from pathlib import Path
from click.testing import CliRunner
from src.nmdc_submission_schema.scripts.generate_env_triad_enums import main
from linkml_runtime.loaders import yaml_loader

SCHEMA_YAML_PATH = Path(__file__).parent / "../src/nmdc_submission_schema/schema/nmdc_submission_schema_base.yaml"

def test_inject_env_local_scale_terms_cli():
    runner = CliRunner()

    # Run the CLI command with the --env-local-file, --schema-input-file, and --schema-output-file options
    result = runner.invoke(
        main,
        [
            "--env-local-file", str("/Users/SMoxon/Documents/src/submission-schema/tests/input/env_local_input_examlpe.tsv"),
            "--schema-input-file", str("/Users/SMoxon/Documents/src/submission-schema/src/nmdc_submission_schema/schema/nmdc_submission_schema_base.yaml"),
            "--schema-output-file", str("/Users/SMoxon/Documents/src/submission-schema/src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml")
        ]
    )

    output_file = tmp_path / "output_schema.yaml"

    # Check that the command completed successfully
    assert result.exit_code == 0, f"CLI command failed with error: {result.output}"

    output_schema = yaml_loader.load(output_file, SchemaDefinition)

    # Verify the enum was added to the schema
    assert 'EnvironmentalTriadLocalEnum' in output_schema.enums
    enum_def = output_schema.enums['EnvironmentalTriadLocalEnum']

    # Check permissible values
    expected_terms = ["TERM1", "TERM2", "TERM3"]
    actual_terms = [pv.text for pv in enum_def.permissible_values]

    assert set(expected_terms) == set(actual_terms), "Permissible values do not match expected terms"
