## Add your own custom Makefile targets here

RUN=poetry run

.PHONY: schemasheets_cleanup schemasheets_all sheets_and_friends_cleanup sheets_and_friends_all
schemasheets_cleanup:
	rm -rf schema_sheets/yaml_out/*

schemasheets_all: schemasheets_cleanup schema_sheets/yaml_out/from_schema_sheets.yaml

schema_sheets/yaml_out/from_schema_sheets.yaml: schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_dh_interfaces.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_enums.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_mixin_slots.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_mixins.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_schema_boilerplate.tsv \
schema_sheets/tsv_in/sheets-for-nmdc-submission-schema_sections_as_slots.tsv
	$(RUN) sheets2linkml \
		--output $@ $^
		# would prefer to discover TSV inputs instead of enumerating them
		#WARNING:root:Filling in missing prefix for: UO => http://purl.obolibrary.org/obo/UO_
		#WARNING:root:Filling in missing prefix for: qud => http://example.org/qud/

# todo: fewer enums
# todo: use booleans for yes/no enumerations
# todo: some numbers appear as strings in the schema (just examples? check for minimum value etc)
# todo maximum value for pH has to be an int?

sheets_and_friends/yaml_out/with_shuttles.yaml: schema_sheets/yaml_out/from_schema_sheets.yaml \
sheets_and_friends/tsv_in/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv
		$(RUN) do_shuttle \
			--config_tsv  $(word 2,$^) \
			--recipient_model $(word 1,$^) \
			--yaml_output $@

# urllib.error.HTTPError: HTTP Error 404:
# https://raw.githubusercontent.com/home/mark/.cache/pypoetry/virtualenvs/submission-schema-DC6HKp4p-py3.9/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/types.yaml