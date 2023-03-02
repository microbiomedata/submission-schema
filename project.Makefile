## Add your own custom Makefile targets here

RUN=poetry run

schema_cleanup: modifications_cleanup schemasheets_cleanup sheets_and_friends_cleanup
	rm -rf src/submission_schema/schema/submission_schema.yaml

src/submission_schema/schema/submission_schema.yaml: sheets_and_friends/yaml_out/with_modifications.yaml
	# still need to do modifications
	# including annotations?
	sleep 5
	cp $< $@

.PHONY: modifications_cleanup \
schema_cleanup \
schema_all \
schemasheets_all \
schemasheets_cleanup \
sheets_and_friends_all \
sheets_and_friends_cleanup


#modifications_all:

schemasheets_cleanup:
	rm -rf schema_sheets/yaml_out/*

#schemasheets_all: schemasheets_cleanup schema_sheets/yaml_out/from_schema_sheets.yaml

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
		#WARNING:root:Filling in missing prefix for: UO => http://purl.obolibrary.org/obo/UO_
		#WARNING:root:Filling in missing prefix for: qud => http://example.org/qud/
		#WARNING:root:Filling in missing prefix for: xsd => http://www.w3.org/2001/XMLSchema#


# todo: fewer enums
# todo: use booleans for yes/no enumerations
# todo: some numbers appear as strings in the schema (just examples? check for minimum value etc)
# todo maximum value for pH has to be an int?


#sheets_and_friends_all: sheets_and_friends_cleanup sheets_and_friends/yaml_out/with_shuttles.yaml

sheets_and_friends_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml

sheets_and_friends/yaml_out/with_shuttles.yaml: schema_sheets/yaml_out/from_schema_sheets.yaml \
sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv
		$(RUN) do_shuttle \
			--config_tsv  $(word 2,$^) \
			--recipient_model $(word 1,$^) \
			--yaml_output $@
		# import nmdc-schema's types or replace these ranges in the modification phase
#		yq -i 'del(.slots.latitude.range)'  $@
#		yq -i 'del(.slots.longitude.range)'  $@
#		yq -i 'del(.slots.language.range)'  $@

# urllib.error.HTTPError: HTTP Error 404:
# https://raw.githubusercontent.com/home/mark/.cache/pypoetry/virtualenvs/submission-schema-DC6HKp4p-py3.9/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/types.yaml
# when source file or URL = https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml
# use https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/nmdc_schema/nmdc_materialized_patterns.yaml instead?!

modifications_cleanup:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

#modifications_all: modifications_cleanup sheets_and_friends/yaml_out/with_modifications.yaml

sheets_and_friends/yaml_out/with_modifications.yaml: sheets_and_friends/yaml_out/with_shuttles.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_modifications_long.tsv \
		--validation_config_tsv sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_validation_converter.tsv \
		--yaml_output $@