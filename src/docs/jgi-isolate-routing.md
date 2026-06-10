# JGI isolate field routing (submission-schema side)

Where the JGI Isolate submission fields land in submission-schema, and how they
relate to nmdc-schema.

The authoritative field-by-field map of all 55 JGI Isolate (NA) form fields to
their destinations lives in nmdc-schema at `src/docs/jgi-isolate-field-routing.md`.
That document is the source of truth for which nmdc-schema slot each form field
maps to. This document covers only the submission-schema side: the interface
classes, which slots they carry, and whether each slot is native to
submission-schema or imported from nmdc-schema.

## Interfaces

A JGI isolate submission is split across a biology interface and a JGI logistics
interface, with separate logistics interfaces for genome and transcriptome
projects:

- **IsolateInterface**: organism biology (genus, species, strain, taxonomic
  classification, genome size, GC, ploidy, single-colony provenance). These
  describe what the organism is. Most are stored in nmdc-schema; the single-colony
  and known-contaminants fields are JGI-only and defined in submission-schema.
- **JgiIsolateGenomeInterface**: JGI submission logistics for isolate genome
  sequencing, plus ribosomal strain-verification sequences and fungal screening.
- **JgiIsolateTranscriptomeInterface**: JGI submission logistics for isolate
  transcriptome sequencing, plus the RNA experiment collection date.

The two JGI interfaces share their common logistics fields through
**JgiIsolateCommonMixin**. Fields that apply only to genome projects (ribosomal,
fungal) are on the genome interface; `rna_collection_date` is on the
transcriptome interface.

In `SampleData`, the aggregation slots are `isolate_data` (IsolateInterface),
`jgi_isolate_genome_data` (JgiIsolateGenomeInterface), and
`jgi_isolate_transcriptome_data` (JgiIsolateTranscriptomeInterface).

## Sourcing

- **native**: defined in `nmdc_submission_schema_base.yaml`. These are JGI-only
  submission fields that nmdc-schema does not store (container, nucleic-acid QC,
  ribosomal verification, JGI sample and project identifiers).
- **imported (ClassName)**: pulled from the named nmdc-schema class via
  `config/nmdc_schema_import.yaml`. Biology and shared MIxS fields come this way.

The tables below are derived from the built schema. Regenerate them if the
interfaces change.

### IsolateInterface

| slot | section | source | required |
|---|---|---|---|
| `samp_name` | sample_id_section | imported (Biosample) | yes |
| `source_mat_id` | sample_id_section | imported (Biosample) |  |
| `analysis_type` | sample_id_section | imported (Biosample) | yes |
| `collection_date` | mixs_modified_section | imported (Biosample) | yes |
| `isolate_single_colony` | organism_section | native | yes |
| `isolate_known_contaminants` | organism_section | native |  |
| `organism_genus` | organism_section | imported (Organism) | yes |
| `organism_species` | organism_section | imported (Organism) | yes |
| `strain_name` | organism_section | imported (Organism) | yes |
| `isolate_name` | organism_section | imported (Organism) |  |
| `classified_as` | organism_section | imported (Organism) | yes |
| `estimated_size` | organism_section | imported (Organism) |  |
| `gc_content` | organism_section | imported (Organism) |  |
| `ploidy` | organism_section | imported (Organism) |  |

### JgiIsolateGenomeInterface

Shared logistics (from JgiIsolateCommonMixin) plus genome-only ribosomal and
fungal fields.

