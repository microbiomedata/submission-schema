## SampleData-water-data-minimal
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_mat_process: text [ONTO:000000000]
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-soil-data-minimal
### Input
```yaml
soil_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 111 to 222
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  elev: 123
  env_broad_scale: urban biome [ENVO:01000249]
  env_local_scale: __tunnel [ENVO:00000068]
  env_medium: bare soil [ENVO:01001616]
  env_package: soil
  growth_facil: greenhouse
  samp_name: b
  samp_store_temp: -80 Celsius
  source_mat_id: x:2
  specific_ecosystem: Unclassified
  store_cond: frozen

```
## SampleData-water-data-exhaustive-max-generic
### Input
```yaml
water_data:
- alkalinity: 100 units
  alkalinity_method: xyz
  alkyl_diethers: 100 units
  alt: 100 units
  aminopept_act: 100 units
  ammonium: 100 units
  analysis_type:
  - metagenomics
  - metatranscriptomics
  atmospheric_data: xyz;100 units
  bac_prod: 100 units
  bac_resp: 100 units
  bacteria_carb_prod: 100 units
  biomass: xyz;100 units
  bishomohopanol: 100 units
  bromide: 100 units
  calcium: 100 units
  carb_nitro_ratio: 1.5
  chem_administration: xyz [XYZ:123];2111-11-11
  chloride: 100 units
  chlorophyll: 100 units
  collection_date: '2021-01-01'
  conduc: 100 units
  density: 100 units
  depth: '1.5'
  diether_lipids: xyz;100 units
  diss_carb_dioxide: 100 units
  diss_hydrogen: 100 units
  diss_inorg_carb: 100 units
  diss_inorg_nitro: 100 units
  diss_inorg_phosp: 100 units
  diss_org_carb: 100 units
  diss_org_nitro: 100 units
  diss_oxygen: 100 units
  down_par: 100 units
  ecosystem: xyz
  ecosystem_category: xyz
  ecosystem_subtype: xyz
  ecosystem_type: xyz
  elev: 1.5
  env_broad_scale: xyz xyz xyz [XYZ:123]
  env_local_scale: xyz xyz xyz [XYZ:123]
  env_medium: xyz xyz xyz [XYZ:123]
  env_package: xyz
  experimental_factor: xyz xyz xyz [XYZ:123]
  fluor: 100 units
  geo_loc_name: 'xyz: xyz, xyz'
  glucosidase_act: 100 units
  horizon_meth: xyz
  lat_lon: 78 89
  light_intensity: 100 units
  mean_frict_vel: 100 units
  mean_peak_frict_vel: 100 units
  misc_param: xyz;100 units
  n_alkanes: xyz;100 units
  nitrate: 100 units
  nitrite: 100 units
  nitro: 100 units
  org_carb: 100 units
  org_matter: 100 units
  org_nitro: 100 units
  organism_count: xyz;100 units;qPCR
  oxy_stat_samp: anaerobe
  part_org_carb: 100 units
  part_org_nitro: 100 units
  perturbation: xyz
  petroleum_hydrocarb: 100 units
  ph: 1.5
  ph_meth: xyz
  phaeopigments: xyz;100 units
  phosphate: 100 units
  phosplipid_fatt_acid: xyz;100 units
  potassium: 100 units
  pressure: 100 units
  primary_prod: 100 units
  redox_potential: 100 units
  rel_to_oxygen: anaerobe
  salinity: 100 units
  samp_collec_device: xyz
  samp_collec_method: xyz
  samp_mat_process: text [ONTO:000000000]
  samp_name: xyz
  samp_size: 100 units
  samp_store_dur: xyz
  samp_store_loc: xyz
  samp_store_temp: 100 units
  sample_link: z:99
  silicate: 100 units
  size_frac: xyz
  size_frac_low: 100 units
  size_frac_up: 100 units
  sodium: 100 units
  soluble_react_phosp: 100 units
  source_mat_id: x:1
  specific_ecosystem: xyz
  sulfate: 100 units
  sulfide: 100 units
  suspend_part_matter: 100 units
  temp: 100 units
  tidal_stage: high tide
  tot_depth_water_col: 100 units
  tot_diss_nitro: 100 units
  tot_inorg_nitro: 100 units
  tot_nitro: 100 units
  tot_part_carb: 100 units
  turbidity: 100 units
  water_current: 100 units

```
## SampleData-emsl_data-exhasutive
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: -80
  project_id: xxx
  replicate_number: 2
  samp_name: xxx
  sample_shipped: 100 units
  sample_type: soil
  source_mat_id: x:1
  technical_reps: 3

