import os
import pprint
import unittest

import requests
import xmltodict
import yaml
from linkml.validators import JsonSchemaDataValidator
from linkml_runtime.dumpers import json_dumper

from nmdc_submission_schema.datamodel.nmdc_submission_schema import SoilInterface

data_file = "../src/data/valid/SampleData-soil-data-minimal.yaml"
schema_file = "../src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"
biosample_id = "SAMN27723301"


class TestBiosampleFromEfetch(unittest.TestCase):
    """Test if a Biosample obtained from the efetch API satisfies class SoilInterface."""

    def test_biosample_from_efetch(self):
        with open(data_file) as f:
            one_soil_interface = yaml.safe_load(f)['soil_data'][0]

        pprint.pprint(one_soil_interface)

        print(f"\nContents of {data_file}:")
        pprint.pprint(one_soil_interface)

        validator = JsonSchemaDataValidator(schema_file)

        # si = SoilInterface(
        #     analysis_type=['metagenomics'],
        #     collection_date='1999-11-11',  # SAMN27723301
        #     depth='111 - 222',  # SAMN27723301
        #     elev="111.0",  # SAMN27723301
        #     env_broad_scale='arid biome [ENVO:01001838]',  # SAMN27723301
        #     env_local_scale='astronomical body part [ENVO:01000813]',  # SAMN27723301
        #     env_medium='pathogen-suppressive soil [ENVO:03600036]',  # SAMN27723301
        #     env_package="xxx",
        #     geo_loc_name='nation: state, location',  # SAMN27723301
        #     growth_facil='experimental_garden',
        #     lat_lon='11 11',  # SAMN27723301
        #     samp_name='SAMN27723301',
        #     samp_store_temp='111 units',
        #     store_cond='fresh',
        # )
        #
        # si_dict = json_dumper.to_dict(si)

        pre_validation = validator.iter_validate_dict(one_soil_interface, target_class_name=SoilInterface.class_name)
        error_count = 0
        for error in pre_validation:
            error_count += 1
            print(f"{error} in {data_file}")
        if not error_count:
            print(f"No errors found in {data_file}")

        params = {
            "db": "biosample",
            "id": biosample_id,
        }
        biosample_etetch_xml = requests.get(url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                                            params=params)

        biosample_efetch_dict = xmltodict.parse(biosample_etetch_xml.text)['BioSampleSet']['BioSample']

        print(f"\nContents of {biosample_id}:")
        pprint.pprint(biosample_efetch_dict)

        if 'Package' in biosample_efetch_dict:
            if '#text' in biosample_efetch_dict['Package']:
                one_soil_interface['env_package'] = biosample_efetch_dict['Package']['#text']

        if '@accession' in biosample_efetch_dict:
            one_soil_interface['samp_name'] = biosample_efetch_dict['@accession']

        for i in biosample_efetch_dict['Attributes']['Attribute']:
            if '@harmonized_name' in i:
                one_soil_interface[i['@harmonized_name']] = i['#text']

        print(f"\nContents of {data_file} overlaid with {biosample_id}:")
        pprint.pprint(one_soil_interface)

        post_validation = validator.iter_validate_dict(one_soil_interface, target_class_name=SoilInterface.class_name)
        error_count = 0
        for error in post_validation:
            error_count += 1
            print(f"{error} when overlaid with {biosample_id}")
        if not error_count:
            print(f"No errors found in {biosample_id}")

        self.assertEqual(error_count, 0)
