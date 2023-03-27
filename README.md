# submission-schema

The home of the NMDC submission schema. *Not* the home of sheets_and_friends. In development: GH pages hosted NMDC DataHarmonizer interface.

Note that the while this repo is named `submission-schema`, the generated artifacts are named `nmdc_submission_schema` for disambiguation purposes when publishing to PyPI.

## Website

* [https://microbiomedata.github.io/submission-schema](https://microbiomedata.github.io/submission-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [nmdc_submission_schema](src/nmdc_submission_schema)
        * [schema](src/nmdc_submission_schema/schema) -- LinkML schema (edit this)
* [datamodel](src/nmdc_submission_schema/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- ~~`make deploy`: deploys site~~

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