```
## SampleData-water-data-exhaustive
### Input
```yaml
water_data:
- alkalinity: 50 milligram per liter
  alkalinity_method: titration
  alkyl_diethers: 0.005 mole per liter
  alt: 100 meter
  aminopept_act: 0.269 mole per liter per hour
  ammonium: 1.5 milligram per liter
  analysis_type:
  - metagenomics
  - metatranscriptomics
  atmospheric_data: wind speed;9 knots|rain;2.3 inches
  bac_prod: 5 milligram per cubic meter per day
  bac_resp: 300 micromole oxygen per liter per hour
  bacteria_carb_prod: 2.53 microgram per liter per hour
  biomass: total;20 gram|archeal;1 gram
  bishomohopanol: 14 microgram per liter
  bromide: 0.05 parts per million
  calcium: 0.2 micromole per liter
  carb_nitro_ratio: 1.5
  chem_administration: agar [CHEBI:2509];2018-05-11|agar [CHEBI:2509];2018-05-22
  chloride: 5000 milligram per liter
  chlorophyll: 5 milligram per cubic meter
  collection_date: '2021-01-01'
  conduc: 10 milliSiemens per centimeter
  density: 1000 kilogram per cubic meter
  depth: '1.5'
  diether_lipids: phosphatidylglycerol;1.5 parts per million|phosphatidylglycerylsulphate;1.5
    parts per million
  diss_carb_dioxide: 5 milligram per liter
  diss_hydrogen: 0.3 micromole per liter
  diss_inorg_carb: 2059 micromole per liter
  diss_inorg_nitro: 761 micromole per liter
  diss_inorg_phosp: 56.5 micromole per liter
  diss_org_carb: 205.9 micromole per liter
  diss_org_nitro: 76.1 micromole per liter
  diss_oxygen: 175 micromole per liter
  down_par: 28.71 microEinstein per square meter per second
  ecosystem: xyz
  ecosystem_category: xyz
  ecosystem_subtype: xyz
  ecosystem_type: xyz
  elev: 1.5
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  experimental_factor: time series design [EFO:0001779]
  fluor: 2.5 volts
  geo_loc_name: 'USA: Maryland, Bethesda'
  glucosidase_act: 5 mol per liter per hour
  horizon_meth: xyz
  lat_lon: 78 89
  light_intensity: 0.3 lux
  mean_frict_vel: 0.5 meter per second
  mean_peak_frict_vel: 1 meter per second
  misc_param: Bicarbonate ion concentration;2075 micromole per kilogram|Perchlorate
    ion concentration;1111 micromole per kilogram
  n_alkanes: n-hexadecane;100 milligram per liter|n-octane;111 milligram per liter
  nitrate: 65 micromole per liter
  nitrite: 0.5 micromole per liter
  nitro: 4.2 micromole per liter
  org_carb: 1.5 microgram per liter
  org_matter: 1.75 milligram per cubic meter
  org_nitro: 4 micromole per liter
  organism_count: total prokaryotes;3.5e7 cells per milliliter;qPCR|total prokaryotes;1e5
    CFU;MPN
  oxy_stat_samp: anaerobe
  part_org_carb: 1.92 micromole per liter
  part_org_nitro: 0.3 micromole per liter
  perturbation: xyz1|xyz2
  petroleum_hydrocarb: 0.05 micromole per liter
  ph: 1.5
  ph_meth: xyz
  phaeopigments: phaeopigment 1;1.5 parts per million|phaeopigment 2;1.5 parts per
    million
  phosphate: 0.7 micromole per liter
  phosplipid_fatt_acid: Tuberculostearic acid;1.5 parts per million|Palmitoleic acid;1.5
    parts per million
  photon_flux: 3.926 micromole photons per second per square meter
  potassium: 463 milligram per liter
  pressure: 50 atmosphere
  primary_prod: 100 milligram per cubic meter per day
  redox_potential: 300 millivolt
  rel_to_oxygen: anaerobe
  salinity: 25 practical salinity unit
  samp_collec_device: xyz
  samp_collec_method: xyz
  samp_mat_process: text [ONTO:000000000]
  samp_name: xyz
  samp_size: 5 liter
  samp_store_dur: xyz
  samp_store_loc: xyz
  samp_store_temp: -80 degree Celsius
  sample_link: z:99
  silicate: 0.05 micromole per liter
  size_frac: xyz
  size_frac_low: 0.2 micrometer
  size_frac_up: 20 micrometer
  sodium: 10.5 milligram per liter
  soluble_react_phosp: 0.1 milligram per liter
  source_mat_id: x:1
  specific_ecosystem: xyz
  sulfate: 5 micromole per liter
  sulfide: 2 micromole per liter
  suspend_part_matter: 0.5 milligram per liter
  temp: 25 degree Celsius
  tidal_stage: high tide
  tot_depth_water_col: 500 meter
  tot_diss_nitro: 40 microgram per liter
  tot_inorg_nitro: 40 microgram per liter
  tot_nitro: 50 micromole per liter
  tot_part_carb: 35 micromole per liter
  turbidity: 0.3 nephelometric turbidity units
  water_current: 10 cubic meter per second

