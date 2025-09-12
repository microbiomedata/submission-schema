import csv
from collections import namedtuple
from pathlib import Path

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue, SlotDefinition


def inject_illumina_instrument_model_enum(
    schema_view: SchemaView, *, source_schema: SchemaView = None
):
    """Inject an enum of Illumina instrument models into the provided schema.

    The enum is derived from the InstrumentModelEnum imported from nmdc-schema, filtering for models
    with 'Illumina' in their aliases. The resulting enum is named IlluminaInstrumentModelEnum.
    """
    instrument_model_enum = source_schema.get_enum("InstrumentModelEnum", strict=True)
    illumina_model_permissible_values = {
        key: value
        for key, value in instrument_model_enum.permissible_values.items()
        if value.aliases is not None
        and any("Illumina" in alias for alias in value.aliases)
    }
    schema_view.add_enum(
        EnumDefinition(
            name="IlluminaInstrumentModelEnum",
            description="Derived from InstrumentModelEnum by filtering for Illumina models",
            permissible_values=illumina_model_permissible_values,
        )
    )


EnumInfo = namedtuple("EnumInfo", ["enum_name", "class_name", "slot_name"])
ENUM_FILE_MAPPINGS: dict[str, EnumInfo] = {
    "post_google_sheets_soil_env_local_scale.tsv": EnumInfo(
        "EnvLocalScaleSoilEnum", "SoilInterface", "env_local_scale"
    ),
    "post_google_sheets_soil_env_medium.tsv": EnumInfo(
        "EnvMediumSoilEnum", "SoilInterface", "env_medium"
    ),
    "post_google_sheets_soil_env_broad_scale.tsv": EnumInfo(
        "EnvBroadScaleSoilEnum", "SoilInterface", "env_broad_scale"
    ),
    "post_google_sheets_water_env_local_scale.tsv": EnumInfo(
        "EnvLocalScaleWaterEnum", "WaterInterface", "env_local_scale"
    ),
    "post_google_sheets_water_env_medium.tsv": EnumInfo(
        "EnvMediumWaterEnum", "WaterInterface", "env_medium"
    ),
    "post_google_sheets_water_env_broad_scale.tsv": EnumInfo(
        "EnvBroadScaleWaterEnum", "WaterInterface", "env_broad_scale"
    ),
    "post_google_sheets_sediment_env_local_scale.tsv": EnumInfo(
        "EnvLocalScaleSedimentEnum", "SedimentInterface", "env_local_scale"
    ),
    "post_google_sheets_sediment_env_medium.tsv": EnumInfo(
        "EnvMediumSedimentEnum", "SedimentInterface", "env_medium"
    ),
    "post_google_sheets_sediment_env_broad_scale.tsv": EnumInfo(
        "EnvBroadScaleSedimentEnum", "SedimentInterface", "env_broad_scale"
    ),
    "post_google_sheets_plant_associated_env_local_scale.tsv": EnumInfo(
        "EnvLocalScalePlantAssociatedEnum",
        "PlantAssociatedInterface",
        "env_local_scale",
    ),
    "post_google_sheets_plant_associated_env_medium.tsv": EnumInfo(
        "EnvMediumPlantAssociatedEnum", "PlantAssociatedInterface", "env_medium"
    ),
    "post_google_sheets_plant_associated_env_broad_scale.tsv": EnumInfo(
        "EnvBroadScalePlantAssociatedEnum",
        "PlantAssociatedInterface",
        "env_broad_scale",
    ),
}


def inject_env_triad_enum(schema_view: SchemaView, tsv_file: Path) -> None:
    """Inject terms from a TSV file into the schema under a specified enumeration name.

    :param schema_view: SchemaView object representing the schema.
    :param tsv_file: Path to the TSV file containing the terms.
    """
    enum_info = ENUM_FILE_MAPPINGS.get(tsv_file.name)
    if enum_info is None:
        raise ValueError(f"Enumeration name not found for file: {tsv_file.name}")

    with open(tsv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")
        data = sorted(reader, key=lambda x: x["label"])

    pvs = [PermissibleValue(text=f"{term['label']} [{term['id']}]") for term in data]

    enum_def = EnumDefinition(
        name=enum_info.enum_name,
        permissible_values=pvs,
        in_subset=["nmdc_env_triad_enums"],
    )
    class_def = schema_view.get_class(enum_info.class_name)
    if class_def is None:
        raise ValueError(f"Class '{enum_info.class_name}' not found in schema.")

    if enum_info.slot_name not in class_def.slot_usage:
        class_def.slot_usage[enum_info.slot_name] = SlotDefinition(
            name=enum_info.slot_name
        )
    slot_usage = class_def.slot_usage[enum_info.slot_name]
    slot_usage.range = None  # Clear existing range if any
    slot_usage.any_of = [{"range": enum_info.enum_name}, {"range": "string"}]
    schema_view.add_enum(enum_def)
