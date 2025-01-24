import importlib.resources

import click


@click.command()
@click.option('--output-file', '-o', type=click.File('w'), default="-")
def main(output_file):
    schema_file_name = 'nmdc_materialized_patterns.yaml'
    with importlib.resources.open_text('nmdc_schema', schema_file_name) as input_file:
        for line in input_file:
            output_file.write(line)


if __name__ == '__main__':
    main()
