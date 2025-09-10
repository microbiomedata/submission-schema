import pytest
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import Example

from nmdc_submission_schema.schematools import import_elements
from nmdc_submission_schema.schematools.importer import (
    ImporterConfig,
    SlotImport,
    SlotModification,
)


@pytest.fixture
def empty_target_schema():
    """Returns an empty target schema for testing."""
    return SchemaView("""
id: http://example.org/target
name: target_schema
""")


def test_import_elements_copies_a_slot(empty_target_schema):
    """When no source, destination, or modifications are specified, the top-level slot definition
    should be copied from the source schema to the target schema as-is."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
            )
        ]
    )

    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slot 'a' was copied to the target schema
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "string"
    assert copied_slot.description == "Source slot a"


def test_import_elements_copies_a_slot_with_source(empty_target_schema):
    """When a source is specified but no destination or modifications, the induced slot definition
    from the specified class in the source schema should be copied to the target schema as-is."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: top-level description of slot a
classes:
  SourceClass:
    slots:
      - a
    slot_usage:
      a:
        description: Induced description of slot a in SourceClass
""")

    config = ImporterConfig(slots=[SlotImport(slot="a", source="SourceClass")])

    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the induced slot 'SourceClass.a' was copied to the target schema
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "string"
    assert copied_slot.description == "Induced description of slot a in SourceClass"


def test_import_elements_copies_a_slot_with_destinations():
    """When a destination is specified but no source or modifications, the top-level slot definition
    should be copied from the source schema to the target schema and associated with the destination
    classes."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
""")

    target_schema = SchemaView("""
id: http://example.org/target
name: target_schema
classes:
  DestinationClass1:
  DestinationClass2:
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a", destinations=["DestinationClass1", "DestinationClass2"]
            )
        ]
    )

    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=target_schema
    )

    # Check that the slot 'a' was copied to the target schema
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "string"
    assert copied_slot.description == "Source slot a"

    # Check that the slot 'a' was added to the specified target classes
    for class_name in config.slots[0].destinations:
        target_class = updated_target.get_class(class_name)
        assert target_class is not None
        assert "a" in target_class.slots


def test_import_elements_copies_a_slot_with_modifications(empty_target_schema):
    """When modifications are specified but no source or destination, the top-level slot definition
    should be copied from the source schema to the target schema with the modifications applied."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema                        
slots:
  a:
    range: string
    description: Source slot a
    examples:
      - value: example1
    multivalued: true
    pattern: ^[a-z]+$
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
                modifications=[
                    SlotModification(
                        # Replace the description and range
                        replace={
                            "description": "Modified description of slot a",
                            "range": "integer",
                        },
                        # Append to the examples list
                        append={
                            "examples": [{"value": "example2"}, {"value": "example3"}]
                        },
                        # Remove the multivalued attribute
                        remove=["multivalued"],
                    )
                ],
            )
        ]
    )
    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slot 'a' was copied to the target schema with modifications applied
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "integer"
    assert copied_slot.description == "Modified description of slot a"
    assert {
        ex.value if isinstance(ex, Example) else ex["value"]
        for ex in copied_slot.examples
    } == {"example1", "example2", "example3"}
    assert copied_slot.multivalued is None
    assert copied_slot.pattern == "^[a-z]+$"


def test_import_elements_copies_a_slot_with_modifications_for_specific_classes():
    """When modifications are specified with in_classes, the top-level slot definition
    should be copied from the source schema to the target schema with the modifications applied
    only to the slot_usage in the specified classes."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
""")

    target_schema = SchemaView("""
id: http://example.org/target
name: target_schema
classes:
  DestinationClass1:
  DestinationClass2:
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
                destinations=["DestinationClass1", "DestinationClass2"],
                modifications=[
                    SlotModification(
                        in_classes=["DestinationClass2"],
                        replace={
                            "description": "Modified description of slot a in DestinationClass1"
                        },
                    )
                ],
            )
        ]
    )

    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=target_schema
    )

    # Check that the slot 'a' was copied to the target schema
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "string"
    assert copied_slot.description == "Source slot a"

    # Check that the slot 'a' was added to DestinationClass1 without modification
    dest_class1_slot = updated_target.induced_slot("a", "DestinationClass1")
    assert dest_class1_slot.description == "Source slot a"

    # Check that the slot 'a' was added to DestinationClass2 with modification
    dest_class2_slot = updated_target.induced_slot("a", "DestinationClass2")
    assert (
        dest_class2_slot.description
        == "Modified description of slot a in DestinationClass1"
    )


def test_import_elements_fails_if_source_slot_not_found(empty_target_schema):
    """If the specified slot does not exist in the source schema, a ValueError should be raised."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="non_existent_slot",
            )
        ]
    )

    with pytest.raises(ValueError):
        import_elements(
            source_schema=source_schema,
            config=config,
            target_schema=empty_target_schema,
        )


def test_import_elements_fails_if_destination_class_not_found(empty_target_schema):
    """If a specified destination class does not exist in the target schema, a ValueError should be raised."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
                destinations=["NonExistentClass"],
            )
        ]
    )
    with pytest.raises(ValueError):
        import_elements(
            source_schema=source_schema,
            config=config,
            target_schema=empty_target_schema,
        )


