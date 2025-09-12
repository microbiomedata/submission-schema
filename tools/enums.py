from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import EnumDefinition


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
