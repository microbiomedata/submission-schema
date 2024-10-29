# could check globally, targeted in slot usages, or in all induced slots from all classes
# check though validation of an instance? requires population of all other required slots too
from pathlib import Path

from jsonasobj2 import JsonObj
from linkml_runtime import SchemaView
from collections import defaultdict
import csv

#
# tsv_file = Path("../schema/nmdc_submission_schema.tsv")
#
# # how to load schema? hardcoded file path, or pathlib?

schema_file = Path("../nmdc_submission_schema/schema/nmdc_submission_schema.yaml")
schema_view = SchemaView(schema_file)  # time it

# # print(schema_view.schema.name)
#
# all_slots = schema_view.all_slots()
#
# attribute_usage_count = defaultdict(int)
#
# # Assume `slot_dict` is your dictionary with slot names as keys and SlotDefinitions as values
# for slot_name, slot_def in sorted(all_slots.items()):
#     # Use vars() to get the dictionary of attributes for the SlotDefinition object
#     attributes = vars(slot_def)
#
#     # Filter the attributes to only show the populated ones (excluding None, empty lists, etc.)
#     populated_attributes = {k: v for k, v in sorted(attributes.items()) if v not in [None, '', [], {}, ()]}
#
#     # Print or log the results as needed
#     # print(f"Slot Name: {slot_name}")
#     for attr_name, attr_value in populated_attributes.items():
#         # print(f"  {attr_name}: {attr_value}")
#         attribute_usage_count[attr_name] += 1
#
# # Convert defaultdict to a regular dict if needed
# attribute_usage_count = dict(attribute_usage_count)
#
# # Print or log the attribute usage count
# for attr_name, count in attribute_usage_count.items():
#     print(f"{attr_name}: {count}")
#
# # Prepare data for TSV file
# # Using an explicit type conversion to str for keys and values
# rows = [{'Attribute Name': str(attr_name), 'Usage Count': int(count)} for attr_name, count in
#         attribute_usage_count.items()]
#
# # Define the TSV file name
# tsv_file_name = "attribute_usage_count.tsv"
#
# # Write the results to a TSV file using DictWriter
# with open(tsv_file_name, mode='w', newline='') as tsv_file:
#     writer = csv.DictWriter(tsv_file, fieldnames=['Attribute Name', 'Usage Count'], delimiter='\t')
#     writer.writeheader()  # Write the header row
#     writer.writerows(rows)  # Write the data rows
#
# print(f"Attribute usage count has been saved to {tsv_file_name}")

all_classes = schema_view.all_classes()
all_class_names = all_classes.keys()

attribute_usage_count = defaultdict(int)

for class_name in sorted(all_class_names):
    print(f"Class Name: {class_name}")
    current_class = schema_view.induced_class(class_name)
    current_slots = current_class.attributes
    for slot_name, slot_def in sorted(current_slots.items()):
        # Use vars() to get the dictionary of attributes for the SlotDefinition object
        attributes = vars(slot_def)

        # Filter the attributes to only show the populated ones (excluding None, empty lists, etc.)
        populated_attributes = {k: v for k, v in sorted(attributes.items()) if
                                v not in [None, '', [], {}, (), JsonObj()]}

        # Print or log the results as needed
        # print(f"Slot Name: {slot_name}")
        for attr_name, attr_value in sorted(populated_attributes.items()):
            print(f"{class_name}:{slot_name} ... {attr_name} = {attr_value}")
            attribute_usage_count[attr_name] += 1

# Convert defaultdict to a regular dict if needed
attribute_usage_count = dict(attribute_usage_count)

# Print or log the attribute usage count
for attr_name, count in attribute_usage_count.items():
    print(f"{attr_name}: {count}")

# Prepare data for TSV file
# Using an explicit type conversion to str for keys and values
rows = [{'Attribute Name': str(attr_name), 'Usage Count': int(count)} for attr_name, count in
        attribute_usage_count.items()]

# Define the TSV file name
tsv_file_name = "attribute_usage_count.tsv"

# Write the results to a TSV file using DictWriter
with open(tsv_file_name, mode='w', newline='') as tsv_file:
    writer = csv.DictWriter(tsv_file, fieldnames=['Attribute Name', 'Usage Count'], delimiter='\t')
    writer.writeheader()  # Write the header row
    writer.writerows(rows)  # Write the data rows

print(f"Attribute usage count has been saved to {tsv_file_name}")
