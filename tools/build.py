"""Main build script for the final submission-schema YAML file."""

import json
from collections.abc import Callable, Iterable
from contextlib import contextmanager
from importlib import metadata
from pathlib import Path

import click
import requests
import yaml
from enums import inject_env_triad_enum, inject_illumina_instrument_model_enum
from gold import inject_gold_pathway_terms
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SlotDefinition
from mixs import translate_string_serializations
from rich.console import Console

from nmdc_submission_schema.schematools import (
    import_elements,
    merge_prefixes,
    remove_class,
)
from nmdc_submission_schema.schematools.importer import ImporterConfig
from nmdc_submission_schema.scripts import nmdc_schema_yaml_path

ROOT = Path(__file__).parent.parent

SCHEMA_DIRECTORY = ROOT / "src/nmdc_submission_schema/schema"
SUBMISSION_SCHEMA_BASE = SCHEMA_DIRECTORY / "nmdc_submission_schema_base.yaml"
SUBMISSION_SCHEMA_OUTPUT = SCHEMA_DIRECTORY / "nmdc_submission_schema.yaml"

CONFIG_DIRECTORY = ROOT / "config"
NMDC_SCHEMA_IMPORT_CONFIG = CONFIG_DIRECTORY / "nmdc_schema_import.yaml"

PROJECT_DIRECTORY = ROOT / "project"
GOLD_ECOSYSTEM_TREE_JSON = PROJECT_DIRECTORY / "thirdparty/GoldEcosystemTree.json"

ENV_TRIAD_ENUM_TSV_DIRECTORY = ROOT / "notebooks/environmental_context_value_sets"

console = Console(highlight=False)


@contextmanager
def log(message: str):
    """Context manager for logging a status that stays in the console."""
    with console.status(" " * 9 + message):
        yield
    console.log(message, _stack_offset=3)


def rel_root(path: Path) -> Path:
    """Return a path relative to the project root"""
    return path.relative_to(ROOT)


def iter_slot_definitions(schema_view: SchemaView) -> Iterable[SlotDefinition]:
    """Yield each slot and slot usage definition in the schema."""
    for slot_def in schema_view.all_slots().values():
        yield slot_def
    for class_def in schema_view.all_classes().values():
        if class_def.slot_usage:
            for slot_usage in class_def.slot_usage.values():
                yield slot_usage


def iter_slot_definitions_with_range(
    schema_view: SchemaView, range_name: str
) -> Iterable[SlotDefinition]:
    """Yield each slot or slot usage definition in the schema where the range is the given value"""
    for slot_def in iter_slot_definitions(schema_view):
        if slot_def.range == range_name:
            yield slot_def


def replace_range(
    schema_view: SchemaView,
    range_name: str,
    replacement: str | Callable[[SlotDefinition], None],
) -> None:
    """Replace the range of each slot or slot usage definition with the given replacement. If the
    replacement is a string it will be used as the new range. If the replacement is a callable, it
    will be called with each slot definition, and it is up to the callable to modify the slot as
    needed."""
    for slot_def in iter_slot_definitions_with_range(schema_view, range_name):
        if isinstance(replacement, str):
            slot_def.range = replacement
        else:
            replacement(slot_def)
    if range_name in schema_view.all_classes():
        remove_class(schema_view, range_name, remove_dangling_classes=True)
    schema_view.set_modified()


def modify_controlled_term_value_slot(slot: SlotDefinition) -> None:
    """Modify a slot that was imported with range ControlledTermValue"""
    slot.range = "string"
    slot.pattern = r"^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$"


def modify_quantity_value_slot(slot: SlotDefinition) -> None:
    """Modify a slot that was imported with range QuantityValue"""
    slot.range = "string"
    if slot.multivalued:
        slot.pattern = r"^([-+]?[0-9]*\.?[0-9]+ +\S.*\|)*([-+]?[0-9]*\.?[0-9]+ +\S.*)$"
    else:
        slot.pattern = r"^[-+]?[0-9]*\.?[0-9]+ +\S.*$"


