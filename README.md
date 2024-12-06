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

### Updating the submission schema

Here's how you can update the submission schema to use a new version of `nmdc-schema`:

1. Update the one occurrence of the `nmdc-schema` version number in `project.Makefile`:

    ```diff
    local/nmdc.yaml:
    -        wget -O $@ https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v11.0.1/nmdc_schema/nmdc_materialized_patterns.yaml
    +        wget -O $@ https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v11.1.0/nmdc_schema/nmdc_materialized_patterns.yaml
    ```

2. Update all the `nmdc-schema` version numbers in `sheets_and_friends/tsv_in/import_slots_regardless.tsv`

    ```diff
    - Biosample	https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v11.0.1/nmdc_schema/nmdc_materialized_patterns.yaml	abs_air_humidity ...
    + Biosample	https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v11.1.0/nmdc_schema/nmdc_materialized_patterns.yaml	abs_air_humidity ...
    ```
    > That is one of the _many_ occurrences in that file.
    >
    > **Note:** The above search-and-replacement (of all occurrences in that file) can be done inside Vim via:
    > ```vim
    > :%s/nmdc-schema\/v11.0.1/nmdc-schema\/v11.1.0/g
    > ```

### Building the submission schema

Here's how you can generate the submission schema release artifacts:

#### Container-based process

##### Prerequisites

- Docker is installed on your computer
- You are in the root directory of the repository

##### Procedure

1. Build the container image you will later use to build the submission schema:
   ```shell
   docker build -t submission-schema-builder -f builder.Dockerfile .
   ```
2. Use that container image to build the submission schema:
   ```shell
   docker run --rm -it -v ${PWD}:/submission-schema submission-schema-builder
   ```
3. (Optional) Delete the container image:
   ```shell
   docker image rm submission-schema-builder
   ```

#### Direct process

##### Prerequisites

- `yq` is installed on your computer, such that the following command shows a version number instead of an error message.
  ```shell
  bash -c 'yq --version'
  ```
  If `yq` is not installed, you can install it by running this, assuming you're using macOS:
  ```shell
  brew install yq
  ```
- `wget` is installed on your computer, such that the following command shows a version number instead of an error message.
  ```shell
  bash -c 'wget --version'
  ```
  If `wget` is not installed, you can install it by running this, assuming you're using macOS:
  ```shell
  brew install wget
  ```

##### Procedure

1. Install Python dependencies:
   ```shell
   poetry shell
   poetry install
   ```
2. Generate the release artefacts:
   ```shell
   make all
   ```
3. Commit the changes, using the new `nmdc-schema` version number as the commit message; like this:
   ```shell
   git add .
   git commit -m "11.1.0"
   ```

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
