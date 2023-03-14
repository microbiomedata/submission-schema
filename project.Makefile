RUN=poetry run

schema_cleanup: modifications_cleanup schemasheets_cleanup sheets_and_friends_cleanup
	rm -rf examples/*.yaml
	rm -rf examples/output/*.db
	rm -rf examples/output/*.json
	rm -rf examples/output/*.tsv
	rm -rf examples/output/*.yaml
	rm -rf examples/output/README.md
	rm -rf examples/output/output
	rm -rf from_schema_sheets.lint_report.txt
	rm -rf schema_sheets/from_schema_sheets.lint_report.txt
	rm -rf schema_sheets/populated_tsv/slot_usage.tsv
	rm -rf schema_sheets/yaml_out/from_schema_sheets.yaml
	rm -rf schema_sheets/yaml_out/from_schema_sheets.yaml.raw
	rm -rf sheets_and_friends/with_modifications.lint_report.txt
	rm -rf sheets_and_friends/with_shuttles.lint_report.txt
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml.raw
	rm -rf src/submission_schema/schema/submission_schema.yaml
	mkdir -p examples/output


src/submission_schema/schema/submission_schema.yaml: sheets_and_friends/yaml_out/with_modifications.yaml
	cp $< $@
	# globally replace structured ranges with strings.
	# there's still more to do. see schema_sheets/populated_tsv/slot_usage.tsv
	# to some degree this should be handled globally by sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter.tsv
	# and on a slot-by-slot basic by sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long.tsv
	yq -i '(.classes.[].slot_usage.[] | select(.range == "ControlledIdentifiedTermValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "ControlledTermValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "GeolocationValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "TextValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "TimestampValue")  | .range ) = "string" ' $@
	yq -i '(.slots.[] | select(.domain == "ControlledTermValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "GeolocationValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.range == "ControlledIdentifiedTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "GeolocationValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "QuantityValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TextValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TimestampValue") | .range ) = "string"' $@
	yq -i 'del(.classes.ControlledIdentifiedTermValue)'  $@
	yq -i 'del(.classes.ControlledTermValue)'  $@
	yq -i 'del(.classes.GeolocationValue)'  $@
	yq -i 'del(.classes.QuantityValue)'  $@
	yq -i 'del(.classes.TextValue)'  $@
	yq -i 'del(.classes.TimestampValue)'  $@
	yq -i 'del(.classes.[].slot_usage.[].pattern)' $@
	yq -i 'del(.slots.[].pattern)' $@
#	yq -i 'del(.classes.[].slot_usage.[].examples.[] | select(.value == ""))' src/submission_schema/schema/submission_schema.yaml
#	yq -i 'del(.classes.[].slot_usage.[].required)' $@
#	yq -i 'del(.slots.[].examples.[] | select(.value == ""))' src/submission_schema/schema/submission_schema.yaml
#	yq -i 'del(.slots.collection_date.required)'  $@
#	yq -i 'del(.slots.[].required)' $@

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
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_schema_only.csv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_slots.csv \
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
			--yaml_output $@.raw
		$(RUN) gen-linkml \
			--no-materialize-attributes \
			--format yaml $@.raw > $@
		- $(RUN) linkml-lint $@ > sheets_and_friends/with_shuttles.lint_report.txt

# fixed?
# safe to use latest linkml-runtime again now? in sheets_and_freinds too?
# urllib.error.HTTPError: HTTP Error 404:
# https://raw.githubusercontent.com/home/mark/.cache/pypoetry/virtualenvs/submission-schema-DC6HKp4p-py3.9/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/types.yaml
# when source file or URL = https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml
# use https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/nmdc_schema/nmdc_materialized_patterns.yaml instead?!

modifications_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

sheets_and_friends/yaml_out/with_modifications.yaml: sheets_and_friends/yaml_out/with_shuttles.yaml sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long.tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter.tsv
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv $(word 2,$^) \
		--validation_config_tsv $(word 3,$^) \
		--yaml_output $@.raw
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@
	- $(RUN) linkml-lint $@ > sheets_and_friends/with_modifications.lint_report.txt

examples/output/README.md: src/submission_schema/schema/submission_schema.yaml
	mkdir -p $(dir $@)
	# RDF/TTL generation is failing
	# WARNING:root:No namespace defined for URI: https://microbiomedata/schema/ecosystem
	# added fix to nmdc-schema repo... regen? merge?
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
examples/output/SampleData-water-data.tsv: src/data/valid/SampleData-water-data.yaml
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

examples/output/SampleData-water-data.db: examples/output/SampleData-water-data.tsv
	$(RUN)  linkml-sqldb dump \
		--db $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema src/submission_schema/schema/submission_schema.yaml \
		--no-validate $<

check-valid-vs-json-schema: src/data/valid/SampleData-water-data.yaml
	$(RUN) check-jsonschema --schemafile project/jsonschema/submission_schema.schema.json $<

check-invalid-vs-json-schema: src/data/invalid/SampleData-water-data.yaml
	! $(RUN) check-jsonschema --schemafile project/jsonschema/submission_schema.schema.json $<

project/json/submission_schema.json: src/submission_schema/schema/submission_schema.yaml
	$(RUN) gen-linkml $< --format json --materialize-patterns --materialize-attributes > $@
