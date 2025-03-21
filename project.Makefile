RUN=poetry run

.PHONY:  modifications-clean schema-clean sheets_and_friends-clean dh-build dh-dev examples-clean post-clean \
run-examples squeaky-clean

# .PHONY clean # from Makefile

squeaky-clean: clean schema-clean

post-clean:
	rm -rf local/*
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles_yq.yaml
	cp placeholder.md local


schema-clean: modifications-clean sheets_and_friends-clean examples-clean post-clean
	rm -rf sheets_and_friends/with_modifications.lint_report.txt
	rm -rf sheets_and_friends/with_shuttles.lint_report.txt
	rm -rf src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	mkdir -p local
	cp placeholder.md local
	mkdir -p examples/output

# todo: fewer enums
# todo: use booleans for yes/no enumerations
# todo: some numbers appear as strings in the schema (just examples? check for minimum value etc)
# todo maximum value for pH has to be an int?

sheets_and_friends-clean:
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml

local/with_shuttles.yaml: src/nmdc_submission_schema/schema/nmdc_submission_schema_base.yaml \
sheets_and_friends/tsv_in/import_slots_regardless.tsv local/nmdc.yaml
		$(RUN) do_shuttle \
			--config_tsv  $(word 2,$^) \
			--recipient_model $(word 1,$^) \
			--yaml_output $@.raw
		$(RUN) gen-linkml \
			--no-materialize-attributes \
			--format yaml $@.raw > $@
		- $(RUN) linkml-lint $@ > local/with_shuttles.lint_report.txt

local/with_shuttles_yq.yaml: local/with_shuttles.yaml
	cp $< $@
	# using \x0A to represent a line feed
	# double $ gets reduced to one by make

	# .string_serialization=="{text};{float} {unit}": what about multivalueds? don't see any at this time
	# ControlledTermValue: experiential factor has string_serialization: '{termLabel} {[termID]}|{text}'
	# ControlledTermValue: what about multivalued CTVs? don't see any besides chem_administration above at this time
	# for water, can depth be a point, a range, or both?


# globally replace structured ranges with strings.
# undoes some of the range alterations that nmdc-schema makes when importing MIxS terms
# future versions of the nmdc-schema might just use strings, too

# to some degree this should be handled globally by sheets_and_friends/tsv_in/validation_converter.tsv
# and on a slot-by-slot basic by sheets_and_friends/tsv_in/modifications_long.tsv

# we should be consistent about the following things in patterns
# single or multiple whitespace?
# [0-9] or \d?
# include scientific notation? (eg quantity value)
# what whitespace to exclude?

# be careful about strings that look like numbers with quotes in YAML
#   impact on other serializations?

# escape pipes that are going to be used literally as future delimiters ?

#	 should add a remove attribute option to sheets and friend's modify and validate
#	  currently have nan string serializations

# scrutininze the slots that currerntly accept xyz or 100 units. how could they be better constrained?

# synchronize between guidance, examples and validation
#   cross reference MIxS' values for those aspects

# use yq to add examples when the examples themselves include the packed value separator |
#   good reason for using ! instead of |
	yq -i '(.classes.[].slot_usage.[] | select(.name=="chem_administration") | .examples) = [{"value": "agar [CHEBI:2509];2018-05-11|agar [CHEBI:2509];2018-05-22"}, {"value": "agar [CHEBI:2509];2018-05"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="heavy_metals") | .examples) = [{"value": "mercury;0.09 ug/g"}, {"value": "mercury;0.09 ug/g|chromium;0.03 ug/g"}]' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name=="non_microb_biomass") | .examples) = [{"value": "insect;0.23 ug"}, {"value": "insect;0.23 ug|plant;1 g"}]' $@

# use yq to add patterns with a secondary condition like mutivalued
	yq -i '(.classes.[].slot_usage.[] | select(.range == "GeolocationValue")  | .pattern) = "^[-+]?([1-8]?\d(\.\d{1,8})?|90(\.0{1,8})?)\s[-+]?(180(\.0{1,8})?|((1[0-7]\d)|([1-9]?\d))(\.\d{1,8})?)$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "GeolocationValue")  | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue") | .pattern) = "^[-+]?[0-9]*\.?[0-9]+ +\S.*$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range == "QuantityValue" and .multivalued == true)  | .pattern) = "^([-+]?[0-9]*\.?[0-9]+ +\S.*\|)*([-+]?[0-9]*\.?[0-9]+ +\S.*)$$"' $@

# add a pattern for {termLabel} {[termID]} in teh validation configuration
# need more invalid examples
	#yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{termLabel} {[termID]}") | .range) = "string"' $@

	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{text};{float} {unit}") | .pattern) = "^[^;\t\r\x0A\|]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A\|]+$$"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.string_serialization=="{text};{float} {unit}" and .multivalued == true ) | .pattern) = "^([^;\t\r\x0A]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A]+\|)*([^;\t\r\x0A]+;[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? [^;\t\r\x0A]+)$$"' $@

	yq -i '(.slots.[] | select(.domain == "Activity") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "Agent") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "AttributeValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "AttributeValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "ControlledTermValue") | .domain ) = "NamedThing"' $@
	yq -i '(.slots.[] | select(.domain == "GeolocationValue") | .domain ) = "NamedThing"' $@

	yq -i 'del(.classes.Activity)'  $@
	yq -i 'del(.classes.Agent)'  $@
	yq -i 'del(.classes.AttributeValue)'  $@
	yq -i 'del(.classes.ControlledIdentifiedTermValue)'  $@
	yq -i 'del(.classes.ControlledTermValue)'  $@
	yq -i 'del(.classes.GeolocationValue)'  $@
	yq -i 'del(.classes.OntologyClass)'  $@
	yq -i 'del(.classes.OntologyRelation)'  $@
	yq -i 'del(.classes.QuantityValue)'  $@
	yq -i 'del(.classes.TextValue)'  $@
	yq -i 'del(.classes.TimestampValue)'  $@

# use yq for global modifications
# rel_to_oxygen / oxy_stat_samp
	yq -i '(.slots.[] | select(.name == "rel_to_oxygen") | .range) = "rel_to_oxygen_enum"' $@
	yq -i '(.slots.[] | select(.name == "oxy_stat_samp") | .range) = "rel_to_oxygen_enum"' $@

# remove slots that are no longer necessary due to removal of classes above
	yq -i 'del(.slots.[] | select(.name == "acted_on_behalf_of"))' $@
	yq -i 'del(.slots.[] | select(.name == "definition"))' $@
	yq -i 'del(.slots.[] | select(.name == "ended_at_time"))' $@
	yq -i 'del(.slots.[] | select(.name == "has_maximum_numeric_value"))' $@
	yq -i 'del(.slots.[] | select(.name == "has_minimum_numeric_value"))' $@
	yq -i 'del(.slots.[] | select(.name == "has_numeric_value"))' $@
	yq -i 'del(.slots.[] | select(.name == "has_raw_value"))' $@
	yq -i 'del(.slots.[] | select(.name == "has_unit"))' $@
	yq -i 'del(.slots.[] | select(.name == "latitude"))' $@
	yq -i 'del(.slots.[] | select(.name == "longitude"))' $@
	yq -i 'del(.slots.[] | select(.name == "relations"))' $@
	yq -i 'del(.slots.[] | select(.name == "started_at_time"))' $@
	yq -i 'del(.slots.[] | select(.name == "term"))' $@
	yq -i 'del(.slots.[] | select(.name == "used"))' $@
	yq -i 'del(.slots.[] | select(.name == "was_associated_with"))' $@
	yq -i 'del(.slots.[] | select(.name == "was_generated_by"))' $@
	yq -i 'del(.slots.[] | select(.name == "was_informed_by"))' $@


modifications-clean:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

local/nmdc.yaml: poetry.lock
	$(RUN) python src/nmdc_submission_schema/scripts/export_nmdc_schema.py -o $@

# sheets-for-nmdc-submission-schema_validation_converter_empty.tsv
local/with_modifications.yaml: local/with_shuttles_yq.yaml \
sheets_and_friends/tsv_in/modifications_long.tsv \
sheets_and_friends/tsv_in/validation_converter.tsv \
local/nmdc.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv $(word 2,$^) \
		--validation_config_tsv $(word 3,$^) \
		--yaml_output $@.raw

	# # having trouble selectively injecting rules based on title pattern
#	yq eval-all \
#		'select(fileIndex==1).classes.JgiMtInterface.rules = (select(fileIndex==0).classes.Biosample.rules.[] | select(.title == "rna*")) | select(fileIndex==1)' \
#		local/nmdc.yaml src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml | cat > ruleswap.yaml
	# # so just inject all rules...
	# # using | cat > because yq fails to write to STDOUT (permissions error?!)
	yq eval-all \
		'select(fileIndex==1).classes.JgiMgInterface.rules = select(fileIndex==0).classes.Biosample.rules | select(fileIndex==1)' \
		local/nmdc.yaml $@.raw | cat > $@.raw2
	yq eval-all \
		'select(fileIndex==1).classes.JgiMtInterface.rules = select(fileIndex==0).classes.Biosample.rules | select(fileIndex==1)' \
		local/nmdc.yaml $@.raw2 | cat > $@.raw
	# # ...then removing rules that aren't relevant to a class
	# # requires some prior knowledge
	yq -i 'del(.classes.JgiMgInterface.rules.[] | select(.title == "rna*"))' $@.raw
	yq -i 'del(.classes.JgiMtInterface.rules.[] | select(.title == "dna*"))' $@.raw

	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@
	- $(RUN) linkml-lint $@ > local/with_modifications.lint_report.txt


########### ENV Triad PV generation ##########
# Specify that 'ingest-triad' is a phony target, meaning it doesn't correspond to an actual file
.PHONY: ingest-triad temp_target
WATCHED_DIR := notebooks/environmental_context_value_sets
# Match only .tsv files with the specific naming convention
WATCHED_FILES := $(shell find $(WATCHED_DIR) -type f \( \
    -name 'post_google_sheets_*_local_scale.tsv' -o \
    -name 'post_google_sheets_*_broad_scale.tsv' -o \
    -name 'post_google_sheets_*_medium.tsv' \))

# Define an intermediate target to prevent re-triggering
.INTERMEDIATE: temp_target

# Main target to run ingestion commands, depending on the intermediate target
ingest-triad: temp_target

# Intermediate target that dynamically processes matching TSV files
temp_target: $(WATCHED_FILES) src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	@echo "Processing all matching TSV files in $(WATCHED_DIR)..."
	@for tsv_file in $(WATCHED_FILES); do \
		echo "Processing $$tsv_file..."; \
		$(RUN) inject-env-triad-terms -f $$tsv_file \
			-i src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
			-o src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml || exit 1; \
	done
	@touch temp_target

test-deploy-docs-gh-action: clean schema-clean src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml ingest-triad project/json/nmdc_submission_schema.json
################################################

src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml: local/with_modifications.yaml project/thirdparty/GoldEcosystemTree.json
	$(RUN) inject-gold-pathway-terms -g $(word 2,$^) -i $< -o $<.tmp1
	$(RUN) python src/nmdc_submission_schema/scripts/instrument_enums.py -i $<.tmp1 -o $@
	#cp $< $@

# remove the multivalued true annotation from these gloabl slot definitions for the sake of linkml-convert
# follow the .string_serialization=="{text};{float} {unit}" and .multivalued == true pattern?

	yq -i '(.slots.[] | select(.range == "ControlledIdentifiedTermValue") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "ControlledTermValue") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "GeolocationValue") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "OntologyClass") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "QuantityValue") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TextValue") | .range) = "string"' $@
	yq -i '(.slots.[] | select(.range == "TimestampValue") | .range) = "string"' $@

#	yq -i '(.slots.[] | select(has("range") | not  ) | .range ) = "string"' $@
#	yq -i '(.classes.[].slot_usage.[] | select(has("range") | not  ) | .range ) = "string"' $@

	yq -i '(.slots.[] | select(.name == "sample_link") | .range ) = "string"' $@

	yq -i '(.slots.[] | select(.range == "string") | .multivalued ) = false' $@
	yq -i '(.classes.[].slot_usage.[] | select(.range=="string") | .multivalued) = false' $@
	yq -i 'del(.slots.[] | select(.multivalued == "false").inlined)' $@
	yq -i 'del(.slots.[] | select(.multivalued == "false").inlined_as_list)' $@
	yq -i 'del(.classes.[].slot_usage.[] | select(.multivalued == "false").inlined)' $@
	yq -i 'del(.classes.[].slot_usage.[] | select(.multivalued == "false").inlined_as_list)' $@

#	yq -i '(.slots.[] | select(.name == "dna_dnase") | .range) = "boolean"' $@
#	yq -i '(.classes.[].slot_usage.[] | select(.name == "dna_dnase") | .range) = "boolean"' $@

	yq -i '(.slots.[] | select(.name == "oxy_stat_samp") | .range) = "OxyStatSampEnum"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name == "oxy_stat_samp") | .range) = "OxyStatSampEnum"' $@

	yq -i '(.slots.[] | select(.name == "dna_dnase") | .range) = "YesNoEnum"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name == "dna_dnase") | .range) = "YesNoEnum"' $@

	yq -i '(.slots.[] | select(.name == "dnase_rna") | .range) = "YesNoEnum"' $@
	yq -i '(.classes.[].slot_usage.[] | select(.name == "dnase_rna") | .range) = "YesNoEnum"' $@

run-examples: examples-clean examples/output/README.md

examples-clean:
	rm -rf examples/*.yaml
	rm -rf examples/output
	cp placeholder.md examples

examples/output/README.md: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
src/data/invalid src/data/valid
	mkdir -p $(dir $@)
	# RDF/TTL generation is failing
	# https://github.com/microbiomedata/submission-schema/issues/13
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory $(word 2,$^) \
		--input-directory $(word 3,$^) \
		--output-directory $(dir $@) \
		--schema $< > $@

project/json/nmdc_submission_schema.json: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	mkdir -p $(@D)
	$(RUN) gen-linkml $< --format json --materialize-patterns --materialize-attributes > $@

project/thirdparty/GoldEcosystemTree.json:
	mkdir -p $(@D)
	wget https://gold.jgi.doe.gov/download?mode=biosampleEcosystemsJson -O $@

dh-dev: project/json/nmdc_submission_schema.json
	cd data_harmonizer && npm run dev

dh-build: project/json/nmdc_submission_schema.json
	cd data_harmonizer && npm run build

###

## todo frozen content in src/data/data_harmonizer_io has been removed
## todo find a better home for the se scripts if they are still of any use
#src/data/data_harmonizer_io/soil_data.json: src/data/data_harmonizer_io/soil_for_linkml.json
#	$(RUN) linkml-json2dh \
#		--input-file $< \
#		--output-dir $(dir $@)

local/usage_template.tsv: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	mkdir -p $(@D)
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file local/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

.PHONY: env-triad-robot-clean env-triad-robot-all

env-triad-robot-all: env-triad-robot-clean notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv

env-triad-robot-clean:
	rm -rf notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv

notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	$(RUN) python src/nmdc_submission_schema/scripts/create_env_context_robot_template.py \
		--envo-owl-path notebooks/environmental_context_value_sets/envo.owl \
		--schema-path $< \
		--output-file $@