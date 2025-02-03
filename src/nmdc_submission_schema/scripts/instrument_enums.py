import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import EnumDefinition

from nmdc_submission_schema.scripts import nmdc_schema_yaml_path


def inject_illumina_instrument_model_enum(schema: SchemaView):
    """Inject an enum of Illumina instrument models into the provided schema.

    The enum is derived from the InstrumentModelEnum in the NMDC schema, filtering for models with
    'Illumina' in their aliases. The resulting enum is named IlluminaInstrumentModelEnum.
    """
    nmdc_schema_view = SchemaView(str(nmdc_schema_yaml_path))
    instrument_model_enum = nmdc_schema_view.get_enum('InstrumentModelEnum')
    illumina_model_permissible_values = {
        key: value
        for key, value in instrument_model_enum.permissible_values.items()
        if value.aliases is not None and any('Illumina' in alias for alias in value.aliases)
    }
    schema.add_enum(
        EnumDefinition(
            name='IlluminaInstrumentModelEnum',
            description='Derived from InstrumentModelEnum by filtering for Illumina models',
            permissible_values=illumina_model_permissible_values
        )
    )


@click.command()
@click.option('--input-file', '-i', type=click.File('r'), default="-")
@click.option('--output-file', '-o', type=click.File('w'), default="-")
def main(input_file, output_file):
    """Inject submission-schema specific instrument model enums into the provided schema."""
    schema_view = SchemaView(input_file.read())
    inject_illumina_instrument_model_enum(schema_view)
    print(yaml_dumper.dumps(schema_view.schema), file=output_file)


if __name__ == '__main__':
    main()
