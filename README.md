# submission-schema

The home of the NMDC submission schema. *Not* the home of sheets_and_friends. *Not* a GH pages host of NMDC DataHarmonizer interfaces.

## Website

* [https://microbiomedata.github.io/submission-schema](https://microbiomedata.github.io/submission-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [submission_schema](src/submission_schema)
        * [schema](src/submission_schema/schema) -- LinkML schema (edit this)
* [datamodel](src/submission_schema/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
