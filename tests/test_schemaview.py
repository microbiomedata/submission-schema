import unittest

from linkml_runtime import SchemaView


class SchemaViewTest(unittest.TestCase):

    def test_schemaview(self):
        v = SchemaView("https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml")
        x = v.get_class("Activity")
        self.assertTrue(True)
