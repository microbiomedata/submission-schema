# Contributing to submission-schema

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to submission-schema. 
These guidelines are not strict rules. Use your best judgment, and feel free to propose 
changes to this document in a pull request.

## Table Of Contents

- [Code of Conduct](#code-of-conduct)
- [Guidelines for Contributions and Requests](#contributions)
    * [Reporting problems with the data model](#reporting-bugs)
- [Development](#development)
    * [Building the schema YAML file](#building-the-schema-yaml-file)
    * [Building the project artifacts](#building-the-project-artifacts)
    * [Automated testing](#automated-testing)
    * [Interactive testing](#interactive-testing)

<a id="code-of-conduct"></a>

## Code of Conduct

The submission-schema team strives to create a
welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-bugs"></a>

### Reporting problems with the data model

Please use our [Issue Tracker](https://github.com/microbiomedata/submission-schema/issues/) for reporting problems with the ontology. 

## Development

### Building the schema YAML file

The source schema is assembled by `make schema-build`, which runs `tools/build.py`.
It merges the hand-written base (`src/nmdc_submission_schema/schema/nmdc_submission_schema_base.yaml`)
with slots imported from nmdc-schema according to `config/nmdc_schema_import.yaml`,
then writes the single built schema at
`src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml`.

The nmdc-schema slots are read from the installed `nmdc_schema` package
(`nmdc_materialized_patterns.yaml`), so the built schema reflects whatever
nmdc-schema version is pinned in `pyproject.toml`. Changing the pin (or the
import config) and rebuilding is what pulls in new or changed upstream slots.

### Building the project artifacts

`make all` runs `schema-build`, `gen-project`, and `gendoc`. Unlike many LinkML
projects, submission-schema **commits its generated artifacts** so downstream
consumers (the DataHarmonizer interface, nmdc-server, Pydantic users) can use
them without running the build:

- `src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml` — the built schema
- `project/jsonschema/nmdc_submission_schema.schema.json` — JSON Schema used for validation
- `project/json/nmdc_submission_schema.json` — materialized schema the DataHarmonizer interface loads
- `src/nmdc_submission_schema/datamodel/nmdc_submission_schema.py` — Pydantic model

Regenerate and commit these whenever the schema source or the nmdc-schema pin
changes, so the committed artifacts never lag the source. (`docs/` is generated
too, but is gitignored.)

### Automated testing

`make test` runs pytest plus `make run-examples`. The example data lives in
`src/data/`:

- every file in `src/data/valid/` must **pass** validation against the built schema
- every file in `src/data/invalid/` is a counter-example that must **fail**, for a
  single intended reason, and is named after the field it violates

Because of the must-fail rule, a counter-example whose only failure was a
constraint that is later removed has to be **deleted**, not left behind: with the
constraint gone it would validate and break the suite. For example, when the
`source_mat_id` format constraint was dropped (esplims does not constrain
culture-collection identifiers), the counter-examples whose only failure was an
out-of-pattern `source_mat_id` were removed.

### Interactive testing

An interactive [DataHarmonizer](https://github.com/cidgoh/DataHarmonizer)-based interface is provided in the `data_harmonzier` directory. To start the interface locally run:

```shell
make dh-dev
```

This interface relies on the `project/json/nmdc_submission_schema.json` artifact. Therefore this file will be rebuilt if needed, and then a local development server will be started. Once startup is complete you should see a message indicating that the interface is ready on `http://127.0.0.1:5173`. 

Let this command continue to run in the background while you're developing and testing. The interface will automatically reload when changes to `project/json/nmdc_submission_schema.json` are detected, for example as a result of running 

```shell
make project/json/nmdc_submission_schema.json
```

This interface is automatically built and deployed along with the docs with every commit to `main`.