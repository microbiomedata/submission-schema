from linkml_runtime import SchemaView


def translate_string_serializations(schema: SchemaView) -> None:
    """Translate string_serialization to pattern for string slots.

    MIxS is moving away from string_serialization to structured_patterns. In the meantime, we need
    to handle populating these patterns ourselves. nmdc-schema emulates MIxS's use of
    string_serialization sometimes. These should be converted to structured_patterns in nmdc-schema.
    In the meantime, we need to handle them as well.

    Go through all slots in the schema, and if they have a string_serialization that we know
    how to translate to a pattern, and they don't already have a pattern or structured_pattern
    defined, then set the pattern based on the string_serialization.

    This intentionally skips slot_usage in classes. There currently are no examples of that, and
    we don't want to support it in the future.
    """

    mixs_string_serializations_to_patterns = {
        "{float} {float}": r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?",
        "{termLabel} {[termID]}": r"\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]",
        "{termLabel} {[termID]};{timestamp}": r"\S+.*\S+ \[[a-zA-Z]{2,}:\d+\];([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?",
        "{text};{float} {unit}": r"[^;\t\r\x0A\|]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A\|]+",
        "{text};{float} {unit};{float} {unit}": r"\S+.*\S+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S+",
        "{text};{timestamp}": r"\S+.*\S+;([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?",
    }
    nmdc_schema_string_serializations_to_patterns = {
        "{date, arbitrary precision}": r"[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?",
        "{float} {unit}": r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S+",
        "{text}:{text}": r"[^\:\n\r]+\:[^\:\n\r]+",
        "{time, seconds optional}": r"([01]?\d|2[0-3]|24(?=:00?:00?$)):([0-5]\d)(:([0-5]\d))?",
    }
    string_serializations_to_patterns = {
        **mixs_string_serializations_to_patterns,
        **nmdc_schema_string_serializations_to_patterns,
    }

    for slot in schema.all_slots().values():
        if (
            slot.range == "string"
            and slot.string_serialization in string_serializations_to_patterns
            and not slot.pattern
            and not slot.structured_pattern
        ):
            pattern = string_serializations_to_patterns[slot.string_serialization]
            if slot.multivalued:
                pattern = f"{pattern}(\\|{pattern})*"
                slot.multivalued = False
                slot.inlined = None
                slot.inlined_as_list = None
            slot.pattern = f"^{pattern}$"
    schema.set_modified()
