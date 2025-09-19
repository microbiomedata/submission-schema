MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
SCHEMA_NAME = nmdc_submission_schema
SOURCE_SCHEMA_PATH = src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
EXAMPLEDIR = examples
MKDOCS = $(RUN) mkdocs

# not declared phony by the cookiecutter this repo was bootstrapped from
.PHONY: serve testdoc

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
.PHONY: help
help:
	@echo ""
	@echo "make install -- install dependencies"
	@echo "make all -- build schema, generate project files, and docs"
	@echo "make schema-build -- only build the schema"
	@echo "make gen-project -- generate project files"
	@echo "make clean -- remove all generated files"
	@echo "make test -- runs tests"
	@echo "make lint -- runs schema linter"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make help -- show this help"
	@echo ""

# install any dependencies required for building
.PHONY: install
install:
	poetry install

.PHONY: all
all: schema-build gen-project gendoc

# generates all project files
# gen-owl fails with LinkML 1.6.x; needs further investigation
# See https://github.com/microbiomedata/issues/issues/542
.PHONY: gen-project
gen-project: $(SOURCE_SCHEMA_PATH) project/json/nmdc_submission_schema.json
	$(RUN) linkml generate project \
		--exclude graphql \
		--exclude jsonld \
		--exclude jsonldcontext \
		--exclude markdown \
		--exclude prefixmap \
		--exclude proto \
		--exclude shacl \
		--exclude shex \
		--exclude excel \
		--include jsonschema \
		--exclude owl \
		--include python \
		--generator-arguments '{jsonschema: {not_closed: false}}' \
		--dir $(DEST) \
		$(SOURCE_SCHEMA_PATH) && \
		mv $(DEST)/*.py $(PYMODEL)

.PHONY: test
test: test-python run-examples

.PHONY: test-python
test-python:
	$(RUN) pytest

.PHONY: lint
lint:
	$(RUN) linkml lint $(SOURCE_SCHEMA_PATH)

# Test documentation locally
.PHONY: serve
serve:
	$(MKDOCS) serve

.PHONY: gendoc
gendoc:
	rm -rf p $(DOCDIR)
	mkdir -p $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DOCDIR)/javascripts
	cp $(SRC)/scripts/*.js $(DOCDIR)/javascripts/

.PHONY: testdoc
testdoc: gendoc serve

.PHONY: clean
clean: schema-clean
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs/*

include project.Makefile
