# Problem examples

These records **pass LinkML validation** (`linkml-validate` and the generated JSON Schema) but
are **not valid JGI submissions**. Each is either missing a JGI product-conditional required
field, or carries a value outside a JGI category-conditional bound.

We have not found a way to express these constraints in submission-schema with the current
version of LinkML. The conditions are keyed on the JGI Sequencing Product (or on fields that
live on a different tab), which the schema does not carry. Capturing them may require more
sophisticated LinkML rules, or nmdc-server TypeScript validation
(`web/src/views/SubmissionPortal/validation.ts`, where the JGI plate-well checks already live;
the product-conditional checks are tracked in https://github.com/microbiomedata/nmdc-server/issues/2176
and https://github.com/microbiomedata/nmdc-server/issues/2177 and are not yet implemented).

The one exception is the microbial `estimated_size` cap: it is in fact expressible as a LinkML
rule, proposed in https://github.com/microbiomedata/submission-schema/pull/456. If that merges,
the corresponding example here becomes a regular `invalid/` counter-example and is removed.

They are deliberately **not** in `valid/` (they are not valid submissions) and **not** in
`invalid/` (they do not fail LinkML). They are also **not exercised by `make run-examples`**,
which only asserts that `valid/` passes and `invalid/` fails. They exist to document, with
concrete data, the gap between what submission-schema currently enforces and what JGI requires.

Each file carries a one-line header naming the specific JGI rule it illustrates. The reason each
rule is not enforced in submission-schema is recorded in `notes:` on the relevant slot in the
schema source (for example `isolate_ribosomal_seq`, `reference_genome`, `replicate_group`,
`nuc_acid_absorb1`).
