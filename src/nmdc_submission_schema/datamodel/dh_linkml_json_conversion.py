import json
import os
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--input-file', '-i', type=click.Path(exists=True), required=True,
              help='Path to the input JSON file')
@click.option('--key', '-k', type=str, required=True,
              help='Name of the key to update')
@click.option('--value', '-v', type=str, required=True,
              help='New value for the specified key')
@click.option('--output-file', '-o', type=click.Path(), required=True,
              help='Path to the output JSON file')
def update(input_file, key, value, output_file):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Update the specified key with the new value
    data[key] = value

    # Save the updated data as a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    click.echo(f'Successfully updated key "{key}" in "{input_file}" and saved the result to "{output_file}"')


@cli.command()
@click.option('--input-file', '-i', type=click.Path(exists=True), required=True,
              help='Path to the input JSON file')
@click.option('--output-dir', '-o', type=click.Path(), required=True,
              help='Path to the output directory')
def linkml2dh(input_file, output_dir):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Make sure the input is a dictionary with one or more key-value pairs,
    # where the values are lists
    if not isinstance(data, dict):
        raise click.BadParameter('Input JSON must contain a dictionary with one or more key-value pairs')

    for key, value in data.items():
        if not isinstance(value, list):
            raise click.BadParameter(f'Value for key "{key}" must be a list')

        # Save each list as a new JSON file with the same name as the key
        output_file = os.path.join(output_dir, f'{key}.json')
        with open(output_file, 'w') as f:
            json.dump(value, f)

        click.echo(f'Successfully extracted list from key "{key}" in "{input_file}" and saved it as "{output_file}"')


if __name__ == '__main__':
    cli()
