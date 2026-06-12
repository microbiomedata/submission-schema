# Problem examples

These records **pass LinkML validation** (`linkml-validate` and the generated JSON Schema) but
are **not valid JGI submissions**. Each is either missing a JGI product-conditional required
field, or carries a value outside a JGI category-conditional bound, that LinkML cannot express
or enforce.

They are deliberately **not** in `valid/` (they are not valid submissions) and **not** in
`invalid/` (they do not fail LinkML). They are also **not exercised by `make run-examples`**,
which only asserts that `valid/` passes and `invalid/` fails. They exist to document, with
concrete data, the gap between what submission-schema can enforce and what JGI requires; these
are the cases the nmdc-server TypeScript validator is expected to catch.

See each file's header comments for the specific JGI rule it illustrates.
