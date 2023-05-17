"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from nmdc_submission_schema.datamodel.nmdc_submission_schema import SampleData

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "valid")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))

MAIN_SCHEMA_CLASS_NAME = SampleData.class_name

ACCEPTABLE_PREFIX = DATA_DIR + "/" + MAIN_SCHEMA_CLASS_NAME


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            print()
            print(f"Testing {path}")
            if path.startswith(ACCEPTABLE_PREFIX):
                obj = yaml_loader.load(path, target_class=SampleData)
                assert obj
            else:
                print()
                print(f"{path} does not match {ACCEPTABLE_PREFIX} so will not be tested")
