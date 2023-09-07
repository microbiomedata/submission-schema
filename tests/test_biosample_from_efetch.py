import os
import pprint
import time
import unittest

import requests
import xmltodict
import yaml
from linkml.validators import JsonSchemaDataValidator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper, yaml_dumper  # for dict dumping

# do we need to tolerate these? https://www.insdc.org/submitting-standards/missing-value-reporting/


data_file = "../src/data/valid/SampleData-soil-data-minimal.yaml"
schema_file = "../src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml"

fetch_base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
search_base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
retmax = 100  # todo would probably have to write iterative searches for > 300

biosample_id = "SAMN27723301"

desired_package = 'MIMS.me.soil.6.0'  # todo should also allow user to specify a free-form entrez query

target_class_name = "SoilInterface"

excused_slots = [
    'analysis_type',  # todo this isn't getting excused!
    'growth_facil',
    'samp_store_temp',
    'store_cond',
]


class TestBiosampleFromEfetch(unittest.TestCase):
    """Test if a Biosample obtained from the efetch API satisfies class SoilInterface."""

    def test_biosample_from_efetch(self):
        with open(data_file) as f:
            one_soil_interface = yaml.safe_load(f)['soil_data'][0]

        print(f"\nContents of {data_file}:")
        pprint.pprint(one_soil_interface)

        validator = JsonSchemaDataValidator(schema_file)

        # todo: I tried to instantiate a SoilInterface object but
        #   eve though I asserted elev=111.0, the validator complained that it was a string

        pre_validation = validator.iter_validate_dict(one_soil_interface,
                                                      target_class_name=target_class_name)  # Expected type 'ClassDefinitionName | None', got 'str' instead
        error_count = 0
        for error in pre_validation:
            error_count += 1
            print(f"{error} in {data_file}")
        if not error_count:
            print(f"No errors found in {data_file}")

        self.assertEquals(error_count, 0)

        params = {
            "db": "biosample",
            "id": biosample_id,
        }
        biosample_efetch_xml = requests.get(url=fetch_base, params=params)
        biosample_etetch_initial_parse = xmltodict.parse(biosample_efetch_xml.text)

        self.assertIn("BioSampleSet", biosample_etetch_initial_parse)
        self.assertIn("BioSample", biosample_etetch_initial_parse["BioSampleSet"])

        biosample_efetch_dict = biosample_etetch_initial_parse['BioSampleSet']['BioSample']

        self.assertIsNotNone(biosample_efetch_dict)

        print(f"\nContents of {biosample_id}:")
        pprint.pprint(biosample_efetch_dict)

        # project the NCBI Biosample's attributes onto the known valid example
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

        post_validation = validator.iter_validate_dict(one_soil_interface, target_class_name=target_class_name)
        error_count = 0
        for error in post_validation:
            error_count += 1
            print(f"{error} when overlaid with {biosample_id}")
        if not error_count:
            print(f"No errors found in {biosample_id}")

        # self.assertEqual(error_count, 0)

    def test_get_by_package(self):

        # print(f"Creating a SchemaView from {schema_file}...")
        nmdc_view = SchemaView(schema_file)
        # print(f"SchemaView created from {schema_file}.")

        target_class = nmdc_view.get_class(target_class_name)
        target_class_name_obj = target_class.name

        target_class_slots = nmdc_view.class_induced_slots(target_class_name_obj)
        target_class_slot_names = [slot.name for slot in target_class_slots]

        enforced_slot_names = list(set(target_class_slot_names) - set(
            excused_slots))  # todo should make these non-required instead of removing them from the class # also, why does analysis_type remain required/associated?
        enforced_slot_names.sort()
        target_class.slots = enforced_slot_names
        # target_class.slot_usage = None
        # todo remove excluded slots from mixins?

        # print(yaml_dumper.dumps(target_class))

        validator = JsonSchemaDataValidator(nmdc_view.schema)

        package_query = desired_package
        package_query = package_query.lower()
        package_query = package_query.replace('.', ' ')
        package_query = f"{package_query}[filter]"

        params = {
            "db": "biosample",
            "retmax": retmax,
            "term": package_query,
        }
        biosample_esearch_xml = requests.get(url=search_base,
                                             params=params)  # todo iterate over retmax chunks # might require a brief sleep between iterations
        biosample_esearch_initial_parse = xmltodict.parse(biosample_esearch_xml.text)
        ids = biosample_esearch_initial_parse['eSearchResult']['IdList']['Id']

        del biosample_esearch_initial_parse['eSearchResult']['IdList']['Id']
        # pprint.pprint(biosample_esearch_initial_parse)

        params = {
            "db": "biosample",
            "id": ids,
        }
        biosample_efetch_xml = requests.post(url=fetch_base, params=params)  # todo see iteration above
        biosample_etetch_initial_parse = xmltodict.parse(biosample_efetch_xml.text)
        returned_biosamples = biosample_etetch_initial_parse['BioSampleSet']['BioSample']

        for returned_biosample in returned_biosamples:
            current_dict = {}
            # pprint.pprint(returned_biosample)
            if "Models" in returned_biosample and "Model" in returned_biosample["Models"]:
                model_tokens = returned_biosample["Models"]["Model"].split(".")
                current_extension = model_tokens[-1]
                current_dict['env_package'] = current_extension
            current_attributes = returned_biosample['Attributes']['Attribute']
            for current_attribute in current_attributes:
                if current_attribute['@harmonized_name'] == "project_name":
                    continue
                elif current_attribute['@harmonized_name'] == "sample_name":
                    current_dict['samp_name'] = current_attribute['#text']
                elif current_attribute['@harmonized_name'] == "elev":
                    try:
                        current_dict['elev'] = float(current_attribute['#text'])
                    except ValueError:
                        print(
                            f"Could not convert {current_attribute['@harmonized_name']} of {current_attribute['#text']} to float from {biosample_id}")
                        current_dict['elev'] = current_attribute['#text']
                elif current_attribute['@harmonized_name'] not in target_class_slot_names:
                    print(
                        f"Attribute {current_attribute['@harmonized_name']} is not known to {target_class_name} from {biosample_id}")
                    # todo some of these could be mapped to a slot that IS associated with the class
                    #   why are some of those attributes in there anyway? breed etc doesn't seem like soil sample attributes
                else:
                    if "@harmonized_name" in current_attribute:
                        current_dict[current_attribute['@harmonized_name']] = current_attribute['#text']
            # pprint.pprint(current_dict)

            validation = validator.iter_validate_dict(current_dict, target_class_name=target_class_name_obj)
            error_count = 0
            for error in validation:
                error_count += 1
                print(f"{error} from {biosample_id}")
            if not error_count:
                print(f"No errors found in {biosample_id}")

        #     self.assertEquals(returned_package, desired_package)
        #
        #     # sleep a little to avoid NCBI's rate limit
        #     time.sleep(0.25)