| slot | section | source | required |
|---|---|---|---|
| `jgi_seq_project` | jgi_isolate_section | native | yes |
| `samp_name` | sample_id_section | imported (Biosample) | yes |
| `jgi_seq_project_name` | jgi_isolate_section | native | yes |
| `source_mat_id` | sample_id_section | imported (Biosample) |  |
| `analysis_type` | sample_id_section | imported (Biosample) | yes |
| `jgi_samp_id` | jgi_isolate_section | native | yes |
| `jgi_sample_name` | jgi_isolate_section | native | yes |
| `replicate_group` | jgi_isolate_section | native |  |
| `nuc_acid_concentration` | jgi_isolate_section | native | yes |
| `nuc_acid_absorb1` | jgi_isolate_section | native |  |
| `jgi_sample_volume` | jgi_isolate_section | native | yes |
| `nuc_acid_absorb2` | jgi_isolate_section | native |  |
| `container_name` | jgi_isolate_section | native | yes |
| `cont_type` | jgi_isolate_section | native | yes |
| `cont_well` | jgi_isolate_section | native |  |
| `jgi_sample_format` | jgi_isolate_section | native | yes |
| `dnase` | jgi_isolate_section | native | yes |
| `isolate_meth` | jgi_isolate_section | native | yes |
| `biosafety_mat_cat` | jgi_isolate_section | native | yes |
| `jgi_sample_contact` | jgi_isolate_section | native | yes |
| `jgi_project_pi` | jgi_isolate_section | native | yes |
| `jgi_proposal_id` | jgi_isolate_section | native | yes |
| `isolate_ribosomal_seq` | jgi_isolate_section | native | yes |
| `isolate_ribosomal_seq_type` | jgi_isolate_section | native | yes |
| `isolate_ribosomal_seq_comments` | jgi_isolate_section | native |  |
| `isolate_second_ribosomal_seq` | jgi_isolate_section | native |  |
| `isolate_second_ribosomal_seq_type` | jgi_isolate_section | native |  |
| `isolate_second_ribosomal_seq_comments` | jgi_isolate_section | native |  |
| `isolate_fungal_16s_screening` | jgi_isolate_section | native |  |
| `isolate_its_match_unite` | jgi_isolate_section | native |  |
| `reference_genome` | jgi_isolate_section | native |  |
| `sample_isolated_from` | jgi_isolate_section | native | yes |
| `collection_site_or_growth_conditions` | jgi_isolate_section | native |  |
| `host_genus` | jgi_isolate_section | imported (Biosample) |  |
| `host_species` | jgi_isolate_section | imported (Biosample) |  |
| `host_strain` | jgi_isolate_section | imported (Biosample) |  |
| `host_taxid` | jgi_isolate_section | imported (Biosample) |  |

### JgiIsolateTranscriptomeInterface

Shared logistics (from JgiIsolateCommonMixin) plus the RNA experiment date. No
ribosomal or fungal fields.

| slot | section | source | required |
|---|---|---|---|
| `jgi_seq_project` | jgi_isolate_section | native | yes |
| `samp_name` | sample_id_section | imported (Biosample) | yes |
| `jgi_seq_project_name` | jgi_isolate_section | native | yes |
| `source_mat_id` | sample_id_section | imported (Biosample) |  |
| `analysis_type` | sample_id_section | imported (Biosample) | yes |
| `jgi_samp_id` | jgi_isolate_section | native | yes |
| `jgi_sample_name` | jgi_isolate_section | native | yes |
| `replicate_group` | jgi_isolate_section | native |  |
| `nuc_acid_concentration` | jgi_isolate_section | native | yes |
| `nuc_acid_absorb1` | jgi_isolate_section | native |  |
| `jgi_sample_volume` | jgi_isolate_section | native | yes |
| `nuc_acid_absorb2` | jgi_isolate_section | native |  |
| `container_name` | jgi_isolate_section | native | yes |
| `cont_type` | jgi_isolate_section | native | yes |
| `cont_well` | jgi_isolate_section | native |  |
| `jgi_sample_format` | jgi_isolate_section | native | yes |
| `dnase` | jgi_isolate_section | native | yes |
| `isolate_meth` | jgi_isolate_section | native | yes |
| `biosafety_mat_cat` | jgi_isolate_section | native | yes |
| `jgi_sample_contact` | jgi_isolate_section | native | yes |
| `jgi_project_pi` | jgi_isolate_section | native | yes |
| `jgi_proposal_id` | jgi_isolate_section | native | yes |
| `reference_genome` | jgi_isolate_section | native |  |
| `sample_isolated_from` | jgi_isolate_section | native | yes |
| `collection_site_or_growth_conditions` | jgi_isolate_section | native |  |
| `rna_collection_date` | jgi_isolate_section | native | yes |
| `host_genus` | jgi_isolate_section | imported (Biosample) |  |
| `host_species` | jgi_isolate_section | imported (Biosample) |  |
| `host_strain` | jgi_isolate_section | imported (Biosample) |  |
| `host_taxid` | jgi_isolate_section | imported (Biosample) |  |

## Related

- nmdc-schema `src/docs/jgi-isolate-field-routing.md`: the authoritative 55-field
  form-to-slot map.
- `config/nmdc_schema_import.yaml`: the import entries for every imported slot
  above.
