.PHONY: schema-clean
schema-clean:
	rm -rf $(SOURCE_SCHEMA_PATH)

.PHONY: schema-build
schema-build:
	$(RUN) python tools/build.py

.PHONY: run-examples
run-examples:
	rm -rf examples/output
	mkdir -p examples/output
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/invalid \
		--input-directory src/data/valid \
		--output-directory examples/output \
		--schema $(SOURCE_SCHEMA_PATH) > examples/output/README.md

project/json/nmdc_submission_schema.json: $(SOURCE_SCHEMA_PATH)
	mkdir -p $(@D)
	$(RUN) linkml generate linkml $< --format json --materialize-patterns --materialize-attributes > $@

.PHONY: dh-dev
dh-dev: project/json/nmdc_submission_schema.json
	cd data_harmonizer && npm run dev

.PHONY: env-triad-robot-all
env-triad-robot-all: env-triad-robot-clean notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv

.PHONY: env-triad-robot-clean
env-triad-robot-clean:
	rm -rf notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv

notebooks/environmental_context_value_sets/nmdc_env_context_subset_membership.tsv: $(SOURCE_SCHEMA_PATH)
	$(RUN) python notebooks/environmental_context_value_sets/create_env_context_robot_template.py \
		--envo-owl-path notebooks/environmental_context_value_sets/envo.owl \
		--schema-path $< \
		--output-file $@