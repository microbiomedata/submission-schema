RUN=poetry run

schema_cleanup: modifications_cleanup schemasheets_cleanup sheets_and_friends_cleanup
	rm -rf examples/*.yaml
	rm -rf examples/output/*.db
	rm -rf examples/output/*.json
	rm -rf examples/output/*.tsv
	rm -rf examples/output/*.ttl
	rm -rf examples/output/*.yaml
	rm -rf examples/output/README.md
	rm -rf examples/output/output
	rm -rf from_schema_sheets.lint_report.txt
	rm -rf schema_sheets/from_schema_sheets.lint_report.txt
	rm -rf schema_sheets/populated_tsv/*.tsv
	rm -rf schema_sheets/populated_tsv/*.txt
	rm -rf schema_sheets/yaml_out/from_schema_sheets.yaml
	rm -rf schema_sheets/yaml_out/from_schema_sheets.yaml.raw
	rm -rf sheets_and_friends/with_modifications.lint_report.txt
	rm -rf sheets_and_friends/with_shuttles.lint_report.txt
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml
	rm -rf sheets_and_friends/yaml_out/with_shuttles_yq.yaml
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml.raw
	rm -rf src/submission_schema/schema/submission_schema.yaml
	mkdir -p examples/output


.PHONY: check-invalid-vs-json-schema \
check-valid-vs-json-schema \
modifications_cleanup \
schema_all \
schema_cleanup \
schemasheets_all \
schemasheets_cleanup \
sheets_and_friends_all \
sheets_and_friends_cleanup

schemasheets_cleanup:
	rm -rf schema_sheets/yaml_out/*

schema_sheets/yaml_out/from_schema_sheets.yaml: schema_sheets/tsv_in/prefixes.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_classes.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_enums.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_schema_only.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_slots.tsv \
schema_sheets/tsv_in/types.tsv
	$(RUN) sheets2linkml \
		--output $@.raw $^
		# would prefer to discover TSV inputs instead of enumerating them
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@
	- $(RUN) linkml-lint $@ > schema_sheets/from_schema_sheets.lint_report.txt


# todo: fewer enums
# todo: use booleans for yes/no enumerations
# todo: some numbers appear as strings in the schema (just examples? check for minimum value etc)
# todo maximum value for pH has to be an int?

sheets_and_friends_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml

sheets_and_friends/yaml_out/with_shuttles.yaml: schema_sheets/yaml_out/from_schema_sheets.yaml \
sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv
	$(RUN) do_shuttle \
		--config_tsv  $(word 2,$^) \
		--recipient_model $(word 1,$^) \
		--yaml_output $@

	$(RUN) linkml2sheets \
		--output-directory schema_sheets/populated_tsv \
		--schema $@ schema_sheets/templates/slot_usage_minimal.tsv

	mv schema_sheets/populated_tsv/slot_usage_minimal.tsv schema_sheets/populated_tsv/with_shuttles_slot_usage_minimal.tsv

sheets_and_friends/yaml_out/with_shuttles_yq.yaml: sheets_and_friends/yaml_out/with_shuttles.yaml
	cp $< $@
	# using \x0A to represent a line feed
	# double $ gets reduced to one by make

	# .string_serialization=="{text};{float} {unit}": what about multivalueds? don't see any at this time
	# ControlledTermValue: experiential factor has string_serialization: '{termLabel} {[termID]}|{text}'
	# ControlledTermValue: what about multivalued CTVs? don't see any besides chem_administration above at this time
	# for water, can depth be a point, a range, or both?

	yq -i '(.classes.[].slot_usage.[] | select(.name=="carb_nitro_ratio")  | .range) = "float"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="chem_administration") | .examples) = [{"value": "agar [CHEBI:2509];2018-05-11|agar [CHEBI:2509];2018-05-22"}, {"value": "agar [CHEBI:2509];2018-05"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="chem_administration") | .pattern) = "^(\S+.*\S+ \[[A-za-z]+:\d+\];[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?\|)*(\S+.*\S+ \[[A-za-z]+:\d+\];[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?)$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="chem_administration") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="collection_date") | .examples) = [{"value": "2023-01-15"}, {"value": "2023-01"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="collection_date") | .pattern) = "^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="collection_date") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="depth") | .pattern) = "^([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? to )?[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="depth") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="experimental_factor") | .examples) = [{"value": "time series design [EFO:0001779]"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="experimental_factor") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="organism_count") | .pattern) = "^(\S+.*\S+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S+.*\S+;(qPCR|ATP|MPN|other)\|)*(\S+.*\S+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S+.*\S+;(qPCR|ATP|MPN|other))$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="organism_count") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.name=="samp_mat_process") | .examples) = [{"value": "filtering of seawater"}, {"value": "storing samples in ethanol"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="samp_mat_process") | .pattern) = ".*"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="samp_mat_process") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "GeolocationValue")  | .pattern) = "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "GeolocationValue")  | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue") | .pattern) = "^[-+]?[0-9]*\.?[0-9]+ +\S.*$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue" and .multivalued == true)  | .pattern) = "^([-+]?[0-9]*\.?[0-9]+ +\S.*\|)*([-+]?[0-9]*\.?[0-9]+ +\S.*)$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue")  | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "TextValue")  | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "TimestampValue")  | .pattern) = "^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "TimestampValue")  | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range=="ControlledTermValue") | .pattern) = "^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range=="ControlledTermValue") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{termLabel} {[termID]}") | .pattern) = "^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{termLabel} {[termID]}") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{text};{float} {unit}") | .pattern) = "^[^;\t\r\x0A\|]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A\|]+$$"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{text};{float} {unit}" and .multivalued == true ) | .pattern) = "^([^;\t\r\x0A]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A]+\|)*([^;\t\r\x0A]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A]+)$$"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{text};{float} {unit}") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "string")  | .multivalued) = false' $@

	yq -i '(.slots.[] | select(.domain == "Activity") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "Agent") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "AttributeValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "AttributeValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "ControlledTermValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "GeolocationValue") | .domain ) = "NamedThing"' $@

	yq -i '(.slots.[] | select(.range == "Activity") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "Agent") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "Agent") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledIdentifiedTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "GeolocationValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "OntologyClass") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "QuantityValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TextValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TimestampValue") | .range ) = "string"' $@

	yq -i 'del(.classes.Activity)'  $@
	yq -i 'del(.classes.Agent)'  $@
	yq -i 'del(.classes.AttributeValue)'  $@
	yq -i 'del(.classes.ControlledIdentifiedTermValue)'  $@
	yq -i 'del(.classes.ControlledTermValue)'  $@
	yq -i 'del(.classes.GeolocationValue)'  $@
	yq -i 'del(.classes.OntologyClass)'  $@
	yq -i 'del(.classes.QuantityValue)'  $@
	yq -i 'del(.classes.TextValue)'  $@
	yq -i 'del(.classes.TimestampValue)'  $@

# remove the multivalued true annotation from these gloabl slot definitions for the sake of linkml-convert
#   esp to tsv? and dumping to SQLite?
# follow the .string_serialization=="{text};{float} {unit}" and .multivalued == true pattern?
	yq -i '(.slots.[] | select(.name == "atmospheric_data") | .multivalued ) = false' $@
	yq -i '(.slots.[] | select(.name == "biomass") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "chem_administration") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "diether_lipids") | .multivalued ) = false' $@
	yq -i '(.slots.[] | select(.name == "misc_param") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "n_alkanes") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "organism_count") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "perturbation") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "phaeopigments") | .multivalued) = false' $@
	yq -i '(.slots.[] | select(.name == "phosplipid_fatt_acid") | .multivalued) = false' $@

#	yq -i '(.slots.[] | select(.name == "analysis_type") | .multivalued ) = true' $@
#	yq -i '(.slots.[].multivalued) = false' $@

#	$(RUN) linkml-run-examples \
#		--output-formats json \
#		--output-formats yaml \
#		--counter-example-input-directory src/data/invalid \
#		--input-directory src/data/valid \
#		--output-directory examples/output/ \
#		--schema $@
#
#temp_cleanup:
#	rm -rf sheets_and_friends/yaml_out/with_shuttles_yq.yaml
#
#temp: temp_cleanup sheets_and_friends/yaml_out/with_shuttles_yq.yaml

#	$(RUN) linkml2sheets \
#		--output-directory schema_sheets/populated_tsv \
#		--schema $@ schema_sheets/templates/slot_usage_minimal.tsv
#
#	mv schema_sheets/populated_tsv/slot_usage_minimal.tsv schema_sheets/populated_tsv/with_shuttles_slot_usage_minimal.tsv
#
#	# globally replace structured ranges with strings.
#	# undoes some of the range alterations that nmdc-schema makes when importing MIxS terms
#	# future versions of the nmdc-schema might just use strings, too/
#	# there's still more to do. see schema_sheets/populated_tsv/slot_usage.tsv
#	# should probably be populating slot usage sheets after each intermediate step
#	# to some degree this should be handled globally by sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter.tsv
#	# and on a slot-by-slot basic by sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long.tsv
#
#	# we should be consistent about the following things in patterns
#	# single or multiple whitespace?
#	# [0-9] or \d?
#	# include scientific notation? (eg quantity value)
#	# what whitespace to exclude?
#	#
#	# be careful about strings that look like numbers with quotes in YAML
#	#   impact on other serializations?
#
#	# escape pipes that are going to be used literally as future delimiters
#
#	$(RUN) gen-linkml \
#		--no-materialize-attributes \
#		--format yaml $@.pregen > $@
#
##	 should add a remove attribute option to sheets and friend's modify and validate
##	  currently have nan string serializations
#
## scrutininze the slots that currerntly accept xyz or abc. how could they be better constrained?
#
## synchronize between guidance, examples and validation
##   cross reference MIxS' values for those aspects
##
##	#add another gen-linkml step here?
##
##	- $(RUN) linkml-lint $@ > sheets_and_friends/with_shuttles.lint_report.tsv
#
## fixed?
## safe to use latest linkml-runtime again now? in sheets_and_friends too?
## urllib.error.HTTPError: HTTP Error 404:
## https://raw.githubusercontent.com/home/mark/.cache/pypoetry/virtualenvs/submission-schema-DC6HKp4p-py3.9/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/types.yaml
## when source file or URL = https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml
## use https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/nmdc_schema/nmdc_materialized_patterns.yaml instead?!

modifications_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

sheets_and_friends/yaml_out/with_modifications.yaml: sheets_and_friends/yaml_out/with_shuttles_yq.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long_empty.tsv \
		--validation_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter_empty.tsv \
		--yaml_output $@.raw
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@
	- $(RUN) linkml-lint $@ > sheets_and_friends/with_modifications.lint_report.txt

src/submission_schema/schema/submission_schema.yaml: sheets_and_friends/yaml_out/with_modifications.yaml
	cp $< $@

examples/output/README.md: src/submission_schema/schema/submission_schema.yaml
	mkdir -p $(dir $@)
	# RDF/TTL generation is failing
	# WARNING:root:No namespace defined for URI: https://microbiomedata/schema/ecosystem
	# added fix to nmdc-schema repo... regen? merge?
	# --output-formats ttl \
	# fixed namespaces but now
	#  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/submission-schema-LusGX8SJ-py3.10/lib/python3.10/site-packages/linkml_runtime/dumpers/rdflib_dumper.py", line 130, in inject_triples
	#    slot_uri = URIRef(schemaview.get_uri(slot, expand=True))
	#  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/submission-schema-LusGX8SJ-py3.10/lib/python3.10/site-packages/linkml_runtime/utils/schemaview.py", line 877, in get_uri
	#    schema = next(sc for sc in self.schema_map.values() if sc.id == e.from_schema)
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/invalid \
		--input-directory src/data/valid \
		--output-directory $(dir $@) \
		--schema $< > $@

schema_sheets/populated_tsv/slot_usage.tsv:
	$(RUN) linkml2sheets \
		--output-directory $(dir $@) \
		--schema src/submission_schema/schema/submission_schema.yaml schema_sheets/templates/slot_usage.tsv

# why is --no-validate required?
# without it...
#jsonschema.exceptions.ValidationError: '1.5' is not of type 'number'
#On instance['water_data'][0]['elev']:
examples/output/SampleData-water-data.tsv: src/data/valid/SampleData-water-data-exhaustive.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema src/submission_schema/schema/submission_schema.yaml \
		--no-validate $<

examples/output/SampleData-water-data.regen.yaml: examples/output/SampleData-water-data.tsv
	$(RUN) linkml-convert \
		--output $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema src/submission_schema/schema/submission_schema.yaml \
		--no-validate $<

examples/output/SampleData-water-data.db: src/data/valid/SampleData-water-data-exhaustive.yaml
	$(RUN)  linkml-sqldb dump \
		--db $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema src/submission_schema/schema/submission_schema.yaml \
		--no-validate $<

check-valid-vs-json-schema: src/data/valid/SampleData-water-data-exhaustive.yaml
	$(RUN) check-jsonschema --schemafile project/jsonschema/submission_schema.schema.json $<

check-invalid-vs-json-schema: src/data/invalid/SampleData-water-data-alkalinity-list.yaml
	! $(RUN) check-jsonschema --schemafile project/jsonschema/submission_schema.schema.json $<


