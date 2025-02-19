MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
# get values from about.yaml file
SCHEMA_NAME = $(shell ${SHELL} ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell ${SHELL} ./utils/get-value.sh source_schema_path)
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
EXAMPLEDIR = examples
SHEET_MODULE = personinfo_enums
SHEET_ID = $(shell ${SHELL} ./utils/get-value.sh google_sheet_id)
SHEET_TABS = $(shell ${SHELL} ./utils/get-value.sh google_sheet_tabs)
SHEET_MODULE_PATH = $(SOURCE_SCHEMA_DIR)/$(SHEET_MODULE).yaml

# environment variables
GEN_PARGS =
ifdef LINKML_COOKIECUTTER_GEN_PROJECT_ARGS
GEN_PARGS = ${LINKML_COOKIECUTTER_GEN_PROJECT_ARGS}
endif

GEN_DARGS =
ifdef LINKML_COOKIECUTTER_GEN_DOC_ARGS
GEN_DARGS = ${LINKML_COOKIECUTTER_GEN_DOC_ARGS}
endif

.PHONY: all clean gen-project gendoc site test test-python

# from project.Makefile
.PHONY: schema-clean

# not declared phony by the cookiecutter this repo was bootstrapped from
.PHONY: check check-config cruft-check cruft-diff git-add git-commit git-init git-init-add git-status help  \
lint run-examples serve setup status test-schema testdoc update  update-linkml update-template

# .PHONY: mkd-% # ???

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perfom linting"
	@echo "make testdoc -- builds docs and runs local test server"
#	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: install gen-project gendoc git-init-add

# install any dependencies required for building
install:
	git init     # issues/33
	poetry install
.PHONY: install

# ---
# Project Syncronization
# ---
#
# check we are up to date
check: cruft-check
cruft-check:
	cruft check
cruft-diff:
	cruft diff

update: update-template update-linkml
update-template:
	cruft update

# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

all: site
site: clean schema-clean src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml ingest-triad \
gen-project gendoc project/json/nmdc_submission_schema.json

%.yaml: gen-project
# make deploy has been depricated by an updated .github/workflows/deploy-docs.yaml
#deploy: all mkd-gh-deploy

# generates all project files
# gen-owl fails with LinkML 1.6.x; needs further investigation
# See https://github.com/microbiomedata/issues/issues/542
gen-project: $(PYMODEL) src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml
	$(RUN) gen-project ${GEN_PARGS}  \
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
		--include sqlddl \
		--generator-arguments '{jsonschema: {not_closed: false}, sqlddl: {output: local/submission_schema.sql}}' \
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: test-python run-examples
test-schema:
	$(RUN) gen-project ${GEN_PARGS} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) pytest

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH)

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n  - Remember to edit 'about.yaml'\n\n" || exit 0)

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc ${GEN_DARGS} -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DOCDIR)/javascripts
	$(RUN) cp $(SRC)/scripts/*.js $(DOCDIR)/javascripts/

testdoc: test_deploy_docs_action gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = sqlschema owl jsonschema
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add .gitignore .github .cruft.json Makefile LICENSE *.md examples utils about.yaml mkdocs.yml poetry.lock project.Makefile pyproject.toml src/nmdc_submission_schema/schema/*yaml src/*/datamodel/*py src/data src/docs tests src/*/_version.py
	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))
git-commit:
	git commit -m 'chore: initial commit' -a
git-status:
	git status

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs/*

include project.Makefile
