import csv

import yaml
from glom import glom, assign
import click
from typing import Dict, Any, Optional, List
import re
from typing import Dict, Any
import click


def load_yaml(file_path: str) -> Dict[str, Any]:
    """Load a YAML file and return its content as a dictionary."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_tsv(file_path: str) -> List[Dict[str | Any, str | Any]]:
    """Load a TSV file and return its content as a list of dictionaries."""
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        return [row for row in reader]  # Convert reader to a list of dictionaries


def save_yaml(data: Dict[str, Any], file_path: str) -> None:
    """Save a dictionary to a YAML file."""
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)


@click.command()
@click.option("--schema", required=True, type=click.Path(exists=True), help="Path to the input YAML file.")
@click.option("--config", required=True, type=click.Path(exists=True),
              help="Path to the TSV configuration file specifying modifications.")
@click.option("--output", required=True, type=click.Path(), help="Path to save the modified YAML file.")
def main(schema: str, config: str, output: str) -> None:
    """
    Modify the input YAML based on rules in the config file and save the result to the output file.

    Args:
        schema (str): Path to the input YAML file.
        config (str): Path to the configuration file specifying modifications.
        output (str): Path to save the modified YAML file.
    """
    # Load input data and configuration
    schema = load_yaml(schema)

    enums = schema.get("enums", {})
    enum_keys = set(enums.keys())  # Collect the keys for quick lookup
    types = schema.get("types", {})
    type_keys = set(types.keys())
    classes = schema.get("classes", {})
    class_keys = set(classes.keys())
    sets = dict()
    sets['enum_keys'] = enum_keys
    sets['type_keys'] = type_keys
    sets['class_keys'] = class_keys
    sets_keys = set(sets.keys())

    raw_config = load_tsv(config)

    for rc in raw_config:
        scope = rc.get('scope')
        criterion_field = rc.get('criterion_field')
        criterion_value = rc.get('criterion_value')
        criterion_in_set = rc.get('criterion_in_set')
        operation = rc.get('operation')
        target_field = rc.get('target_field')
        target_value = rc.get('target_value')
        element_key = rc.get('element_key')
        active = rc.get('active')
        # make active uppercase
        if active.upper() != "TRUE":
            continue

        if operation == 'set' \
                and criterion_field == "" \
                and criterion_in_set == "" \
                and criterion_value == "" \
                and element_key in schema['slots'] \
                and scope in ['slot', 'slot_or_usage'] \
                and target_field in schema['slots'][element_key]:
            schema['slots'][element_key][target_field] = target_value

        if operation == 'delete_element' \
                and criterion_field == "" \
                and criterion_in_set == "" \
                and criterion_value == "" \
                and element_key == "" \
                and scope in ['slot', 'slot_or_usage'] \
                and target_field in schema['slots']:
            del schema['slots'][target_field]

        for ck, cv in schema['classes'].items():
            if 'slots' in cv:
                slots_list = cv['slots']
                if operation == 'delete_element' \
                        and criterion_field == "" \
                        and criterion_in_set == "" \
                        and criterion_value == "" \
                        and element_key == "" \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in slots_list:
                    slots_list.remove(target_field)
            if 'slot_usage' in cv:
                if operation == 'delete_element' \
                        and criterion_field == "" \
                        and criterion_in_set == "" \
                        and criterion_value == "" \
                        and element_key == "" \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in cv['slot_usage']:
                    del cv['slot_usage'][target_field]
                if operation == 'set' \
                        and criterion_field == "" \
                        and criterion_in_set == "" \
                        and criterion_value == "" \
                        and element_key in cv['slot_usage'] \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in cv['slot_usage'][element_key]:
                    cv['slot_usage'][element_key][target_field] = target_value

        if operation == 'delete_element' \
                and criterion_field == "" \
                and criterion_in_set == "" \
                and criterion_value == "" \
                and element_key == "" \
                and scope in ['class'] \
                and target_field in schema['classes']:
            del schema['classes'][target_field]

        for ok, ov in schema.items():  # o for outer
            # print(ok)
            #
            # types
            #
            # classes
            # enums
            # slots
            # subsets
            if ok == 'slots' \
                    and scope in ['slot', 'slot_or_usage', 'all_elements']:
                for sk, sv in ov.items():  # s for slot
                    if criterion_field in sv \
                            and criterion_in_set == "" \
                            and element_key == "" \
                            and operation == 'set' \
                            and sv[criterion_field] == criterion_value:
                        # click.echo(
                        #     f"setting {target_field} to {target_value} in slot {sk} because {criterion_field} == {criterion_value}")
                        sv[target_field] = target_value
                    if criterion_field in sv \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and sv[criterion_field] in sets[criterion_in_set] \
                            and target_field in sv \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in slot {sk} because {sv[criterion_field]} is in {criterion_in_set}")
                        del sv[target_field]
                    if criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and target_field in sv:
                        # click.echo(f"globally deleting {target_field} in slot {sk}")
                        del sv[target_field]
                    if sk == element_key \
                            and criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and operation == 'set':
                        # click.echo(f"setting {target_field} to {target_value} in slot {sk}")
                        sv[target_field] = target_value
                    if sk == element_key \
                            and criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and operation == 'delete_field' \
                            and target_field in sv:
                        click.echo(f"deleting {target_field} in slot {sk}")
                        del sv[target_field]
                    if criterion_field in sv \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and sv[criterion_field] == criterion_value \
                            and target_field in sv \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in slot {sk} because {sv[criterion_field]} == {criterion_value}")
                        del sv[target_field]
            if ok == 'classes' \
                    and scope in ['class', 'all_elements']:
                for ck, cv in ov.items():  # c for class
                    if criterion_field in cv \
                            and criterion_in_set == "" \
                            and element_key == "" \
                            and operation == 'set' \
                            and cv[criterion_field] == criterion_value:
                        click.echo(
                            f"setting {target_field} to {target_value} in class {ck} because {criterion_field} == {criterion_value}")
                        cv[target_field] = target_value
                    if criterion_field in cv \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and cv[criterion_field] in sets[criterion_in_set] \
                            and target_field in cv \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in class {ck}  because {cv[criterion_field]} is in {criterion_in_set}")
                        del cv[target_field]
                    if criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and target_field in cv:
                        # click.echo(f"globally deleting {target_field} in class {ck}")
                        del cv[target_field]
            if ok == 'classes' \
                    and scope in ['usage', 'slot_or_usage', 'all_elements']:
                for ck, cv in ov.items():  # c for class
                    if 'slot_usage' in cv:
                        for sk, sv in cv['slot_usage'].items():
                            # click.echo(f"checking slot_usage in class {ck} slot {sk}")
                            if criterion_field in sv \
                                    and criterion_in_set == "" \
                                    and element_key == "" \
                                    and operation == 'set' \
                                    and sv[criterion_field] == criterion_value:
                                # click.echo(
                                #     f"setting {target_field} to {target_value} in class {ck} usage of slot {sk} because {criterion_field} == {criterion_value}")
                                sv[target_field] = target_value
                            if criterion_field in sv \
                                    and criterion_value == "" \
                                    and element_key == "" \
                                    and operation == 'delete_field' \
                                    and sv[criterion_field] in sets[criterion_in_set] \
                                    and target_field in sv \
                                    and target_value == "":
                                # click.echo(
                                #     f"deleting {target_field} in class {ck} usage {sk} because {sv[criterion_field]} is in {criterion_in_set}")
                                del sv[target_field]
                            if criterion_field == "" \
                                    and criterion_in_set == "" \
                                    and criterion_value == "" \
                                    and element_key == "" \
                                    and operation == 'delete_field' \
                                    and target_field in sv:
                                # click.echo(f"globally deleting {target_field} in class {ck} usage {sk}")
                                del sv[target_field]
                            if criterion_field in sv \
                                    and element_key == "" \
                                    and operation == 'delete_field' \
                                    and sv[criterion_field] == criterion_value \
                                    and target_field in sv \
                                    and target_value == "":
                                # click.echo(
                                #     f"deleting {target_field} in {ck} usage {sk} because {sv[criterion_field]} == {criterion_value}")
                                del sv[target_field]
            if ok == 'enums' \
                    and scope in ['enum', 'all_elements']:
                for ek, ev in ov.items():
                    # click.echo(f"checking enum {ek}")
                    if criterion_field in ev \
                            and criterion_in_set == "" \
                            and element_key == "" \
                            and operation == 'set' \
                            and ev[criterion_field] == criterion_value:
                        click.echo(
                            f"setting {target_field} to {target_value} in enum {ek} because {criterion_field} == {criterion_value}")
                        ev[target_field] = target_value
                    if criterion_field in ev \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and ev[criterion_field] in sets[criterion_in_set] \
                            and target_field in ev \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in enum {ek} because {ek[criterion_field]} is in {criterion_in_set}")
                        del ev[target_field]
                    if criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and target_field in ev:
                        # click.echo(f"globally deleting {target_field} in enum {ek}")
                        del ev[target_field]
            if ok == 'subsets' \
                    and scope in ['all_elements']:
                for uk, uv in ov.items():
                    # click.echo(f"checking subset {uk}")
                    if criterion_field in uv \
                            and criterion_in_set == "" \
                            and element_key == "" \
                            and operation == 'set' \
                            and uv[criterion_field] == criterion_value:
                        click.echo(
                            f"setting {target_field} to {target_value} in subset {uk} because {criterion_field} == {criterion_value}")
                        uv[target_field] = target_value
                    if criterion_field in uv \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and uv[criterion_field] in sets[criterion_in_set] \
                            and target_field in uv \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in subset {uk} because {uk[criterion_field]} is in {criterion_in_set}")
                        del uv[target_field]
                    if criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and target_field in uv:
                        # click.echo(f"globally deleting {target_field} in subset {uk}")
                        del uv[target_field]
            if ok == 'types' \
                    and scope in ['all_elements']:  # or might want to remove all linkml types and add an import
                for tk, tv in ov.items():
                    # click.echo(f"checking type {tk}")
                    if criterion_field in tv \
                            and criterion_in_set == "" \
                            and element_key == "" \
                            and operation == 'set' \
                            and tv[criterion_field] == criterion_value:
                        click.echo(
                            f"setting {target_field} to {target_value} in type {tk} because {criterion_field} == {criterion_value}")
                        tv[target_field] = target_value
                    if criterion_field in tv \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and tv[criterion_field] in sets[criterion_in_set] \
                            and target_field in tv \
                            and target_value == "":
                        click.echo(
                            f"deleting {target_field} in type {tk} because {tk[criterion_field]} is in {criterion_in_set}")
                        del tv[target_field]
                    if criterion_field == "" \
                            and criterion_in_set == "" \
                            and criterion_value == "" \
                            and element_key == "" \
                            and operation == 'delete_field' \
                            and target_field in tv:
                        # click.echo(f"globally deleting {target_field} in type {tk}")
                        del tv[target_field]

    # Save the modified data to the output file
    save_yaml(schema, output)
    # click.echo(f"Modifications applied to {input_yaml} and saved to {output_file} as per {config_file}.")


if __name__ == "__main__":
    main()
