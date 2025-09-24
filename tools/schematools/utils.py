from linkml_runtime import SchemaView


def remove_class(
    schema_view: SchemaView,
    class_name: str,
    *,
    force: bool = False,
    remove_dangling_classes: bool = False,
) -> None:
    """Remove a class and all references to it from the schema.

    :param schema_view: The SchemaView object representing the schema.
    :param class_name: The name of the class to remove.
    :param force: If True, remove the class even if it is referenced elsewhere.
                  If False, raise an error if the class is referenced.
    :param remove_dangling_classes: If True, also remove any classes that become unreferenced as a result of removing this class.
    """

    def _remove_class(class_name: str) -> None:
        # Check if the class exists
        class_def = schema_view.get_class(class_name)
        if not class_def:
            raise ValueError(f"Class '{class_name}' does not exist in the schema.")

        # Check for references to the class in inherited classes
        references = schema_view.class_descendants(class_name, reflexive=False)
        if references and not force:
            raise ValueError(
                f"Class '{class_name}' is referenced by other classes: {references}. "
                "Use force=True to remove it anyway."
            )

        # Check for references to the class in slot ranges
        for slot in schema_view.all_slots().values():
            if slot.range == class_name and not force:
                raise ValueError(
                    f"Class '{class_name}' is used as the range of slot '{slot.name}'. Use force=True to remove it anyway."
                )

        # Find the class's direct slots that can be removed because they aren't used elsewhere
        slots_to_remove = set()
        slots_to_check = set(class_def.slots or [])
        while slots_to_check:
            slot_name = slots_to_check.pop()
            slot = schema_view.get_slot(slot_name, strict=False)
            if not slot:
                continue
            slot_is_used_elsewhere = False
            for other_class in schema_view.all_classes().values():
                if other_class.name != class_name and slot_name in other_class.slots:
                    slot_is_used_elsewhere = True
                    break
            for other_slot in schema_view.all_slots().values():
                if (
                    other_slot.name != slot_name
                    and other_slot.name not in slots_to_remove
                    and other_slot.is_a == slot_name
                ):
                    slot_is_used_elsewhere = True
                    break
            if not slot_is_used_elsewhere:
                slots_to_remove.add(slot_name)
                if slot.is_a:
                    slots_to_check.add(slot.is_a)

        # Get a list of additional classes to check for dangling references
        additional_classes_to_check = set()
        if remove_dangling_classes:
            for slot_name in slots_to_remove:
                slot = schema_view.get_slot(slot_name, strict=False)
                if slot and slot.range and slot.range in schema_view.all_classes():
                    additional_classes_to_check.add(slot.range)
            if class_def.is_a:
                additional_classes_to_check.add(class_def.is_a)
            for mixin in class_def.mixins or []:
                additional_classes_to_check.add(mixin)

        # Remove the class and all possible slots from the schema
        del schema_view.schema.classes[class_name]
        for slot_name in slots_to_remove:
            del schema_view.schema.slots[slot_name]
        schema_view.set_modified()

        # Recursively check for dangling classes to remove
        if remove_dangling_classes:
            for other_class_name in additional_classes_to_check:
                try:
                    _remove_class(other_class_name)
                except ValueError:
                    # The class is still referenced, so we can't remove it
                    pass

    _remove_class(class_name)


def merge_prefixes(
    schema_view: SchemaView, *, source_schema: SchemaView, overwrite: bool = False
) -> None:
    """Merge prefixes from source_schema into schema_view.

    :param schema_view: The target SchemaView object to merge prefixes into.
    :param source_schema: The source SchemaView object to merge prefixes from.
    :param overwrite: If True, existing prefixes in schema_view will be overwritten by those in source_schema.
                      If False, existing prefixes will be preserved.
    """
    for prefix, uri in source_schema.schema.prefixes.items():
        if overwrite or prefix not in schema_view.schema.prefixes:
            schema_view.schema.prefixes[prefix] = uri
    schema_view.set_modified()
