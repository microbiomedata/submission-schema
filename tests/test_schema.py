import unittest
from pathlib import Path

from linkml_runtime import SchemaView

SCHEMA_YAML_PATH = Path(__file__).parent / "../src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"


class TestSchema(unittest.TestCase):
    """Tests that the schema itself is well-formed, outside any specific data instances"""

    def test_excel_worksheet_name_annotations(self):
        """Test that all DhInterface subclasses have an excel_worksheet_name annotation and that its
        value is not longer than 31 characters, which is the maximum length of a worksheet name in
        Excel.
        """

        schema_view = SchemaView(SCHEMA_YAML_PATH)
        for class_name, class_def in schema_view.all_classes().items():
            if class_def.is_a != "DhInterface":
                continue

            excel_worksheet_name_annotation = class_def.annotations.get("excel_worksheet_name")
            self.assertIsNotNone(
                excel_worksheet_name_annotation,
                f"Missing excel_worksheet_name annotation for {class_name}"
            )
            self.assertLessEqual(
                len(excel_worksheet_name_annotation.value),
                31,
                f"excel_worksheet_name \"{excel_worksheet_name_annotation.value}\" is too long"
            )
