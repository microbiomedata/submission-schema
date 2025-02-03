import click

from nmdc_submission_schema.scripts import nmdc_schema_yaml_path


@click.command()
@click.option('--output-file', '-o', type=click.File('w'), default="-")
def main(output_file):
    r"""
    Dumps a YAML representation of the NMDC Schema to the specified file.
    """
    with open(nmdc_schema_yaml_path) as input_file:
        for line in input_file:
            output_file.write(line)


if __name__ == '__main__':
    main()
