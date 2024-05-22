RUN=poetry run

.PHONY:  modifications-clean run-linkml-validation schema-clean schema_all schemasheets-clean schemasheets_all \
sheets_and_friends-clean sheets_and_friends_all

squeaky-clean: clean schema-clean examples-clean

schema-clean: modifications-clean schemasheets-clean sheets_and_friends-clean
	rm -rf examples/*.yaml
	rm -rf examples/output/*.db
	rm -rf examples/output/*.json
	rm -rf examples/output/*.tsv
	rm -rf examples/output/*.ttl
	rm -rf examples/output/*.yaml
	rm -rf examples/output/README.md
	rm -rf from_schemasheets.lint_report.txt
	rm -rf schemasheets/from_schemasheets.lint_report.txt
	rm -rf schemasheets/populated_tsv/*.tsv
	rm -rf schemasheets/populated_tsv/*.txt
	rm -rf schemasheets/yaml_out/from_schemasheets.yaml
	rm -rf schemasheets/yaml_out/from_schemasheets.yaml.raw
	rm -rf sheets_and_friends/with_modifications.lint_report.txt
	rm -rf sheets_and_friends/with_shuttles.lint_report.txt
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml.raw
	rm -rf sheets_and_friends/yaml_out/with_shuttles_yq.yaml
	rm -rf src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	rm -rf local/*
	mkdir -p local
	cp placeholder.md local
	mkdir -p examples/output

schemasheets-clean:
	rm -rf schemasheets/yaml_out/*.yaml

local/from_schemasheets.yaml: schemasheets/tsv_in/prefixes.tsv \
schemasheets/tsv_in/classes.tsv \
schemasheets/tsv_in/enums.tsv \
schemasheets/tsv_in/schema_only.tsv \
schemasheets/tsv_in/slots.tsv \
schemasheets/tsv_in/types.tsv
	$(RUN) sheets2linkml \
		--output $@.raw $^
		# would prefer to discover TSV inputs instead of enumerating them
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@
	- $(RUN) linkml-lint $@ > local/from_schemasheets.lint_report.txt


# todo: fewer enums
# todo: use booleans for yes/no enumerations
# todo: some numbers appear as strings in the schema (just examples? check for minimum value etc)
# todo maximum value for pH has to be an int?

sheets_and_friends-clean:
	rm -rf sheets_and_friends/yaml_out/with_shuttles.yaml

local/with_shuttles.yaml: local/from_schemasheets.yaml \
sheets_and_friends/tsv_in/import_slots_regardless.tsv
		$(RUN) do_shuttle \
			--config_tsv  $(word 2,$^) \
			--recipient_model $(word 1,$^) \
			--yaml_output $@.raw
		$(RUN) gen-linkml \
			--no-materialize-attributes \
			--format yaml $@.raw > $@
		- $(RUN) linkml-lint $@ > local/with_shuttles.lint_report.txt

local/with_shuttles_yq.yaml: local/with_shuttles.yaml assets/yq-for-shuttles.txt
	cp $< $@
	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done

modifications-clean:
	rm -rf sheets_and_friends/yaml_out/with_modifications.yaml

local/nmdc.yaml:
	wget -O $@ https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v10.3.0/nmdc_schema/nmdc_materialized_patterns.yaml

local/with_modifications.yaml: local/with_shuttles_yq.yaml \
sheets_and_friends/tsv_in/modifications_long.tsv \
sheets_and_friends/tsv_in/validation_converter.tsv \
local/nmdc.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv $(word 2,$^) \
		--validation_config_tsv $(word 3,$^) \
		--yaml_output $@.raw

	# apply all rules from Biosample to JgiMgInterface and JgiMtInterface
	yq eval-all \
		'select(fileIndex==1).classes.JgiMgInterface.rules = select(fileIndex==0).classes.Biosample.rules | select(fileIndex==1)' \
		local/nmdc.yaml $@.raw | cat > $@.raw2
	yq eval-all \
		'select(fileIndex==1).classes.JgiMtInterface.rules = select(fileIndex==0).classes.Biosample.rules | select(fileIndex==1)' \
		local/nmdc.yaml $@.raw2 | cat > $@.raw

	# remove some rules
	yq -i 'del(.classes.JgiMgInterface.rules.[] | select(.title == "rna*"))' $@.raw
	yq -i 'del(.classes.JgiMtInterface.rules.[] | select(.title == "dna*"))' $@.raw

	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml $@.raw > $@

	- $(RUN) linkml-lint $@ > local/with_modifications.lint_report.txt

src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml: local/with_modifications.yaml \
project/thirdparty/GoldEcosystemTree.json assets/yq-final.txt
	$(RUN) inject-gold-pathway-terms -g $(word 2,$^) -i $< -o $@
	grep "^'" $(word 3, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done

run-examples: examples-clean examples/output/README.md

examples-clean:
	rm -rf examples/output

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

# see local/usage_template.tsv
## target was was local/slot_usage.tsv,
##   but I changed the destination to a checked-in directory
##   so collaborators can sort and filter the slot attributes
##   and I switched to a smaller template
#schemasheets/populated_tsv/slot_usage_minimal.tsv: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
#schemasheets/templates/slot_usage_minimal.tsv
#	$(RUN) linkml2sheets \
#		--output-directory $(dir $@) \
#		--schema $< $(word 2,$^)
## WARNING:root:Not implemented: slot

local/SampleData-water-data-exhaustive.tsv: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
src/data/valid/SampleData-water-data-exhaustive.yaml
	mkdir -p local
	$(RUN) linkml-convert \
		--output $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema $(word 1,$^) $(word 2,$^)

examples/output/SampleData-water-data-exhaustive.regen.yaml: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
local/SampleData-water-data-exhaustive.tsv
	mkdir -p examples/output
	$(RUN) linkml-convert \
		--output $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema $(word 1,$^) $(word 2,$^)

local/SampleData-water-data-exhaustive.db: src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml \
src/data/valid/SampleData-water-data-exhaustive.yaml
	$(RUN)  linkml-sqldb dump \
		--db $@ \
		--target-class SampleData \
		--index-slot water_data \
		--schema $(word 1,$^) $(word 2,$^)


# # could run these inbetween every step
# #  but should probably save output into a .gitignored dir like local
# #  but check if it is .gitignored!
#
#	$(RUN) gen-linkml \
#		--no-materialize-attributes \
#		--format yaml $@.raw > $@
#
#	- $(RUN) linkml-lint $@ > sheets_and_friends/with_modifications.lint_report.txt

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

local/envo.db.gz:
	wget https://s3.amazonaws.com/bbop-sqlite/envo.db.gz -O $@

local/envo.db: local/envo.db.gz
	gzip -d $<



local/terrestrial_biome_tree_down.txt: local/envo.db
	$(RUN) runoak \
		-i $< tree \
		--down \
		--output $@ \
		--predicates rdfs:subClassOf 'terrestrial biome'

local/terrestrial_biome_pvs.txt: local/terrestrial_biome_tree_down.txt
	$(RUN) oak-tree-to-pv-list \
		--discard-line-pattern 'terrestrial biome'  \
		--input-file $< \
		--output-file $@



#local/alpine_biome_tree_down.txt: local/envo.db
#	$(RUN) runoak \
#		-i $< tree \
#		--down \
#		--output $@ \
#		--predicates rdfs:subClassOf 'alpine biome'
#
#local/alpine_biome_pvs.txt: local/alpine_biome_tree_down.txt
#	$(RUN) oak-tree-to-pv-list \
#		--discard-line-pattern 'alpine biome'  \
#		--input-file $< \
#		--output-file $@



local/aquatic_biome_tree_down.txt: local/envo.db
	$(RUN) runoak \
		-i $< tree \
		--down \
		--output $@ \
		--predicates rdfs:subClassOf 'aquatic biome'

local/aquatic_biome_pvs.txt: local/aquatic_biome_tree_down.txt
	$(RUN) oak-tree-to-pv-list \
		--discard-line-pattern 'aquatic biome'  \
		--input-file $< \
		--output-file $@


local/biome_tree_down.txt: local/envo.db
	$(RUN) runoak \
		-i $< tree \
		--down \
		--output $@ \
		--predicates rdfs:subClassOf 'biome'

local/biome_pvs.txt: local/biome_tree_down.txt
	$(RUN) oak-tree-to-pv-list \
		--discard-line-pattern 'xxx'  \
		--input-file $< \
		--output-file $@


local/soil_tree_down.txt: local/envo.db
	$(RUN) runoak \
		-i $< tree \
		--down \
		--output $@ \
		--predicates rdfs:subClassOf 'soil'

local/soil_pvs.txt: local/soil_tree_down.txt
	$(RUN) oak-tree-to-pv-list \
		--discard-line-pattern 'xxx'  \
		--input-file $< \
		--output-file $@


local/abp_tree_down.txt: local/envo.db
	$(RUN) runoak \
		-i $< tree \
		--down \
		--output $@ \
		--predicates rdfs:subClassOf 'astronomical body part'

local/abp_pvs.txt: local/abp_tree_down.txt
	$(RUN) oak-tree-to-pv-list \
		--discard-line-pattern 'xxx'  \
		--input-file $< \
		--output-file $@

#x:  local/envo.db
#	$(RUN) runoak -i $< extract-triples .desc//p=i 'terrestrial biome'

# now add/edit those in the schema sheets enums file
# would like to compose with and, or, not etc
# would like to sort alphabetically within heirarchical groups

# for local:
# human construction
# astronomical body part

src/data/data_harmonizer_io/soil_for_linkml.json: src/data/data_harmonizer_io/soil_from_dh.json
	$(RUN) dh-json2linkml \
		--input-file $< \
		--output-file $@ \
		--key soil_data


src/data/data_harmonizer_io/soil_data.json: src/data/data_harmonizer_io/soil_for_linkml.json
	$(RUN) linkml-json2dh \
		--input-file $< \
		--output-dir $(dir $@)

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
