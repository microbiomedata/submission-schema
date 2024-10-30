import csv
import pprint

import yaml
from glom import glom, assign
import click
from typing import Dict, Any, Optional, List
import re
from typing import Dict, Any
import click

emptyish = ["", "NULL", None]  # standardize the config values to just one of these


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
@click.option('--collapse-annotations/--no-collapse-annotations', default=True,
              help="convert annotations to simple dict form.")
@click.option('--drop-redundant-aliases/--no-drop-redundant-aliases', default=True,
              help="drop aliases that are the same as the title.")
def main(schema: str, config: str, output: str, collapse_annotations: bool, drop_redundant_aliases: bool) -> None:
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
    # sets_keys = set(sets.keys())

    raw_config = load_tsv(config)

    # pprint.pprint(raw_config)

    for sk, sv in schema['slots'].items():
        if collapse_annotations and 'annotations' in sv:  # pull out of rc loop
            for ak, av in sv['annotations'].items():
                if 'tag' in av and 'value' in av:
                    # click.echo(f"setting {ak} to {av['value']} for {sk}")
                    sv['annotations'][ak] = av['value']
        if drop_redundant_aliases and 'aliases' in sv:
            current_aliases = sv['aliases']
            for alias in sv['aliases']:
                if 'title' in sv and alias == sv['title']:
                    # click.echo(f"removing redundant alias {alias} from slot {sk}")
                    current_aliases.remove(alias)
            if len(current_aliases) == 0:
                del sv['aliases']
            else:
                sv['aliases'] = current_aliases
    for ck, cv in schema['classes'].items():
        if collapse_annotations and 'annotations' in cv:
            for ak, av in cv['annotations'].items():
                if 'tag' in av and 'value' in av:
                    # click.echo(f"setting {ak} to {av['value']} for {ck}")
                    cv['annotations'][ak] = av['value']
        if drop_redundant_aliases and 'aliases' in cv:
            current_aliases = cv['aliases']
            for alias in cv['aliases']:
                if 'title' in cv and alias == cv['title']:
                    click.echo(f"removing redundant alias {alias} from {ck}")
                    current_aliases.remove(alias)
            if len(current_aliases) == 0:
                del cv['aliases']
            else:
                cv['aliases'] = current_aliases
        if 'slot_usage' in cv:
            for sk, sv in cv['slot_usage'].items():
                if collapse_annotations and 'annotations' in sv:
                    for ak, av in sv['annotations'].items():
                        if 'tag' in av and 'value' in av:
                            # click.echo(f"setting {ak} to {av['value']} for {sk} in {ck}")
                            sv['annotations'][ak] = av['value']
                if drop_redundant_aliases and 'aliases' in sv:
                    current_aliases = sv['aliases']
                    for alias in sv['aliases']:
                        if 'title' in sv and alias == sv['title']:
                            # click.echo(f"removing redundant alias {alias} from slot {sk} in {ck}")
                            current_aliases.remove(alias)
                    if len(current_aliases) == 0:
                        del sv['aliases']
                    else:
                        sv['aliases'] = current_aliases

    for ek, ev in schema['enums'].items():
        if collapse_annotations and 'annotations' in ev:
            for ak, av in ev['annotations'].items():
                if 'tag' in av and 'value' in av:
                    click.echo(f"setting {ak} to {av['value']} for {ek}")
                    ev['annotations'][ak] = av['value']
        if drop_redundant_aliases and 'aliases' in ev:
            current_aliases = ev['aliases']
            for alias in ev['aliases']:
                if 'title' in ev and alias == ev['title']:
                    click.echo(f"removing redundant alias {alias} from {ek}")
                    current_aliases.remove(alias)
            if len(current_aliases) == 0:
                del ev['aliases']
            else:
                ev['aliases'] = current_aliases
        if 'permissible_values' in ev:
            for vk, vv in ev['permissible_values'].items():
                if collapse_annotations and 'annotations' in vv:
                    for ak, av in vv['annotations'].items():
                        if 'tag' in av and 'value' in av:
                            # click.echo(f"setting {ak} to {av['value']} for {vk} in {ek}")
                            vv['annotations'][ak] = av['value']
                if drop_redundant_aliases and 'aliases' in vv:
                    current_aliases = vv['aliases']
                    for alias in vv['aliases']:
                        if 'title' in vv and alias == vv['title']:
                            click.echo(f"removing redundant alias {alias} from {vk} in {ek}")
                            current_aliases.remove(alias)
                    if len(current_aliases) == 0:
                        del vv['aliases']
                    else:
                        vv['aliases'] = current_aliases

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
                and criterion_field in emptyish \
                and criterion_in_set in emptyish \
                and criterion_value in emptyish \
                and element_key in schema['slots'] \
                and scope in ['slot', 'slot_or_usage'] \
                and target_field in schema['slots'][element_key]:
            schema['slots'][element_key][target_field] = target_value

        if operation == 'delete_element' \
                and criterion_field in emptyish \
                and criterion_in_set in emptyish \
                and criterion_value in emptyish \
                and element_key in emptyish \
                and scope in ['slot', 'slot_or_usage'] \
                and target_field in schema['slots']:
            del schema['slots'][target_field]

        for ck, cv in schema['classes'].items():
            if 'slots' in cv:
                slots_list = cv['slots']
                if operation == 'delete_element' \
                        and criterion_field in emptyish \
                        and criterion_in_set in emptyish \
                        and criterion_value in emptyish \
                        and element_key in emptyish \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in slots_list:
                    slots_list.remove(target_field)
            if 'slot_usage' in cv:
                if operation == 'delete_element' \
                        and criterion_field in emptyish \
                        and criterion_in_set in emptyish \
                        and criterion_value in emptyish \
                        and element_key in emptyish \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in cv['slot_usage']:
                    del cv['slot_usage'][target_field]
                if operation == 'set' \
                        and criterion_field in emptyish \
                        and criterion_in_set in emptyish \
                        and criterion_value in emptyish \
                        and element_key in cv['slot_usage'] \
                        and scope in ['usage', 'slot_or_usage'] \
                        and target_field in cv['slot_usage'][element_key]:
                    cv['slot_usage'][element_key][target_field] = target_value

        if operation == 'delete_element' \
                and criterion_field in emptyish \
                and criterion_in_set in emptyish \
                and criterion_value in emptyish \
                and element_key in emptyish \
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
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'set' \
                            and sv[criterion_field] == criterion_value \
                            and target_field not in emptyish:
                        # click.echo(
                        #     f"setting {target_field} to {target_value} in slot {sk} because {criterion_field} == {criterion_value}")
                        sv[target_field] = target_value
                    if sk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and operation == 'set' \
                            and target_field not in emptyish \
                            and target_value not in emptyish:
                        # click.echo(f"setting {target_field} to {target_value} in slot {sk}")
                        sv[target_field] = target_value
                    if criterion_field in sv \
                            and criterion_field not in emptyish \
                            and criterion_in_set not in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and sv[criterion_field] in sets[criterion_in_set] \
                            and target_field in sv \
                            and target_value in emptyish:
                        # click.echo(
                        #     f"deleting {target_field} in slot {sk} because {sv[criterion_field]} is in {criterion_in_set}")
                        del sv[target_field]
                    if criterion_field in sv \
                            and criterion_field not in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and sv[criterion_field] == criterion_value \
                            and target_field in sv \
                            and target_value in emptyish:
                        # click.echo(
                        # f"deleting {target_field} in slot {sk} because {criterion_field} == {criterion_value}")
                        del sv[target_field]
                    if criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and target_field in sv \
                            and target_value in emptyish:
                        # click.echo(f"globally deleting {target_field} in slot {sk}")
                        del sv[target_field]
                    if sk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key not in emptyish \
                            and operation == 'delete_field' \
                            and target_field in sv \
                            and target_value in emptyish:
                        # click.echo(f"deleting {target_field} in slot {sk}")
                        del sv[target_field]

            if ok == 'classes' \
                    and scope in ['class', 'all_elements']:
                for ck, cv in ov.items():  # c for class
                    if criterion_field in cv \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'set' \
                            and cv[criterion_field] == criterion_value \
                            and target_field not in emptyish:
                        click.echo(
                            f"setting {target_field} to {target_value} in class {ck} because {criterion_field} == {criterion_value}")
                        cv[target_field] = target_value
                    if ck == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and operation == 'set' \
                            and target_field not in emptyish \
                            and target_value not in emptyish:
                        click.echo(f"setting {target_field} to {target_value} in class {ck}")
                        cv[target_field] = target_value
                    if criterion_field in cv \
                            and criterion_field not in emptyish \
                            and criterion_in_set not in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and cv[criterion_field] in sets[criterion_in_set] \
                            and target_field in cv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in class {ck} because {cv[criterion_field]} is in {criterion_in_set}")
                        del cv[target_field]
                    if criterion_field in cv \
                            and criterion_field not in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and cv[criterion_field] == criterion_value \
                            and target_field in cv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in class {ck} because {criterion_field} == {criterion_value}")
                        del cv[target_field]
                    if criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and target_field in cv \
                            and target_value in emptyish:
                        # click.echo(f"globally deleting {target_field} in class {ck}")
                        del cv[target_field]
                    if ck == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key not in emptyish \
                            and operation == 'delete_field' \
                            and target_field in cv \
                            and target_value in emptyish:
                        click.echo(f"deleting {target_field} in class {ck}")
                        del cv[target_field]

            if ok == 'classes' \
                    and scope in ['usage', 'slot_or_usage', 'all_elements']:
                for ck, cv in ov.items():  # c for class
                    if 'slot_usage' in cv:
                        for sk, sv in cv['slot_usage'].items():
                            if criterion_field in sv \
                                    and criterion_in_set in emptyish \
                                    and criterion_value not in emptyish \
                                    and element_key in emptyish \
                                    and operation == 'set' \
                                    and sv[criterion_field] == criterion_value \
                                    and target_field not in emptyish:
                                click.echo(
                                    f"setting {target_field} to {target_value} in class {ck} usage {sk} because {criterion_field} == {criterion_value}")
                                sv[target_field] = target_value
                            if sk == element_key \
                                    and criterion_field in emptyish \
                                    and criterion_in_set in emptyish \
                                    and criterion_value in emptyish \
                                    and operation == 'set' \
                                    and target_field not in emptyish \
                                    and target_value not in emptyish:
                                # click.echo(f"setting {target_field} to {target_value} in class {ck} usage {sk}")
                                sv[target_field] = target_value
                            if criterion_field in sv \
                                    and criterion_field not in emptyish \
                                    and criterion_in_set not in emptyish \
                                    and criterion_value in emptyish \
                                    and element_key in emptyish \
                                    and operation == 'delete_field' \
                                    and sv[criterion_field] in sets[criterion_in_set] \
                                    and target_field in sv \
                                    and target_value in emptyish:
                                # click.echo(
                                #     f"deleting {target_field} in class {ck} usage {sk} because {sv[criterion_field]} is in {criterion_in_set}")
                                del sv[target_field]
                            if criterion_field in sv \
                                    and criterion_field not in emptyish \
                                    and criterion_in_set in emptyish \
                                    and criterion_value not in emptyish \
                                    and element_key in emptyish \
                                    and operation == 'delete_field' \
                                    and sv[criterion_field] == criterion_value \
                                    and target_field in sv \
                                    and target_value in emptyish:
                                # click.echo(
                                #     f"deleting {target_field} in class {ck} usage {sk} because {criterion_field} == {criterion_value}")
                                del sv[target_field]
                            if criterion_field in emptyish \
                                    and criterion_in_set in emptyish \
                                    and criterion_value in emptyish \
                                    and element_key in emptyish \
                                    and operation == 'delete_field' \
                                    and target_field in sv \
                                    and target_value in emptyish:
                                # click.echo(f"globally deleting {target_field} in class {ck} usage {sk}")
                                del sv[target_field]
                            if sk == element_key \
                                    and criterion_field in emptyish \
                                    and criterion_in_set in emptyish \
                                    and criterion_value in emptyish \
                                    and element_key not in emptyish \
                                    and operation == 'delete_field' \
                                    and target_field in sv \
                                    and target_value in emptyish:
                                click.echo(f"deleting {target_field} class {ck} usage {sk}")
                                del sv[target_field]
            if ok == 'enums' \
                    and scope in ['enum', 'all_elements']:
                for ek, ev in ov.items():
                    if criterion_field in ev \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'set' \
                            and ev[criterion_field] == criterion_value \
                            and target_field not in emptyish:
                        click.echo(
                            f"setting {target_field} to {target_value} in enum {ek} because {criterion_field} == {criterion_value}")
                        ev[target_field] = target_value
                    if ek == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and operation == 'set' \
                            and target_field not in emptyish \
                            and target_value not in emptyish:
                        click.echo(f"setting {target_field} to {target_value} in enum {ek}")
                        ev[target_field] = target_value
                    if criterion_field in ev \
                            and criterion_field not in emptyish \
                            and criterion_in_set not in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and ev[criterion_field] in sets[criterion_in_set] \
                            and target_field in ev \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in enum {ek} because {ev[criterion_field]} is in {criterion_in_set}")
                        del ev[target_field]
                    if criterion_field in ev \
                            and criterion_field not in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and ev[criterion_field] == criterion_value \
                            and target_field in ev \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in enum {ek} because {criterion_field} == {criterion_value}")
                        del ev[target_field]
                    if criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and target_field in ev \
                            and target_value in emptyish:
                        # click.echo(f"globally deleting {target_field} in enum {ek}")
                        del ev[target_field]
                    if ek == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key not in emptyish \
                            and operation == 'delete_field' \
                            and target_field in ev \
                            and target_value in emptyish:
                        click.echo(f"deleting {target_field} in enum {ek}")
                        del ev[target_field]
                    for vk, vv in ev.get('permissible_values', {}).items():
                        if criterion_field in vv \
                                and criterion_in_set in emptyish \
                                and criterion_value not in emptyish \
                                and element_key in emptyish \
                                and operation == 'set' \
                                and vv[criterion_field] == criterion_value \
                                and target_field not in emptyish:
                            click.echo(
                                f"setting {target_field} to {target_value} in PV {vk} from enum {ek} because {criterion_field} == {criterion_value}")
                            vv[target_field] = target_value
                        if vk == element_key \
                                and criterion_field in emptyish \
                                and criterion_in_set in emptyish \
                                and criterion_value in emptyish \
                                and operation == 'set' \
                                and target_field not in emptyish \
                                and target_value not in emptyish:
                            click.echo(f"setting {target_field} to {target_value} in PV {vk} from enum {ek}")
                            vv[target_field] = target_value
                        if criterion_field in vv \
                                and criterion_field not in emptyish \
                                and criterion_in_set not in emptyish \
                                and criterion_value in emptyish \
                                and element_key in emptyish \
                                and operation == 'delete_field' \
                                and vv[criterion_field] in sets[criterion_in_set] \
                                and target_field in vv \
                                and target_value in emptyish:
                            click.echo(
                                f"deleting {target_field} in PV {vk} from enum {ek} because {vv[criterion_field]} is in {criterion_in_set}")
                            del vv[target_field]
                        if criterion_field in vv \
                                and criterion_field not in emptyish \
                                and criterion_in_set in emptyish \
                                and criterion_value not in emptyish \
                                and element_key in emptyish \
                                and operation == 'delete_field' \
                                and vv[criterion_field] == criterion_value \
                                and target_field in vv \
                                and target_value in emptyish:
                            click.echo(
                                f"deleting {target_field} in PV {vk} from enum {ek} because {criterion_field} == {criterion_value}")
                            del vv[target_field]
                        if criterion_field in emptyish \
                                and criterion_in_set in emptyish \
                                and criterion_value in emptyish \
                                and element_key in emptyish \
                                and operation == 'delete_field' \
                                and target_field in vv \
                                and target_value in emptyish:
                            # click.echo(f"globally deleting {target_field} in PV {vk} from enum {ek}")
                            del vv[target_field]
                        if vk == element_key \
                                and criterion_field in emptyish \
                                and criterion_in_set in emptyish \
                                and criterion_value in emptyish \
                                and element_key not in emptyish \
                                and operation == 'delete_field' \
                                and target_field in vv \
                                and target_value in emptyish:
                            click.echo(f"deleting {target_field} in PV {vk} from enum {ek}")
                            del vv[target_field]

            if ok == 'subsets' \
                    and scope in ['all_elements']:
                for uk, uv in ov.items():
                    if criterion_field in uv \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'set' \
                            and uv[criterion_field] == criterion_value \
                            and target_field not in emptyish:
                        click.echo(
                            f"setting {target_field} to {target_value} in subset {uk} because {criterion_field} == {criterion_value}")
                        uv[target_field] = target_value
                    if uk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and operation == 'set' \
                            and target_field not in emptyish \
                            and target_value not in emptyish:
                        click.echo(f"setting {target_field} to {target_value} in subset {uk}")
                        uv[target_field] = target_value
                    if criterion_field in uv \
                            and criterion_field not in emptyish \
                            and criterion_in_set not in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and uv[criterion_field] in sets[criterion_in_set] \
                            and target_field in uv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in subset {uk} because {uv[criterion_field]} is in {criterion_in_set}")
                        del uv[target_field]
                    if criterion_field in uv \
                            and criterion_field not in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and uv[criterion_field] == criterion_value \
                            and target_field in uv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in subset {uk} because {criterion_field} == {criterion_value}")
                        del uv[target_field]
                    if criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and target_field in uv \
                            and target_value in emptyish:
                        # click.echo(f"globally deleting {target_field} in subset {uk}")
                        del uv[target_field]
                    if uk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key not in emptyish \
                            and operation == 'delete_field' \
                            and target_field in uv \
                            and target_value in emptyish:
                        click.echo(f"deleting {target_field} in subset {uk}")
                        del uv[target_field]
            if ok == 'types' \
                    and scope in ['all_elements']:  # or might want to remove all linkml types and add an import
                for tk, tv in ov.items():
                    if criterion_field in tv \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'set' \
                            and tv[criterion_field] == criterion_value \
                            and target_field not in emptyish:
                        click.echo(
                            f"setting {target_field} to {target_value} in type {tk} because {criterion_field} == {criterion_value}")
                        tv[target_field] = target_value
                    if tk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and operation == 'set' \
                            and target_field not in emptyish \
                            and target_value not in emptyish:
                        click.echo(f"setting {target_field} to {target_value} in type {tk}")
                        tv[target_field] = target_value
                    if criterion_field in tv \
                            and criterion_field not in emptyish \
                            and criterion_in_set not in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and tv[criterion_field] in sets[criterion_in_set] \
                            and target_field in tv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in type {tk} because {tv[criterion_field]} is in {criterion_in_set}")
                        del tv[target_field]
                    if criterion_field in tv \
                            and criterion_field not in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value not in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and tv[criterion_field] == criterion_value \
                            and target_field in tv \
                            and target_value in emptyish:
                        click.echo(
                            f"deleting {target_field} in type {tk} because {criterion_field} == {criterion_value}")
                        del tv[target_field]
                    if criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key in emptyish \
                            and operation == 'delete_field' \
                            and target_field in tv \
                            and target_value in emptyish:
                        # click.echo(f"globally deleting {target_field} in type {tk}")
                        del tv[target_field]
                    if tk == element_key \
                            and criterion_field in emptyish \
                            and criterion_in_set in emptyish \
                            and criterion_value in emptyish \
                            and element_key not in emptyish \
                            and operation == 'delete_field' \
                            and target_field in tv \
                            and target_value in emptyish:
                        click.echo(f"deleting {target_field} in type {tk}")
                        del tv[target_field]

    # Save the modified data to the output file
    save_yaml(schema, output)
    # click.echo(f"Modifications applied to {input_yaml} and saved to {output_file} as per {config_file}.")


if __name__ == "__main__":
    main()