# find package=MIMS.me.soil.6.0 Biosamples

# Base URL
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
#
# Required Parameters
# db
# Database to search. Value must be a valid Entrez database name (default = pubmed).
#
# term
# Entrez text query. All special characters must be URL encoded. Spaces may be replaced by '+' signs. For very long queries (more than several hundred characters long), consider using an HTTP POST call. See the PubMed or Entrez help for information about search field descriptions and tags. Search fields and tags are database specific.
#
# esearch.fcgi?db=pubmed&term=asthma

# sshproxy.sh -u <NERSC_USER_NAME>
# ssh -i ~/.ssh/nersc -L 15432:biosample-postgres-loadbalancer.mam.production.svc.spin.nersc.org:5432 <NERSC_USER_NAME>@dtn01.nersc.gov

# select
# 	package,
# 	count(1)
# from
# 	non_attribute_metadata nam
# group by
# 	package
# order by
# 	package ;

# |package                                 |count     |
# |----------------------------------------|----------|
# |Beta-lactamase.1.0                      |833       |
# |Generic.1.0                             |21,267,429|
# |Human.1.0                               |754,697   |
# |Invertebrate.1.0                        |322,755   |
# |Metagenome.environmental.1.0            |2,284,135 |
# |Microbe.1.0                             |621,323   |
# |MIGS.ba.6.0                             |41,949    |
# |MIGS.ba.agriculture.6.0                 |31        |
# |MIGS.ba.air.6.0                         |62        |
# |MIGS.ba.built.6.0                       |686       |
# |MIGS.ba.food-animal.6.0                 |16        |
# |MIGS.ba.food-farm_env.6.0               |2         |
# |MIGS.ba.food-human_foods.6.0            |54        |
# |MIGS.ba.food-prod_facility.6.0          |44        |
# |MIGS.ba.host-associated.6.0             |13,466    |
# |MIGS.ba.human-associated.6.0            |18,830    |
# |MIGS.ba.human-gut.6.0                   |16,498    |
# |MIGS.ba.human-oral.6.0                  |562       |
# |MIGS.ba.human-skin.6.0                  |3,919     |
# |MIGS.ba.human-vaginal.6.0               |456       |
# |MIGS.ba.microbial.6.0                   |565       |
# |MIGS.ba.miscellaneous.6.0               |1,897     |
# |MIGS.ba.plant-associated.6.0            |4,590     |
# |MIGS.ba.sediment.6.0                    |1,238     |
# |MIGS.ba.soil.6.0                        |4,368     |
# |MIGS.ba.symbiont-associated.6.0         |8         |
# |MIGS.ba.wastewater.6.0                  |2,741     |
# |MIGS.ba.water.6.0                       |5,210     |
# |MIGS.eu.6.0                             |153,717   |
# |MIGS.eu.agriculture.6.0                 |306       |
# |MIGS.eu.air.6.0                         |645       |
# |MIGS.eu.built.6.0                       |251       |
# |MIGS.eu.food-animal.6.0                 |21        |
# |MIGS.eu.food-human_foods.6.0            |2         |
# |MIGS.eu.food-prod_facility.6.0          |20        |
# |MIGS.eu.host-associated.6.0             |12,664    |
# |MIGS.eu.human-associated.6.0            |4,646     |
# |MIGS.eu.human-gut.6.0                   |837       |
# |MIGS.eu.human-oral.6.0                  |44        |
# |MIGS.eu.human-skin.6.0                  |44        |
# |MIGS.eu.human-vaginal.6.0               |1         |
# |MIGS.eu.microbial.6.0                   |302       |
# |MIGS.eu.miscellaneous.6.0               |1,314     |
# |MIGS.eu.plant-associated.6.0            |12,081    |
# |MIGS.eu.sediment.6.0                    |286       |
# |MIGS.eu.soil.6.0                        |1,399     |
# |MIGS.eu.symbiont-associated.6.0         |101       |
# |MIGS.eu.wastewater.6.0                  |28        |
# |MIGS.eu.water.6.0                       |5,881     |
# |MIGS.vi.6.0                             |1,104     |
# |MIGS.vi.agriculture.6.0                 |7         |
# |MIGS.vi.food-animal.6.0                 |38        |
# |MIGS.vi.host-associated.6.0             |703       |
# |MIGS.vi.human-associated.6.0            |1,685     |
# |MIGS.vi.human-gut.6.0                   |2,198     |
# |MIGS.vi.human-oral.6.0                  |139       |
# |MIGS.vi.human-skin.6.0                  |54        |
# |MIGS.vi.microbial.6.0                   |6         |
# |MIGS.vi.miscellaneous.6.0               |212       |
# |MIGS.vi.plant-associated.6.0            |125       |
# |MIGS.vi.sediment.6.0                    |2         |
# |MIGS.vi.soil.6.0                        |31        |
# |MIGS.vi.wastewater.6.0                  |417       |
# |MIGS.vi.water.6.0                       |109       |
# |MIMAG.6.0                               |24,434    |
# |MIMAG.agriculture.6.0                   |1         |
# |MIMAG.air.6.0                           |6         |
# |MIMAG.built.6.0                         |165       |
# |MIMAG.host-associated.6.0               |19,576    |
# |MIMAG.human-associated.6.0              |1,242     |
# |MIMAG.human-gut.6.0                     |31,799    |
# |MIMAG.human-oral.6.0                    |543       |
# |MIMAG.human-vaginal.6.0                 |564       |
# |MIMAG.microbial.6.0                     |3,975     |
# |MIMAG.miscellaneous.6.0                 |1,268     |
# |MIMAG.plant-associated.6.0              |1,090     |
# |MIMAG.sediment.6.0                      |17,050    |
# |MIMAG.soil.6.0                          |4,826     |
# |MIMAG.symbiont-associated.6.0           |30        |
# |MIMAG.wastewater.6.0                    |17,751    |
# |MIMAG.water.6.0                         |16,739    |
# |MIMARKS.specimen.6.0                    |17,281    |
# |MIMARKS.specimen.air.6.0                |182       |
# |MIMARKS.specimen.built.6.0              |529       |
# |MIMARKS.specimen.food-animal.6.0        |32        |
# |MIMARKS.specimen.food-farm_env.6.0      |32        |
# |MIMARKS.specimen.food-human_foods.6.0   |57        |
# |MIMARKS.specimen.host-associated.6.0    |55,503    |
# |MIMARKS.specimen.human-associated.6.0   |18,523    |
# |MIMARKS.specimen.human-gut.6.0          |28,355    |
# |MIMARKS.specimen.human-oral.6.0         |9,770     |
# |MIMARKS.specimen.human-skin.6.0         |1,350     |
# |MIMARKS.specimen.human-vaginal.6.0      |8,377     |
# |MIMARKS.specimen.microbial.6.0          |1,546     |
# |MIMARKS.specimen.miscellaneous.6.0      |5,336     |
# |MIMARKS.specimen.plant-associated.6.0   |11,001    |
# |MIMARKS.specimen.sediment.6.0           |2,234     |
# |MIMARKS.specimen.soil.6.0               |11,522    |
# |MIMARKS.specimen.symbiont-associated.6.0|84        |
# |MIMARKS.specimen.wastewater.6.0         |1,991     |
# |MIMARKS.specimen.water.6.0              |6,592     |
# |MIMARKS.survey.agriculture.6.0          |672       |
# |MIMARKS.survey.air.6.0                  |2,439     |
# |MIMARKS.survey.built.6.0                |5,860     |
# |MIMARKS.survey.food-animal.6.0          |43        |
# |MIMARKS.survey.food-farm_env.6.0        |481       |
# |MIMARKS.survey.food-human_foods.6.0     |109       |
# |MIMARKS.survey.host-associated.6.0      |188,317   |
# |MIMARKS.survey.human-associated.6.0     |68,271    |
# |MIMARKS.survey.human-gut.6.0            |103,816   |
# |MIMARKS.survey.human-oral.6.0           |34,783    |
# |MIMARKS.survey.human-skin.6.0           |11,211    |
# |MIMARKS.survey.human-vaginal.6.0        |28,165    |
# |MIMARKS.survey.microbial.6.0            |7,205     |
# |MIMARKS.survey.miscellaneous.6.0        |42,912    |
# |MIMARKS.survey.plant-associated.6.0     |94,289    |
# |MIMARKS.survey.sediment.6.0             |21,592    |
# |MIMARKS.survey.soil.6.0                 |102,823   |
# |MIMARKS.survey.symbiont-associated.6.0  |58        |
# |MIMARKS.survey.wastewater.6.0           |16,029    |
# |MIMARKS.survey.water.6.0                |70,715    |
# |MIMS.me.agriculture.6.0                 |322       |
# |MIMS.me.air.6.0                         |4,451     |
# |MIMS.me.built.6.0                       |3,755     |
# |MIMS.me.food-animal.6.0                 |124       |
# |MIMS.me.food-farm_env.6.0               |63        |
# |MIMS.me.food-human_foods.6.0            |376       |
# |MIMS.me.food-prod_facility.6.0          |30        |
# |MIMS.me.host-associated.6.0             |129,136   |
# |MIMS.me.human-associated.6.0            |40,837    |
# |MIMS.me.human-gut.6.0                   |125,745   |
# |MIMS.me.human-oral.6.0                  |28,320    |
# |MIMS.me.human-skin.6.0                  |18,814    |
# |MIMS.me.human-vaginal.6.0               |10,142    |
# |MIMS.me.microbial.6.0                   |6,222     |
# |MIMS.me.miscellaneous.6.0               |20,011    |
# |MIMS.me.plant-associated.6.0            |49,874    |
# |MIMS.me.sediment.6.0                    |19,345    |
# |MIMS.me.soil.6.0                        |95,799    |
# |MIMS.me.symbiont-associated.6.0         |116       |
# |MIMS.me.wastewater.6.0                  |14,864    |
# |MIMS.me.water.6.0                       |55,341    |
# |MISAG.6.0                               |864       |
# |MISAG.built.6.0                         |3         |
# |MISAG.food-animal.6.0                   |2         |
# |MISAG.food-farm_env.6.0                 |16        |
# |MISAG.host-associated.6.0               |757       |
# |MISAG.human-associated.6.0              |498       |
# |MISAG.human-gut.6.0                     |863       |
# |MISAG.human-skin.6.0                    |825       |
# |MISAG.human-vaginal.6.0                 |1         |
# |MISAG.microbial.6.0                     |14        |
# |MISAG.miscellaneous.6.0                 |109       |
# |MISAG.plant-associated.6.0              |185       |
# |MISAG.sediment.6.0                      |115       |
# |MISAG.soil.6.0                          |4,845     |
# |MISAG.symbiont-associated.6.0           |2         |
# |MISAG.wastewater.6.0                    |37        |
# |MISAG.water.6.0                         |8,259     |
# |MIUVIG.6.0                              |494       |
# |MIUVIG.built.6.0                        |4         |
# |MIUVIG.host-associated.6.0              |482       |
# |MIUVIG.human-associated.6.0             |262       |
# |MIUVIG.human-gut.6.0                    |418       |
# |MIUVIG.human-oral.6.0                   |43        |
# |MIUVIG.human-vaginal.6.0                |1         |
# |MIUVIG.microbial.6.0                    |47        |
# |MIUVIG.plant-associated.6.0             |41        |
# |MIUVIG.sediment.6.0                     |5         |
# |MIUVIG.wastewater.6.0                   |127       |
# |MIUVIG.water.6.0                        |40        |
# |Model.organism.animal.1.0               |863,133   |
# |OneHealthEnteric.1.0                    |4,144     |
# |Pathogen.cl.1.0                         |1,348,668 |
# |Pathogen.env.1.0                        |417,257   |
# |Plant.1.0                               |904,032   |
# |SARS-CoV-2.cl.1.0                       |3,240,748 |
# |SARS-CoV-2.wwsurv.1.0                   |63,633    |
# |Virus.1.0                               |34,962    |