```
## SampleData-water-data-0-dim-depth
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '1.5'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-emsl_data-minimal
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: -80
  project_id: xxx
  samp_name: xxx
  sample_shipped: 100 units
  sample_type: soil
  source_mat_id: x:1

```
## SampleData-soil-data-exhaustive
### Input
```yaml
soil_data:
- air_temp_regm: xxx
  al_sat_meth: xxx
  alt: 111 units
  analysis_type:
  - metagenomics
  - metatranscriptomics
  annual_precpt: 111 units
  annual_temp: 111 units
  biotic_regm: xxx
  biotic_relationship: free living
  carb_nitro_ratio: 0.5
  chem_administration: agar [CHEBI:2509];2018-05-11|agar [CHEBI:2509];2018-05-22
  climate_environment: xxx
  collection_date: '2022-01-15'
  collection_date_inc: '2022-01-22'
  collection_time: '11:11'
  collection_time_inc: '11:11'
  crop_rotation: xxx
  cur_land_use: cities
  cur_vegetation: xxx
  cur_vegetation_meth: xxx
  depth: '111'
  drainage_class: well
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  elev: 123
  env_broad_scale: urban biome [ENVO:01000249]
  env_local_scale: __tunnel [ENVO:00000068]
  env_medium: bare soil [ENVO:01001616]
  env_package: soil
  experimental_factor: xxx [ENVO:00000000]
  experimental_factor_other: xxx
  extreme_event: xxx
  fao_class: Rankers
  filter_method: xxx
  fire: '2022-01-15'
  flooding: xxx
  gaseous_environment: xxx
  geo_loc_name: 'USA: Maryland, Bethesda'
  growth_facil: greenhouse
  heavy_metals_meth: xxx
  horizon_meth: xxx
  humidity_regm: xxx
  isotope_exposure: strontium 90 [ONTO:00000000]; 2010-10-31T08:45:15.432-0700
  lat_lon: 77 88
  light_regm: incandescant light;10 lux;450 nanometer
  link_class_info: xxx
  link_climate_info: xxx
  local_class: xxx
  local_class_meth: xxx
  micro_biomass_c_meth: xxx
  micro_biomass_meth: xxx
  micro_biomass_n_meth: xxx
  microbial_biomass: 111 units
  microbial_biomass_c: 111 units
  microbial_biomass_n: 111 units
  non_microb_biomass: xxx;123.45 units
  non_microb_biomass_method: xxx
  org_matter: 111 units
  org_nitro: 111 units
  org_nitro_method: xxx
  other_treatment: xxx
  oxy_stat_samp: anaerobe
  ph: 9
  ph_meth: xxx
  phosphate: 111 units
  prev_land_use_meth: xxx
  previous_land_use: circus tent;+0530
  profile_position: summit
  rel_to_oxygen: anaerobe
  salinity: 111 units
  salinity_meth: xxx
  samp_collec_device: xxx
  samp_collec_method: xxx
  samp_mat_process: text [ONTO:000000000]
  samp_name: a
  samp_size: 111 units
  samp_store_temp: -80 Celsius
  sample_link: z:99
  season_precpt: 111 units
  season_temp: 111 units
  sieving: xxx
  size_frac_low: 99 units
  size_frac_up: 111 units
  slope_aspect: 100 units
  slope_gradient: 111 units
  soil_horizon: O horizon
  soil_text_measure: 111 units
  soil_texture_meth: xxx
  soil_type: xxx [ENVO:00000000]
  soil_type_meth: xxx
  source_mat_id: x:1
  specific_ecosystem: Unclassified
  start_date_inc: '2022-02-15'
  start_time_inc: '13:33:55'
  store_cond: frozen
  temp: 111 units
  tillage:
  - drill
  - chisel
  tot_carb: 111 units
  tot_nitro_cont_meth: xxx
  tot_nitro_content: 111 units
  tot_org_c_meth: xxx
  tot_org_carb: 111 units
  tot_phosp: 111 units
  water_cont_soil_meth: xxx
  water_content: 111 units
  watering_regm: xxx
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 111 to 222
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  elev: 123
  env_broad_scale: urban biome [ENVO:01000249]
  env_local_scale: __tunnel [ENVO:00000068]
  env_medium: bare soil [ENVO:01001616]
  env_package: soil
  geo_loc_name: 'USA: Maryland, Bethesda'
  growth_facil: greenhouse
  lat_lon: 77 88
  samp_name: b
  samp_store_temp: -80 Celsius
  sample_link: z:99
  slope_aspect: 100 units
  source_mat_id: x:2
  specific_ecosystem: Unclassified
  store_cond: frozen

```
## SampleData-water-data-1-dim-depth
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 1.5 to 2.5
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-jgi_mg_data-minimal
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: C3
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 999
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-jgi_mg_data-exhaustive
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_absorb1: 1.23
  dna_absorb2: 1.23
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: C3
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_organisms: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-water-data-invalid-analysis-type
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - invalid
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-emsl_data-bad-emsl_store_temp
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: ice cold
  project_id: xxx
  samp_name: xxx
  sample_shipped: 100 units
  sample_type: soil
  source_mat_id: x:1

