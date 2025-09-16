import logging
from copy import deepcopy
from typing import Any, Optional

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import (
    ClassDefinition,
    Element,
    EnumDefinition,
    SlotDefinition,
    TypeDefinition,
)
from pydantic import BaseModel

LOGGER = logging.getLogger(__name__)


class SlotModification(BaseModel):
    """Configuration for modifying a slot during import."""

    in_classes: Optional[list[str]] = None
    replace: Optional[dict[str, Any]] = None
    append: Optional[dict[str, Any]] = None
    remove: Optional[list[str]] = None


class SlotImport(BaseModel):
    """Configuration for importing a single slot."""

    slot: str
    source: Optional[str] = None
    destinations: list[str] = []
    modifications: list[SlotModification] = []


class ImporterConfig(BaseModel):
    """Configuration for the Importer class."""

    slots: list[SlotImport] = []


AUTOMATIC_ON_REMOVAL = {
    "multivalued": SlotModification(remove=["inlined", "inlined_as_list"]),
}

AUTOMATIC_ON_REPLACE = {
    ("multivalued", False): AUTOMATIC_ON_REMOVAL["multivalued"],
    ("required", True): SlotModification(remove=["recommended"]),
}


def apply_slot_modification(
    slot: SlotDefinition, modification: SlotModification
) -> None:
    """
    Apply a SlotModification to a SlotDefinition.

    :param slot: The SlotDefinition to modify.
    :param modification: The SlotModification objects to apply.
    """
    if modification.replace:
        for key, value in modification.replace.items():
            setattr(slot, key, value)
            try:
                if (key, value) in AUTOMATIC_ON_REPLACE:
                    apply_slot_modification(slot, AUTOMATIC_ON_REPLACE[(key, value)])
            except TypeError:
                pass
    if modification.append:
        for key, value in modification.append.items():
            current_value = getattr(slot, key, [])
            if isinstance(current_value, list):
                current_value.extend(value)
                setattr(slot, key, current_value)
    if modification.remove:
        for key in modification.remove:
            if hasattr(slot, key):
                try:
                    delattr(slot, key)
                except AttributeError:
                    setattr(slot, key, None)
            if key in AUTOMATIC_ON_REMOVAL:
                apply_slot_modification(slot, AUTOMATIC_ON_REMOVAL[key])


def _import_elements_with_dependencies(
    element: Element,
    *,
    source_schema: SchemaView,
    target_schema: SchemaView,
    include_self: bool = True,
) -> None:
    """
    Import the given element and its dependent elements from the source schema to the target schema.

    :param element: The Element to import along with its dependent elements.
    :param source_schema: The SchemaView object representing the source schema.
    :param target_schema: The SchemaView object representing the target schema.
    """
    if include_self and target_schema.get_element(element.name):
        return

    if isinstance(element, ClassDefinition):
        if include_self:
            target_schema.add_class(element)

        # Import class ancestors (is_a and mixins)
        for ancestor in source_schema.class_ancestors(
            element.name, reflexive=False, is_a=True, mixins=True
        ):
            ancestor_class = source_schema.get_class(ancestor)
            _import_elements_with_dependencies(
                ancestor_class, source_schema=source_schema, target_schema=target_schema
            )

        # Import slots used by the class
        for slot_name in element.slots:
            slot = source_schema.get_slot(slot_name)
            _import_elements_with_dependencies(
                slot, source_schema=source_schema, target_schema=target_schema
            )

        # Import any overridden ranges
        for slot_usage in element.slot_usage.values():
            if "range" in slot_usage:
                range_element = source_schema.get_element(slot_usage.range)
                if range_element:
                    _import_elements_with_dependencies(
                        range_element,
                        source_schema=source_schema,
                        target_schema=target_schema,
                    )

    elif isinstance(element, SlotDefinition):
        if include_self:
            target_schema.add_slot(element)

        # Import slot ancestors (is_a and mixins)
        for ancestor in source_schema.slot_ancestors(
            element.name, reflexive=False, is_a=True, mixins=True
        ):
            ancestor_slot = source_schema.get_slot(ancestor)
            if ancestor_slot:
                _import_elements_with_dependencies(
                    ancestor_slot,
                    source_schema=source_schema,
                    target_schema=target_schema,
                )

        # Import range element
        range_element = source_schema.get_element(element.range)
        if range_element:
            _import_elements_with_dependencies(
                range_element, source_schema=source_schema, target_schema=target_schema
            )

    elif isinstance(element, EnumDefinition):
        if include_self:
            target_schema.add_enum(element)

    elif isinstance(element, TypeDefinition):
        if include_self:
            target_schema.add_type(element)

        # Import any parent types
        for ancestor in source_schema.type_ancestors(element.name, reflexive=False):
            ancestor_type = source_schema.get_type(ancestor)
            _import_elements_with_dependencies(
                ancestor_type, source_schema=source_schema, target_schema=target_schema
            )
    else:
        LOGGER.warning("Unsupported element type: %s", type(element))
        return


