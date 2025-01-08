"""Tests that the schema itself is well-formed, outside any specific data instances"""

import re
from copy import deepcopy
from pathlib import Path

from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime import SchemaView

SCHEMA_YAML_PATH = (
    Path(__file__).parent
    / "../src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"
)

TEMPLATE_INSTANCES = {
    "AirInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "BiofilmInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "BuiltEnvInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
    },
    "EmslInterface": {
        "analysis_type": ["metagenomics"],
        "samp_name": "000001",
        "project_id": "123456",
        "sample_type": "soil",
        "sample_shipped": "1 g",
        "emsl_store_temp": -80,
    },
    "HcrCoresInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "HcrFluidsSwabsInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "HostAssociatedInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "JgiMgInterface": {
        "analysis_type": ["metagenomics"],
        "dna_concentration": 0.0,
        "dna_cont_type": "plate",
        "dna_cont_well": "C5",
        "dna_container_id": "0000001",
        "dna_dnase": "no",
        "dna_isolate_meth": "lorem ipsum",
        "dna_project_contact": "dolor sit amet",
        "dna_samp_id": "000001",
        "dna_sample_format": "Water",
        "dna_sample_name": "000001",
        "dna_seq_project": "100000",
        "dna_seq_project_name": "100000",
        "dna_seq_project_pi": "Morbi posuere nisi",
        "dna_volume": 1.0,
        "proposal_dna": "100001",
        "samp_name": "000001",
    },
    "JgiMgLrInterface": {
        "analysis_type": ["metagenomics"],
        "dna_absorb1": 0.0,
        "dna_absorb2": 0.0,
        "dna_concentration": 0.0,
        "dna_cont_type": "plate",
        "dna_cont_well": "C5",
        "dna_container_id": "0000001",
        "dna_dnase": "no",
        "dna_isolate_meth": "lorem ipsum",
        "dna_project_contact": "dolor sit amet",
        "dna_samp_id": "000001",
        "dna_sample_format": "Water",
        "dna_sample_name": "000001",
        "dna_seq_project": "100000",
        "dna_seq_project_name": "100000",
        "dna_seq_project_pi": "Morbi posuere nisi",
        "dna_volume": 1.0,
        "proposal_dna": "100001",
        "samp_name": "000001",
    },
    "JgiMtInterface": {
        "analysis_type": ["metatranscriptomics"],
        "dnase_rna": "no",
        "proposal_rna": "100001",
        "rna_concentration": 0.0,
        "rna_cont_type": "plate",
        "rna_cont_well": "C5",
        "rna_container_id": "0000001",
        "rna_isolate_meth": "lorem ipsum",
        "rna_project_contact": "dolor sit amet",
        "rna_samp_id": "000001",
        "rna_sample_format": "Water",
        "rna_sample_name": "000001",
        "rna_seq_project": "100000",
        "rna_seq_project_name": "100000",
        "rna_seq_project_pi": "Morbi posuere nisi",
        "rna_volume": 1.0,
        "samp_name": "000001",
    },
    "MiscEnvsInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "PlantAssociatedInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "growth_facil": "field",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "SedimentInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "depth": "1-2",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "SoilInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "depth": "1-2",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "growth_facil": "field",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
        "store_cond": "fresh",
    },
    "WastewaterSludgeInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "elev": 0.0,
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "lat_lon": "0.0 0.0",
        "samp_name": "000001",
        "samp_store_temp": "0 C",
    },
    "WaterInterface": {
        "analysis_type": ["metagenomics"],
        "collection_date": "1970-01-01",
        "depth": "1",
        "env_broad_scale": "lorem ipsum [ENVO:00000001]",
        "env_local_scale": "dolor sit amet [ENVO:00000002]",
        "env_medium": "consectetur [ENVO:00000003]",
        "geo_loc_name": "Country: Province, City",
        "samp_name": "000001",
    },
}


def test_excel_worksheet_name_annotations():
    """Test that all DhInterface subclasses have an excel_worksheet_name annotation and that its
    value is not longer than 31 characters, which is the maximum length of a worksheet name in
    Excel.
    """

    schema_view = SchemaView(SCHEMA_YAML_PATH)
    for class_name, class_def in schema_view.all_classes().items():
        if class_def.is_a != "DhInterface":
            continue

        excel_worksheet_name_annotation = class_def.annotations.get(
            "excel_worksheet_name"
        )
        assert (
            excel_worksheet_name_annotation is not None
        ), f"Missing excel_worksheet_name annotation for {class_name}"

        assert (
            len(excel_worksheet_name_annotation.value) <= 31
        ), f'excel_worksheet_name "{excel_worksheet_name_annotation.value}" is too long'


def test_examples():
    """Verify that the examples listed in slot definitions are valid"""
    schema_view = SchemaView(SCHEMA_YAML_PATH)
    validator = Validator(
        schema=schema_view.schema,
        strict=True,
        validation_plugins=[
            JsonschemaValidationPlugin(closed=True),
        ],
    )

    for class_def in schema_view.all_classes().values():
        if class_def.mixin or class_def.abstract:
            continue

        if class_def.name not in TEMPLATE_INSTANCES:
            continue

        instance = TEMPLATE_INSTANCES[class_def.name]
        report = validator.validate(instance, target_class=class_def.name)
        assert (
            report.results == []
        ), f"Template instance for {class_def.name} failed validation"

        slots = schema_view.class_induced_slots(class_def.name)
        for slot in slots:
            if not slot.examples:
                continue

            for example in slot.examples:
                new_instance = deepcopy(instance)

                new_value = example.value
                if not new_value:
                    continue
                if slot.multivalued:
                    new_value = re.split(";\\s*", new_value)
                if slot.range == "integer":
                    new_value = int(new_value)
                elif slot.range == "float":
                    new_value = float(new_value)
                elif slot.range == "double":
                    new_value = float(new_value)

                new_instance[slot.name] = new_value
                report = validator.validate(new_instance, target_class=class_def.name)
                assert (
                    report.results == []
                ), f"Example '{example}' on {class_def.name}.{slot.name} failed validation"
