RUN=poetry run

schema_cleanup: modifications_cleanup schemasheets_cleanup sheets_and_friends_cleanup
	rm -rf src/submission_schema/schema/submission_schema.yaml
	rm -rf src/data/output

src/submission_schema/schema/submission_schema.yaml: sheets_and_friends/yaml_out/with_modifications.yaml
	cp $< $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "ControlledIdentifiedTermValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "ControlledTermValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue")  | .range ) = "string" ' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "TextValue")  | .range ) = "string" ' $@
	yq -i '(.slots.[] | select(.domain == "ControlledTermValue") | .domain ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledIdentifiedTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledTermValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "QuantityValue") | .range ) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TextValue") | .range ) = "string"' $@
	yq -i 'del(.classes.ControlledIdentifiedTermValue)'  $@
	yq -i 'del(.classes.ControlledTermValue)'  $@
	yq -i 'del(.classes.QuantityValue)'  $@
	yq -i 'del(.classes.TextValue)'  $@

	yq -i 'del(.classes.[].slot_usage.[].pattern)' $@
	yq -i 'del(.classes.[].slot_usage.[].required)' $@
	yq -i 'del(.slots.[].pattern)' $@
	yq -i 'del(.slots.[].pattern)' $@
	yq -i 'del(.slots.[].required)' $@
	yq -i 'del(.slots.collection_date.required)'  $@

.PHONY: modifications_cleanup \
schema_cleanup \
schema_all \
schemasheets_all \
schemasheets_cleanup \
sheets_and_friends_all \
sheets_and_friends_cleanup

schemasheets_cleanup:
	rm -rf schema_sheets/yaml_out/*

schema_sheets/yaml_out/from_schema_sheets.yaml: schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_dh_interfaces.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_enums.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_mixin_slots.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_mixins.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_schema_boilerplate.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_sections_as_slots.tsv \
schema_sheets/tsv_in/prefixes.tsv \
schema_sheets/tsv_in/types.tsv
	$(RUN) sheets2linkml \
		--output $@ $^
		# would prefer to discover TSV inputs instead of enumerating them


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
		#yq '(.classes.TextValue)'  $@



# urllib.error.HTTPError: HTTP Error 404:
# https://raw.githubusercontent.com/home/mark/.cache/pypoetry/virtualenvs/submission-schema-DC6HKp4p-py3.9/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/types.yaml
# when source file or URL = https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml
# use https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/nmdc_schema/nmdc_materialized_patterns.yaml instead?!

modifications_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

sheets_and_friends/yaml_out/with_modifications.yaml: sheets_and_friends/yaml_out/with_shuttles.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long.tsv \
		--validation_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter.tsv \
		--yaml_output $@
	#yq -i 'del(.classes.[].slot_usage.collection_date.required)'  $@

src/data/output: src/submission_schema/schema/submission_schema.yaml
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--counter-example-input-directory src/data/invalid \
		--input-directory src/data/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

# Warning: The following errors were encountered in the schema
  #                :  Slot dh_mutliview_common_columns_source_mat_id is declared inline but single valued

schema_sheets/populated_tsv/slot_usage.tsv:
	$(RUN) linkml2sheets \
		--output-directory $(dir $@) \
		--schema src/submission_schema/schema/submission_schema.yaml schema_sheets/templates/slot_usage.tsv