```
## SampleData-water-data-missing-broad
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-invalid-tidal_stage
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified
  tidal_stage: xyz

```
## SampleData-water-data-broad-label-only
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-organsim_count-invalid-method
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  organism_count: xyz;100 units;xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-jgi_mg_data-bad-dna_cont_type
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: bucket
  dna_cont_well: H3
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-emsl_data-bad-sample_type
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: -80
  project_id: xxx
  samp_name: xxx
  sample_shipped: 100 units
  sample_type: sandwich
  source_mat_id: x:1

```
## SampleData-jgi_mg_data-bad-dna_cont_well
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: Z99
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-emsl_data-bad-sample_shipped
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: -80
  project_id: xxx
  samp_name: xxx
  sample_shipped: three buckets
  sample_type: soil
  source_mat_id: x:1

```
## SampleData-water-data-string-alkalinity
### Input
```yaml
water_data:
- alkalinity: really high
  analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-string-c-n-ratio
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  carb_nitro_ratio: really high
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-scalar-analysis-type
### Input
```yaml
water_data:
- analysis_type: metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-numeric-alkalinity
### Input
```yaml
water_data:
- alkalinity: 999
  analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-jgi_mg_data-bad-dna_dnase
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: C3
  dna_container_id: xxx
  dna_dnase: false
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-jgi_mg_data-bad-dna_volume
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: C3
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: DNAStable
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23 liters
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-emsl_data-bad-source_mat_id
### Input
```yaml
emsl_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  emsl_store_temp: -80
  project_id: xxx
  samp_name: xxx
  sample_shipped: 100 units
  sample_type: soil
  source_mat_id: no_colon

```
## SampleData-water-data-invalid-rel_to_oxygen
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  rel_to_oxygen: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-numeric-depth
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 1.5
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-no-source_mat_id
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  specific_ecosystem: Unclassified

```
## SampleData-water-data-broad-term-only
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_local_scale:
  - ONTO:1234
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-soil-data-missing-elev
### Input
```yaml
soil_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 111 to 222
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: urban biome [ENVO:01000249]
  env_local_scale: __tunnel [ENVO:00000068]
  env_medium: bare soil [ENVO:01001616]
  env_package: soil
  growth_facil: greenhouse
  samp_name: b
  samp_store_temp: -80 Celsius
  source_mat_id: x:2
  specific_ecosystem: Unclassified
  store_cond: frozen

```
## SampleData-water-data-alkalinity-list
### Input
```yaml
water_data:
- alkalinity:
  - 50 milligram per liter
  - 100 spoons per bucket
  analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_mat_process: text [ONTO:000000000]
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-string-depth
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: meters
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-jgi_mg_data-bad-dna_sample_format
### Input
```yaml
jgi_mg_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  dna_collect_site: xxx
  dna_concentration: 1.23
  dna_cont_type: plate
  dna_cont_well: C3
  dna_container_id: xxx
  dna_dnase: 'no'
  dna_isolate_meth: xxx
  dna_project_contact: xxx
  dna_samp_id: xxx
  dna_sample_format: red red wine
  dna_sample_name: xxx
  dna_seq_project: xxx
  dna_seq_project_name: xxx
  dna_seq_project_pi: xxx
  dna_volume: 1.23
  proposal_dna: xxx
  samp_name: xxx
  source_mat_id: x:1

```
## SampleData-water-data-incomplete-organsim_count
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  organism_count: xyz;100 units
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-depth-invalid-range
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: 1.5-2.5
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  samp_name: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
## SampleData-water-data-no-samp_name
### Input
```yaml
water_data:
- analysis_type:
  - metagenomics
  - metatranscriptomics
  collection_date: '2022-01-15'
  depth: '111'
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale: oceanic epipelagic zone biome [ENVO:01000033]
  env_local_scale: sand [ONTO:1234]
  env_medium: sand [ONTO:1234]
  env_package: xyz
  source_mat_id: x:1
  specific_ecosystem: Unclassified

```
