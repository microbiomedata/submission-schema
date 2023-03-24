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

`TODO`

### Building the project artifacts

`TODO`

### Automated testing

`TODO`

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