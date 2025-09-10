import pytest
from linkml_runtime import SchemaView

from nmdc_submission_schema.schematools import remove_class


def test_remove_class_removes_class_and_unused_slots():
    """Test that remove_class correctly removes a class and its unused slots."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
classes:
  TestClass:
    slots:
      - a
""")
    remove_class(schema, "TestClass")
    assert "TestClass" not in schema.all_classes()
    assert "a" not in schema.all_slots()


def test_remove_class_handles_nonexistent_class():
    """Test that remove_class raises an error for a nonexistent class."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
classes:
  TestClass:
    slots:
      - a
""")
    with pytest.raises(
        ValueError, match="Class 'NonExistentClass' does not exist in the schema."
    ):
        remove_class(schema, "NonExistentClass")


def test_remove_class_error_on_class_referenced_via_inheritance():
    """Test that remove_class raises an error when the class is used as a class parent."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
classes:
  ParentClass:
    slots:
      - a
  ChildClass:
    is_a: ParentClass
""")
    with pytest.raises(
        ValueError, match="Class 'ParentClass' is referenced by other classes"
    ):
        remove_class(schema, "ParentClass")


def test_remove_class_error_on_class_referenced_as_slot_range():
    """Test that remove_class raises an error when the class is referenced as a slot range."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
  b:
    range: TestClass
classes:
  TestClass:
    slots:
      - a
""")
    with pytest.raises(
        ValueError, match="Class 'TestClass' is used as the range of slot 'b'"
    ):
        remove_class(schema, "TestClass")


def test_remove_class_with_force_removes_class_referenced_via_inheritance():
    """Test that remove_class with force=True removes a class even if it is used as a parent class."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
classes:
  ParentClass:
    slots:
      - a
  ChildClass:
    is_a: ParentClass
""")
    remove_class(schema, "ParentClass", force=True)
    assert "ParentClass" not in schema.all_classes()
    assert "a" not in schema.all_slots()
    # ChildClass should still exist even though its parent was removed
    assert "ChildClass" in schema.all_classes()


def test_remove_class_with_force_removes_class_referenced_as_slot_range():
    """Test that remove_class with force=True removes a class even if it is used as a slot range."""
    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
    range: string
  b:
    range: TestClass
classes:
  TestClass:
    slots:
        - a
""")
    remove_class(schema, "TestClass", force=True)
    assert "TestClass" not in schema.all_classes()
    assert "a" not in schema.all_slots()
    # Slot 'b' should still exist even though its range was removed
    assert "b" in schema.all_slots()


def test_remove_class_removes_dangling_classes():
    """Test that remove_class with remove_dangling_classes=True removes classes that become dangling."""

    schema = SchemaView("""
id: http://example.org/test
name: TestSchema
slots:
  a:
  b:
  c:
    range: DanglingClass
  d:
  e:
    is_a: d
classes:
  ParentClass:
    slots:
      - a
  TestClass:
    is_a: ParentClass
    slots:
      - b
      - c
  DanglingClass:
    slots:
      - d
  OtherClass:
    slots:
      - e
""")

    remove_class(schema, "TestClass", remove_dangling_classes=True)
    # Ensure that TestClass and its direct slots are removed
    assert "TestClass" not in schema.all_classes()
    assert "b" not in schema.all_slots()
    assert "c" not in schema.all_slots()
    # DanglingClass should be removed because it is no longer referenced
    assert "DanglingClass" not in schema.all_classes()
    # Slot 'd' should remain in the schema because it is referenced by slot 'e' which isn't removed
    assert "d" in schema.all_slots()
    # ParentClass and its slot should be removed because they are no longer referenced
    assert "ParentClass" not in schema.all_classes()
    assert "a" not in schema.all_slots()
    # OtherClass and its slot should remain because they were not referenced by the removed class
    assert "OtherClass" in schema.all_classes()
    assert "e" in schema.all_slots()