def modify_multivalued_string_slot(slot: SlotDefinition) -> None:
    """Modify a slot that was imported as multivalued with range string"""
    if slot.range == "string" and slot.multivalued:
        slot.multivalued = False
        slot.inlined = None
        slot.inlined_as_list = None


def download_terms_from_gold() -> dict:
    """Download the GOLD Ecosystem Classification terms in JSON format"""
    url = "https://gold.jgi.doe.gov/download?mode=biosampleEcosystemsJson"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@click.command()
@click.option("--download-gold-ecosystem-terms", is_flag=True)
def main(download_gold_ecosystem_terms: bool) -> None:
    """Run all the steps to produce the final submission-schema YAML file"""
    with log(
        f"Loading submission-schema base from [bold]{rel_root(SUBMISSION_SCHEMA_BASE)}"
    ):
        submission_schema = SchemaView(SUBMISSION_SCHEMA_BASE)

    with log(f"Loading nmdc-schema version [bold]{metadata.version('nmdc_schema')}"):
        nmdc_schema = SchemaView(nmdc_schema_yaml_path)

    with log(
        f"Loading nmdc-schema import config from [bold]{rel_root(NMDC_SCHEMA_IMPORT_CONFIG)}"
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

    with log("Merging nmdc-schema prefixes into submission-schema"):
        merge_prefixes(submission_schema, source_schema=nmdc_schema)

    with log("Translating MIxS string_serializations into patterns"):
        translate_string_serializations(submission_schema)

    with log("Performing standard range replacements"):
        replace_range(submission_schema, "ControlledIdentifiedTermValue", "string")
        replace_range(
            submission_schema, "ControlledTermValue", modify_controlled_term_value_slot
        )
        replace_range(submission_schema, "QuantityValue", modify_quantity_value_slot)
        replace_range(submission_schema, "TextValue", "string")
        replace_range(submission_schema, "TimestampValue", "string")

    with log("Removing unused classes"):
        remove_class(submission_schema, "OntologyRelation", force=True)
        remove_class(submission_schema, "OntologyClass")

    with log("Making string slots single-valued"):
        for slot_def in iter_slot_definitions(submission_schema):
            modify_multivalued_string_slot(slot_def)
        submission_schema.set_modified()

    if GOLD_ECOSYSTEM_TREE_JSON.exists() and not download_gold_ecosystem_terms:
        with log(
            f"Reading GOLD Ecosystem Classification terms from existing [bold]{rel_root(GOLD_ECOSYSTEM_TREE_JSON)}"
        ):
            with open(GOLD_ECOSYSTEM_TREE_JSON) as f:
                gold_terms = json.load(f)
    else:
        with log(
            f"Downloading GOLD Ecosystem Classification terms to [bold]{rel_root(GOLD_ECOSYSTEM_TREE_JSON)}"
        ):
            gold_terms = download_terms_from_gold()
            with open(GOLD_ECOSYSTEM_TREE_JSON, "w") as f:
                json.dump(gold_terms, f)

    with log("Injecting GOLD Ecosystem Classification term enums"):
        inject_gold_pathway_terms(submission_schema, gold_terms)

    with log("Injecting Illumina instrument enum"):
        inject_illumina_instrument_model_enum(
            submission_schema, source_schema=nmdc_schema
        )

    with log("Injecting environment triad enums"):
        for tsv_file in ENV_TRIAD_ENUM_TSV_DIRECTORY.glob(
            "**/post_google_sheets_*.tsv"
        ):
            inject_env_triad_enum(submission_schema, tsv_file)

    with log("Materializing structured patterns"):
        submission_schema.materialize_patterns()

    with log(
        f"Writing final submission-schema to [bold]{rel_root(SUBMISSION_SCHEMA_OUTPUT)}"
    ):
        yaml_dumper.dump(submission_schema.schema, SUBMISSION_SCHEMA_OUTPUT)

    console.log("Done", style="green")


if __name__ == "__main__":
    main()
