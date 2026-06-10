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

`make schema-build` runs `tools/build.py`, which combines the hand-written base
schema (`src/nmdc_submission_schema/schema/nmdc_submission_schema_base.yaml`) with
slots pulled from nmdc-schema as listed in `config/nmdc_schema_import.yaml`. It
writes one built schema file:
`src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml`.

The nmdc-schema slots come from the installed `nmdc_schema` Python package, so the
built schema reflects the nmdc-schema version pinned in `pyproject.toml`. To pick
up new or changed nmdc-schema slots, update the pin (or the import list) and
rebuild.

### Building the project artifacts

`make all` runs `schema-build`, then generates the project files, then the docs.
This repository commits its generated files so that tools using the schema do not
have to build it themselves:

- `src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml`: the built schema
- `project/jsonschema/nmdc_submission_schema.schema.json`: the JSON Schema used for validation
- `project/json/nmdc_submission_schema.json`: the file the DataHarmonizer interface loads
- `src/nmdc_submission_schema/datamodel/nmdc_submission_schema.py`: the Pydantic classes

Run `make all` and commit these files whenever you change the schema source or the
nmdc-schema pin, so they stay in sync with the source. The `docs/` folder is also
generated, but it is not committed.

### Automated testing

`make test` runs the Python tests and checks the example data in `src/data/`:

- every file in `src/data/valid/` must pass validation
- every file in `src/data/invalid/` must fail validation, and should fail for one
  specific reason, named in the file name

The example data uses synthetic values. The organism identity is real (for example
Dictyoglomus turgidum DSM 6724), but the JGI logistics values (sample and project
IDs, contacts, container) are invented and shaped to match real GOLD formats. No
rows are copied from the JGI example submission spreadsheet or the JGI/GOLD
lakehouse, because those carry real proposal and personnel identifiers. An earlier
lakehouse-derived example was removed and replaced with a synthetic one for this
reason.

One consequence: if you remove a constraint, an invalid example whose only error
was that constraint will start passing, which breaks the test. Delete those
examples. For instance, when the `source_mat_id` format check was removed (JGI
accepts culture-collection IDs such as "ATCC 5680"), the invalid examples that
failed only that check were deleted.

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