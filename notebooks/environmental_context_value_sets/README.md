# Environmental triad value sets

`tools/build.py` turns the `post_google_sheets_*.tsv` files in this directory into the enumerations that constrain `env_broad_scale`, `env_local_scale` and `env_medium` for the soil, water, sediment and plant-associated templates. Each TSV has an `id` and a `label` column.

The TSVs were first made from Google Sheets in which squad members voted on candidate ENVO classes. The notebooks that did that were removed after the 11.25.0 release. They are still at https://github.com/microbiomedata/submission-schema/tree/v11.25.0/notebooks/environmental_context_value_sets. Most of the voting sheets have restricted access.

## How each value set was chosen

- Water, all three slots, and plant-associated `env_broad_scale` and `env_medium`: the rows marked `TRUE` in the `include_in_enum` column of that value set's voting sheet.
- Sediment, all three slots: the classes @turbomam voted to include (`mam_vote` is 1). The `include_in_enum` column was not used.
- Plant-associated `env_local_scale`: the classes @turbomam voted to include, minus any that @cmungall voted to exclude.
- Soil `env_broad_scale`: every subclass of terrestrial biome (ENVO:00000446).
- Soil `env_local_scale`: every class whose vote sum is 1 or more and whose `IAA_score` is 0 or more. Votes were -1, 0 or +1. This includes some National Land Cover Database (NLCD) land cover classes under environmental zone (ENVO:01000408), despite the modeling questions in https://github.com/EnvironmentOntology/envo/issues/1527 and https://github.com/EnvironmentOntology/envo/issues/1583.
- Soil `env_medium`: every subclass of soil (ENVO:00001998), except subclasses of enriched soil, and except soils that ENVO relates to a class in the soil `env_local_scale` value set. For example, garden soil is left out because garden is in that set. `soil/env_medium/discover_excludable_soils_curated.tsv` lists the candidate relationships, and its `override` column records manual `keep soil` and `exclude soil` decisions.
