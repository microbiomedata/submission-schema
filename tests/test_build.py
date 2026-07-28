"""Tests for the build-time schema transforms in tools/build.py"""

import pytest
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import Example, SchemaDefinition, SlotDefinition

from tools.build import scalarize_object_examples


def schema_with_slot(slot: SlotDefinition) -> SchemaView:
    schema = SchemaDefinition(id="https://example.org/test", name="test")
    schema.slots[slot.name] = slot
    return SchemaView(schema)


def only_slot(schema_view: SchemaView) -> SlotDefinition:
    return next(iter(schema_view.all_slots().values()))


def object_example(**kwargs) -> Example:
    example = Example()
    example.object = kwargs
    return example


# One case per wrapper class nmdc-schema uses, since the derivation claims a single rule
# covers all of them. Values are the real ones from nmdc-schema src/schema/mixs.yaml.
WRAPPER_EXAMPLES = [
    pytest.param(
        object_example(
            type="nmdc:QuantityValue",
            has_raw_value="20 Cel",
            has_numeric_value=20,
            has_unit="Cel",
        ),
        "20 Cel",
        id="QuantityValue",
    ),
    pytest.param(
        object_example(type="nmdc:TextValue", has_raw_value="deciduous forest"),
        "deciduous forest",
        id="TextValue",
    ),
    pytest.param(
        object_example(
            type="nmdc:ControlledIdentifiedTermValue",
            has_raw_value="soil [ENVO:00001998]",
            term={"id": "ENVO:00001998", "type": "nmdc:OntologyClass"},
        ),
        "soil [ENVO:00001998]",
        id="ControlledIdentifiedTermValue",
    ),
    pytest.param(
        object_example(
            type="nmdc:GeolocationValue",
            latitude=50.586825,
            longitude=6.408977,
            has_raw_value="50.586825 6.408977",
        ),
        "50.586825 6.408977",
        id="GeolocationValue",
    ),
]


@pytest.mark.parametrize("example,expected", WRAPPER_EXAMPLES)
def test_object_example_becomes_its_raw_value(example, expected):
    schema_view = schema_with_slot(SlotDefinition("s", examples=[example]))
    scalarize_object_examples(schema_view)
    derived = only_slot(schema_view).examples
    assert [e.value for e in derived] == [expected]
    assert [e.object for e in derived] == [None]


def test_scalar_examples_are_left_alone():
    """The build must keep working against a pinned nmdc-schema that has scalar examples."""
    schema_view = schema_with_slot(
        SlotDefinition("s", examples=[Example(value="20 Cel")])
    )
    scalarize_object_examples(schema_view)
    assert [e.value for e in only_slot(schema_view).examples] == ["20 Cel"]


def test_object_example_without_has_raw_value_is_left_alone():
    """Doi and other non-wrapper classes are not collapsed to scalars, so leave them be."""
    doi = object_example(type="nmdc:Doi", doi_value="doi:10.1234/5678")
    schema_view = schema_with_slot(SlotDefinition("s", examples=[doi]))
    scalarize_object_examples(schema_view)
    derived = only_slot(schema_view).examples
    assert derived[0].value is None
    assert derived[0].object is not None


def test_description_survives_derivation():
    """nmdc-schema puts submitter-facing guidance in the example description."""
    example = object_example(type="nmdc:QuantityValue", has_raw_value="5.46 mg/L")
    example.description = "Milligram per liter; roughly 1 to 20 mg/L is typical."
    schema_view = schema_with_slot(SlotDefinition("s", examples=[example]))
    scalarize_object_examples(schema_view)
    derived = only_slot(schema_view).examples[0]
    assert derived.value == "5.46 mg/L"
    assert derived.description == "Milligram per liter; roughly 1 to 20 mg/L is typical."


def test_slot_usage_examples_are_derived_too():
    """Biosample slot_usage overrides in nmdc-schema carry objectified examples as well."""
    from linkml_runtime.linkml_model import ClassDefinition

    schema = SchemaDefinition(id="https://example.org/test", name="test")
    schema.slots["s"] = SlotDefinition("s")
    cls = ClassDefinition("C", slots=["s"])
    cls.slot_usage["s"] = SlotDefinition(
        "s", examples=[object_example(type="nmdc:TextValue", has_raw_value="4 mm sieved")]
    )
    schema.classes["C"] = cls
    schema_view = SchemaView(schema)

    scalarize_object_examples(schema_view)

    usage = schema_view.get_class("C").slot_usage["s"]
    assert [e.value for e in usage.examples] == ["4 mm sieved"]


def test_mixed_examples_on_one_slot():
    """A config override can leave a hand-authored scalar next to an inherited object."""
    schema_view = schema_with_slot(
        SlotDefinition(
            "s",
            examples=[
                Example(value="hand written"),
                object_example(type="nmdc:TextValue", has_raw_value="from nmdc-schema"),
            ],
        )
    )
    scalarize_object_examples(schema_view)
    assert [e.value for e in only_slot(schema_view).examples] == [
        "hand written",
        "from nmdc-schema",
    ]
