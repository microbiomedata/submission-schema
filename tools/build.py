"""Main build script for the final submission-schema YAML file."""

from contextlib import contextmanager
from importlib import metadata
from pathlib import Path

import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from rich.console import Console

from nmdc_submission_schema.schematools import import_elements
from nmdc_submission_schema.schematools.importer import ImporterConfig
from nmdc_submission_schema.scripts import nmdc_schema_yaml_path

PROJECT_ROOT = Path(__file__).parent.parent

SCHEMA_DIRECTORY = PROJECT_ROOT / "src/nmdc_submission_schema/schema"
SUBMISSION_SCHEMA_BASE = SCHEMA_DIRECTORY / "nmdc_submission_schema_base.yaml"
SUBMISSION_SCHEMA_OUTPUT = SCHEMA_DIRECTORY / "nmdc_submission_schema.yaml"

CONFIG_DIRECTORY = PROJECT_ROOT / "config"
NMDC_SCHEMA_IMPORT_CONFIG = CONFIG_DIRECTORY / "nmdc_schema_import.yaml"

console = Console(highlight=False)


@contextmanager
def log(message: str):
    """Context manager for logging a status that stays in the console."""
    with console.status(message):
        yield
    console.print(message)


def project_rel(path: Path) -> Path:
    """Return a path relative to the project root"""
    return path.relative_to(PROJECT_ROOT)


def main() -> None:
    with log(
        f"Loading submission-schema base from [bold]{project_rel(SUBMISSION_SCHEMA_BASE)}"
    ):
        submission_schema = SchemaView(SUBMISSION_SCHEMA_BASE)

    with log(f"Loading nmdc-schema version [bold]{metadata.version('nmdc_schema')}"):
        nmdc_schema = SchemaView(nmdc_schema_yaml_path)

    with log(
        f"Loading nmdc-schema import config from [bold]{project_rel(NMDC_SCHEMA_IMPORT_CONFIG)}"
    ):
        with open(NMDC_SCHEMA_IMPORT_CONFIG) as config_file:
            config_dict = yaml.safe_load(config_file)
        nmdc_schema_import_config = ImporterConfig.model_validate(config_dict)

    with log("Importing elements from nmdc-schema into submission-schema"):
        import_elements(
            source_schema=nmdc_schema,
            target_schema=submission_schema,
            config=nmdc_schema_import_config,
        )

    with log(
        f"Writing final submission-schema to [bold]{project_rel(SUBMISSION_SCHEMA_OUTPUT)}"
    ):
        yaml_dumper.dump(submission_schema.schema, SUBMISSION_SCHEMA_OUTPUT)

    console.print("Done", style="green")


if __name__ == "__main__":
    main()
