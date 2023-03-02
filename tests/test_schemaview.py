import unittest

from linkml_runtime import SchemaView


class SchemaViewTest(unittest.TestCase):

    def test_schemaview(self):
        v = SchemaView(
            "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/nmdc_schema/nmdc_materialized_patterns.yaml")
        print(v.schema.name)
        v.get_class("Activity")
        # x = v.get_class("Activity")
        self.assertTrue(True)