def test_import_elements_performs_automatic_modifications(empty_target_schema):
    """When a slot is imported with modification, certain automatic modifications should be applied."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    description: Source slot a
    multivalued: true
    inlined: false
    inlined_as_list: true
  b:
    range: string
    recommended: true
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
                modifications=[
                    SlotModification(
                        replace={
                            "multivalued": False,
                        },
                    )
                ],
            ),
            SlotImport(
                slot="b",
                modifications=[
                    SlotModification(
                        replace={
                            "required": True,
                        },
                    )
                ],
            ),
        ]
    )
    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slot 'a' was copied to the target schema with automatic modifications applied
    slot_a = updated_target.get_slot("a")
    assert slot_a is not None
    assert slot_a.multivalued is False
    # 'inlined' and 'inlined_as_list' should be removed automatically
    assert slot_a.inlined is None
    assert slot_a.inlined_as_list is None

    # Check that the slot 'b' was copied to the target schema with automatic modifications applied
    slot_b = updated_target.get_slot("b")
    assert slot_b is not None
    assert slot_b.required is True
    # 'recommended' should be removed automatically
    assert slot_b.recommended is None


def test_import_elements_imports_slot_ancestors(empty_target_schema):
    """When a slot is imported, its ancestor slots should also be imported."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
  b:
  c:
  d:
    is_a: a
    mixins:
     - b
     - c
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="d",
            )
        ]
    )
    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slot 'd' was copied to the target schema
    slot_d = updated_target.get_slot("d")
    assert slot_d is not None
    assert slot_d.is_a == "a"
    assert slot_d.mixins == ["b", "c"]
    # Check that the ancestor slots 'a', 'b', and 'c' were also copied to the target schema
    for ancestor in ["a", "b", "c"]:
        slot = updated_target.get_slot(ancestor)
        assert slot is not None, f"Ancestor slot '{ancestor}' was not imported"


def test_import_elements_imports_slot_ranges(empty_target_schema):
    """When a slot is imported, its range (type, enum, or class) should also be imported."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
    slot_with_type:
        range: TestType
    slot_with_enum:
        range: TestEnum
    slot_with_class:
        range: TestClass
types:
    TestType:
        uri: xsd:integer
        base: int
enums:
    TestEnum:
        permissible_values:
            VALUE1:
            VALUE2:
classes:
    TestClass:
""")

    config = ImporterConfig(
        slots=[
            SlotImport(slot="slot_with_type"),
            SlotImport(slot="slot_with_enum"),
            SlotImport(slot="slot_with_class"),
        ]
    )
    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slots were copied to the target schema
    for slot_name in [
        "slot_with_type",
        "slot_with_enum",
        "slot_with_class",
    ]:
        slot = updated_target.get_slot(slot_name)
        assert slot is not None, f"Slot '{slot_name}' was not imported"

    # Check that the type 'TestType' was copied to the target schema
    type_def = updated_target.get_type("TestType")
    assert type_def is not None, "Type 'TestType' was not imported"
    assert type_def.uri == "xsd:integer"
    assert type_def.base == "int"

    # Check that the enum 'TestEnum' was copied to the target schema
    enum_def = updated_target.get_enum("TestEnum")
    assert enum_def is not None, "Enum 'TestEnum' was not imported"
    assert set(enum_def.permissible_values.keys()) == {"VALUE1", "VALUE2"}

    # Check that the class 'TestClass' was copied to the target schema
    class_def = updated_target.get_class("TestClass")
    assert class_def is not None, "Class 'TestClass' was not imported"


def test_import_elements_does_not_import_range_if_modified(empty_target_schema):
    """When a slot is imported with a modification to its range, the original range should not be imported."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
    slot_with_type:
        range: TestType
types:
    TestType:
        uri: xsd:integer
        base: int
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="slot_with_type",
                modifications=[
                    SlotModification(
                        replace={
                            "range": "string",
                        },
                    )
                ],
            )
        ]
    )
    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )
    # Check that the slot was copied to the target schema with modified range
    slot = updated_target.get_slot("slot_with_type")
    assert slot is not None, "Slot 'slot_with_type' was not imported"
    assert slot.range == "string"
    # Check that the type 'TestType' was NOT copied to the target schema
    type_def = updated_target.get_type("TestType")
    assert type_def is None, "Type 'TestType' should not have been imported"


def test_import_elements_removes_domain_and_owner(empty_target_schema):
    """When a slot is imported, its domain and owner attributes should be removed."""

    source_schema = SchemaView("""
id: http://example.org/source
name: source_schema
slots:
  a:
    range: string
    domain_of: SomeClass
    owner: SomeClass
classes:
  SomeClass:
    slots:
      - a
""")

    config = ImporterConfig(
        slots=[
            SlotImport(
                slot="a",
            )
        ]
    )

    updated_target = import_elements(
        source_schema=source_schema, config=config, target_schema=empty_target_schema
    )

    # Check that the slot 'a' was copied to the target schema
    copied_slot = updated_target.get_slot("a")
    assert copied_slot is not None
    assert copied_slot.range == "string"
    # Check that the domain and owner attributes were removed
    assert copied_slot.domain_of == []
    assert copied_slot.owner is None