def import_elements(
    *, source_schema: SchemaView, config: ImporterConfig, target_schema: SchemaView
):
    """
    Import slots from a source schema into a target schema based on the provided configuration.

    This function modifies the target schema by importing specified slots from the source schema.
    It applies any defined modifications to the slots during the import process.

    :param source_schema: The SchemaView object representing the source schema.
    :param config: The ImporterConfig object containing import configurations.
    :param target_schema: The SchemaView object representing the target schema.
    """
    for slot_import in config.slots:
        source_slot = source_schema.get_slot(slot_import.slot)
        if not source_slot:
            raise ValueError(f"Slot '{slot_import.slot}' not found in source schema.")

        # Create a copy of the source slot to modify. If a source was specified, use the induced
        # slot definition from that class, otherwise use the top-level slot definition.
        if slot_import.source:
            new_slot = source_schema.induced_slot(slot_import.slot, slot_import.source)
            # induced_slot() sets the alias to the name of the slot itself. It's unclear why it does
            # that, but it makes the schema incompatible with schemaloader (which is used by, for
            # example, PythonGenerator). So we clear it here.
            # TODO: make an issue in linkml or linkml-runtime to fix this
            if new_slot.alias == new_slot.name:
                new_slot.alias = None
        else:
            new_slot: SlotDefinition = deepcopy(source_slot)

        # Clear metaslots that are no longer relevant
        new_slot.domain_of = []
        new_slot.owner = None

        # Apply modifications
        for modification in slot_import.modifications:
            if not modification.in_classes:
                # Modifications that do not specify in_classes apply to the top-level slot definition
                apply_slot_modification(new_slot, modification)

            else:
                # Modifications that specify in_classes apply are applied on the slot_usage of the
                # slot in the specified classes
                for class_name in modification.in_classes:
                    if class_name not in slot_import.destinations:
                        raise ValueError(
                            f"Class '{class_name}' specified in modifications for slot '{slot_import.slot}' is not in destinations."
                        )
                    class_def = target_schema.get_class(class_name, strict=True)
                    if slot_import.slot not in class_def.slot_usage:
                        class_def.slot_usage[slot_import.slot] = SlotDefinition(
                            name=slot_import.slot
                        )
                    slot_usage = class_def.slot_usage[slot_import.slot]
                    apply_slot_modification(slot_usage, modification)

        # Add the modified slot to the target schema
        if target_schema.get_slot(new_slot.name):
            raise ValueError(f"Slot '{new_slot.name}' already exists in target schema.")
        target_schema.add_slot(new_slot)

        # Add the slot to the destination classes
        for destination in slot_import.destinations:
            destination_class = target_schema.get_class(destination, strict=True)
            destination_class.slots.append(new_slot.name)

        # Automatically add dependent elements to the target schema
        _import_elements_with_dependencies(
            new_slot,
            source_schema=source_schema,
            target_schema=target_schema,
            include_self=False,
        )

    target_schema.set_modified()
