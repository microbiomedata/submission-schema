# Auto generated from submission_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T14:07:05
# Schema: nmdc_submission_schema
#
# id: https://example.com/nmdc_submission_schema
# description: Schema for creating Data Harmonizer interfaces for biosamples based on MIxS and other standards
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Datetime, Double, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
COG = CurieNamespace('COG', 'https://unknown.to.linter.org/')
EC = CurieNamespace('EC', 'https://unknown.to.linter.org/')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD = CurieNamespace('GOLD', 'http://identifiers.org/gold/')
IMG_TAXON = CurieNamespace('IMG_TAXON', 'http://identifiers.org/img.taxon/')
ISA = CurieNamespace('ISA', 'https://unknown.to.linter.org/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'http://identifiers.org/kegg.orthology/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'http://identifiers.org/kegg.pathway/')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
METACYC = CurieNamespace('MetaCyc', 'https://identifiers.org/metacyc.reaction/')
METANETX = CurieNamespace('MetaNetX', 'https://unknown.to.linter.org/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RETRORULES = CurieNamespace('RetroRules', 'https://unknown.to.linter.org/')
SEED = CurieNamespace('SEED', 'http://identifiers.org/seed/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'https://identifiers.org/uniprot/')
BARE = CurieNamespace('bare', 'https://unknown.to.linter.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EMSL = CurieNamespace('emsl', 'https://unknown.to.linter.org/')
GTPO = CurieNamespace('gtpo', 'https://unknown.to.linter.org/')
IGSN = CurieNamespace('igsn', 'https://app.geosamples.org/sample/igsn/')
IGSNVOC = CurieNamespace('igsnvoc', 'https://igsn.org/voc/v1/')
INSDC_SRS = CurieNamespace('insdc_srs', 'https://unknown.to.linter.org/')
JGI = CurieNamespace('jgi', 'https://unknown.to.linter.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MGNIFY = CurieNamespace('mgnify', 'https://unknown.to.linter.org/')
MIXS_VOCAB = CurieNamespace('mixs_vocab', 'https://genomicsstandardsconsortium.github.io/mixs/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
NMDC_SUB_SCHEMA = CurieNamespace('nmdc_sub_schema', 'https://example.com/nmdc_sub_schema/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS84 = CurieNamespace('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC_SUB_SCHEMA


# Types
class DecimalDegree(float):
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = NMDC_SUB_SCHEMA.DecimalDegree


class LanguageCode(str):
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = NMDC_SUB_SCHEMA.LanguageCode


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = NMDC_SUB_SCHEMA.Unit


# Class references
class DhMutliviewCommonColumnsSourceMatId(extended_str):
    pass


class ActivityId(extended_str):
    pass


class NamedThingId(extended_str):
    pass


class OntologyClassId(NamedThingId):
    pass


@dataclass
class SampleData(YAMLRoot):
    """
    represents data produced by the DataHarmonizer tabs of the submission portal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampleData
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SampleData"
    class_name: ClassVar[str] = "SampleData"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampleData

    air_data: Optional[Union[Union[dict, "Air"], List[Union[dict, "Air"]]]] = empty_list()
    biofilm_data: Optional[Union[Union[dict, "Biofilm"], List[Union[dict, "Biofilm"]]]] = empty_list()
    bioscales_data: Optional[Union[Union[dict, "Bioscales"], List[Union[dict, "Bioscales"]]]] = empty_list()
    built_env_data: Optional[Union[Union[dict, "BuiltEnv"], List[Union[dict, "BuiltEnv"]]]] = empty_list()
    host_associated_data: Optional[Union[Union[dict, "HostAssociated"], List[Union[dict, "HostAssociated"]]]] = empty_list()
    plant_associated_data: Optional[Union[Union[dict, "PlantAssociated"], List[Union[dict, "PlantAssociated"]]]] = empty_list()
    sediment_data: Optional[Union[Union[dict, "Sediment"], List[Union[dict, "Sediment"]]]] = empty_list()
    soil_data: Optional[Union[Union[dict, "Soil"], List[Union[dict, "Soil"]]]] = empty_list()
    wastewater_sludge_data: Optional[Union[Union[dict, "WastewaterSludge"], List[Union[dict, "WastewaterSludge"]]]] = empty_list()
    water_data: Optional[Union[Union[dict, "Water"], List[Union[dict, "Water"]]]] = empty_list()
    emsl_data: Optional[Union[Union[dict, "Emsl"], List[Union[dict, "Emsl"]]]] = empty_list()
    jgi_mg_data: Optional[Union[Union[dict, "JgiMg"], List[Union[dict, "JgiMg"]]]] = empty_list()
    jgi_mt_data: Optional[Union[Union[dict, "JgiMt"], List[Union[dict, "JgiMt"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.air_data, list):
            self.air_data = [self.air_data] if self.air_data is not None else []
        self.air_data = [v if isinstance(v, Air) else Air(**as_dict(v)) for v in self.air_data]

        if not isinstance(self.biofilm_data, list):
            self.biofilm_data = [self.biofilm_data] if self.biofilm_data is not None else []
        self.biofilm_data = [v if isinstance(v, Biofilm) else Biofilm(**as_dict(v)) for v in self.biofilm_data]

        if not isinstance(self.bioscales_data, list):
            self.bioscales_data = [self.bioscales_data] if self.bioscales_data is not None else []
        self.bioscales_data = [v if isinstance(v, Bioscales) else Bioscales(**as_dict(v)) for v in self.bioscales_data]

        if not isinstance(self.built_env_data, list):
            self.built_env_data = [self.built_env_data] if self.built_env_data is not None else []
        self.built_env_data = [v if isinstance(v, BuiltEnv) else BuiltEnv(**as_dict(v)) for v in self.built_env_data]

        if not isinstance(self.host_associated_data, list):
            self.host_associated_data = [self.host_associated_data] if self.host_associated_data is not None else []
        self.host_associated_data = [v if isinstance(v, HostAssociated) else HostAssociated(**as_dict(v)) for v in self.host_associated_data]

        if not isinstance(self.plant_associated_data, list):
            self.plant_associated_data = [self.plant_associated_data] if self.plant_associated_data is not None else []
        self.plant_associated_data = [v if isinstance(v, PlantAssociated) else PlantAssociated(**as_dict(v)) for v in self.plant_associated_data]

        if not isinstance(self.sediment_data, list):
            self.sediment_data = [self.sediment_data] if self.sediment_data is not None else []
        self.sediment_data = [v if isinstance(v, Sediment) else Sediment(**as_dict(v)) for v in self.sediment_data]

        if not isinstance(self.soil_data, list):
            self.soil_data = [self.soil_data] if self.soil_data is not None else []
        self.soil_data = [v if isinstance(v, Soil) else Soil(**as_dict(v)) for v in self.soil_data]

        if not isinstance(self.wastewater_sludge_data, list):
            self.wastewater_sludge_data = [self.wastewater_sludge_data] if self.wastewater_sludge_data is not None else []
        self.wastewater_sludge_data = [v if isinstance(v, WastewaterSludge) else WastewaterSludge(**as_dict(v)) for v in self.wastewater_sludge_data]

        if not isinstance(self.water_data, list):
            self.water_data = [self.water_data] if self.water_data is not None else []
        self.water_data = [v if isinstance(v, Water) else Water(**as_dict(v)) for v in self.water_data]

        if not isinstance(self.emsl_data, list):
            self.emsl_data = [self.emsl_data] if self.emsl_data is not None else []
        self.emsl_data = [v if isinstance(v, Emsl) else Emsl(**as_dict(v)) for v in self.emsl_data]

        if not isinstance(self.jgi_mg_data, list):
            self.jgi_mg_data = [self.jgi_mg_data] if self.jgi_mg_data is not None else []
        self.jgi_mg_data = [v if isinstance(v, JgiMg) else JgiMg(**as_dict(v)) for v in self.jgi_mg_data]

        if not isinstance(self.jgi_mt_data, list):
            self.jgi_mt_data = [self.jgi_mt_data] if self.jgi_mt_data is not None else []
        self.jgi_mt_data = [v if isinstance(v, JgiMt) else JgiMt(**as_dict(v)) for v in self.jgi_mt_data]

        super().__post_init__(**kwargs)


class DhInterface(YAMLRoot):
    """
    One DataHarmonizer interface, for the specified combination of a checklist, enviornmental_package, and various
    standards, user facilities or analysis types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:DhInterface"
    class_name: ClassVar[str] = "dh_interface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhInterface


@dataclass
class Air(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Air
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Air"
    class_name: ClassVar[str] = "air"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Air

    air_PM_concen: Optional[Union[str, List[str]]] = empty_list()
    alt: Optional[str] = None
    barometric_press: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    geo_loc_name: Optional[str] = None
    humidity: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    methane: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    oxygen: Optional[str] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    pollutants: Optional[Union[str, List[str]]] = empty_list()
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    size_frac: Optional[str] = None
    solar_irradiance: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    temp: Optional[str] = None
    ventilation_rate: Optional[str] = None
    ventilation_type: Optional[str] = None
    volatile_org_comp: Optional[Union[str, List[str]]] = empty_list()
    wind_direction: Optional[str] = None
    wind_speed: Optional[str] = None
    horizon_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.air_PM_concen, list):
            self.air_PM_concen = [self.air_PM_concen] if self.air_PM_concen is not None else []
        self.air_PM_concen = [v if isinstance(v, str) else str(v) for v in self.air_PM_concen]

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.barometric_press is not None and not isinstance(self.barometric_press, str):
            self.barometric_press = str(self.barometric_press)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.oxygen is not None and not isinstance(self.oxygen, str):
            self.oxygen = str(self.oxygen)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if not isinstance(self.pollutants, list):
            self.pollutants = [self.pollutants] if self.pollutants is not None else []
        self.pollutants = [v if isinstance(v, str) else str(v) for v in self.pollutants]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.ventilation_rate is not None and not isinstance(self.ventilation_rate, str):
            self.ventilation_rate = str(self.ventilation_rate)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if not isinstance(self.volatile_org_comp, list):
            self.volatile_org_comp = [self.volatile_org_comp] if self.volatile_org_comp is not None else []
        self.volatile_org_comp = [v if isinstance(v, str) else str(v) for v in self.volatile_org_comp]

        if self.wind_direction is not None and not isinstance(self.wind_direction, str):
            self.wind_direction = str(self.wind_direction)

        if self.wind_speed is not None and not isinstance(self.wind_speed, str):
            self.wind_speed = str(self.wind_speed)

        if not isinstance(self.air_PM_concen, list):
            self.air_PM_concen = [self.air_PM_concen] if self.air_PM_concen is not None else []
        self.air_PM_concen = [v if isinstance(v, str) else str(v) for v in self.air_PM_concen]

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.barometric_press is not None and not isinstance(self.barometric_press, str):
            self.barometric_press = str(self.barometric_press)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.oxygen is not None and not isinstance(self.oxygen, str):
            self.oxygen = str(self.oxygen)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if not isinstance(self.pollutants, list):
            self.pollutants = [self.pollutants] if self.pollutants is not None else []
        self.pollutants = [v if isinstance(v, str) else str(v) for v in self.pollutants]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.ventilation_rate is not None and not isinstance(self.ventilation_rate, str):
            self.ventilation_rate = str(self.ventilation_rate)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if not isinstance(self.volatile_org_comp, list):
            self.volatile_org_comp = [self.volatile_org_comp] if self.volatile_org_comp is not None else []
        self.volatile_org_comp = [v if isinstance(v, str) else str(v) for v in self.volatile_org_comp]

        if self.wind_direction is not None and not isinstance(self.wind_direction, str):
            self.wind_direction = str(self.wind_direction)

        if self.wind_speed is not None and not isinstance(self.wind_speed, str):
            self.wind_speed = str(self.wind_speed)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class Biofilm(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Biofilm
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Biofilm"
    class_name: ClassVar[str] = "biofilm"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Biofilm

    alkalinity: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    alt: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biomass: Optional[Union[str, List[str]]] = empty_list()
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[str] = None
    diether_lipids: Optional[Union[str, List[str]]] = empty_list()
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    geo_loc_name: Optional[str] = None
    glucosidase_act: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    methane: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    n_alkanes: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    part_org_carb: Optional[str] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    phaeopigments: Optional[Union[str, List[str]]] = empty_list()
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[Union[str, List[str]]] = empty_list()
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    redox_potential: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    silicate: Optional[str] = None
    size_frac: Optional[str] = None
    sodium: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    tot_carb: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_content: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if not isinstance(self.water_content, list):
            self.water_content = [self.water_content] if self.water_content is not None else []
        self.water_content = [v if isinstance(v, str) else str(v) for v in self.water_content]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class Bioscales(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Bioscales
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Bioscales"
    class_name: ClassVar[str] = "bioscales"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Bioscales

    agrochem_addition: Optional[Union[str, List[str]]] = empty_list()
    air_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    al_sat: Optional[str] = None
    al_sat_meth: Optional[str] = None
    alt: Optional[str] = None
    ammonium_nitrogen: Optional[str] = None
    annual_precpt: Optional[str] = None
    annual_temp: Optional[str] = None
    biotic_regm: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    crop_rotation: Optional[str] = None
    cur_land_use: Optional[Union[str, "CurLandUseEnum"]] = None
    cur_vegetation: Optional[str] = None
    cur_vegetation_meth: Optional[str] = None
    depth: Optional[str] = None
    drainage_class: Optional[Union[str, "DrainageClassEnum"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    extreme_event: Optional[Union[dict, "TimestampValue"]] = None
    fao_class: Optional[Union[str, "FaoClassEnum"]] = None
    fire: Optional[Union[dict, "TimestampValue"]] = None
    flooding: Optional[Union[dict, "TimestampValue"]] = None
    gaseous_environment: Optional[Union[str, List[str]]] = empty_list()
    geo_loc_name: Optional[str] = None
    growth_facil: Optional[str] = None
    heavy_metals: Optional[Union[str, List[str]]] = empty_list()
    heavy_metals_meth: Optional[str] = None
    horizon_meth: Optional[str] = None
    humidity_regm: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    lbc_thirty: Optional[str] = None
    lbceq: Optional[str] = None
    light_regm: Optional[str] = None
    link_class_info: Optional[str] = None
    link_climate_info: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
    magnesium: Optional[str] = None
    manganese: Optional[str] = None
    micro_biomass_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate_nitrogen: Optional[str] = None
    nitrite_nitrogen: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    phosphate: Optional[str] = None
    potassium: Optional[str] = None
    prev_land_use_meth: Optional[str] = None
    previous_land_use: Optional[str] = None
    profile_position: Optional[Union[str, "ProfilePositionEnum"]] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    salinity_meth: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_temp: Optional[str] = None
    season_precpt: Optional[str] = None
    season_temp: Optional[str] = None
    sieving: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    slope_aspect: Optional[str] = None
    slope_gradient: Optional[str] = None
    soil_horizon: Optional[Union[str, "SoilHorizonEnum"]] = None
    soil_text_measure: Optional[str] = None
    soil_texture_meth: Optional[str] = None
    soil_type: Optional[str] = None
    soil_type_meth: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    store_cond: Optional[str] = None
    temp: Optional[str] = None
    tillage: Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]] = empty_list()
    tot_carb: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    tot_phosp: Optional[str] = None
    water_cont_soil_meth: Optional[str] = None
    water_content: Optional[str] = None
    watering_regm: Optional[Union[str, List[str]]] = empty_list()
    zinc: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium_nitrogen is not None and not isinstance(self.ammonium_nitrogen, str):
            self.ammonium_nitrogen = str(self.ammonium_nitrogen)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, TimestampValue):
            self.extreme_event = TimestampValue(**as_dict(self.extreme_event))

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, TimestampValue):
            self.fire = TimestampValue(**as_dict(self.fire))

        if self.flooding is not None and not isinstance(self.flooding, TimestampValue):
            self.flooding = TimestampValue(**as_dict(self.flooding))

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.lbc_thirty is not None and not isinstance(self.lbc_thirty, str):
            self.lbc_thirty = str(self.lbc_thirty)

        if self.lbceq is not None and not isinstance(self.lbceq, str):
            self.lbceq = str(self.lbceq)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.manganese is not None and not isinstance(self.manganese, str):
            self.manganese = str(self.manganese)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate_nitrogen is not None and not isinstance(self.nitrate_nitrogen, str):
            self.nitrate_nitrogen = str(self.nitrate_nitrogen)

        if self.nitrite_nitrogen is not None and not isinstance(self.nitrite_nitrogen, str):
            self.nitrite_nitrogen = str(self.nitrite_nitrogen)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, str):
            self.soil_text_measure = str(self.soil_text_measure)

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.store_cond is not None and not isinstance(self.store_cond, str):
            self.store_cond = str(self.store_cond)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if self.zinc is not None and not isinstance(self.zinc, str):
            self.zinc = str(self.zinc)

        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium_nitrogen is not None and not isinstance(self.ammonium_nitrogen, str):
            self.ammonium_nitrogen = str(self.ammonium_nitrogen)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.ecosystem is not None and not isinstance(self.ecosystem, EcosystemEnum):
            self.ecosystem = EcosystemEnum(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, EcosystemCategoryEnum):
            self.ecosystem_category = EcosystemCategoryEnum(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, EcosystemSubtypeEnum):
            self.ecosystem_subtype = EcosystemSubtypeEnum(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, EcosystemTypeEnum):
            self.ecosystem_type = EcosystemTypeEnum(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, EnvBroadScaleSoilEnum):
            self.env_broad_scale = EnvBroadScaleSoilEnum(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, EnvLocalScaleSoilEnum):
            self.env_local_scale = EnvLocalScaleSoilEnum(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, EnvMediumSoilEnum):
            self.env_medium = EnvMediumSoilEnum(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, str):
            self.extreme_event = str(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, str):
            self.fire = str(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, str):
            self.flooding = str(self.flooding)

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.growth_facil is not None and not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if not isinstance(self.heavy_metals_meth, list):
            self.heavy_metals_meth = [self.heavy_metals_meth] if self.heavy_metals_meth is not None else []
        self.heavy_metals_meth = [v if isinstance(v, str) else str(v) for v in self.heavy_metals_meth]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.lbc_thirty is not None and not isinstance(self.lbc_thirty, str):
            self.lbc_thirty = str(self.lbc_thirty)

        if self.lbceq is not None and not isinstance(self.lbceq, str):
            self.lbceq = str(self.lbceq)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.manganese is not None and not isinstance(self.manganese, str):
            self.manganese = str(self.manganese)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate_nitrogen is not None and not isinstance(self.nitrate_nitrogen, str):
            self.nitrate_nitrogen = str(self.nitrate_nitrogen)

        if self.nitrite_nitrogen is not None and not isinstance(self.nitrite_nitrogen, str):
            self.nitrite_nitrogen = str(self.nitrite_nitrogen)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, str):
            self.soil_text_measure = str(self.soil_text_measure)

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, SpecificEcosystemEnum):
            self.specific_ecosystem = SpecificEcosystemEnum(self.specific_ecosystem)

        if self.store_cond is not None and not isinstance(self.store_cond, StoreCondEnum):
            self.store_cond = StoreCondEnum(self.store_cond)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if not isinstance(self.water_content, list):
            self.water_content = [self.water_content] if self.water_content is not None else []
        self.water_content = [v if isinstance(v, str) else str(v) for v in self.water_content]

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if self.zinc is not None and not isinstance(self.zinc, str):
            self.zinc = str(self.zinc)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class BuiltEnv(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BuiltEnv
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:BuiltEnv"
    class_name: ClassVar[str] = "built_env"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BuiltEnv

    abs_air_humidity: Optional[str] = None
    address: Optional[str] = None
    adj_room: Optional[str] = None
    aero_struc: Optional[str] = None
    alt: Optional[str] = None
    amount_light: Optional[str] = None
    arch_struc: Optional[Union[str, "ArchStrucEnum"]] = None
    avg_dew_point: Optional[str] = None
    avg_occup: Optional[str] = None
    avg_temp: Optional[str] = None
    bathroom_count: Optional[str] = None
    bedroom_count: Optional[str] = None
    build_docs: Optional[Union[str, "BuildDocsEnum"]] = None
    build_occup_type: Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]] = empty_list()
    building_setting: Optional[Union[str, "BuildingSettingEnum"]] = None
    built_struc_age: Optional[str] = None
    built_struc_set: Optional[str] = None
    built_struc_type: Optional[str] = None
    carb_dioxide: Optional[str] = None
    ceil_area: Optional[str] = None
    ceil_cond: Optional[Union[str, "CeilCondEnum"]] = None
    ceil_finish_mat: Optional[Union[str, "CeilFinishMatEnum"]] = None
    ceil_struc: Optional[str] = None
    ceil_texture: Optional[Union[str, "CeilTextureEnum"]] = None
    ceil_thermal_mass: Optional[str] = None
    ceil_type: Optional[Union[str, "CeilTypeEnum"]] = None
    ceil_water_mold: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    cool_syst_id: Optional[str] = None
    date_last_rain: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[str] = None
    dew_point: Optional[str] = None
    door_comp_type: Optional[Union[str, "DoorCompTypeEnum"]] = None
    door_cond: Optional[Union[str, "DoorCondEnum"]] = None
    door_direct: Optional[Union[str, "DoorDirectEnum"]] = None
    door_loc: Optional[Union[str, "DoorLocEnum"]] = None
    door_mat: Optional[Union[str, "DoorMatEnum"]] = None
    door_move: Optional[Union[str, "DoorMoveEnum"]] = None
    door_size: Optional[str] = None
    door_type: Optional[Union[str, "DoorTypeEnum"]] = None
    door_type_metal: Optional[Union[str, "DoorTypeMetalEnum"]] = None
    door_type_wood: Optional[Union[str, "DoorTypeWoodEnum"]] = None
    door_water_mold: Optional[str] = None
    drawings: Optional[Union[str, "DrawingsEnum"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    elevator: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    escalator: Optional[str] = None
    exp_duct: Optional[str] = None
    exp_pipe: Optional[str] = None
    experimental_factor: Optional[str] = None
    ext_door: Optional[str] = None
    ext_wall_orient: Optional[Union[str, "ExtWallOrientEnum"]] = None
    ext_window_orient: Optional[Union[str, "ExtWindowOrientEnum"]] = None
    filter_type: Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]] = empty_list()
    fireplace_type: Optional[str] = None
    floor_age: Optional[str] = None
    floor_area: Optional[str] = None
    floor_cond: Optional[Union[str, "FloorCondEnum"]] = None
    floor_count: Optional[str] = None
    floor_finish_mat: Optional[Union[str, "FloorFinishMatEnum"]] = None
    floor_struc: Optional[Union[str, "FloorStrucEnum"]] = None
    floor_thermal_mass: Optional[str] = None
    floor_water_mold: Optional[Union[str, "FloorWaterMoldEnum"]] = None
    freq_clean: Optional[str] = None
    freq_cook: Optional[str] = None
    furniture: Optional[Union[str, "FurnitureEnum"]] = None
    gender_restroom: Optional[Union[str, "GenderRestroomEnum"]] = None
    geo_loc_name: Optional[str] = None
    hall_count: Optional[str] = None
    handidness: Optional[Union[str, "HandidnessEnum"]] = None
    heat_cool_type: Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]] = empty_list()
    heat_deliv_loc: Optional[Union[str, "HeatDelivLocEnum"]] = None
    heat_sys_deliv_meth: Optional[str] = None
    heat_system_id: Optional[str] = None
    height_carper_fiber: Optional[str] = None
    indoor_space: Optional[Union[str, "IndoorSpaceEnum"]] = None
    indoor_surf: Optional[Union[str, "IndoorSurfEnum"]] = None
    inside_lux: Optional[str] = None
    int_wall_cond: Optional[Union[str, "IntWallCondEnum"]] = None
    last_clean: Optional[Union[dict, "TimestampValue"]] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    light_type: Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]] = empty_list()
    max_occup: Optional[str] = None
    mech_struc: Optional[Union[str, "MechStrucEnum"]] = None
    number_pets: Optional[str] = None
    number_plants: Optional[str] = None
    number_resident: Optional[str] = None
    occup_density_samp: Optional[str] = None
    occup_document: Optional[Union[str, "OccupDocumentEnum"]] = None
    occup_samp: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    pres_animal_insect: Optional[str] = None
    quad_pos: Optional[Union[str, "QuadPosEnum"]] = None
    rel_air_humidity: Optional[str] = None
    rel_humidity_out: Optional[str] = None
    rel_samp_loc: Optional[Union[str, "RelSampLocEnum"]] = None
    room_air_exch_rate: Optional[str] = None
    room_architec_elem: Optional[str] = None
    room_condt: Optional[Union[str, "RoomCondtEnum"]] = None
    room_connected: Optional[Union[str, "RoomConnectedEnum"]] = None
    room_count: Optional[str] = None
    room_dim: Optional[str] = None
    room_door_dist: Optional[str] = None
    room_door_share: Optional[str] = None
    room_hallway: Optional[str] = None
    room_loc: Optional[Union[str, "RoomLocEnum"]] = None
    room_moist_dam_hist: Optional[int] = None
    room_net_area: Optional[str] = None
    room_occup: Optional[str] = None
    room_samp_pos: Optional[Union[str, "RoomSampPosEnum"]] = None
    room_type: Optional[Union[str, "RoomTypeEnum"]] = None
    room_vol: Optional[str] = None
    room_wall_share: Optional[str] = None
    room_window_count: Optional[int] = None
    samp_floor: Optional[Union[str, "SampFloorEnum"]] = None
    samp_room_id: Optional[str] = None
    samp_sort_meth: Optional[Union[str, List[str]]] = empty_list()
    samp_time_out: Optional[str] = None
    samp_weather: Optional[Union[str, "SampWeatherEnum"]] = None
    season: Optional[str] = None
    season_use: Optional[Union[str, "SeasonUseEnum"]] = None
    shad_dev_water_mold: Optional[str] = None
    shading_device_cond: Optional[Union[str, "ShadingDeviceCondEnum"]] = None
    shading_device_loc: Optional[str] = None
    shading_device_mat: Optional[str] = None
    shading_device_type: Optional[Union[str, "ShadingDeviceTypeEnum"]] = None
    size_frac: Optional[str] = None
    space_typ_state: Optional[str] = None
    specific: Optional[Union[str, "SpecificEnum"]] = None
    specific_ecosystem: Optional[str] = None
    specific_humidity: Optional[str] = None
    substructure_type: Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]] = empty_list()
    surf_air_cont: Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]] = empty_list()
    surf_humidity: Optional[str] = None
    surf_material: Optional[Union[str, "SurfMaterialEnum"]] = None
    surf_moisture: Optional[str] = None
    surf_moisture_ph: Optional[float] = None
    surf_temp: Optional[str] = None
    temp_out: Optional[str] = None
    train_line: Optional[Union[str, "TrainLineEnum"]] = None
    train_stat_loc: Optional[Union[str, "TrainStatLocEnum"]] = None
    train_stop_loc: Optional[Union[str, "TrainStopLocEnum"]] = None
    typ_occup_density: Optional[float] = None
    ventilation_type: Optional[str] = None
    vis_media: Optional[Union[str, "VisMediaEnum"]] = None
    wall_area: Optional[str] = None
    wall_const_type: Optional[Union[str, "WallConstTypeEnum"]] = None
    wall_finish_mat: Optional[Union[str, "WallFinishMatEnum"]] = None
    wall_height: Optional[str] = None
    wall_loc: Optional[Union[str, "WallLocEnum"]] = None
    wall_surf_treatment: Optional[Union[str, "WallSurfTreatmentEnum"]] = None
    wall_texture: Optional[Union[str, "WallTextureEnum"]] = None
    wall_thermal_mass: Optional[str] = None
    wall_water_mold: Optional[str] = None
    water_feat_size: Optional[str] = None
    water_feat_type: Optional[Union[str, "WaterFeatTypeEnum"]] = None
    weekday: Optional[Union[str, "WeekdayEnum"]] = None
    window_cond: Optional[Union[str, "WindowCondEnum"]] = None
    window_cover: Optional[Union[str, "WindowCoverEnum"]] = None
    window_horiz_pos: Optional[Union[str, "WindowHorizPosEnum"]] = None
    window_loc: Optional[Union[str, "WindowLocEnum"]] = None
    window_mat: Optional[Union[str, "WindowMatEnum"]] = None
    window_open_freq: Optional[str] = None
    window_size: Optional[str] = None
    window_status: Optional[str] = None
    window_type: Optional[Union[str, "WindowTypeEnum"]] = None
    window_vert_pos: Optional[Union[str, "WindowVertPosEnum"]] = None
    window_water_mold: Optional[str] = None
    horizon_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.abs_air_humidity is not None and not isinstance(self.abs_air_humidity, str):
            self.abs_air_humidity = str(self.abs_air_humidity)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.adj_room is not None and not isinstance(self.adj_room, str):
            self.adj_room = str(self.adj_room)

        if self.aero_struc is not None and not isinstance(self.aero_struc, str):
            self.aero_struc = str(self.aero_struc)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.amount_light is not None and not isinstance(self.amount_light, str):
            self.amount_light = str(self.amount_light)

        if self.arch_struc is not None and not isinstance(self.arch_struc, ArchStrucEnum):
            self.arch_struc = ArchStrucEnum(self.arch_struc)

        if self.avg_dew_point is not None and not isinstance(self.avg_dew_point, str):
            self.avg_dew_point = str(self.avg_dew_point)

        if self.avg_occup is not None and not isinstance(self.avg_occup, str):
            self.avg_occup = str(self.avg_occup)

        if self.avg_temp is not None and not isinstance(self.avg_temp, str):
            self.avg_temp = str(self.avg_temp)

        if self.bathroom_count is not None and not isinstance(self.bathroom_count, str):
            self.bathroom_count = str(self.bathroom_count)

        if self.bedroom_count is not None and not isinstance(self.bedroom_count, str):
            self.bedroom_count = str(self.bedroom_count)

        if self.build_docs is not None and not isinstance(self.build_docs, BuildDocsEnum):
            self.build_docs = BuildDocsEnum(self.build_docs)

        if not isinstance(self.build_occup_type, list):
            self.build_occup_type = [self.build_occup_type] if self.build_occup_type is not None else []
        self.build_occup_type = [v if isinstance(v, BuildOccupTypeEnum) else BuildOccupTypeEnum(v) for v in self.build_occup_type]

        if self.building_setting is not None and not isinstance(self.building_setting, BuildingSettingEnum):
            self.building_setting = BuildingSettingEnum(self.building_setting)

        if self.built_struc_age is not None and not isinstance(self.built_struc_age, str):
            self.built_struc_age = str(self.built_struc_age)

        if self.built_struc_set is not None and not isinstance(self.built_struc_set, str):
            self.built_struc_set = str(self.built_struc_set)

        if self.built_struc_type is not None and not isinstance(self.built_struc_type, str):
            self.built_struc_type = str(self.built_struc_type)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.ceil_area is not None and not isinstance(self.ceil_area, str):
            self.ceil_area = str(self.ceil_area)

        if self.ceil_cond is not None and not isinstance(self.ceil_cond, CeilCondEnum):
            self.ceil_cond = CeilCondEnum(self.ceil_cond)

        if self.ceil_finish_mat is not None and not isinstance(self.ceil_finish_mat, CeilFinishMatEnum):
            self.ceil_finish_mat = CeilFinishMatEnum(self.ceil_finish_mat)

        if self.ceil_struc is not None and not isinstance(self.ceil_struc, str):
            self.ceil_struc = str(self.ceil_struc)

        if self.ceil_texture is not None and not isinstance(self.ceil_texture, CeilTextureEnum):
            self.ceil_texture = CeilTextureEnum(self.ceil_texture)

        if self.ceil_thermal_mass is not None and not isinstance(self.ceil_thermal_mass, str):
            self.ceil_thermal_mass = str(self.ceil_thermal_mass)

        if self.ceil_type is not None and not isinstance(self.ceil_type, CeilTypeEnum):
            self.ceil_type = CeilTypeEnum(self.ceil_type)

        if self.ceil_water_mold is not None and not isinstance(self.ceil_water_mold, str):
            self.ceil_water_mold = str(self.ceil_water_mold)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.cool_syst_id is not None and not isinstance(self.cool_syst_id, str):
            self.cool_syst_id = str(self.cool_syst_id)

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, TimestampValue):
            self.date_last_rain = TimestampValue(**as_dict(self.date_last_rain))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.dew_point is not None and not isinstance(self.dew_point, str):
            self.dew_point = str(self.dew_point)

        if self.door_comp_type is not None and not isinstance(self.door_comp_type, DoorCompTypeEnum):
            self.door_comp_type = DoorCompTypeEnum(self.door_comp_type)

        if self.door_cond is not None and not isinstance(self.door_cond, DoorCondEnum):
            self.door_cond = DoorCondEnum(self.door_cond)

        if self.door_direct is not None and not isinstance(self.door_direct, DoorDirectEnum):
            self.door_direct = DoorDirectEnum(self.door_direct)

        if self.door_loc is not None and not isinstance(self.door_loc, DoorLocEnum):
            self.door_loc = DoorLocEnum(self.door_loc)

        if self.door_mat is not None and not isinstance(self.door_mat, DoorMatEnum):
            self.door_mat = DoorMatEnum(self.door_mat)

        if self.door_move is not None and not isinstance(self.door_move, DoorMoveEnum):
            self.door_move = DoorMoveEnum(self.door_move)

        if self.door_size is not None and not isinstance(self.door_size, str):
            self.door_size = str(self.door_size)

        if self.door_type is not None and not isinstance(self.door_type, DoorTypeEnum):
            self.door_type = DoorTypeEnum(self.door_type)

        if self.door_type_metal is not None and not isinstance(self.door_type_metal, DoorTypeMetalEnum):
            self.door_type_metal = DoorTypeMetalEnum(self.door_type_metal)

        if self.door_type_wood is not None and not isinstance(self.door_type_wood, DoorTypeWoodEnum):
            self.door_type_wood = DoorTypeWoodEnum(self.door_type_wood)

        if self.door_water_mold is not None and not isinstance(self.door_water_mold, str):
            self.door_water_mold = str(self.door_water_mold)

        if self.drawings is not None and not isinstance(self.drawings, DrawingsEnum):
            self.drawings = DrawingsEnum(self.drawings)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.elevator is not None and not isinstance(self.elevator, str):
            self.elevator = str(self.elevator)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.escalator is not None and not isinstance(self.escalator, str):
            self.escalator = str(self.escalator)

        if self.exp_duct is not None and not isinstance(self.exp_duct, str):
            self.exp_duct = str(self.exp_duct)

        if self.exp_pipe is not None and not isinstance(self.exp_pipe, str):
            self.exp_pipe = str(self.exp_pipe)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.ext_door is not None and not isinstance(self.ext_door, str):
            self.ext_door = str(self.ext_door)

        if self.ext_wall_orient is not None and not isinstance(self.ext_wall_orient, ExtWallOrientEnum):
            self.ext_wall_orient = ExtWallOrientEnum(self.ext_wall_orient)

        if self.ext_window_orient is not None and not isinstance(self.ext_window_orient, ExtWindowOrientEnum):
            self.ext_window_orient = ExtWindowOrientEnum(self.ext_window_orient)

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, FilterTypeEnum) else FilterTypeEnum(v) for v in self.filter_type]

        if self.fireplace_type is not None and not isinstance(self.fireplace_type, str):
            self.fireplace_type = str(self.fireplace_type)

        if self.floor_age is not None and not isinstance(self.floor_age, str):
            self.floor_age = str(self.floor_age)

        if self.floor_area is not None and not isinstance(self.floor_area, str):
            self.floor_area = str(self.floor_area)

        if self.floor_cond is not None and not isinstance(self.floor_cond, FloorCondEnum):
            self.floor_cond = FloorCondEnum(self.floor_cond)

        if self.floor_count is not None and not isinstance(self.floor_count, str):
            self.floor_count = str(self.floor_count)

        if self.floor_finish_mat is not None and not isinstance(self.floor_finish_mat, FloorFinishMatEnum):
            self.floor_finish_mat = FloorFinishMatEnum(self.floor_finish_mat)

        if self.floor_struc is not None and not isinstance(self.floor_struc, FloorStrucEnum):
            self.floor_struc = FloorStrucEnum(self.floor_struc)

        if self.floor_thermal_mass is not None and not isinstance(self.floor_thermal_mass, str):
            self.floor_thermal_mass = str(self.floor_thermal_mass)

        if self.floor_water_mold is not None and not isinstance(self.floor_water_mold, FloorWaterMoldEnum):
            self.floor_water_mold = FloorWaterMoldEnum(self.floor_water_mold)

        if self.freq_clean is not None and not isinstance(self.freq_clean, str):
            self.freq_clean = str(self.freq_clean)

        if self.freq_cook is not None and not isinstance(self.freq_cook, str):
            self.freq_cook = str(self.freq_cook)

        if self.furniture is not None and not isinstance(self.furniture, FurnitureEnum):
            self.furniture = FurnitureEnum(self.furniture)

        if self.gender_restroom is not None and not isinstance(self.gender_restroom, GenderRestroomEnum):
            self.gender_restroom = GenderRestroomEnum(self.gender_restroom)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hall_count is not None and not isinstance(self.hall_count, str):
            self.hall_count = str(self.hall_count)

        if self.handidness is not None and not isinstance(self.handidness, HandidnessEnum):
            self.handidness = HandidnessEnum(self.handidness)

        if not isinstance(self.heat_cool_type, list):
            self.heat_cool_type = [self.heat_cool_type] if self.heat_cool_type is not None else []
        self.heat_cool_type = [v if isinstance(v, HeatCoolTypeEnum) else HeatCoolTypeEnum(v) for v in self.heat_cool_type]

        if self.heat_deliv_loc is not None and not isinstance(self.heat_deliv_loc, HeatDelivLocEnum):
            self.heat_deliv_loc = HeatDelivLocEnum(self.heat_deliv_loc)

        if self.heat_sys_deliv_meth is not None and not isinstance(self.heat_sys_deliv_meth, str):
            self.heat_sys_deliv_meth = str(self.heat_sys_deliv_meth)

        if self.heat_system_id is not None and not isinstance(self.heat_system_id, str):
            self.heat_system_id = str(self.heat_system_id)

        if self.height_carper_fiber is not None and not isinstance(self.height_carper_fiber, str):
            self.height_carper_fiber = str(self.height_carper_fiber)

        if self.indoor_space is not None and not isinstance(self.indoor_space, IndoorSpaceEnum):
            self.indoor_space = IndoorSpaceEnum(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, IndoorSurfEnum):
            self.indoor_surf = IndoorSurfEnum(self.indoor_surf)

        if self.inside_lux is not None and not isinstance(self.inside_lux, str):
            self.inside_lux = str(self.inside_lux)

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, IntWallCondEnum):
            self.int_wall_cond = IntWallCondEnum(self.int_wall_cond)

        if self.last_clean is not None and not isinstance(self.last_clean, TimestampValue):
            self.last_clean = TimestampValue(**as_dict(self.last_clean))

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if not isinstance(self.light_type, list):
            self.light_type = [self.light_type] if self.light_type is not None else []
        self.light_type = [v if isinstance(v, LightTypeEnum) else LightTypeEnum(v) for v in self.light_type]

        if self.max_occup is not None and not isinstance(self.max_occup, str):
            self.max_occup = str(self.max_occup)

        if self.mech_struc is not None and not isinstance(self.mech_struc, MechStrucEnum):
            self.mech_struc = MechStrucEnum(self.mech_struc)

        if self.number_pets is not None and not isinstance(self.number_pets, str):
            self.number_pets = str(self.number_pets)

        if self.number_plants is not None and not isinstance(self.number_plants, str):
            self.number_plants = str(self.number_plants)

        if self.number_resident is not None and not isinstance(self.number_resident, str):
            self.number_resident = str(self.number_resident)

        if self.occup_density_samp is not None and not isinstance(self.occup_density_samp, str):
            self.occup_density_samp = str(self.occup_density_samp)

        if self.occup_document is not None and not isinstance(self.occup_document, OccupDocumentEnum):
            self.occup_document = OccupDocumentEnum(self.occup_document)

        if self.occup_samp is not None and not isinstance(self.occup_samp, str):
            self.occup_samp = str(self.occup_samp)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.pres_animal_insect is not None and not isinstance(self.pres_animal_insect, str):
            self.pres_animal_insect = str(self.pres_animal_insect)

        if self.quad_pos is not None and not isinstance(self.quad_pos, QuadPosEnum):
            self.quad_pos = QuadPosEnum(self.quad_pos)

        if self.rel_air_humidity is not None and not isinstance(self.rel_air_humidity, str):
            self.rel_air_humidity = str(self.rel_air_humidity)

        if self.rel_humidity_out is not None and not isinstance(self.rel_humidity_out, str):
            self.rel_humidity_out = str(self.rel_humidity_out)

        if self.rel_samp_loc is not None and not isinstance(self.rel_samp_loc, RelSampLocEnum):
            self.rel_samp_loc = RelSampLocEnum(self.rel_samp_loc)

        if self.room_air_exch_rate is not None and not isinstance(self.room_air_exch_rate, str):
            self.room_air_exch_rate = str(self.room_air_exch_rate)

        if self.room_architec_elem is not None and not isinstance(self.room_architec_elem, str):
            self.room_architec_elem = str(self.room_architec_elem)

        if self.room_condt is not None and not isinstance(self.room_condt, RoomCondtEnum):
            self.room_condt = RoomCondtEnum(self.room_condt)

        if self.room_connected is not None and not isinstance(self.room_connected, RoomConnectedEnum):
            self.room_connected = RoomConnectedEnum(self.room_connected)

        if self.room_count is not None and not isinstance(self.room_count, str):
            self.room_count = str(self.room_count)

        if self.room_dim is not None and not isinstance(self.room_dim, str):
            self.room_dim = str(self.room_dim)

        if self.room_door_dist is not None and not isinstance(self.room_door_dist, str):
            self.room_door_dist = str(self.room_door_dist)

        if self.room_door_share is not None and not isinstance(self.room_door_share, str):
            self.room_door_share = str(self.room_door_share)

        if self.room_hallway is not None and not isinstance(self.room_hallway, str):
            self.room_hallway = str(self.room_hallway)

        if self.room_loc is not None and not isinstance(self.room_loc, RoomLocEnum):
            self.room_loc = RoomLocEnum(self.room_loc)

        if self.room_moist_dam_hist is not None and not isinstance(self.room_moist_dam_hist, int):
            self.room_moist_dam_hist = int(self.room_moist_dam_hist)

        if self.room_net_area is not None and not isinstance(self.room_net_area, str):
            self.room_net_area = str(self.room_net_area)

        if self.room_occup is not None and not isinstance(self.room_occup, str):
            self.room_occup = str(self.room_occup)

        if self.room_samp_pos is not None and not isinstance(self.room_samp_pos, RoomSampPosEnum):
            self.room_samp_pos = RoomSampPosEnum(self.room_samp_pos)

        if self.room_type is not None and not isinstance(self.room_type, RoomTypeEnum):
            self.room_type = RoomTypeEnum(self.room_type)

        if self.room_vol is not None and not isinstance(self.room_vol, str):
            self.room_vol = str(self.room_vol)

        if self.room_wall_share is not None and not isinstance(self.room_wall_share, str):
            self.room_wall_share = str(self.room_wall_share)

        if self.room_window_count is not None and not isinstance(self.room_window_count, int):
            self.room_window_count = int(self.room_window_count)

        if self.samp_floor is not None and not isinstance(self.samp_floor, SampFloorEnum):
            self.samp_floor = SampFloorEnum(self.samp_floor)

        if self.samp_room_id is not None and not isinstance(self.samp_room_id, str):
            self.samp_room_id = str(self.samp_room_id)

        if not isinstance(self.samp_sort_meth, list):
            self.samp_sort_meth = [self.samp_sort_meth] if self.samp_sort_meth is not None else []
        self.samp_sort_meth = [v if isinstance(v, str) else str(v) for v in self.samp_sort_meth]

        if self.samp_time_out is not None and not isinstance(self.samp_time_out, str):
            self.samp_time_out = str(self.samp_time_out)

        if self.samp_weather is not None and not isinstance(self.samp_weather, SampWeatherEnum):
            self.samp_weather = SampWeatherEnum(self.samp_weather)

        if self.season is not None and not isinstance(self.season, str):
            self.season = str(self.season)

        if self.season_use is not None and not isinstance(self.season_use, SeasonUseEnum):
            self.season_use = SeasonUseEnum(self.season_use)

        if self.shad_dev_water_mold is not None and not isinstance(self.shad_dev_water_mold, str):
            self.shad_dev_water_mold = str(self.shad_dev_water_mold)

        if self.shading_device_cond is not None and not isinstance(self.shading_device_cond, ShadingDeviceCondEnum):
            self.shading_device_cond = ShadingDeviceCondEnum(self.shading_device_cond)

        if self.shading_device_loc is not None and not isinstance(self.shading_device_loc, str):
            self.shading_device_loc = str(self.shading_device_loc)

        if self.shading_device_mat is not None and not isinstance(self.shading_device_mat, str):
            self.shading_device_mat = str(self.shading_device_mat)

        if self.shading_device_type is not None and not isinstance(self.shading_device_type, ShadingDeviceTypeEnum):
            self.shading_device_type = ShadingDeviceTypeEnum(self.shading_device_type)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.space_typ_state is not None and not isinstance(self.space_typ_state, str):
            self.space_typ_state = str(self.space_typ_state)

        if self.specific is not None and not isinstance(self.specific, SpecificEnum):
            self.specific = SpecificEnum(self.specific)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.specific_humidity is not None and not isinstance(self.specific_humidity, str):
            self.specific_humidity = str(self.specific_humidity)

        if not isinstance(self.substructure_type, list):
            self.substructure_type = [self.substructure_type] if self.substructure_type is not None else []
        self.substructure_type = [v if isinstance(v, SubstructureTypeEnum) else SubstructureTypeEnum(v) for v in self.substructure_type]

        if not isinstance(self.surf_air_cont, list):
            self.surf_air_cont = [self.surf_air_cont] if self.surf_air_cont is not None else []
        self.surf_air_cont = [v if isinstance(v, SurfAirContEnum) else SurfAirContEnum(v) for v in self.surf_air_cont]

        if self.surf_humidity is not None and not isinstance(self.surf_humidity, str):
            self.surf_humidity = str(self.surf_humidity)

        if self.surf_material is not None and not isinstance(self.surf_material, SurfMaterialEnum):
            self.surf_material = SurfMaterialEnum(self.surf_material)

        if self.surf_moisture is not None and not isinstance(self.surf_moisture, str):
            self.surf_moisture = str(self.surf_moisture)

        if self.surf_moisture_ph is not None and not isinstance(self.surf_moisture_ph, float):
            self.surf_moisture_ph = float(self.surf_moisture_ph)

        if self.surf_temp is not None and not isinstance(self.surf_temp, str):
            self.surf_temp = str(self.surf_temp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.temp_out is not None and not isinstance(self.temp_out, str):
            self.temp_out = str(self.temp_out)

        if self.train_line is not None and not isinstance(self.train_line, TrainLineEnum):
            self.train_line = TrainLineEnum(self.train_line)

        if self.train_stat_loc is not None and not isinstance(self.train_stat_loc, TrainStatLocEnum):
            self.train_stat_loc = TrainStatLocEnum(self.train_stat_loc)

        if self.train_stop_loc is not None and not isinstance(self.train_stop_loc, TrainStopLocEnum):
            self.train_stop_loc = TrainStopLocEnum(self.train_stop_loc)

        if self.typ_occup_density is not None and not isinstance(self.typ_occup_density, float):
            self.typ_occup_density = float(self.typ_occup_density)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if self.vis_media is not None and not isinstance(self.vis_media, VisMediaEnum):
            self.vis_media = VisMediaEnum(self.vis_media)

        if self.wall_area is not None and not isinstance(self.wall_area, str):
            self.wall_area = str(self.wall_area)

        if self.wall_const_type is not None and not isinstance(self.wall_const_type, WallConstTypeEnum):
            self.wall_const_type = WallConstTypeEnum(self.wall_const_type)

        if self.wall_finish_mat is not None and not isinstance(self.wall_finish_mat, WallFinishMatEnum):
            self.wall_finish_mat = WallFinishMatEnum(self.wall_finish_mat)

        if self.wall_height is not None and not isinstance(self.wall_height, str):
            self.wall_height = str(self.wall_height)

        if self.wall_loc is not None and not isinstance(self.wall_loc, WallLocEnum):
            self.wall_loc = WallLocEnum(self.wall_loc)

        if self.wall_surf_treatment is not None and not isinstance(self.wall_surf_treatment, WallSurfTreatmentEnum):
            self.wall_surf_treatment = WallSurfTreatmentEnum(self.wall_surf_treatment)

        if self.wall_texture is not None and not isinstance(self.wall_texture, WallTextureEnum):
            self.wall_texture = WallTextureEnum(self.wall_texture)

        if self.wall_thermal_mass is not None and not isinstance(self.wall_thermal_mass, str):
            self.wall_thermal_mass = str(self.wall_thermal_mass)

        if self.wall_water_mold is not None and not isinstance(self.wall_water_mold, str):
            self.wall_water_mold = str(self.wall_water_mold)

        if self.water_feat_size is not None and not isinstance(self.water_feat_size, str):
            self.water_feat_size = str(self.water_feat_size)

        if self.water_feat_type is not None and not isinstance(self.water_feat_type, WaterFeatTypeEnum):
            self.water_feat_type = WaterFeatTypeEnum(self.water_feat_type)

        if self.weekday is not None and not isinstance(self.weekday, WeekdayEnum):
            self.weekday = WeekdayEnum(self.weekday)

        if self.window_cond is not None and not isinstance(self.window_cond, WindowCondEnum):
            self.window_cond = WindowCondEnum(self.window_cond)

        if self.window_cover is not None and not isinstance(self.window_cover, WindowCoverEnum):
            self.window_cover = WindowCoverEnum(self.window_cover)

        if self.window_horiz_pos is not None and not isinstance(self.window_horiz_pos, WindowHorizPosEnum):
            self.window_horiz_pos = WindowHorizPosEnum(self.window_horiz_pos)

        if self.window_loc is not None and not isinstance(self.window_loc, WindowLocEnum):
            self.window_loc = WindowLocEnum(self.window_loc)

        if self.window_mat is not None and not isinstance(self.window_mat, WindowMatEnum):
            self.window_mat = WindowMatEnum(self.window_mat)

        if self.window_open_freq is not None and not isinstance(self.window_open_freq, str):
            self.window_open_freq = str(self.window_open_freq)

        if self.window_size is not None and not isinstance(self.window_size, str):
            self.window_size = str(self.window_size)

        if self.window_status is not None and not isinstance(self.window_status, str):
            self.window_status = str(self.window_status)

        if self.window_type is not None and not isinstance(self.window_type, WindowTypeEnum):
            self.window_type = WindowTypeEnum(self.window_type)

        if self.window_vert_pos is not None and not isinstance(self.window_vert_pos, WindowVertPosEnum):
            self.window_vert_pos = WindowVertPosEnum(self.window_vert_pos)

        if self.window_water_mold is not None and not isinstance(self.window_water_mold, str):
            self.window_water_mold = str(self.window_water_mold)

        if self.abs_air_humidity is not None and not isinstance(self.abs_air_humidity, str):
            self.abs_air_humidity = str(self.abs_air_humidity)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.adj_room is not None and not isinstance(self.adj_room, str):
            self.adj_room = str(self.adj_room)

        if self.aero_struc is not None and not isinstance(self.aero_struc, str):
            self.aero_struc = str(self.aero_struc)

        if self.air_temp is not None and not isinstance(self.air_temp, str):
            self.air_temp = str(self.air_temp)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.amount_light is not None and not isinstance(self.amount_light, str):
            self.amount_light = str(self.amount_light)

        if self.arch_struc is not None and not isinstance(self.arch_struc, ArchStrucEnum):
            self.arch_struc = ArchStrucEnum(self.arch_struc)

        if self.avg_dew_point is not None and not isinstance(self.avg_dew_point, str):
            self.avg_dew_point = str(self.avg_dew_point)

        if self.avg_occup is not None and not isinstance(self.avg_occup, str):
            self.avg_occup = str(self.avg_occup)

        if self.avg_temp is not None and not isinstance(self.avg_temp, str):
            self.avg_temp = str(self.avg_temp)

        if self.bathroom_count is not None and not isinstance(self.bathroom_count, str):
            self.bathroom_count = str(self.bathroom_count)

        if self.bedroom_count is not None and not isinstance(self.bedroom_count, str):
            self.bedroom_count = str(self.bedroom_count)

        if self.build_docs is not None and not isinstance(self.build_docs, BuildDocsEnum):
            self.build_docs = BuildDocsEnum(self.build_docs)

        if not isinstance(self.build_occup_type, list):
            self.build_occup_type = [self.build_occup_type] if self.build_occup_type is not None else []
        self.build_occup_type = [v if isinstance(v, BuildOccupTypeEnum) else BuildOccupTypeEnum(v) for v in self.build_occup_type]

        if self.building_setting is not None and not isinstance(self.building_setting, BuildingSettingEnum):
            self.building_setting = BuildingSettingEnum(self.building_setting)

        if self.built_struc_age is not None and not isinstance(self.built_struc_age, str):
            self.built_struc_age = str(self.built_struc_age)

        if self.built_struc_set is not None and not isinstance(self.built_struc_set, str):
            self.built_struc_set = str(self.built_struc_set)

        if self.built_struc_type is not None and not isinstance(self.built_struc_type, str):
            self.built_struc_type = str(self.built_struc_type)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.ceil_area is not None and not isinstance(self.ceil_area, str):
            self.ceil_area = str(self.ceil_area)

        if self.ceil_cond is not None and not isinstance(self.ceil_cond, CeilCondEnum):
            self.ceil_cond = CeilCondEnum(self.ceil_cond)

        if self.ceil_finish_mat is not None and not isinstance(self.ceil_finish_mat, CeilFinishMatEnum):
            self.ceil_finish_mat = CeilFinishMatEnum(self.ceil_finish_mat)

        if self.ceil_struc is not None and not isinstance(self.ceil_struc, str):
            self.ceil_struc = str(self.ceil_struc)

        if self.ceil_texture is not None and not isinstance(self.ceil_texture, CeilTextureEnum):
            self.ceil_texture = CeilTextureEnum(self.ceil_texture)

        if self.ceil_thermal_mass is not None and not isinstance(self.ceil_thermal_mass, str):
            self.ceil_thermal_mass = str(self.ceil_thermal_mass)

        if self.ceil_type is not None and not isinstance(self.ceil_type, CeilTypeEnum):
            self.ceil_type = CeilTypeEnum(self.ceil_type)

        if self.ceil_water_mold is not None and not isinstance(self.ceil_water_mold, str):
            self.ceil_water_mold = str(self.ceil_water_mold)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.cool_syst_id is not None and not isinstance(self.cool_syst_id, str):
            self.cool_syst_id = str(self.cool_syst_id)

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, TimestampValue):
            self.date_last_rain = TimestampValue(**as_dict(self.date_last_rain))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.dew_point is not None and not isinstance(self.dew_point, str):
            self.dew_point = str(self.dew_point)

        if self.door_comp_type is not None and not isinstance(self.door_comp_type, DoorCompTypeEnum):
            self.door_comp_type = DoorCompTypeEnum(self.door_comp_type)

        if self.door_cond is not None and not isinstance(self.door_cond, DoorCondEnum):
            self.door_cond = DoorCondEnum(self.door_cond)

        if self.door_direct is not None and not isinstance(self.door_direct, DoorDirectEnum):
            self.door_direct = DoorDirectEnum(self.door_direct)

        if self.door_loc is not None and not isinstance(self.door_loc, DoorLocEnum):
            self.door_loc = DoorLocEnum(self.door_loc)

        if self.door_mat is not None and not isinstance(self.door_mat, DoorMatEnum):
            self.door_mat = DoorMatEnum(self.door_mat)

        if self.door_move is not None and not isinstance(self.door_move, DoorMoveEnum):
            self.door_move = DoorMoveEnum(self.door_move)

        if self.door_size is not None and not isinstance(self.door_size, str):
            self.door_size = str(self.door_size)

        if self.door_type is not None and not isinstance(self.door_type, DoorTypeEnum):
            self.door_type = DoorTypeEnum(self.door_type)

        if self.door_type_metal is not None and not isinstance(self.door_type_metal, DoorTypeMetalEnum):
            self.door_type_metal = DoorTypeMetalEnum(self.door_type_metal)

        if self.door_type_wood is not None and not isinstance(self.door_type_wood, DoorTypeWoodEnum):
            self.door_type_wood = DoorTypeWoodEnum(self.door_type_wood)

        if self.door_water_mold is not None and not isinstance(self.door_water_mold, str):
            self.door_water_mold = str(self.door_water_mold)

        if self.drawings is not None and not isinstance(self.drawings, DrawingsEnum):
            self.drawings = DrawingsEnum(self.drawings)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.elevator is not None and not isinstance(self.elevator, str):
            self.elevator = str(self.elevator)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.escalator is not None and not isinstance(self.escalator, str):
            self.escalator = str(self.escalator)

        if self.exp_duct is not None and not isinstance(self.exp_duct, str):
            self.exp_duct = str(self.exp_duct)

        if self.exp_pipe is not None and not isinstance(self.exp_pipe, str):
            self.exp_pipe = str(self.exp_pipe)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.ext_door is not None and not isinstance(self.ext_door, str):
            self.ext_door = str(self.ext_door)

        if self.ext_wall_orient is not None and not isinstance(self.ext_wall_orient, ExtWallOrientEnum):
            self.ext_wall_orient = ExtWallOrientEnum(self.ext_wall_orient)

        if self.ext_window_orient is not None and not isinstance(self.ext_window_orient, ExtWindowOrientEnum):
            self.ext_window_orient = ExtWindowOrientEnum(self.ext_window_orient)

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, FilterTypeEnum) else FilterTypeEnum(v) for v in self.filter_type]

        if self.fireplace_type is not None and not isinstance(self.fireplace_type, str):
            self.fireplace_type = str(self.fireplace_type)

        if self.floor_age is not None and not isinstance(self.floor_age, str):
            self.floor_age = str(self.floor_age)

        if self.floor_area is not None and not isinstance(self.floor_area, str):
            self.floor_area = str(self.floor_area)

        if self.floor_cond is not None and not isinstance(self.floor_cond, FloorCondEnum):
            self.floor_cond = FloorCondEnum(self.floor_cond)

        if self.floor_count is not None and not isinstance(self.floor_count, str):
            self.floor_count = str(self.floor_count)

        if self.floor_finish_mat is not None and not isinstance(self.floor_finish_mat, FloorFinishMatEnum):
            self.floor_finish_mat = FloorFinishMatEnum(self.floor_finish_mat)

        if self.floor_struc is not None and not isinstance(self.floor_struc, FloorStrucEnum):
            self.floor_struc = FloorStrucEnum(self.floor_struc)

        if self.floor_thermal_mass is not None and not isinstance(self.floor_thermal_mass, str):
            self.floor_thermal_mass = str(self.floor_thermal_mass)

        if self.floor_water_mold is not None and not isinstance(self.floor_water_mold, FloorWaterMoldEnum):
            self.floor_water_mold = FloorWaterMoldEnum(self.floor_water_mold)

        if self.freq_clean is not None and not isinstance(self.freq_clean, str):
            self.freq_clean = str(self.freq_clean)

        if self.freq_cook is not None and not isinstance(self.freq_cook, str):
            self.freq_cook = str(self.freq_cook)

        if self.furniture is not None and not isinstance(self.furniture, FurnitureEnum):
            self.furniture = FurnitureEnum(self.furniture)

        if self.gender_restroom is not None and not isinstance(self.gender_restroom, GenderRestroomEnum):
            self.gender_restroom = GenderRestroomEnum(self.gender_restroom)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hall_count is not None and not isinstance(self.hall_count, str):
            self.hall_count = str(self.hall_count)

        if self.handidness is not None and not isinstance(self.handidness, HandidnessEnum):
            self.handidness = HandidnessEnum(self.handidness)

        if not isinstance(self.heat_cool_type, list):
            self.heat_cool_type = [self.heat_cool_type] if self.heat_cool_type is not None else []
        self.heat_cool_type = [v if isinstance(v, HeatCoolTypeEnum) else HeatCoolTypeEnum(v) for v in self.heat_cool_type]

        if self.heat_deliv_loc is not None and not isinstance(self.heat_deliv_loc, HeatDelivLocEnum):
            self.heat_deliv_loc = HeatDelivLocEnum(self.heat_deliv_loc)

        if self.heat_sys_deliv_meth is not None and not isinstance(self.heat_sys_deliv_meth, str):
            self.heat_sys_deliv_meth = str(self.heat_sys_deliv_meth)

        if self.heat_system_id is not None and not isinstance(self.heat_system_id, str):
            self.heat_system_id = str(self.heat_system_id)

        if self.height_carper_fiber is not None and not isinstance(self.height_carper_fiber, str):
            self.height_carper_fiber = str(self.height_carper_fiber)

        if self.indoor_space is not None and not isinstance(self.indoor_space, IndoorSpaceEnum):
            self.indoor_space = IndoorSpaceEnum(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, IndoorSurfEnum):
            self.indoor_surf = IndoorSurfEnum(self.indoor_surf)

        if self.inside_lux is not None and not isinstance(self.inside_lux, str):
            self.inside_lux = str(self.inside_lux)

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, IntWallCondEnum):
            self.int_wall_cond = IntWallCondEnum(self.int_wall_cond)

        if self.last_clean is not None and not isinstance(self.last_clean, TimestampValue):
            self.last_clean = TimestampValue(**as_dict(self.last_clean))

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if not isinstance(self.light_type, list):
            self.light_type = [self.light_type] if self.light_type is not None else []
        self.light_type = [v if isinstance(v, LightTypeEnum) else LightTypeEnum(v) for v in self.light_type]

        if self.max_occup is not None and not isinstance(self.max_occup, str):
            self.max_occup = str(self.max_occup)

        if self.mech_struc is not None and not isinstance(self.mech_struc, MechStrucEnum):
            self.mech_struc = MechStrucEnum(self.mech_struc)

        if self.number_pets is not None and not isinstance(self.number_pets, str):
            self.number_pets = str(self.number_pets)

        if self.number_plants is not None and not isinstance(self.number_plants, str):
            self.number_plants = str(self.number_plants)

        if self.number_resident is not None and not isinstance(self.number_resident, str):
            self.number_resident = str(self.number_resident)

        if self.occup_density_samp is not None and not isinstance(self.occup_density_samp, str):
            self.occup_density_samp = str(self.occup_density_samp)

        if self.occup_document is not None and not isinstance(self.occup_document, OccupDocumentEnum):
            self.occup_document = OccupDocumentEnum(self.occup_document)

        if self.occup_samp is not None and not isinstance(self.occup_samp, str):
            self.occup_samp = str(self.occup_samp)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.pres_animal_insect is not None and not isinstance(self.pres_animal_insect, str):
            self.pres_animal_insect = str(self.pres_animal_insect)

        if self.quad_pos is not None and not isinstance(self.quad_pos, QuadPosEnum):
            self.quad_pos = QuadPosEnum(self.quad_pos)

        if self.rel_air_humidity is not None and not isinstance(self.rel_air_humidity, str):
            self.rel_air_humidity = str(self.rel_air_humidity)

        if self.rel_humidity_out is not None and not isinstance(self.rel_humidity_out, str):
            self.rel_humidity_out = str(self.rel_humidity_out)

        if self.rel_samp_loc is not None and not isinstance(self.rel_samp_loc, RelSampLocEnum):
            self.rel_samp_loc = RelSampLocEnum(self.rel_samp_loc)

        if self.room_air_exch_rate is not None and not isinstance(self.room_air_exch_rate, str):
            self.room_air_exch_rate = str(self.room_air_exch_rate)

        if self.room_architec_elem is not None and not isinstance(self.room_architec_elem, str):
            self.room_architec_elem = str(self.room_architec_elem)

        if self.room_condt is not None and not isinstance(self.room_condt, RoomCondtEnum):
            self.room_condt = RoomCondtEnum(self.room_condt)

        if self.room_connected is not None and not isinstance(self.room_connected, RoomConnectedEnum):
            self.room_connected = RoomConnectedEnum(self.room_connected)

        if self.room_count is not None and not isinstance(self.room_count, str):
            self.room_count = str(self.room_count)

        if self.room_dim is not None and not isinstance(self.room_dim, str):
            self.room_dim = str(self.room_dim)

        if self.room_door_dist is not None and not isinstance(self.room_door_dist, str):
            self.room_door_dist = str(self.room_door_dist)

        if self.room_door_share is not None and not isinstance(self.room_door_share, str):
            self.room_door_share = str(self.room_door_share)

        if self.room_hallway is not None and not isinstance(self.room_hallway, str):
            self.room_hallway = str(self.room_hallway)

        if self.room_loc is not None and not isinstance(self.room_loc, RoomLocEnum):
            self.room_loc = RoomLocEnum(self.room_loc)

        if self.room_moist_dam_hist is not None and not isinstance(self.room_moist_dam_hist, int):
            self.room_moist_dam_hist = int(self.room_moist_dam_hist)

        if self.room_net_area is not None and not isinstance(self.room_net_area, str):
            self.room_net_area = str(self.room_net_area)

        if self.room_occup is not None and not isinstance(self.room_occup, str):
            self.room_occup = str(self.room_occup)

        if self.room_samp_pos is not None and not isinstance(self.room_samp_pos, RoomSampPosEnum):
            self.room_samp_pos = RoomSampPosEnum(self.room_samp_pos)

        if self.room_type is not None and not isinstance(self.room_type, RoomTypeEnum):
            self.room_type = RoomTypeEnum(self.room_type)

        if self.room_vol is not None and not isinstance(self.room_vol, str):
            self.room_vol = str(self.room_vol)

        if self.room_wall_share is not None and not isinstance(self.room_wall_share, str):
            self.room_wall_share = str(self.room_wall_share)

        if self.room_window_count is not None and not isinstance(self.room_window_count, int):
            self.room_window_count = int(self.room_window_count)

        if self.samp_floor is not None and not isinstance(self.samp_floor, SampFloorEnum):
            self.samp_floor = SampFloorEnum(self.samp_floor)

        if self.samp_room_id is not None and not isinstance(self.samp_room_id, str):
            self.samp_room_id = str(self.samp_room_id)

        if not isinstance(self.samp_sort_meth, list):
            self.samp_sort_meth = [self.samp_sort_meth] if self.samp_sort_meth is not None else []
        self.samp_sort_meth = [v if isinstance(v, str) else str(v) for v in self.samp_sort_meth]

        if self.samp_time_out is not None and not isinstance(self.samp_time_out, str):
            self.samp_time_out = str(self.samp_time_out)

        if self.samp_weather is not None and not isinstance(self.samp_weather, SampWeatherEnum):
            self.samp_weather = SampWeatherEnum(self.samp_weather)

        if self.season is not None and not isinstance(self.season, str):
            self.season = str(self.season)

        if self.season_use is not None and not isinstance(self.season_use, SeasonUseEnum):
            self.season_use = SeasonUseEnum(self.season_use)

        if self.shad_dev_water_mold is not None and not isinstance(self.shad_dev_water_mold, str):
            self.shad_dev_water_mold = str(self.shad_dev_water_mold)

        if self.shading_device_cond is not None and not isinstance(self.shading_device_cond, ShadingDeviceCondEnum):
            self.shading_device_cond = ShadingDeviceCondEnum(self.shading_device_cond)

        if self.shading_device_loc is not None and not isinstance(self.shading_device_loc, str):
            self.shading_device_loc = str(self.shading_device_loc)

        if self.shading_device_mat is not None and not isinstance(self.shading_device_mat, str):
            self.shading_device_mat = str(self.shading_device_mat)

        if self.shading_device_type is not None and not isinstance(self.shading_device_type, ShadingDeviceTypeEnum):
            self.shading_device_type = ShadingDeviceTypeEnum(self.shading_device_type)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.space_typ_state is not None and not isinstance(self.space_typ_state, str):
            self.space_typ_state = str(self.space_typ_state)

        if self.specific is not None and not isinstance(self.specific, SpecificEnum):
            self.specific = SpecificEnum(self.specific)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.specific_humidity is not None and not isinstance(self.specific_humidity, str):
            self.specific_humidity = str(self.specific_humidity)

        if not isinstance(self.substructure_type, list):
            self.substructure_type = [self.substructure_type] if self.substructure_type is not None else []
        self.substructure_type = [v if isinstance(v, SubstructureTypeEnum) else SubstructureTypeEnum(v) for v in self.substructure_type]

        if not isinstance(self.surf_air_cont, list):
            self.surf_air_cont = [self.surf_air_cont] if self.surf_air_cont is not None else []
        self.surf_air_cont = [v if isinstance(v, SurfAirContEnum) else SurfAirContEnum(v) for v in self.surf_air_cont]

        if self.surf_humidity is not None and not isinstance(self.surf_humidity, str):
            self.surf_humidity = str(self.surf_humidity)

        if self.surf_material is not None and not isinstance(self.surf_material, SurfMaterialEnum):
            self.surf_material = SurfMaterialEnum(self.surf_material)

        if self.surf_moisture is not None and not isinstance(self.surf_moisture, str):
            self.surf_moisture = str(self.surf_moisture)

        if self.surf_moisture_ph is not None and not isinstance(self.surf_moisture_ph, float):
            self.surf_moisture_ph = float(self.surf_moisture_ph)

        if self.surf_temp is not None and not isinstance(self.surf_temp, str):
            self.surf_temp = str(self.surf_temp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.temp_out is not None and not isinstance(self.temp_out, str):
            self.temp_out = str(self.temp_out)

        if self.train_line is not None and not isinstance(self.train_line, TrainLineEnum):
            self.train_line = TrainLineEnum(self.train_line)

        if self.train_stat_loc is not None and not isinstance(self.train_stat_loc, TrainStatLocEnum):
            self.train_stat_loc = TrainStatLocEnum(self.train_stat_loc)

        if self.train_stop_loc is not None and not isinstance(self.train_stop_loc, TrainStopLocEnum):
            self.train_stop_loc = TrainStopLocEnum(self.train_stop_loc)

        if self.typ_occup_density is not None and not isinstance(self.typ_occup_density, float):
            self.typ_occup_density = float(self.typ_occup_density)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if self.vis_media is not None and not isinstance(self.vis_media, VisMediaEnum):
            self.vis_media = VisMediaEnum(self.vis_media)

        if self.wall_area is not None and not isinstance(self.wall_area, str):
            self.wall_area = str(self.wall_area)

        if self.wall_const_type is not None and not isinstance(self.wall_const_type, WallConstTypeEnum):
            self.wall_const_type = WallConstTypeEnum(self.wall_const_type)

        if self.wall_finish_mat is not None and not isinstance(self.wall_finish_mat, WallFinishMatEnum):
            self.wall_finish_mat = WallFinishMatEnum(self.wall_finish_mat)

        if self.wall_height is not None and not isinstance(self.wall_height, str):
            self.wall_height = str(self.wall_height)

        if self.wall_loc is not None and not isinstance(self.wall_loc, WallLocEnum):
            self.wall_loc = WallLocEnum(self.wall_loc)

        if self.wall_surf_treatment is not None and not isinstance(self.wall_surf_treatment, WallSurfTreatmentEnum):
            self.wall_surf_treatment = WallSurfTreatmentEnum(self.wall_surf_treatment)

        if self.wall_texture is not None and not isinstance(self.wall_texture, WallTextureEnum):
            self.wall_texture = WallTextureEnum(self.wall_texture)

        if self.wall_thermal_mass is not None and not isinstance(self.wall_thermal_mass, str):
            self.wall_thermal_mass = str(self.wall_thermal_mass)

        if self.wall_water_mold is not None and not isinstance(self.wall_water_mold, str):
            self.wall_water_mold = str(self.wall_water_mold)

        if self.water_feat_size is not None and not isinstance(self.water_feat_size, str):
            self.water_feat_size = str(self.water_feat_size)

        if self.water_feat_type is not None and not isinstance(self.water_feat_type, WaterFeatTypeEnum):
            self.water_feat_type = WaterFeatTypeEnum(self.water_feat_type)

        if self.weekday is not None and not isinstance(self.weekday, WeekdayEnum):
            self.weekday = WeekdayEnum(self.weekday)

        if self.window_cond is not None and not isinstance(self.window_cond, WindowCondEnum):
            self.window_cond = WindowCondEnum(self.window_cond)

        if self.window_cover is not None and not isinstance(self.window_cover, WindowCoverEnum):
            self.window_cover = WindowCoverEnum(self.window_cover)

        if self.window_horiz_pos is not None and not isinstance(self.window_horiz_pos, WindowHorizPosEnum):
            self.window_horiz_pos = WindowHorizPosEnum(self.window_horiz_pos)

        if self.window_loc is not None and not isinstance(self.window_loc, WindowLocEnum):
            self.window_loc = WindowLocEnum(self.window_loc)

        if self.window_mat is not None and not isinstance(self.window_mat, WindowMatEnum):
            self.window_mat = WindowMatEnum(self.window_mat)

        if self.window_open_freq is not None and not isinstance(self.window_open_freq, str):
            self.window_open_freq = str(self.window_open_freq)

        if self.window_size is not None and not isinstance(self.window_size, str):
            self.window_size = str(self.window_size)

        if self.window_status is not None and not isinstance(self.window_status, str):
            self.window_status = str(self.window_status)

        if self.window_type is not None and not isinstance(self.window_type, WindowTypeEnum):
            self.window_type = WindowTypeEnum(self.window_type)

        if self.window_vert_pos is not None and not isinstance(self.window_vert_pos, WindowVertPosEnum):
            self.window_vert_pos = WindowVertPosEnum(self.window_vert_pos)

        if self.window_water_mold is not None and not isinstance(self.window_water_mold, str):
            self.window_water_mold = str(self.window_water_mold)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class DhMutliviewCommonColumns(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMutliviewCommonColumns
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:DhMutliviewCommonColumns"
    class_name: ClassVar[str] = "dh_mutliview_common_columns"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMutliviewCommonColumns

    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_mat_id):
            self.MissingRequiredField("source_mat_id")
        if not isinstance(self.source_mat_id, DhMutliviewCommonColumnsSourceMatId):
            self.source_mat_id = DhMutliviewCommonColumnsSourceMatId(self.source_mat_id)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        super().__post_init__(**kwargs)


@dataclass
class Emsl(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Emsl
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Emsl"
    class_name: ClassVar[str] = "emsl"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Emsl

    EMSL_store_temp: Optional[str] = None
    project_ID: Optional[str] = None
    replicate_number: Optional[str] = None
    sample_shipped: Optional[str] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    technical_reps: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.EMSL_store_temp is not None and not isinstance(self.EMSL_store_temp, str):
            self.EMSL_store_temp = str(self.EMSL_store_temp)

        if self.project_ID is not None and not isinstance(self.project_ID, str):
            self.project_ID = str(self.project_ID)

        if self.replicate_number is not None and not isinstance(self.replicate_number, str):
            self.replicate_number = str(self.replicate_number)

        if self.sample_shipped is not None and not isinstance(self.sample_shipped, str):
            self.sample_shipped = str(self.sample_shipped)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.technical_reps is not None and not isinstance(self.technical_reps, str):
            self.technical_reps = str(self.technical_reps)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class HcrCores(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrCores
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HcrCores"
    class_name: ClassVar[str] = "hcr_cores"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrCores

    additional_info: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alt: Optional[str] = None
    ammonium: Optional[str] = None
    api: Optional[str] = None
    aromatics_pc: Optional[str] = None
    asphaltenes_pc: Optional[str] = None
    basin: Optional[str] = None
    benzene: Optional[str] = None
    calcium: Optional[str] = None
    chloride: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    density: Optional[str] = None
    depos_env: Optional[Union[str, "DeposEnvEnum"]] = None
    depth: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_iron: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_oxygen_fluid: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    ethylbenzene: Optional[str] = None
    experimental_factor: Optional[str] = None
    field: Optional[str] = None
    geo_loc_name: Optional[str] = None
    hc_produced: Optional[Union[str, "HcProducedEnum"]] = None
    hcr: Optional[Union[str, "HcrEnum"]] = None
    hcr_fw_salinity: Optional[str] = None
    hcr_geol_age: Optional[Union[str, "HcrGeolAgeEnum"]] = None
    hcr_pressure: Optional[str] = None
    hcr_temp: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    lithology: Optional[Union[str, "LithologyEnum"]] = None
    magnesium: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    org_count_qpcr_info: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    owc_tvdss: Optional[str] = None
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    permeability: Optional[str] = None
    ph: Optional[float] = None
    porosity: Optional[str] = None
    potassium: Optional[str] = None
    pour_point: Optional[str] = None
    pressure: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    reservoir: Optional[str] = None
    resins_pc: Optional[str] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_md: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_subtype: Optional[Union[str, "SampSubtypeEnum"]] = None
    samp_transport_cond: Optional[str] = None
    samp_tvdss: Optional[str] = None
    samp_type: Optional[str] = None
    samp_well_name: Optional[str] = None
    saturates_pc: Optional[str] = None
    size_frac: Optional[str] = None
    sodium: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sr_dep_env: Optional[Union[str, "SrDepEnvEnum"]] = None
    sr_geol_age: Optional[Union[str, "SrGeolAgeEnum"]] = None
    sr_kerog_type: Optional[Union[str, "SrKerogTypeEnum"]] = None
    sr_lithology: Optional[Union[str, "SrLithologyEnum"]] = None
    sulfate: Optional[str] = None
    sulfate_fw: Optional[str] = None
    sulfide: Optional[str] = None
    suspend_solids: Optional[Union[str, List[str]]] = empty_list()
    tan: Optional[str] = None
    temp: Optional[str] = None
    toluene: Optional[str] = None
    tot_iron: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_phosp: Optional[str] = None
    tot_sulfur: Optional[str] = None
    tvdss_of_hcr_press: Optional[str] = None
    tvdss_of_hcr_temp: Optional[str] = None
    vfa: Optional[str] = None
    vfa_fw: Optional[str] = None
    viscosity: Optional[str] = None
    win: Optional[str] = None
    xylene: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hc_produced is not None and not isinstance(self.hc_produced, HcProducedEnum):
            self.hc_produced = HcProducedEnum(self.hc_produced)

        if self.hcr is not None and not isinstance(self.hcr, HcrEnum):
            self.hcr = HcrEnum(self.hcr)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, HcrGeolAgeEnum):
            self.hcr_geol_age = HcrGeolAgeEnum(self.hcr_geol_age)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.lithology is not None and not isinstance(self.lithology, LithologyEnum):
            self.lithology = LithologyEnum(self.lithology)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.org_count_qpcr_info is not None and not isinstance(self.org_count_qpcr_info, str):
            self.org_count_qpcr_info = str(self.org_count_qpcr_info)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.owc_tvdss is not None and not isinstance(self.owc_tvdss, str):
            self.owc_tvdss = str(self.owc_tvdss)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.permeability is not None and not isinstance(self.permeability, str):
            self.permeability = str(self.permeability)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_md is not None and not isinstance(self.samp_md, str):
            self.samp_md = str(self.samp_md)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, SampSubtypeEnum):
            self.samp_subtype = SampSubtypeEnum(self.samp_subtype)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_tvdss is not None and not isinstance(self.samp_tvdss, str):
            self.samp_tvdss = str(self.samp_tvdss)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sr_dep_env is not None and not isinstance(self.sr_dep_env, SrDepEnvEnum):
            self.sr_dep_env = SrDepEnvEnum(self.sr_dep_env)

        if self.sr_geol_age is not None and not isinstance(self.sr_geol_age, SrGeolAgeEnum):
            self.sr_geol_age = SrGeolAgeEnum(self.sr_geol_age)

        if self.sr_kerog_type is not None and not isinstance(self.sr_kerog_type, SrKerogTypeEnum):
            self.sr_kerog_type = SrKerogTypeEnum(self.sr_kerog_type)

        if self.sr_lithology is not None and not isinstance(self.sr_lithology, SrLithologyEnum):
            self.sr_lithology = SrLithologyEnum(self.sr_lithology)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.tvdss_of_hcr_press is not None and not isinstance(self.tvdss_of_hcr_press, str):
            self.tvdss_of_hcr_press = str(self.tvdss_of_hcr_press)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hc_produced is not None and not isinstance(self.hc_produced, HcProducedEnum):
            self.hc_produced = HcProducedEnum(self.hc_produced)

        if self.hcr is not None and not isinstance(self.hcr, HcrEnum):
            self.hcr = HcrEnum(self.hcr)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, HcrGeolAgeEnum):
            self.hcr_geol_age = HcrGeolAgeEnum(self.hcr_geol_age)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.lithology is not None and not isinstance(self.lithology, LithologyEnum):
            self.lithology = LithologyEnum(self.lithology)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.org_count_qpcr_info is not None and not isinstance(self.org_count_qpcr_info, str):
            self.org_count_qpcr_info = str(self.org_count_qpcr_info)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.owc_tvdss is not None and not isinstance(self.owc_tvdss, str):
            self.owc_tvdss = str(self.owc_tvdss)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.permeability is not None and not isinstance(self.permeability, str):
            self.permeability = str(self.permeability)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_md is not None and not isinstance(self.samp_md, str):
            self.samp_md = str(self.samp_md)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, SampSubtypeEnum):
            self.samp_subtype = SampSubtypeEnum(self.samp_subtype)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_tvdss is not None and not isinstance(self.samp_tvdss, str):
            self.samp_tvdss = str(self.samp_tvdss)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sr_dep_env is not None and not isinstance(self.sr_dep_env, SrDepEnvEnum):
            self.sr_dep_env = SrDepEnvEnum(self.sr_dep_env)

        if self.sr_geol_age is not None and not isinstance(self.sr_geol_age, SrGeolAgeEnum):
            self.sr_geol_age = SrGeolAgeEnum(self.sr_geol_age)

        if self.sr_kerog_type is not None and not isinstance(self.sr_kerog_type, SrKerogTypeEnum):
            self.sr_kerog_type = SrKerogTypeEnum(self.sr_kerog_type)

        if self.sr_lithology is not None and not isinstance(self.sr_lithology, SrLithologyEnum):
            self.sr_lithology = SrLithologyEnum(self.sr_lithology)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.tvdss_of_hcr_press is not None and not isinstance(self.tvdss_of_hcr_press, str):
            self.tvdss_of_hcr_press = str(self.tvdss_of_hcr_press)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class HcrFluidsSwabs(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrFluidsSwabs
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HcrFluidsSwabs"
    class_name: ClassVar[str] = "hcr_fluids_swabs"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrFluidsSwabs

    add_recov_method: Optional[str] = None
    additional_info: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alt: Optional[str] = None
    ammonium: Optional[str] = None
    api: Optional[str] = None
    aromatics_pc: Optional[str] = None
    asphaltenes_pc: Optional[str] = None
    basin: Optional[str] = None
    benzene: Optional[str] = None
    biocide: Optional[str] = None
    biocide_admin_method: Optional[str] = None
    calcium: Optional[str] = None
    chem_treat_method: Optional[str] = None
    chem_treatment: Optional[str] = None
    chloride: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    density: Optional[str] = None
    depos_env: Optional[Union[str, "DeposEnvEnum"]] = None
    depth: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_iron: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_oxygen_fluid: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    ethylbenzene: Optional[str] = None
    experimental_factor: Optional[str] = None
    field: Optional[str] = None
    geo_loc_name: Optional[str] = None
    hc_produced: Optional[Union[str, "HcProducedEnum"]] = None
    hcr: Optional[Union[str, "HcrEnum"]] = None
    hcr_fw_salinity: Optional[str] = None
    hcr_geol_age: Optional[Union[str, "HcrGeolAgeEnum"]] = None
    hcr_pressure: Optional[str] = None
    hcr_temp: Optional[str] = None
    iw_bt_date_well: Optional[Union[dict, "TimestampValue"]] = None
    iwf: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    lithology: Optional[Union[str, "LithologyEnum"]] = None
    magnesium: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    org_count_qpcr_info: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    ph: Optional[float] = None
    potassium: Optional[str] = None
    pour_point: Optional[str] = None
    pressure: Optional[str] = None
    prod_rate: Optional[str] = None
    prod_start_date: Optional[Union[dict, "TimestampValue"]] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    reservoir: Optional[str] = None
    resins_pc: Optional[str] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_collect_point: Optional[Union[str, "SampCollectPointEnum"]] = None
    samp_loc_corr_rate: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_preserv: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_subtype: Optional[Union[str, "SampSubtypeEnum"]] = None
    samp_transport_cond: Optional[str] = None
    samp_type: Optional[str] = None
    samp_well_name: Optional[str] = None
    saturates_pc: Optional[str] = None
    size_frac: Optional[str] = None
    sodium: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sulfate: Optional[str] = None
    sulfate_fw: Optional[str] = None
    sulfide: Optional[str] = None
    suspend_solids: Optional[Union[str, List[str]]] = empty_list()
    tan: Optional[str] = None
    temp: Optional[str] = None
    toluene: Optional[str] = None
    tot_iron: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_phosp: Optional[str] = None
    tot_sulfur: Optional[str] = None
    tvdss_of_hcr_press: Optional[str] = None
    tvdss_of_hcr_temp: Optional[str] = None
    vfa: Optional[str] = None
    vfa_fw: Optional[str] = None
    viscosity: Optional[str] = None
    water_cut: Optional[str] = None
    water_prod_rate: Optional[str] = None
    win: Optional[str] = None
    xylene: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.add_recov_method is not None and not isinstance(self.add_recov_method, str):
            self.add_recov_method = str(self.add_recov_method)

        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.biocide is not None and not isinstance(self.biocide, str):
            self.biocide = str(self.biocide)

        if self.biocide_admin_method is not None and not isinstance(self.biocide_admin_method, str):
            self.biocide_admin_method = str(self.biocide_admin_method)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.chem_treat_method is not None and not isinstance(self.chem_treat_method, str):
            self.chem_treat_method = str(self.chem_treat_method)

        if self.chem_treatment is not None and not isinstance(self.chem_treatment, str):
            self.chem_treatment = str(self.chem_treatment)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hc_produced is not None and not isinstance(self.hc_produced, HcProducedEnum):
            self.hc_produced = HcProducedEnum(self.hc_produced)

        if self.hcr is not None and not isinstance(self.hcr, HcrEnum):
            self.hcr = HcrEnum(self.hcr)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, HcrGeolAgeEnum):
            self.hcr_geol_age = HcrGeolAgeEnum(self.hcr_geol_age)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, TimestampValue):
            self.iw_bt_date_well = TimestampValue(**as_dict(self.iw_bt_date_well))

        if self.iwf is not None and not isinstance(self.iwf, str):
            self.iwf = str(self.iwf)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.lithology is not None and not isinstance(self.lithology, LithologyEnum):
            self.lithology = LithologyEnum(self.lithology)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.org_count_qpcr_info is not None and not isinstance(self.org_count_qpcr_info, str):
            self.org_count_qpcr_info = str(self.org_count_qpcr_info)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.prod_rate is not None and not isinstance(self.prod_rate, str):
            self.prod_rate = str(self.prod_rate)

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, TimestampValue):
            self.prod_start_date = TimestampValue(**as_dict(self.prod_start_date))

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_collect_point is not None and not isinstance(self.samp_collect_point, SampCollectPointEnum):
            self.samp_collect_point = SampCollectPointEnum(self.samp_collect_point)

        if self.samp_loc_corr_rate is not None and not isinstance(self.samp_loc_corr_rate, str):
            self.samp_loc_corr_rate = str(self.samp_loc_corr_rate)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_preserv is not None and not isinstance(self.samp_preserv, str):
            self.samp_preserv = str(self.samp_preserv)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, SampSubtypeEnum):
            self.samp_subtype = SampSubtypeEnum(self.samp_subtype)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.tvdss_of_hcr_press is not None and not isinstance(self.tvdss_of_hcr_press, str):
            self.tvdss_of_hcr_press = str(self.tvdss_of_hcr_press)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.water_cut is not None and not isinstance(self.water_cut, str):
            self.water_cut = str(self.water_cut)

        if self.water_prod_rate is not None and not isinstance(self.water_prod_rate, str):
            self.water_prod_rate = str(self.water_prod_rate)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.add_recov_method is not None and not isinstance(self.add_recov_method, str):
            self.add_recov_method = str(self.add_recov_method)

        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.biocide is not None and not isinstance(self.biocide, str):
            self.biocide = str(self.biocide)

        if self.biocide_admin_method is not None and not isinstance(self.biocide_admin_method, str):
            self.biocide_admin_method = str(self.biocide_admin_method)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.chem_treat_method is not None and not isinstance(self.chem_treat_method, str):
            self.chem_treat_method = str(self.chem_treat_method)

        if self.chem_treatment is not None and not isinstance(self.chem_treatment, str):
            self.chem_treatment = str(self.chem_treatment)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.hc_produced is not None and not isinstance(self.hc_produced, HcProducedEnum):
            self.hc_produced = HcProducedEnum(self.hc_produced)

        if self.hcr is not None and not isinstance(self.hcr, HcrEnum):
            self.hcr = HcrEnum(self.hcr)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, HcrGeolAgeEnum):
            self.hcr_geol_age = HcrGeolAgeEnum(self.hcr_geol_age)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, TimestampValue):
            self.iw_bt_date_well = TimestampValue(**as_dict(self.iw_bt_date_well))

        if self.iwf is not None and not isinstance(self.iwf, str):
            self.iwf = str(self.iwf)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.lithology is not None and not isinstance(self.lithology, LithologyEnum):
            self.lithology = LithologyEnum(self.lithology)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.org_count_qpcr_info is not None and not isinstance(self.org_count_qpcr_info, str):
            self.org_count_qpcr_info = str(self.org_count_qpcr_info)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.prod_rate is not None and not isinstance(self.prod_rate, str):
            self.prod_rate = str(self.prod_rate)

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, TimestampValue):
            self.prod_start_date = TimestampValue(**as_dict(self.prod_start_date))

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_collect_point is not None and not isinstance(self.samp_collect_point, SampCollectPointEnum):
            self.samp_collect_point = SampCollectPointEnum(self.samp_collect_point)

        if self.samp_loc_corr_rate is not None and not isinstance(self.samp_loc_corr_rate, str):
            self.samp_loc_corr_rate = str(self.samp_loc_corr_rate)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_preserv is not None and not isinstance(self.samp_preserv, str):
            self.samp_preserv = str(self.samp_preserv)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, SampSubtypeEnum):
            self.samp_subtype = SampSubtypeEnum(self.samp_subtype)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.tvdss_of_hcr_press is not None and not isinstance(self.tvdss_of_hcr_press, str):
            self.tvdss_of_hcr_press = str(self.tvdss_of_hcr_press)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.water_cut is not None and not isinstance(self.water_cut, str):
            self.water_cut = str(self.water_cut)

        if self.water_prod_rate is not None and not isinstance(self.water_prod_rate, str):
            self.water_prod_rate = str(self.water_prod_rate)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class HostAssociated(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HostAssociated
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HostAssociated"
    class_name: ClassVar[str] = "host_associated"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HostAssociated

    alt: Optional[str] = None
    ances_data: Optional[str] = None
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    blood_press_diast: Optional[str] = None
    blood_press_syst: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    genetic_mod: Optional[str] = None
    geo_loc_name: Optional[str] = None
    gravidity: Optional[str] = None
    host_age: Optional[str] = None
    host_body_habitat: Optional[str] = None
    host_body_product: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_color: Optional[str] = None
    host_common_name: Optional[str] = None
    host_diet: Optional[Union[str, List[str]]] = empty_list()
    host_dry_mass: Optional[str] = None
    host_family_relation: Optional[Union[str, List[str]]] = empty_list()
    host_genotype: Optional[str] = None
    host_growth_cond: Optional[str] = None
    host_height: Optional[str] = None
    host_last_meal: Optional[Union[str, List[str]]] = empty_list()
    host_length: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_sex: Optional[Union[str, "HostSexEnum"]] = None
    host_shape: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_subspecf_genlin: Optional[Union[str, List[str]]] = empty_list()
    host_substrate: Optional[str] = None
    host_symbiont: Optional[Union[str, List[str]]] = empty_list()
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_capt_status: Optional[Union[str, "SampCaptStatusEnum"]] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_dis_stage: Optional[Union[str, "SampDisStageEnum"]] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    size_frac: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    temp: Optional[str] = None
    horizon_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.blood_press_diast is not None and not isinstance(self.blood_press_diast, str):
            self.blood_press_diast = str(self.blood_press_diast)

        if self.blood_press_syst is not None and not isinstance(self.blood_press_syst, str):
            self.blood_press_syst = str(self.blood_press_syst)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.gravidity is not None and not isinstance(self.gravidity, str):
            self.gravidity = str(self.gravidity)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_body_habitat is not None and not isinstance(self.host_body_habitat, str):
            self.host_body_habitat = str(self.host_body_habitat)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_color is not None and not isinstance(self.host_color, str):
            self.host_color = str(self.host_color)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if not isinstance(self.host_diet, list):
            self.host_diet = [self.host_diet] if self.host_diet is not None else []
        self.host_diet = [v if isinstance(v, str) else str(v) for v in self.host_diet]

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if not isinstance(self.host_family_relation, list):
            self.host_family_relation = [self.host_family_relation] if self.host_family_relation is not None else []
        self.host_family_relation = [v if isinstance(v, str) else str(v) for v in self.host_family_relation]

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_growth_cond is not None and not isinstance(self.host_growth_cond, str):
            self.host_growth_cond = str(self.host_growth_cond)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if not isinstance(self.host_last_meal, list):
            self.host_last_meal = [self.host_last_meal] if self.host_last_meal is not None else []
        self.host_last_meal = [v if isinstance(v, str) else str(v) for v in self.host_last_meal]

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_sex is not None and not isinstance(self.host_sex, HostSexEnum):
            self.host_sex = HostSexEnum(self.host_sex)

        if self.host_shape is not None and not isinstance(self.host_shape, str):
            self.host_shape = str(self.host_shape)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if not isinstance(self.host_subspecf_genlin, list):
            self.host_subspecf_genlin = [self.host_subspecf_genlin] if self.host_subspecf_genlin is not None else []
        self.host_subspecf_genlin = [v if isinstance(v, str) else str(v) for v in self.host_subspecf_genlin]

        if self.host_substrate is not None and not isinstance(self.host_substrate, str):
            self.host_substrate = str(self.host_substrate)

        if not isinstance(self.host_symbiont, list):
            self.host_symbiont = [self.host_symbiont] if self.host_symbiont is not None else []
        self.host_symbiont = [v if isinstance(v, str) else str(v) for v in self.host_symbiont]

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, SampCaptStatusEnum):
            self.samp_capt_status = SampCaptStatusEnum(self.samp_capt_status)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, SampDisStageEnum):
            self.samp_dis_stage = SampDisStageEnum(self.samp_dis_stage)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.blood_press_diast is not None and not isinstance(self.blood_press_diast, str):
            self.blood_press_diast = str(self.blood_press_diast)

        if self.blood_press_syst is not None and not isinstance(self.blood_press_syst, str):
            self.blood_press_syst = str(self.blood_press_syst)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.gravidity is not None and not isinstance(self.gravidity, str):
            self.gravidity = str(self.gravidity)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_body_habitat is not None and not isinstance(self.host_body_habitat, str):
            self.host_body_habitat = str(self.host_body_habitat)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_color is not None and not isinstance(self.host_color, str):
            self.host_color = str(self.host_color)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if not isinstance(self.host_diet, list):
            self.host_diet = [self.host_diet] if self.host_diet is not None else []
        self.host_diet = [v if isinstance(v, str) else str(v) for v in self.host_diet]

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if not isinstance(self.host_family_relation, list):
            self.host_family_relation = [self.host_family_relation] if self.host_family_relation is not None else []
        self.host_family_relation = [v if isinstance(v, str) else str(v) for v in self.host_family_relation]

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_growth_cond is not None and not isinstance(self.host_growth_cond, str):
            self.host_growth_cond = str(self.host_growth_cond)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if not isinstance(self.host_last_meal, list):
            self.host_last_meal = [self.host_last_meal] if self.host_last_meal is not None else []
        self.host_last_meal = [v if isinstance(v, str) else str(v) for v in self.host_last_meal]

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_sex is not None and not isinstance(self.host_sex, HostSexEnum):
            self.host_sex = HostSexEnum(self.host_sex)

        if self.host_shape is not None and not isinstance(self.host_shape, str):
            self.host_shape = str(self.host_shape)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if not isinstance(self.host_subspecf_genlin, list):
            self.host_subspecf_genlin = [self.host_subspecf_genlin] if self.host_subspecf_genlin is not None else []
        self.host_subspecf_genlin = [v if isinstance(v, str) else str(v) for v in self.host_subspecf_genlin]

        if self.host_substrate is not None and not isinstance(self.host_substrate, str):
            self.host_substrate = str(self.host_substrate)

        if not isinstance(self.host_symbiont, list):
            self.host_symbiont = [self.host_symbiont] if self.host_symbiont is not None else []
        self.host_symbiont = [v if isinstance(v, str) else str(v) for v in self.host_symbiont]

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, SampCaptStatusEnum):
            self.samp_capt_status = SampCaptStatusEnum(self.samp_capt_status)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, SampDisStageEnum):
            self.samp_dis_stage = SampDisStageEnum(self.samp_dis_stage)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class JgiMg(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMg
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:JgiMg"
    class_name: ClassVar[str] = "jgi_mg"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMg

    dna_absorb1: Optional[str] = None
    dna_absorb2: Optional[str] = None
    dna_collect_site: Optional[str] = None
    dna_concentration: Optional[str] = None
    dna_cont_type: Optional[Union[str, "DnaContTypeEnum"]] = None
    dna_cont_well: Optional[str] = None
    dna_container_ID: Optional[str] = None
    dna_dnase: Optional[Union[str, "DnaDnaseEnum"]] = None
    dna_isolate_meth: Optional[str] = None
    dna_organisms: Optional[str] = None
    dna_project_contact: Optional[str] = None
    dna_samp_ID: Optional[str] = None
    dna_sample_format: Optional[Union[str, "DnaSampleFormatEnum"]] = None
    dna_sample_name: Optional[str] = None
    dna_seq_project: Optional[str] = None
    dna_seq_project_PI: Optional[str] = None
    dna_seq_project_name: Optional[str] = None
    dna_volume: Optional[str] = None
    proposal_dna: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dna_absorb1 is not None and not isinstance(self.dna_absorb1, str):
            self.dna_absorb1 = str(self.dna_absorb1)

        if self.dna_absorb2 is not None and not isinstance(self.dna_absorb2, str):
            self.dna_absorb2 = str(self.dna_absorb2)

        if self.dna_collect_site is not None and not isinstance(self.dna_collect_site, str):
            self.dna_collect_site = str(self.dna_collect_site)

        if self.dna_concentration is not None and not isinstance(self.dna_concentration, str):
            self.dna_concentration = str(self.dna_concentration)

        if self.dna_cont_type is not None and not isinstance(self.dna_cont_type, DnaContTypeEnum):
            self.dna_cont_type = DnaContTypeEnum(self.dna_cont_type)

        if self.dna_cont_well is not None and not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if self.dna_container_ID is not None and not isinstance(self.dna_container_ID, str):
            self.dna_container_ID = str(self.dna_container_ID)

        if self.dna_dnase is not None and not isinstance(self.dna_dnase, DnaDnaseEnum):
            self.dna_dnase = DnaDnaseEnum(self.dna_dnase)

        if self.dna_isolate_meth is not None and not isinstance(self.dna_isolate_meth, str):
            self.dna_isolate_meth = str(self.dna_isolate_meth)

        if self.dna_organisms is not None and not isinstance(self.dna_organisms, str):
            self.dna_organisms = str(self.dna_organisms)

        if self.dna_project_contact is not None and not isinstance(self.dna_project_contact, str):
            self.dna_project_contact = str(self.dna_project_contact)

        if self.dna_samp_ID is not None and not isinstance(self.dna_samp_ID, str):
            self.dna_samp_ID = str(self.dna_samp_ID)

        if self.dna_sample_format is not None and not isinstance(self.dna_sample_format, DnaSampleFormatEnum):
            self.dna_sample_format = DnaSampleFormatEnum(self.dna_sample_format)

        if self.dna_sample_name is not None and not isinstance(self.dna_sample_name, str):
            self.dna_sample_name = str(self.dna_sample_name)

        if self.dna_seq_project is not None and not isinstance(self.dna_seq_project, str):
            self.dna_seq_project = str(self.dna_seq_project)

        if self.dna_seq_project_PI is not None and not isinstance(self.dna_seq_project_PI, str):
            self.dna_seq_project_PI = str(self.dna_seq_project_PI)

        if self.dna_seq_project_name is not None and not isinstance(self.dna_seq_project_name, str):
            self.dna_seq_project_name = str(self.dna_seq_project_name)

        if self.dna_volume is not None and not isinstance(self.dna_volume, str):
            self.dna_volume = str(self.dna_volume)

        if self.proposal_dna is not None and not isinstance(self.proposal_dna, str):
            self.proposal_dna = str(self.proposal_dna)

        if self.dna_cont_well is not None and not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class JgiMt(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMt
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:JgiMt"
    class_name: ClassVar[str] = "jgi_mt"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMt

    dnase_rna: Optional[Union[str, "DnaseRnaEnum"]] = None
    proposal_rna: Optional[str] = None
    rna_absorb1: Optional[str] = None
    rna_absorb2: Optional[str] = None
    rna_collect_site: Optional[str] = None
    rna_concentration: Optional[str] = None
    rna_cont_type: Optional[Union[str, "RnaContTypeEnum"]] = None
    rna_cont_well: Optional[str] = None
    rna_container_ID: Optional[str] = None
    rna_isolate_meth: Optional[str] = None
    rna_organisms: Optional[str] = None
    rna_project_contact: Optional[str] = None
    rna_samp_ID: Optional[str] = None
    rna_sample_format: Optional[Union[str, "RnaSampleFormatEnum"]] = None
    rna_sample_name: Optional[str] = None
    rna_seq_project: Optional[str] = None
    rna_seq_project_PI: Optional[str] = None
    rna_seq_project_name: Optional[str] = None
    rna_volume: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dnase_rna is not None and not isinstance(self.dnase_rna, DnaseRnaEnum):
            self.dnase_rna = DnaseRnaEnum(self.dnase_rna)

        if self.proposal_rna is not None and not isinstance(self.proposal_rna, str):
            self.proposal_rna = str(self.proposal_rna)

        if self.rna_absorb1 is not None and not isinstance(self.rna_absorb1, str):
            self.rna_absorb1 = str(self.rna_absorb1)

        if self.rna_absorb2 is not None and not isinstance(self.rna_absorb2, str):
            self.rna_absorb2 = str(self.rna_absorb2)

        if self.rna_collect_site is not None and not isinstance(self.rna_collect_site, str):
            self.rna_collect_site = str(self.rna_collect_site)

        if self.rna_concentration is not None and not isinstance(self.rna_concentration, str):
            self.rna_concentration = str(self.rna_concentration)

        if self.rna_cont_type is not None and not isinstance(self.rna_cont_type, RnaContTypeEnum):
            self.rna_cont_type = RnaContTypeEnum(self.rna_cont_type)

        if self.rna_cont_well is not None and not isinstance(self.rna_cont_well, str):
            self.rna_cont_well = str(self.rna_cont_well)

        if self.rna_container_ID is not None and not isinstance(self.rna_container_ID, str):
            self.rna_container_ID = str(self.rna_container_ID)

        if self.rna_isolate_meth is not None and not isinstance(self.rna_isolate_meth, str):
            self.rna_isolate_meth = str(self.rna_isolate_meth)

        if self.rna_organisms is not None and not isinstance(self.rna_organisms, str):
            self.rna_organisms = str(self.rna_organisms)

        if self.rna_project_contact is not None and not isinstance(self.rna_project_contact, str):
            self.rna_project_contact = str(self.rna_project_contact)

        if self.rna_samp_ID is not None and not isinstance(self.rna_samp_ID, str):
            self.rna_samp_ID = str(self.rna_samp_ID)

        if self.rna_sample_format is not None and not isinstance(self.rna_sample_format, RnaSampleFormatEnum):
            self.rna_sample_format = RnaSampleFormatEnum(self.rna_sample_format)

        if self.rna_sample_name is not None and not isinstance(self.rna_sample_name, str):
            self.rna_sample_name = str(self.rna_sample_name)

        if self.rna_seq_project is not None and not isinstance(self.rna_seq_project, str):
            self.rna_seq_project = str(self.rna_seq_project)

        if self.rna_seq_project_PI is not None and not isinstance(self.rna_seq_project_PI, str):
            self.rna_seq_project_PI = str(self.rna_seq_project_PI)

        if self.rna_seq_project_name is not None and not isinstance(self.rna_seq_project_name, str):
            self.rna_seq_project_name = str(self.rna_seq_project_name)

        if self.rna_volume is not None and not isinstance(self.rna_volume, str):
            self.rna_volume = str(self.rna_volume)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class MiscEnvs(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.MiscEnvs
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:MiscEnvs"
    class_name: ClassVar[str] = "misc_envs"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.MiscEnvs

    alkalinity: Optional[str] = None
    alt: Optional[str] = None
    ammonium: Optional[str] = None
    biomass: Optional[Union[str, List[str]]] = empty_list()
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    density: Optional[str] = None
    depth: Optional[str] = None
    diether_lipids: Optional[Union[str, List[str]]] = empty_list()
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    geo_loc_name: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    ph: Optional[float] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[Union[str, List[str]]] = empty_list()
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    silicate: Optional[str] = None
    size_frac: Optional[str] = None
    sodium: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    water_current: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class PlantAssociated(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.PlantAssociated
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:PlantAssociated"
    class_name: ClassVar[str] = "plant_associated"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.PlantAssociated

    air_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    alt: Optional[str] = None
    ances_data: Optional[str] = None
    antibiotic_regm: Optional[Union[str, List[str]]] = empty_list()
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chem_mutagen: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    cult_root_med: Optional[str] = None
    depth: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    fertilizer_regm: Optional[Union[str, List[str]]] = empty_list()
    fungicide_regm: Optional[Union[str, List[str]]] = empty_list()
    gaseous_environment: Optional[Union[str, List[str]]] = empty_list()
    genetic_mod: Optional[str] = None
    geo_loc_name: Optional[str] = None
    gravity: Optional[Union[str, List[str]]] = empty_list()
    growth_facil: Optional[str] = None
    growth_habit: Optional[Union[str, "GrowthHabitEnum"]] = None
    growth_hormone_regm: Optional[Union[str, List[str]]] = empty_list()
    herbicide_regm: Optional[Union[str, List[str]]] = empty_list()
    host_age: Optional[str] = None
    host_common_name: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_genotype: Optional[str] = None
    host_height: Optional[str] = None
    host_length: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_subspecf_genlin: Optional[Union[str, List[str]]] = empty_list()
    host_symbiont: Optional[Union[str, List[str]]] = empty_list()
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_wet_mass: Optional[str] = None
    humidity_regm: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    light_regm: Optional[str] = None
    mechanical_damage: Optional[Union[str, List[str]]] = empty_list()
    mineral_nutr_regm: Optional[Union[str, List[str]]] = empty_list()
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    non_min_nutr_regm: Optional[Union[str, List[str]]] = empty_list()
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    pesticide_regm: Optional[Union[str, List[str]]] = empty_list()
    ph_regm: Optional[Union[str, List[str]]] = empty_list()
    plant_growth_med: Optional[str] = None
    plant_product: Optional[str] = None
    plant_sex: Optional[Union[str, "PlantSexEnum"]] = None
    plant_struc: Optional[str] = None
    radiation_regm: Optional[Union[str, List[str]]] = empty_list()
    rainfall_regm: Optional[Union[str, List[str]]] = empty_list()
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    root_cond: Optional[str] = None
    root_med_carbon: Optional[str] = None
    root_med_macronutr: Optional[str] = None
    root_med_micronutr: Optional[str] = None
    root_med_ph: Optional[str] = None
    root_med_regl: Optional[str] = None
    root_med_solid: Optional[str] = None
    root_med_suppl: Optional[str] = None
    salinity: Optional[str] = None
    salt_regm: Optional[Union[str, List[str]]] = empty_list()
    samp_capt_status: Optional[Union[str, "SampCaptStatusEnum"]] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_dis_stage: Optional[Union[str, "SampDisStageEnum"]] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    season_environment: Optional[Union[str, List[str]]] = empty_list()
    size_frac: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    standing_water_regm: Optional[Union[str, List[str]]] = empty_list()
    temp: Optional[str] = None
    tiss_cult_growth_med: Optional[str] = None
    water_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    watering_regm: Optional[Union[str, List[str]]] = empty_list()
    horizon_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if not isinstance(self.antibiotic_regm, list):
            self.antibiotic_regm = [self.antibiotic_regm] if self.antibiotic_regm is not None else []
        self.antibiotic_regm = [v if isinstance(v, str) else str(v) for v in self.antibiotic_regm]

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.chem_mutagen, list):
            self.chem_mutagen = [self.chem_mutagen] if self.chem_mutagen is not None else []
        self.chem_mutagen = [v if isinstance(v, str) else str(v) for v in self.chem_mutagen]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if not isinstance(self.fertilizer_regm, list):
            self.fertilizer_regm = [self.fertilizer_regm] if self.fertilizer_regm is not None else []
        self.fertilizer_regm = [v if isinstance(v, str) else str(v) for v in self.fertilizer_regm]

        if not isinstance(self.fungicide_regm, list):
            self.fungicide_regm = [self.fungicide_regm] if self.fungicide_regm is not None else []
        self.fungicide_regm = [v if isinstance(v, str) else str(v) for v in self.fungicide_regm]

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if not isinstance(self.gravity, list):
            self.gravity = [self.gravity] if self.gravity is not None else []
        self.gravity = [v if isinstance(v, str) else str(v) for v in self.gravity]

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if not isinstance(self.growth_hormone_regm, list):
            self.growth_hormone_regm = [self.growth_hormone_regm] if self.growth_hormone_regm is not None else []
        self.growth_hormone_regm = [v if isinstance(v, str) else str(v) for v in self.growth_hormone_regm]

        if not isinstance(self.herbicide_regm, list):
            self.herbicide_regm = [self.herbicide_regm] if self.herbicide_regm is not None else []
        self.herbicide_regm = [v if isinstance(v, str) else str(v) for v in self.herbicide_regm]

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if not isinstance(self.host_subspecf_genlin, list):
            self.host_subspecf_genlin = [self.host_subspecf_genlin] if self.host_subspecf_genlin is not None else []
        self.host_subspecf_genlin = [v if isinstance(v, str) else str(v) for v in self.host_subspecf_genlin]

        if not isinstance(self.host_symbiont, list):
            self.host_symbiont = [self.host_symbiont] if self.host_symbiont is not None else []
        self.host_symbiont = [v if isinstance(v, str) else str(v) for v in self.host_symbiont]

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if not isinstance(self.mechanical_damage, list):
            self.mechanical_damage = [self.mechanical_damage] if self.mechanical_damage is not None else []
        self.mechanical_damage = [v if isinstance(v, str) else str(v) for v in self.mechanical_damage]

        if not isinstance(self.mineral_nutr_regm, list):
            self.mineral_nutr_regm = [self.mineral_nutr_regm] if self.mineral_nutr_regm is not None else []
        self.mineral_nutr_regm = [v if isinstance(v, str) else str(v) for v in self.mineral_nutr_regm]

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.non_min_nutr_regm, list):
            self.non_min_nutr_regm = [self.non_min_nutr_regm] if self.non_min_nutr_regm is not None else []
        self.non_min_nutr_regm = [v if isinstance(v, str) else str(v) for v in self.non_min_nutr_regm]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if not isinstance(self.pesticide_regm, list):
            self.pesticide_regm = [self.pesticide_regm] if self.pesticide_regm is not None else []
        self.pesticide_regm = [v if isinstance(v, str) else str(v) for v in self.pesticide_regm]

        if not isinstance(self.ph_regm, list):
            self.ph_regm = [self.ph_regm] if self.ph_regm is not None else []
        self.ph_regm = [v if isinstance(v, str) else str(v) for v in self.ph_regm]

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_product is not None and not isinstance(self.plant_product, str):
            self.plant_product = str(self.plant_product)

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, str):
            self.plant_struc = str(self.plant_struc)

        if not isinstance(self.radiation_regm, list):
            self.radiation_regm = [self.radiation_regm] if self.radiation_regm is not None else []
        self.radiation_regm = [v if isinstance(v, str) else str(v) for v in self.radiation_regm]

        if not isinstance(self.rainfall_regm, list):
            self.rainfall_regm = [self.rainfall_regm] if self.rainfall_regm is not None else []
        self.rainfall_regm = [v if isinstance(v, str) else str(v) for v in self.rainfall_regm]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.root_med_ph is not None and not isinstance(self.root_med_ph, str):
            self.root_med_ph = str(self.root_med_ph)

        if self.root_med_regl is not None and not isinstance(self.root_med_regl, str):
            self.root_med_regl = str(self.root_med_regl)

        if self.root_med_solid is not None and not isinstance(self.root_med_solid, str):
            self.root_med_solid = str(self.root_med_solid)

        if self.root_med_suppl is not None and not isinstance(self.root_med_suppl, str):
            self.root_med_suppl = str(self.root_med_suppl)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if not isinstance(self.salt_regm, list):
            self.salt_regm = [self.salt_regm] if self.salt_regm is not None else []
        self.salt_regm = [v if isinstance(v, str) else str(v) for v in self.salt_regm]

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, SampCaptStatusEnum):
            self.samp_capt_status = SampCaptStatusEnum(self.samp_capt_status)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, SampDisStageEnum):
            self.samp_dis_stage = SampDisStageEnum(self.samp_dis_stage)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if not isinstance(self.season_environment, list):
            self.season_environment = [self.season_environment] if self.season_environment is not None else []
        self.season_environment = [v if isinstance(v, str) else str(v) for v in self.season_environment]

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.standing_water_regm, list):
            self.standing_water_regm = [self.standing_water_regm] if self.standing_water_regm is not None else []
        self.standing_water_regm = [v if isinstance(v, str) else str(v) for v in self.standing_water_regm]

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if not isinstance(self.water_temp_regm, list):
            self.water_temp_regm = [self.water_temp_regm] if self.water_temp_regm is not None else []
        self.water_temp_regm = [v if isinstance(v, str) else str(v) for v in self.water_temp_regm]

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if not isinstance(self.antibiotic_regm, list):
            self.antibiotic_regm = [self.antibiotic_regm] if self.antibiotic_regm is not None else []
        self.antibiotic_regm = [v if isinstance(v, str) else str(v) for v in self.antibiotic_regm]

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.chem_mutagen, list):
            self.chem_mutagen = [self.chem_mutagen] if self.chem_mutagen is not None else []
        self.chem_mutagen = [v if isinstance(v, str) else str(v) for v in self.chem_mutagen]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if not isinstance(self.fertilizer_regm, list):
            self.fertilizer_regm = [self.fertilizer_regm] if self.fertilizer_regm is not None else []
        self.fertilizer_regm = [v if isinstance(v, str) else str(v) for v in self.fertilizer_regm]

        if not isinstance(self.fungicide_regm, list):
            self.fungicide_regm = [self.fungicide_regm] if self.fungicide_regm is not None else []
        self.fungicide_regm = [v if isinstance(v, str) else str(v) for v in self.fungicide_regm]

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if not isinstance(self.gravity, list):
            self.gravity = [self.gravity] if self.gravity is not None else []
        self.gravity = [v if isinstance(v, str) else str(v) for v in self.gravity]

        if self.growth_facil is not None and not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if not isinstance(self.growth_hormone_regm, list):
            self.growth_hormone_regm = [self.growth_hormone_regm] if self.growth_hormone_regm is not None else []
        self.growth_hormone_regm = [v if isinstance(v, str) else str(v) for v in self.growth_hormone_regm]

        if not isinstance(self.herbicide_regm, list):
            self.herbicide_regm = [self.herbicide_regm] if self.herbicide_regm is not None else []
        self.herbicide_regm = [v if isinstance(v, str) else str(v) for v in self.herbicide_regm]

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if not isinstance(self.host_subspecf_genlin, list):
            self.host_subspecf_genlin = [self.host_subspecf_genlin] if self.host_subspecf_genlin is not None else []
        self.host_subspecf_genlin = [v if isinstance(v, str) else str(v) for v in self.host_subspecf_genlin]

        if not isinstance(self.host_symbiont, list):
            self.host_symbiont = [self.host_symbiont] if self.host_symbiont is not None else []
        self.host_symbiont = [v if isinstance(v, str) else str(v) for v in self.host_symbiont]

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if not isinstance(self.mechanical_damage, list):
            self.mechanical_damage = [self.mechanical_damage] if self.mechanical_damage is not None else []
        self.mechanical_damage = [v if isinstance(v, str) else str(v) for v in self.mechanical_damage]

        if not isinstance(self.mineral_nutr_regm, list):
            self.mineral_nutr_regm = [self.mineral_nutr_regm] if self.mineral_nutr_regm is not None else []
        self.mineral_nutr_regm = [v if isinstance(v, str) else str(v) for v in self.mineral_nutr_regm]

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.non_min_nutr_regm, list):
            self.non_min_nutr_regm = [self.non_min_nutr_regm] if self.non_min_nutr_regm is not None else []
        self.non_min_nutr_regm = [v if isinstance(v, str) else str(v) for v in self.non_min_nutr_regm]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if not isinstance(self.pesticide_regm, list):
            self.pesticide_regm = [self.pesticide_regm] if self.pesticide_regm is not None else []
        self.pesticide_regm = [v if isinstance(v, str) else str(v) for v in self.pesticide_regm]

        if not isinstance(self.ph_regm, list):
            self.ph_regm = [self.ph_regm] if self.ph_regm is not None else []
        self.ph_regm = [v if isinstance(v, str) else str(v) for v in self.ph_regm]

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_product is not None and not isinstance(self.plant_product, str):
            self.plant_product = str(self.plant_product)

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, str):
            self.plant_struc = str(self.plant_struc)

        if not isinstance(self.radiation_regm, list):
            self.radiation_regm = [self.radiation_regm] if self.radiation_regm is not None else []
        self.radiation_regm = [v if isinstance(v, str) else str(v) for v in self.radiation_regm]

        if not isinstance(self.rainfall_regm, list):
            self.rainfall_regm = [self.rainfall_regm] if self.rainfall_regm is not None else []
        self.rainfall_regm = [v if isinstance(v, str) else str(v) for v in self.rainfall_regm]

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.root_med_ph is not None and not isinstance(self.root_med_ph, str):
            self.root_med_ph = str(self.root_med_ph)

        if self.root_med_regl is not None and not isinstance(self.root_med_regl, str):
            self.root_med_regl = str(self.root_med_regl)

        if self.root_med_solid is not None and not isinstance(self.root_med_solid, str):
            self.root_med_solid = str(self.root_med_solid)

        if self.root_med_suppl is not None and not isinstance(self.root_med_suppl, str):
            self.root_med_suppl = str(self.root_med_suppl)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if not isinstance(self.salt_regm, list):
            self.salt_regm = [self.salt_regm] if self.salt_regm is not None else []
        self.salt_regm = [v if isinstance(v, str) else str(v) for v in self.salt_regm]

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, SampCaptStatusEnum):
            self.samp_capt_status = SampCaptStatusEnum(self.samp_capt_status)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, SampDisStageEnum):
            self.samp_dis_stage = SampDisStageEnum(self.samp_dis_stage)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if not isinstance(self.season_environment, list):
            self.season_environment = [self.season_environment] if self.season_environment is not None else []
        self.season_environment = [v if isinstance(v, str) else str(v) for v in self.season_environment]

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.standing_water_regm, list):
            self.standing_water_regm = [self.standing_water_regm] if self.standing_water_regm is not None else []
        self.standing_water_regm = [v if isinstance(v, str) else str(v) for v in self.standing_water_regm]

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if not isinstance(self.water_temp_regm, list):
            self.water_temp_regm = [self.water_temp_regm] if self.water_temp_regm is not None else []
        self.water_temp_regm = [v if isinstance(v, str) else str(v) for v in self.water_temp_regm]

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class SampIdNewTermsMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampIdNewTermsMixin
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SampIdNewTermsMixin"
    class_name: ClassVar[str] = "samp_id_new_terms_mixin"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampIdNewTermsMixin

    env_package: Optional[str] = None
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class Sediment(DhInterface):
    """
    sediment dev
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Sediment
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Sediment"
    class_name: ClassVar[str] = "sediment"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Sediment

    alkalinity: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    alt: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biomass: Optional[Union[str, List[str]]] = empty_list()
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    density: Optional[str] = None
    depth: Optional[str] = None
    diether_lipids: Optional[Union[str, List[str]]] = empty_list()
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    geo_loc_name: Optional[str] = None
    glucosidase_act: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    methane: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    n_alkanes: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    part_org_carb: Optional[str] = None
    particle_class: Optional[Union[str, List[str]]] = empty_list()
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    phaeopigments: Optional[Union[str, List[str]]] = empty_list()
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[Union[str, List[str]]] = empty_list()
    porosity: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    redox_potential: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    sediment_type: Optional[Union[str, "SedimentTypeEnum"]] = None
    silicate: Optional[str] = None
    size_frac: Optional[str] = None
    sodium: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tot_carb: Optional[str] = None
    tot_depth_water_col: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_content: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if not isinstance(self.particle_class, list):
            self.particle_class = [self.particle_class] if self.particle_class is not None else []
        self.particle_class = [v if isinstance(v, str) else str(v) for v in self.particle_class]

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.sediment_type is not None and not isinstance(self.sediment_type, SedimentTypeEnum):
            self.sediment_type = SedimentTypeEnum(self.sediment_type)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if not isinstance(self.particle_class, list):
            self.particle_class = [self.particle_class] if self.particle_class is not None else []
        self.particle_class = [v if isinstance(v, str) else str(v) for v in self.particle_class]

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.sediment_type is not None and not isinstance(self.sediment_type, SedimentTypeEnum):
            self.sediment_type = SedimentTypeEnum(self.sediment_type)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if not isinstance(self.water_content, list):
            self.water_content = [self.water_content] if self.water_content is not None else []
        self.water_content = [v if isinstance(v, str) else str(v) for v in self.water_content]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class Soil(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Soil
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Soil"
    class_name: ClassVar[str] = "soil"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Soil

    agrochem_addition: Optional[Union[str, List[str]]] = empty_list()
    air_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    al_sat: Optional[str] = None
    al_sat_meth: Optional[str] = None
    alt: Optional[str] = None
    annual_precpt: Optional[str] = None
    annual_temp: Optional[str] = None
    biotic_regm: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    crop_rotation: Optional[str] = None
    cur_land_use: Optional[Union[str, "CurLandUseEnum"]] = None
    cur_vegetation: Optional[str] = None
    cur_vegetation_meth: Optional[str] = None
    depth: Optional[str] = None
    drainage_class: Optional[Union[str, "DrainageClassEnum"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    extreme_event: Optional[Union[dict, "TimestampValue"]] = None
    fao_class: Optional[Union[str, "FaoClassEnum"]] = None
    fire: Optional[Union[dict, "TimestampValue"]] = None
    flooding: Optional[Union[dict, "TimestampValue"]] = None
    gaseous_environment: Optional[Union[str, List[str]]] = empty_list()
    geo_loc_name: Optional[str] = None
    growth_facil: Optional[str] = None
    heavy_metals: Optional[Union[str, List[str]]] = empty_list()
    heavy_metals_meth: Optional[str] = None
    horizon_meth: Optional[str] = None
    humidity_regm: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    light_regm: Optional[str] = None
    link_class_info: Optional[str] = None
    link_climate_info: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
    micro_biomass_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    phosphate: Optional[str] = None
    prev_land_use_meth: Optional[str] = None
    previous_land_use: Optional[str] = None
    profile_position: Optional[Union[str, "ProfilePositionEnum"]] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    salinity_meth: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_temp: Optional[str] = None
    season_precpt: Optional[str] = None
    season_temp: Optional[str] = None
    sieving: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    slope_aspect: Optional[str] = None
    slope_gradient: Optional[str] = None
    soil_horizon: Optional[Union[str, "SoilHorizonEnum"]] = None
    soil_text_measure: Optional[str] = None
    soil_texture_meth: Optional[str] = None
    soil_type: Optional[str] = None
    soil_type_meth: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    store_cond: Optional[str] = None
    temp: Optional[str] = None
    tillage: Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]] = empty_list()
    tot_carb: Optional[str] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    tot_phosp: Optional[str] = None
    water_cont_soil_meth: Optional[str] = None
    water_content: Optional[str] = None
    watering_regm: Optional[Union[str, List[str]]] = empty_list()
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    collection_date_inc: Optional[str] = None
    collection_time: Optional[str] = None
    collection_time_inc: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    filter_method: Optional[str] = None
    isotope_exposure: Optional[str] = None
    micro_biomass_C_meth: Optional[str] = None
    micro_biomass_N_meth: Optional[str] = None
    microbial_biomass_C: Optional[str] = None
    microbial_biomass_N: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other_treatment: Optional[str] = None
    start_date_inc: Optional[str] = None
    start_time_inc: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, TimestampValue):
            self.extreme_event = TimestampValue(**as_dict(self.extreme_event))

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, TimestampValue):
            self.fire = TimestampValue(**as_dict(self.fire))

        if self.flooding is not None and not isinstance(self.flooding, TimestampValue):
            self.flooding = TimestampValue(**as_dict(self.flooding))

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, str):
            self.soil_text_measure = str(self.soil_text_measure)

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.store_cond is not None and not isinstance(self.store_cond, str):
            self.store_cond = str(self.store_cond)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.ecosystem is not None and not isinstance(self.ecosystem, EcosystemEnum):
            self.ecosystem = EcosystemEnum(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, EcosystemCategoryEnum):
            self.ecosystem_category = EcosystemCategoryEnum(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, EcosystemSubtypeEnum):
            self.ecosystem_subtype = EcosystemSubtypeEnum(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, EcosystemTypeEnum):
            self.ecosystem_type = EcosystemTypeEnum(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, EnvBroadScaleSoilEnum):
            self.env_broad_scale = EnvBroadScaleSoilEnum(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, EnvLocalScaleSoilEnum):
            self.env_local_scale = EnvLocalScaleSoilEnum(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, EnvMediumSoilEnum):
            self.env_medium = EnvMediumSoilEnum(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, str):
            self.extreme_event = str(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, str):
            self.fire = str(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, str):
            self.flooding = str(self.flooding)

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.growth_facil is not None and not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if not isinstance(self.heavy_metals_meth, list):
            self.heavy_metals_meth = [self.heavy_metals_meth] if self.heavy_metals_meth is not None else []
        self.heavy_metals_meth = [v if isinstance(v, str) else str(v) for v in self.heavy_metals_meth]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, str):
            self.soil_text_measure = str(self.soil_text_measure)

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, SpecificEcosystemEnum):
            self.specific_ecosystem = SpecificEcosystemEnum(self.specific_ecosystem)

        if self.store_cond is not None and not isinstance(self.store_cond, StoreCondEnum):
            self.store_cond = StoreCondEnum(self.store_cond)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if not isinstance(self.water_content, list):
            self.water_content = [self.water_content] if self.water_content is not None else []
        self.water_content = [v if isinstance(v, str) else str(v) for v in self.water_content]

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.collection_date_inc is not None and not isinstance(self.collection_date_inc, str):
            self.collection_date_inc = str(self.collection_date_inc)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.collection_time_inc is not None and not isinstance(self.collection_time_inc, str):
            self.collection_time_inc = str(self.collection_time_inc)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.micro_biomass_C_meth is not None and not isinstance(self.micro_biomass_C_meth, str):
            self.micro_biomass_C_meth = str(self.micro_biomass_C_meth)

        if self.micro_biomass_N_meth is not None and not isinstance(self.micro_biomass_N_meth, str):
            self.micro_biomass_N_meth = str(self.micro_biomass_N_meth)

        if self.microbial_biomass_C is not None and not isinstance(self.microbial_biomass_C, str):
            self.microbial_biomass_C = str(self.microbial_biomass_C)

        if self.microbial_biomass_N is not None and not isinstance(self.microbial_biomass_N, str):
            self.microbial_biomass_N = str(self.microbial_biomass_N)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.start_time_inc is not None and not isinstance(self.start_time_inc, str):
            self.start_time_inc = str(self.start_time_inc)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class SoilMixsInspiredMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilMixsInspiredMixin
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SoilMixsInspiredMixin"
    class_name: ClassVar[str] = "soil_mixs_inspired_mixin"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilMixsInspiredMixin

    collection_date_inc: Optional[str] = None
    collection_time: Optional[str] = None
    collection_time_inc: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    filter_method: Optional[str] = None
    isotope_exposure: Optional[str] = None
    micro_biomass_C_meth: Optional[str] = None
    micro_biomass_N_meth: Optional[str] = None
    microbial_biomass_C: Optional[str] = None
    microbial_biomass_N: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other_treatment: Optional[str] = None
    start_date_inc: Optional[str] = None
    start_time_inc: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.collection_date_inc is not None and not isinstance(self.collection_date_inc, str):
            self.collection_date_inc = str(self.collection_date_inc)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.collection_time_inc is not None and not isinstance(self.collection_time_inc, str):
            self.collection_time_inc = str(self.collection_time_inc)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.micro_biomass_C_meth is not None and not isinstance(self.micro_biomass_C_meth, str):
            self.micro_biomass_C_meth = str(self.micro_biomass_C_meth)

        if self.micro_biomass_N_meth is not None and not isinstance(self.micro_biomass_N_meth, str):
            self.micro_biomass_N_meth = str(self.micro_biomass_N_meth)

        if self.microbial_biomass_C is not None and not isinstance(self.microbial_biomass_C, str):
            self.microbial_biomass_C = str(self.microbial_biomass_C)

        if self.microbial_biomass_N is not None and not isinstance(self.microbial_biomass_N, str):
            self.microbial_biomass_N = str(self.microbial_biomass_N)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.start_time_inc is not None and not isinstance(self.start_time_inc, str):
            self.start_time_inc = str(self.start_time_inc)

        super().__post_init__(**kwargs)


@dataclass
class WastewaterSludge(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WastewaterSludge
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:WastewaterSludge"
    class_name: ClassVar[str] = "wastewater_sludge"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WastewaterSludge

    alkalinity: Optional[str] = None
    alt: Optional[str] = None
    biochem_oxygen_dem: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chem_oxygen_dem: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    efficiency_percent: Optional[str] = None
    elev: Optional[str] = None
    emulsions: Optional[Union[str, List[str]]] = empty_list()
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    gaseous_substances: Optional[Union[str, List[str]]] = empty_list()
    geo_loc_name: Optional[str] = None
    indust_eff_percent: Optional[str] = None
    inorg_particles: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    org_particles: Optional[Union[str, List[str]]] = empty_list()
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    ph: Optional[float] = None
    phosphate: Optional[str] = None
    pre_treatment: Optional[str] = None
    primary_treatment: Optional[str] = None
    reactor_type: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    secondary_treatment: Optional[str] = None
    sewage_type: Optional[str] = None
    size_frac: Optional[str] = None
    sludge_retent_time: Optional[str] = None
    sodium: Optional[str] = None
    soluble_inorg_mat: Optional[Union[str, List[str]]] = empty_list()
    soluble_org_mat: Optional[Union[str, List[str]]] = empty_list()
    specific_ecosystem: Optional[str] = None
    suspend_solids: Optional[Union[str, List[str]]] = empty_list()
    temp: Optional[str] = None
    tertiary_treatment: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_phosphate: Optional[str] = None
    wastewater_type: Optional[str] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.biochem_oxygen_dem is not None and not isinstance(self.biochem_oxygen_dem, str):
            self.biochem_oxygen_dem = str(self.biochem_oxygen_dem)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chem_oxygen_dem is not None and not isinstance(self.chem_oxygen_dem, str):
            self.chem_oxygen_dem = str(self.chem_oxygen_dem)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, str):
            self.efficiency_percent = str(self.efficiency_percent)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if not isinstance(self.emulsions, list):
            self.emulsions = [self.emulsions] if self.emulsions is not None else []
        self.emulsions = [v if isinstance(v, str) else str(v) for v in self.emulsions]

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if not isinstance(self.gaseous_substances, list):
            self.gaseous_substances = [self.gaseous_substances] if self.gaseous_substances is not None else []
        self.gaseous_substances = [v if isinstance(v, str) else str(v) for v in self.gaseous_substances]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.indust_eff_percent is not None and not isinstance(self.indust_eff_percent, str):
            self.indust_eff_percent = str(self.indust_eff_percent)

        if not isinstance(self.inorg_particles, list):
            self.inorg_particles = [self.inorg_particles] if self.inorg_particles is not None else []
        self.inorg_particles = [v if isinstance(v, str) else str(v) for v in self.inorg_particles]

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if not isinstance(self.org_particles, list):
            self.org_particles = [self.org_particles] if self.org_particles is not None else []
        self.org_particles = [v if isinstance(v, str) else str(v) for v in self.org_particles]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.pre_treatment is not None and not isinstance(self.pre_treatment, str):
            self.pre_treatment = str(self.pre_treatment)

        if self.primary_treatment is not None and not isinstance(self.primary_treatment, str):
            self.primary_treatment = str(self.primary_treatment)

        if self.reactor_type is not None and not isinstance(self.reactor_type, str):
            self.reactor_type = str(self.reactor_type)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.secondary_treatment is not None and not isinstance(self.secondary_treatment, str):
            self.secondary_treatment = str(self.secondary_treatment)

        if self.sewage_type is not None and not isinstance(self.sewage_type, str):
            self.sewage_type = str(self.sewage_type)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sludge_retent_time is not None and not isinstance(self.sludge_retent_time, str):
            self.sludge_retent_time = str(self.sludge_retent_time)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if not isinstance(self.soluble_inorg_mat, list):
            self.soluble_inorg_mat = [self.soluble_inorg_mat] if self.soluble_inorg_mat is not None else []
        self.soluble_inorg_mat = [v if isinstance(v, str) else str(v) for v in self.soluble_inorg_mat]

        if not isinstance(self.soluble_org_mat, list):
            self.soluble_org_mat = [self.soluble_org_mat] if self.soluble_org_mat is not None else []
        self.soluble_org_mat = [v if isinstance(v, str) else str(v) for v in self.soluble_org_mat]

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tertiary_treatment is not None and not isinstance(self.tertiary_treatment, str):
            self.tertiary_treatment = str(self.tertiary_treatment)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosphate is not None and not isinstance(self.tot_phosphate, str):
            self.tot_phosphate = str(self.tot_phosphate)

        if self.wastewater_type is not None and not isinstance(self.wastewater_type, str):
            self.wastewater_type = str(self.wastewater_type)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.biochem_oxygen_dem is not None and not isinstance(self.biochem_oxygen_dem, str):
            self.biochem_oxygen_dem = str(self.biochem_oxygen_dem)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chem_oxygen_dem is not None and not isinstance(self.chem_oxygen_dem, str):
            self.chem_oxygen_dem = str(self.chem_oxygen_dem)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, str):
            self.efficiency_percent = str(self.efficiency_percent)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if not isinstance(self.emulsions, list):
            self.emulsions = [self.emulsions] if self.emulsions is not None else []
        self.emulsions = [v if isinstance(v, str) else str(v) for v in self.emulsions]

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if not isinstance(self.gaseous_substances, list):
            self.gaseous_substances = [self.gaseous_substances] if self.gaseous_substances is not None else []
        self.gaseous_substances = [v if isinstance(v, str) else str(v) for v in self.gaseous_substances]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.indust_eff_percent is not None and not isinstance(self.indust_eff_percent, str):
            self.indust_eff_percent = str(self.indust_eff_percent)

        if not isinstance(self.inorg_particles, list):
            self.inorg_particles = [self.inorg_particles] if self.inorg_particles is not None else []
        self.inorg_particles = [v if isinstance(v, str) else str(v) for v in self.inorg_particles]

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if not isinstance(self.org_particles, list):
            self.org_particles = [self.org_particles] if self.org_particles is not None else []
        self.org_particles = [v if isinstance(v, str) else str(v) for v in self.org_particles]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.pre_treatment is not None and not isinstance(self.pre_treatment, str):
            self.pre_treatment = str(self.pre_treatment)

        if self.primary_treatment is not None and not isinstance(self.primary_treatment, str):
            self.primary_treatment = str(self.primary_treatment)

        if self.reactor_type is not None and not isinstance(self.reactor_type, str):
            self.reactor_type = str(self.reactor_type)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.secondary_treatment is not None and not isinstance(self.secondary_treatment, str):
            self.secondary_treatment = str(self.secondary_treatment)

        if self.sewage_type is not None and not isinstance(self.sewage_type, str):
            self.sewage_type = str(self.sewage_type)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sludge_retent_time is not None and not isinstance(self.sludge_retent_time, str):
            self.sludge_retent_time = str(self.sludge_retent_time)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if not isinstance(self.soluble_inorg_mat, list):
            self.soluble_inorg_mat = [self.soluble_inorg_mat] if self.soluble_inorg_mat is not None else []
        self.soluble_inorg_mat = [v if isinstance(v, str) else str(v) for v in self.soluble_inorg_mat]

        if not isinstance(self.soluble_org_mat, list):
            self.soluble_org_mat = [self.soluble_org_mat] if self.soluble_org_mat is not None else []
        self.soluble_org_mat = [v if isinstance(v, str) else str(v) for v in self.soluble_org_mat]

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, str) else str(v) for v in self.suspend_solids]

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tertiary_treatment is not None and not isinstance(self.tertiary_treatment, str):
            self.tertiary_treatment = str(self.tertiary_treatment)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosphate is not None and not isinstance(self.tot_phosphate, str):
            self.tot_phosphate = str(self.tot_phosphate)

        if self.wastewater_type is not None and not isinstance(self.wastewater_type, str):
            self.wastewater_type = str(self.wastewater_type)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class Water(DhInterface):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Water
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Water"
    class_name: ClassVar[str] = "water"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Water

    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    alt: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    atmospheric_data: Optional[Union[str, List[str]]] = empty_list()
    bac_prod: Optional[str] = None
    bac_resp: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biomass: Optional[Union[str, List[str]]] = empty_list()
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    conduc: Optional[str] = None
    density: Optional[str] = None
    depth: Optional[str] = None
    diether_lipids: Optional[Union[str, List[str]]] = empty_list()
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_nitro: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    down_par: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    elev: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    fluor: Optional[str] = None
    geo_loc_name: Optional[str] = None
    glucosidase_act: Optional[str] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    light_intensity: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    n_alkanes: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    part_org_carb: Optional[str] = None
    part_org_nitro: Optional[str] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    phaeopigments: Optional[Union[str, List[str]]] = empty_list()
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[Union[str, List[str]]] = empty_list()
    photon_flux: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    primary_prod: Optional[str] = None
    redox_potential: Optional[str] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    silicate: Optional[str] = None
    size_frac: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    sodium: Optional[str] = None
    soluble_react_phosp: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    suspend_part_matter: Optional[str] = None
    temp: Optional[str] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tot_depth_water_col: Optional[str] = None
    tot_diss_nitro: Optional[str] = None
    tot_inorg_nitro: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_part_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_current: Optional[str] = None
    carb_nitro_ratio: Optional[float] = None
    horizon_meth: Optional[str] = None
    ph_meth: Optional[str] = None
    env_package: Optional[str] = None
    sample_link: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    samp_name: Optional[str] = None
    source_mat_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if not isinstance(self.atmospheric_data, list):
            self.atmospheric_data = [self.atmospheric_data] if self.atmospheric_data is not None else []
        self.atmospheric_data = [v if isinstance(v, str) else str(v) for v in self.atmospheric_data]

        if self.bac_prod is not None and not isinstance(self.bac_prod, str):
            self.bac_prod = str(self.bac_prod)

        if self.bac_resp is not None and not isinstance(self.bac_resp, str):
            self.bac_resp = str(self.bac_resp)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, str):
            self.diss_inorg_nitro = str(self.diss_inorg_nitro)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.down_par is not None and not isinstance(self.down_par, str):
            self.down_par = str(self.down_par)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, str):
            self.part_org_nitro = str(self.part_org_nitro)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.photon_flux is not None and not isinstance(self.photon_flux, str):
            self.photon_flux = str(self.photon_flux)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.primary_prod is not None and not isinstance(self.primary_prod, str):
            self.primary_prod = str(self.primary_prod)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, str):
            self.soluble_react_phosp = str(self.soluble_react_phosp)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, str):
            self.suspend_part_matter = str(self.suspend_part_matter)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, str):
            self.tot_diss_nitro = str(self.tot_diss_nitro)

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, str):
            self.tot_inorg_nitro = str(self.tot_inorg_nitro)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, str):
            self.tot_part_carb = str(self.tot_part_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if not isinstance(self.atmospheric_data, list):
            self.atmospheric_data = [self.atmospheric_data] if self.atmospheric_data is not None else []
        self.atmospheric_data = [v if isinstance(v, str) else str(v) for v in self.atmospheric_data]

        if self.bac_prod is not None and not isinstance(self.bac_prod, str):
            self.bac_prod = str(self.bac_prod)

        if self.bac_resp is not None and not isinstance(self.bac_resp, str):
            self.bac_resp = str(self.bac_resp)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, str) else str(v) for v in self.biomass]

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, str) else str(v) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, str):
            self.diss_inorg_nitro = str(self.diss_inorg_nitro)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.down_par is not None and not isinstance(self.down_par, str):
            self.down_par = str(self.down_par)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, str) else str(v) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, str) else str(v) for v in self.organism_count]

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, RelToOxygenEnum):
            self.oxy_stat_samp = RelToOxygenEnum(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, str):
            self.part_org_nitro = str(self.part_org_nitro)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, str) else str(v) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, str) else str(v) for v in self.phosplipid_fatt_acid]

        if self.photon_flux is not None and not isinstance(self.photon_flux, str):
            self.photon_flux = str(self.photon_flux)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.primary_prod is not None and not isinstance(self.primary_prod, str):
            self.primary_prod = str(self.primary_prod)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, str):
            self.soluble_react_phosp = str(self.soluble_react_phosp)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, str):
            self.suspend_part_matter = str(self.suspend_part_matter)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, str):
            self.tot_diss_nitro = str(self.tot_diss_nitro)

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, str):
            self.tot_inorg_nitro = str(self.tot_inorg_nitro)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, str):
            self.tot_part_carb = str(self.tot_part_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Activity
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Activity

    id: Union[str, ActivityId] = None
    name: Optional[str] = None
    started_at_time: Optional[Union[str, XSDDateTime]] = None
    ended_at_time: Optional[Union[str, XSDDateTime]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None
    was_associated_with: Optional[Union[dict, "Agent"]] = None
    used: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.started_at_time is not None and not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, Agent):
            self.was_associated_with = Agent(**as_dict(self.was_associated_with))

        if self.used is not None and not isinstance(self.used, str):
            self.used = str(self.used)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Agent
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.Agent

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**as_dict(self.acted_on_behalf_of))

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        super().__post_init__(**kwargs)


@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.AttributeValue
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.AttributeValue

    has_raw_value: Optional[str] = None
    was_generated_by: Optional[Union[str, ActivityId]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityId):
            self.was_generated_by = ActivityId(self.was_generated_by)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class GeolocationValue(AttributeValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.GeolocationValue
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:GeolocationValue"
    class_name: ClassVar[str] = "GeolocationValue"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.GeolocationValue

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:TimestampValue"
    class_name: ClassVar[str] = "TimestampValue"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.TimestampValue


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.NamedThing
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class AnalysisTypeEnum(EnumDefinitionImpl):

    metabolomics = PermissibleValue(text="metabolomics")
    metagenomics = PermissibleValue(text="metagenomics")
    metaproteomics = PermissibleValue(text="metaproteomics")
    metatranscriptomics = PermissibleValue(text="metatranscriptomics")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural organic matter",
                PermissibleValue(text="natural organic matter") )

class BioticRelationshipEnum(EnumDefinitionImpl):

    parasite = PermissibleValue(text="parasite")
    commensal = PermissibleValue(text="commensal")
    symbiont = PermissibleValue(text="symbiont")

    _defn = EnumDefinition(
        name="BioticRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "free living",
                PermissibleValue(text="free living") )

class DnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="DnaContTypeEnum",
    )

class DnaDnaseEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaDnaseEnum",
    )

class DnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="DnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )

class DnaseRnaEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaseRnaEnum",
    )

class EcosystemCategoryEnum(EnumDefinitionImpl):

    Terrestrial = PermissibleValue(text="Terrestrial")

    _defn = EnumDefinition(
        name="EcosystemCategoryEnum",
    )

class EcosystemEnum(EnumDefinitionImpl):

    Environmental = PermissibleValue(text="Environmental")

    _defn = EnumDefinition(
        name="EcosystemEnum",
    )

class EcosystemSubtypeEnum(EnumDefinitionImpl):

    Biocrust = PermissibleValue(text="Biocrust")
    Biofilm = PermissibleValue(text="Biofilm")
    Clay = PermissibleValue(text="Clay")
    Floodplain = PermissibleValue(text="Floodplain")
    Fossil = PermissibleValue(text="Fossil")
    Glacier = PermissibleValue(text="Glacier")
    Loam = PermissibleValue(text="Loam")
    Pasture = PermissibleValue(text="Pasture")
    Peat = PermissibleValue(text="Peat")
    Ranch = PermissibleValue(text="Ranch")
    Sand = PermissibleValue(text="Sand")
    Silt = PermissibleValue(text="Silt")
    Unclassified = PermissibleValue(text="Unclassified")
    Watershed = PermissibleValue(text="Watershed")
    Wetlands = PermissibleValue(text="Wetlands")

    _defn = EnumDefinition(
        name="EcosystemSubtypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bulk soil",
                PermissibleValue(text="Bulk soil") )
        setattr(cls, "Mineral horizon",
                PermissibleValue(text="Mineral horizon") )
        setattr(cls, "Nature reserve",
                PermissibleValue(text="Nature reserve") )
        setattr(cls, "Organic layer",
                PermissibleValue(text="Organic layer") )
        setattr(cls, "Paddy field/soil",
                PermissibleValue(text="Paddy field/soil") )
        setattr(cls, "Soil crust",
                PermissibleValue(text="Soil crust") )

class EcosystemTypeEnum(EnumDefinitionImpl):

    Soil = PermissibleValue(text="Soil")

    _defn = EnumDefinition(
        name="EcosystemTypeEnum",
    )

class EnvBroadScaleSoilEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnvBroadScaleSoilEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "______mediterranean savanna biome [ENVO:01000229]",
                PermissibleValue(text="______mediterranean savanna biome [ENVO:01000229]") )
        setattr(cls, "____flooded savanna biome [ENVO:01000190]",
                PermissibleValue(text="____flooded savanna biome [ENVO:01000190]") )
        setattr(cls, "____mediterranean savanna biome [ENVO:01000229]",
                PermissibleValue(text="____mediterranean savanna biome [ENVO:01000229]") )
        setattr(cls, "____mediterranean shrubland biome [ENVO:01000217]",
                PermissibleValue(text="____mediterranean shrubland biome [ENVO:01000217]") )
        setattr(cls, "____mediterranean woodland biome [ENVO:01000208]",
                PermissibleValue(text="____mediterranean woodland biome [ENVO:01000208]") )
        setattr(cls, "____montane savanna biome [ENVO:01000223]",
                PermissibleValue(text="____montane savanna biome [ENVO:01000223]") )
        setattr(cls, "____subtropical savanna biome [ENVO:01000187]",
                PermissibleValue(text="____subtropical savanna biome [ENVO:01000187]") )
        setattr(cls, "____temperate savanna biome [ENVO:01000189]",
                PermissibleValue(text="____temperate savanna biome [ENVO:01000189]") )
        setattr(cls, "____tropical savanna biome [ENVO:01000188]",
                PermissibleValue(text="____tropical savanna biome [ENVO:01000188]") )
        setattr(cls, "__alpine tundra biome [ENVO:01001505]",
                PermissibleValue(text="__alpine tundra biome [ENVO:01001505]") )
        setattr(cls, "__mediterranean biome [ENVO:01001833]",
                PermissibleValue(text="__mediterranean biome [ENVO:01001833]") )
        setattr(cls, "__montane savanna biome [ENVO:01000223]",
                PermissibleValue(text="__montane savanna biome [ENVO:01000223]") )
        setattr(cls, "__montane shrubland biome [ENVO:01000216]",
                PermissibleValue(text="__montane shrubland biome [ENVO:01000216]") )
        setattr(cls, "__rangeland biome [ENVO:01000247]",
                PermissibleValue(text="__rangeland biome [ENVO:01000247]") )
        setattr(cls, "__savanna biome [ENVO:01000178]",
                PermissibleValue(text="__savanna biome [ENVO:01000178]") )
        setattr(cls, "__subtropical savanna biome [ENVO:01000187]",
                PermissibleValue(text="__subtropical savanna biome [ENVO:01000187]") )
        setattr(cls, "__subtropical shrubland biome [ENVO:01000213]",
                PermissibleValue(text="__subtropical shrubland biome [ENVO:01000213]") )
        setattr(cls, "__subtropical woodland biome [ENVO:01000222]",
                PermissibleValue(text="__subtropical woodland biome [ENVO:01000222]") )
        setattr(cls, "__temperate savanna biome [ENVO:01000189]",
                PermissibleValue(text="__temperate savanna biome [ENVO:01000189]") )
        setattr(cls, "__temperate shrubland biome [ENVO:01000215]",
                PermissibleValue(text="__temperate shrubland biome [ENVO:01000215]") )
        setattr(cls, "__temperate woodland biome [ENVO:01000221]",
                PermissibleValue(text="__temperate woodland biome [ENVO:01000221]") )
        setattr(cls, "__tropical savanna biome [ENVO:01000188]",
                PermissibleValue(text="__tropical savanna biome [ENVO:01000188]") )
        setattr(cls, "__tropical shrubland biome [ENVO:01000214]",
                PermissibleValue(text="__tropical shrubland biome [ENVO:01000214]") )
        setattr(cls, "__tropical woodland biome [ENVO:01000220]",
                PermissibleValue(text="__tropical woodland biome [ENVO:01000220]") )
        setattr(cls, "__village biome [ENVO:01000246]",
                PermissibleValue(text="__village biome [ENVO:01000246]") )
        setattr(cls, "alpine biome [ENVO:01001835]",
                PermissibleValue(text="alpine biome [ENVO:01001835]") )
        setattr(cls, "anthropogenic terrestrial biome [ENVO:01000219]",
                PermissibleValue(text="anthropogenic terrestrial biome [ENVO:01000219]") )
        setattr(cls, "arid biome [ENVO:01001838]",
                PermissibleValue(text="arid biome [ENVO:01001838]") )
        setattr(cls, "mangrove biome [ENVO:01000181]",
                PermissibleValue(text="mangrove biome [ENVO:01000181]") )
        setattr(cls, "montane biome [ENVO:01001836]",
                PermissibleValue(text="montane biome [ENVO:01001836]") )
        setattr(cls, "polar biome [ENVO:01000339]",
                PermissibleValue(text="polar biome [ENVO:01000339]") )
        setattr(cls, "shrubland biome [ENVO:01000176]",
                PermissibleValue(text="shrubland biome [ENVO:01000176]") )
        setattr(cls, "subalpine biome [ENVO:01001837]",
                PermissibleValue(text="subalpine biome [ENVO:01001837]") )
        setattr(cls, "subpolar biome [ENVO:01001834]",
                PermissibleValue(text="subpolar biome [ENVO:01001834]") )
        setattr(cls, "subtropical biome [ENVO:01001832]",
                PermissibleValue(text="subtropical biome [ENVO:01001832]") )
        setattr(cls, "temperate biome [ENVO:01001831]",
                PermissibleValue(text="temperate biome [ENVO:01001831]") )
        setattr(cls, "tropical biome [ENVO:01001830]",
                PermissibleValue(text="tropical biome [ENVO:01001830]") )
        setattr(cls, "tundra biome [ENVO:01000180]",
                PermissibleValue(text="tundra biome [ENVO:01000180]") )
        setattr(cls, "urban biome [ENVO:01000249]",
                PermissibleValue(text="urban biome [ENVO:01000249]") )
        setattr(cls, "woodland biome [ENVO:01000175]",
                PermissibleValue(text="woodland biome [ENVO:01000175]") )

class EnvLocalScaleSoilEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnvLocalScaleSoilEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "__canyon [ENVO:00000169]",
                PermissibleValue(text="__canyon [ENVO:00000169]") )
        setattr(cls, "__cliff [ENVO:00000087]",
                PermissibleValue(text="__cliff [ENVO:00000087]") )
        setattr(cls, "__dry valley [ENVO:00000128]",
                PermissibleValue(text="__dry valley [ENVO:00000128]") )
        setattr(cls, "__dune [ENVO:00000170]",
                PermissibleValue(text="__dune [ENVO:00000170]") )
        setattr(cls, "__glacial valley [ENVO:00000248]",
                PermissibleValue(text="__glacial valley [ENVO:00000248]") )
        setattr(cls, "__hillside [ENVO:01000333]",
                PermissibleValue(text="__hillside [ENVO:01000333]") )
        setattr(cls, "__tunnel [ENVO:00000068]",
                PermissibleValue(text="__tunnel [ENVO:00000068]") )
        setattr(cls, "active geological fault [ENVO:01000669]",
                PermissibleValue(text="active geological fault [ENVO:01000669]") )
        setattr(cls, "agricultural field [ENVO:00000114]",
                PermissibleValue(text="agricultural field [ENVO:00000114]") )
        setattr(cls, "beach [ENVO:00000091]",
                PermissibleValue(text="beach [ENVO:00000091]") )
        setattr(cls, "cave [ENVO:00000067]",
                PermissibleValue(text="cave [ENVO:00000067]") )
        setattr(cls, "channel [ENVO:03000117]",
                PermissibleValue(text="channel [ENVO:03000117]") )
        setattr(cls, "coast [ENVO:01000687]",
                PermissibleValue(text="coast [ENVO:01000687]") )
        setattr(cls, "dry lake [ENVO:00000277]",
                PermissibleValue(text="dry lake [ENVO:00000277]") )
        setattr(cls, "dry river [ENVO:01000995]",
                PermissibleValue(text="dry river [ENVO:01000995]") )
        setattr(cls, "garden [ENVO:00000011]",
                PermissibleValue(text="garden [ENVO:00000011]") )
        setattr(cls, "hill [ENVO:00000083]",
                PermissibleValue(text="hill [ENVO:00000083]") )
        setattr(cls, "hummock [ENVO:00000516]",
                PermissibleValue(text="hummock [ENVO:00000516]") )
        setattr(cls, "impact crater [ENVO:01001071]",
                PermissibleValue(text="impact crater [ENVO:01001071]") )
        setattr(cls, "isthmus [ENVO:00000174]",
                PermissibleValue(text="isthmus [ENVO:00000174]") )
        setattr(cls, "karst [ENVO:00000175]",
                PermissibleValue(text="karst [ENVO:00000175]") )
        setattr(cls, "lake shore [ENVO:00000382]",
                PermissibleValue(text="lake shore [ENVO:00000382]") )
        setattr(cls, "lava field [ENVO:01000437]",
                PermissibleValue(text="lava field [ENVO:01000437]") )
        setattr(cls, "mesa [ENVO:00000179]",
                PermissibleValue(text="mesa [ENVO:00000179]") )
        setattr(cls, "mountain [ENVO:00000081]",
                PermissibleValue(text="mountain [ENVO:00000081]") )
        setattr(cls, "peatland [ENVO:00000044]",
                PermissibleValue(text="peatland [ENVO:00000044]") )
        setattr(cls, "peninsula [ENVO:00000305]",
                PermissibleValue(text="peninsula [ENVO:00000305]") )
        setattr(cls, "plain [ENVO:00000086]",
                PermissibleValue(text="plain [ENVO:00000086]") )
        setattr(cls, "plateau [ENVO:00000182]",
                PermissibleValue(text="plateau [ENVO:00000182]") )
        setattr(cls, "ridge [ENVO:00000283]",
                PermissibleValue(text="ridge [ENVO:00000283]") )
        setattr(cls, "slope [ENVO:00002000]",
                PermissibleValue(text="slope [ENVO:00002000]") )
        setattr(cls, "snow field [ENVO:00000146]",
                PermissibleValue(text="snow field [ENVO:00000146]") )
        setattr(cls, "tombolo [ENVO:00000420]",
                PermissibleValue(text="tombolo [ENVO:00000420]") )
        setattr(cls, "tuff cone [ENVO:01000664]",
                PermissibleValue(text="tuff cone [ENVO:01000664]") )
        setattr(cls, "valley [ENVO:00000100]",
                PermissibleValue(text="valley [ENVO:00000100]") )
        setattr(cls, "vein [ENVO:01000670]",
                PermissibleValue(text="vein [ENVO:01000670]") )
        setattr(cls, "volcano [ENVO:00000247]",
                PermissibleValue(text="volcano [ENVO:00000247]") )
        setattr(cls, "woodland clearing [ENVO:00000444]",
                PermissibleValue(text="woodland clearing [ENVO:00000444]") )

class EnvMediumSoilEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnvMediumSoilEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "____peaty paddy field soil [ENVO:00005776]",
                PermissibleValue(text="____peaty paddy field soil [ENVO:00005776]") )
        setattr(cls, "__acrisol [ENVO:00002234]",
                PermissibleValue(text="__acrisol [ENVO:00002234]") )
        setattr(cls, "__alluvial swamp soil [ENVO:00005758]",
                PermissibleValue(text="__alluvial swamp soil [ENVO:00005758]") )
        setattr(cls, "__beech forest soil [ENVO:00005770]",
                PermissibleValue(text="__beech forest soil [ENVO:00005770]") )
        setattr(cls, "__bluegrass field soil [ENVO:00005789]",
                PermissibleValue(text="__bluegrass field soil [ENVO:00005789]") )
        setattr(cls, "__cryosol [ENVO:00002236]",
                PermissibleValue(text="__cryosol [ENVO:00002236]") )
        setattr(cls, "__eucalyptus forest soil [ENVO:00005787]",
                PermissibleValue(text="__eucalyptus forest soil [ENVO:00005787]") )
        setattr(cls, "__friable-frozen soil [ENVO:01001528]",
                PermissibleValue(text="__friable-frozen soil [ENVO:01001528]") )
        setattr(cls, "__frozen compost soil [ENVO:00005765]",
                PermissibleValue(text="__frozen compost soil [ENVO:00005765]") )
        setattr(cls, "__mountain forest soil [ENVO:00005769]",
                PermissibleValue(text="__mountain forest soil [ENVO:00005769]") )
        setattr(cls, "__paddy field soil [ENVO:00005740]",
                PermissibleValue(text="__paddy field soil [ENVO:00005740]") )
        setattr(cls, "__plastic-frozen soil [ENVO:01001527]",
                PermissibleValue(text="__plastic-frozen soil [ENVO:01001527]") )
        setattr(cls, "__rubber plantation soil [ENVO:00005788]",
                PermissibleValue(text="__rubber plantation soil [ENVO:00005788]") )
        setattr(cls, "__savanna soil [ENVO:00005746]",
                PermissibleValue(text="__savanna soil [ENVO:00005746]") )
        setattr(cls, "__steppe soil [ENVO:00005777]",
                PermissibleValue(text="__steppe soil [ENVO:00005777]") )
        setattr(cls, "__volcanic soil [ENVO:01001841]",
                PermissibleValue(text="__volcanic soil [ENVO:01001841]") )
        setattr(cls, "__xylene contaminated soil [ENVO:00002146]",
                PermissibleValue(text="__xylene contaminated soil [ENVO:00002146]") )
        setattr(cls, "agricultural soil [ENVO:00002259]",
                PermissibleValue(text="agricultural soil [ENVO:00002259]") )
        setattr(cls, "albeluvisol [ENVO:00002233]",
                PermissibleValue(text="albeluvisol [ENVO:00002233]") )
        setattr(cls, "alisol [ENVO:00002231]",
                PermissibleValue(text="alisol [ENVO:00002231]") )
        setattr(cls, "alluvial soil [ENVO:00002871]",
                PermissibleValue(text="alluvial soil [ENVO:00002871]") )
        setattr(cls, "alpine soil [ENVO:00005741]",
                PermissibleValue(text="alpine soil [ENVO:00005741]") )
        setattr(cls, "andosol [ENVO:00002232]",
                PermissibleValue(text="andosol [ENVO:00002232]") )
        setattr(cls, "anthrosol [ENVO:00002230]",
                PermissibleValue(text="anthrosol [ENVO:00002230]") )
        setattr(cls, "arenosol [ENVO:00002229]",
                PermissibleValue(text="arenosol [ENVO:00002229]") )
        setattr(cls, "bare soil [ENVO:01001616]",
                PermissibleValue(text="bare soil [ENVO:01001616]") )
        setattr(cls, "burned soil [ENVO:00005760]",
                PermissibleValue(text="burned soil [ENVO:00005760]") )
        setattr(cls, "calcisol [ENVO:00002239]",
                PermissibleValue(text="calcisol [ENVO:00002239]") )
        setattr(cls, "cambisol [ENVO:00002235]",
                PermissibleValue(text="cambisol [ENVO:00002235]") )
        setattr(cls, "carbon nanotube enriched soil [ENVO:01000427]",
                PermissibleValue(text="carbon nanotube enriched soil [ENVO:01000427]") )
        setattr(cls, "chernozem [ENVO:00002237]",
                PermissibleValue(text="chernozem [ENVO:00002237]") )
        setattr(cls, "compost soil [ENVO:00005747]",
                PermissibleValue(text="compost soil [ENVO:00005747]") )
        setattr(cls, "contaminated soil [ENVO:00002116]",
                PermissibleValue(text="contaminated soil [ENVO:00002116]") )
        setattr(cls, "dune soil [ENVO:00002260]",
                PermissibleValue(text="dune soil [ENVO:00002260]") )
        setattr(cls, "durisol [ENVO:00002238]",
                PermissibleValue(text="durisol [ENVO:00002238]") )
        setattr(cls, "ferralsol [ENVO:00002246]",
                PermissibleValue(text="ferralsol [ENVO:00002246]") )
        setattr(cls, "fluvisol [ENVO:00002273]",
                PermissibleValue(text="fluvisol [ENVO:00002273]") )
        setattr(cls, "forest soil [ENVO:00002261]",
                PermissibleValue(text="forest soil [ENVO:00002261]") )
        setattr(cls, "frost-susceptible soil [ENVO:01001638]",
                PermissibleValue(text="frost-susceptible soil [ENVO:01001638]") )
        setattr(cls, "frozen soil [ENVO:01001526]",
                PermissibleValue(text="frozen soil [ENVO:01001526]") )
        setattr(cls, "gleysol [ENVO:00002244]",
                PermissibleValue(text="gleysol [ENVO:00002244]") )
        setattr(cls, "grassland soil [ENVO:00005750]",
                PermissibleValue(text="grassland soil [ENVO:00005750]") )
        setattr(cls, "greenhouse soil [ENVO:00005780]",
                PermissibleValue(text="greenhouse soil [ENVO:00005780]") )
        setattr(cls, "gypsisol [ENVO:00002245]",
                PermissibleValue(text="gypsisol [ENVO:00002245]") )
        setattr(cls, "histosol [ENVO:00002243]",
                PermissibleValue(text="histosol [ENVO:00002243]") )
        setattr(cls, "humus-rich acidic ash soil [ENVO:00005763]",
                PermissibleValue(text="humus-rich acidic ash soil [ENVO:00005763]") )
        setattr(cls, "jungle soil [ENVO:00005751]",
                PermissibleValue(text="jungle soil [ENVO:00005751]") )
        setattr(cls, "kastanozem [ENVO:00002240]",
                PermissibleValue(text="kastanozem [ENVO:00002240]") )
        setattr(cls, "leptosol [ENVO:00002241]",
                PermissibleValue(text="leptosol [ENVO:00002241]") )
        setattr(cls, "limed soil [ENVO:00005766]",
                PermissibleValue(text="limed soil [ENVO:00005766]") )
        setattr(cls, "lixisol [ENVO:00002242]",
                PermissibleValue(text="lixisol [ENVO:00002242]") )
        setattr(cls, "loam [ENVO:00002258]",
                PermissibleValue(text="loam [ENVO:00002258]") )
        setattr(cls, "luvisol [ENVO:00002248]",
                PermissibleValue(text="luvisol [ENVO:00002248]") )
        setattr(cls, "manured soil [ENVO:00005767]",
                PermissibleValue(text="manured soil [ENVO:00005767]") )
        setattr(cls, "meadow soil [ENVO:00005761]",
                PermissibleValue(text="meadow soil [ENVO:00005761]") )
        setattr(cls, "muddy soil [ENVO:00005771]",
                PermissibleValue(text="muddy soil [ENVO:00005771]") )
        setattr(cls, "nitisol [ENVO:00002247]",
                PermissibleValue(text="nitisol [ENVO:00002247]") )
        setattr(cls, "orchard soil [ENVO:00005772]",
                PermissibleValue(text="orchard soil [ENVO:00005772]") )
        setattr(cls, "ornithogenic soil [ENVO:00005782]",
                PermissibleValue(text="ornithogenic soil [ENVO:00005782]") )
        setattr(cls, "pantothenate enriched soil [ENVO:00003088]",
                PermissibleValue(text="pantothenate enriched soil [ENVO:00003088]") )
        setattr(cls, "pasture soil [ENVO:00005773]",
                PermissibleValue(text="pasture soil [ENVO:00005773]") )
        setattr(cls, "peat soil [ENVO:00005774]",
                PermissibleValue(text="peat soil [ENVO:00005774]") )
        setattr(cls, "phaeozem [ENVO:00002249]",
                PermissibleValue(text="phaeozem [ENVO:00002249]") )
        setattr(cls, "planosol [ENVO:00002251]",
                PermissibleValue(text="planosol [ENVO:00002251]") )
        setattr(cls, "plinthosol [ENVO:00002250]",
                PermissibleValue(text="plinthosol [ENVO:00002250]") )
        setattr(cls, "podzol [ENVO:00002257]",
                PermissibleValue(text="podzol [ENVO:00002257]") )
        setattr(cls, "poly-beta-hydroxybutyrate enriched soil [ENVO:00003093]",
                PermissibleValue(text="poly-beta-hydroxybutyrate enriched soil [ENVO:00003093]") )
        setattr(cls, "pond soil [ENVO:00005764]",
                PermissibleValue(text="pond soil [ENVO:00005764]") )
        setattr(cls, "quinate enriched soil [ENVO:00003095]",
                PermissibleValue(text="quinate enriched soil [ENVO:00003095]") )
        setattr(cls, "regosol [ENVO:00002256]",
                PermissibleValue(text="regosol [ENVO:00002256]") )
        setattr(cls, "sarcosine enriched soil [ENVO:00003083]",
                PermissibleValue(text="sarcosine enriched soil [ENVO:00003083]") )
        setattr(cls, "skatole enriched soil [ENVO:00003085]",
                PermissibleValue(text="skatole enriched soil [ENVO:00003085]") )
        setattr(cls, "solonchak [ENVO:00002252]",
                PermissibleValue(text="solonchak [ENVO:00002252]") )
        setattr(cls, "solonetz [ENVO:00002255]",
                PermissibleValue(text="solonetz [ENVO:00002255]") )
        setattr(cls, "stagnosol [ENVO:00002274]",
                PermissibleValue(text="stagnosol [ENVO:00002274]") )
        setattr(cls, "surface soil [ENVO:02000059]",
                PermissibleValue(text="surface soil [ENVO:02000059]") )
        setattr(cls, "technosol [ENVO:00002275]",
                PermissibleValue(text="technosol [ENVO:00002275]") )
        setattr(cls, "threonine enriched soil [ENVO:00003091]",
                PermissibleValue(text="threonine enriched soil [ENVO:00003091]") )
        setattr(cls, "trimethylamine enriched soil [ENVO:00003084]",
                PermissibleValue(text="trimethylamine enriched soil [ENVO:00003084]") )
        setattr(cls, "tropical soil [ENVO:00005778]",
                PermissibleValue(text="tropical soil [ENVO:00005778]") )
        setattr(cls, "ultisol [ENVO:01001397]",
                PermissibleValue(text="ultisol [ENVO:01001397]") )
        setattr(cls, "umbrisol [ENVO:00002253]",
                PermissibleValue(text="umbrisol [ENVO:00002253]") )
        setattr(cls, "upland soil [ENVO:00005786]",
                PermissibleValue(text="upland soil [ENVO:00005786]") )
        setattr(cls, "urea enriched soil [ENVO:00005753]",
                PermissibleValue(text="urea enriched soil [ENVO:00005753]") )
        setattr(cls, "vertisol [ENVO:00002254]",
                PermissibleValue(text="vertisol [ENVO:00002254]") )

class EnvPackageEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")

    _defn = EnumDefinition(
        name="EnvPackageEnum",
    )

class GrowthFacilEnum(EnumDefinitionImpl):

    experimental_garden = PermissibleValue(text="experimental_garden")
    field = PermissibleValue(text="field")
    field_incubation = PermissibleValue(text="field_incubation")
    glasshouse = PermissibleValue(text="glasshouse")
    greenhouse = PermissibleValue(text="greenhouse")
    growth_chamber = PermissibleValue(text="growth_chamber")
    lab_incubation = PermissibleValue(text="lab_incubation")
    open_top_chamber = PermissibleValue(text="open_top_chamber")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="GrowthFacilEnum",
    )

class RelToOxygenEnum(EnumDefinitionImpl):

    aerobe = PermissibleValue(text="aerobe")
    anaerobe = PermissibleValue(text="anaerobe")
    facultative = PermissibleValue(text="facultative")
    microaerophilic = PermissibleValue(text="microaerophilic")
    microanaerobe = PermissibleValue(text="microanaerobe")

    _defn = EnumDefinition(
        name="RelToOxygenEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "obligate aerobe",
                PermissibleValue(text="obligate aerobe") )
        setattr(cls, "obligate anaerobe",
                PermissibleValue(text="obligate anaerobe") )

class RnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="RnaContTypeEnum",
    )

class RnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="RnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )

class SampleTypeEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")
    water_extract_soil = PermissibleValue(text="water_extract_soil")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
    )

class SpecificEcosystemEnum(EnumDefinitionImpl):

    Agricultural = PermissibleValue(text="Agricultural")
    Alpine = PermissibleValue(text="Alpine")
    Bog = PermissibleValue(text="Bog")
    Contaminated = PermissibleValue(text="Contaminated")
    Desert = PermissibleValue(text="Desert")
    Farm = PermissibleValue(text="Farm")
    Grasslands = PermissibleValue(text="Grasslands")
    Meadow = PermissibleValue(text="Meadow")
    Mine = PermissibleValue(text="Mine")
    Permafrost = PermissibleValue(text="Permafrost")
    River = PermissibleValue(text="River")
    Shrubland = PermissibleValue(text="Shrubland")
    Unclassified = PermissibleValue(text="Unclassified")

    _defn = EnumDefinition(
        name="SpecificEcosystemEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Agricultural land",
                PermissibleValue(text="Agricultural land") )
        setattr(cls, "Agricultural soil",
                PermissibleValue(text="Agricultural soil") )
        setattr(cls, "Boreal forest",
                PermissibleValue(text="Boreal forest") )
        setattr(cls, "Forest Soil",
                PermissibleValue(text="Forest Soil") )
        setattr(cls, "Forest soil",
                PermissibleValue(text="Forest soil") )
        setattr(cls, "Mine drainage",
                PermissibleValue(text="Mine drainage") )
        setattr(cls, "Oil-contaminated",
                PermissibleValue(text="Oil-contaminated") )
        setattr(cls, "Orchard soil",
                PermissibleValue(text="Orchard soil") )
        setattr(cls, "Riparian soil",
                PermissibleValue(text="Riparian soil") )
        setattr(cls, "Tropical rainforest",
                PermissibleValue(text="Tropical rainforest") )
        setattr(cls, "Uranium contaminated",
                PermissibleValue(text="Uranium contaminated") )

class StoreCondEnum(EnumDefinitionImpl):

    fresh = PermissibleValue(text="fresh")
    frozen = PermissibleValue(text="frozen")
    lyophilized = PermissibleValue(text="lyophilized")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="StoreCondEnum",
    )

class FilterTypeEnum(EnumDefinitionImpl):

    HEPA = PermissibleValue(text="HEPA")
    electrostatic = PermissibleValue(text="electrostatic")

    _defn = EnumDefinition(
        name="FilterTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "particulate air filter",
                PermissibleValue(text="particulate air filter") )
        setattr(cls, "chemical air filter",
                PermissibleValue(text="chemical air filter") )
        setattr(cls, "low-MERV pleated media",
                PermissibleValue(text="low-MERV pleated media") )
        setattr(cls, "gas-phase or ultraviolet air treatments",
                PermissibleValue(text="gas-phase or ultraviolet air treatments") )

class WallSurfTreatmentEnum(EnumDefinitionImpl):

    painted = PermissibleValue(text="painted")
    paneling = PermissibleValue(text="paneling")
    stucco = PermissibleValue(text="stucco")
    fabric = PermissibleValue(text="fabric")

    _defn = EnumDefinition(
        name="WallSurfTreatmentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "wall paper",
                PermissibleValue(text="wall paper") )
        setattr(cls, "no treatment",
                PermissibleValue(text="no treatment") )

class WindowTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WindowTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-hung sash window",
                PermissibleValue(text="single-hung sash window") )
        setattr(cls, "horizontal sash window",
                PermissibleValue(text="horizontal sash window") )
        setattr(cls, "fixed window",
                PermissibleValue(text="fixed window") )

class SpecificEnum(EnumDefinitionImpl):

    operation = PermissibleValue(text="operation")
    construction = PermissibleValue(text="construction")
    bid = PermissibleValue(text="bid")
    design = PermissibleValue(text="design")
    photos = PermissibleValue(text="photos")

    _defn = EnumDefinition(
        name="SpecificEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as built",
                PermissibleValue(text="as built") )

class WallConstTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WallConstTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "frame construction",
                PermissibleValue(text="frame construction") )
        setattr(cls, "joisted masonry",
                PermissibleValue(text="joisted masonry") )
        setattr(cls, "light noncombustible",
                PermissibleValue(text="light noncombustible") )
        setattr(cls, "masonry noncombustible",
                PermissibleValue(text="masonry noncombustible") )
        setattr(cls, "modified fire resistive",
                PermissibleValue(text="modified fire resistive") )
        setattr(cls, "fire resistive",
                PermissibleValue(text="fire resistive") )

class WindowVertPosEnum(EnumDefinitionImpl):

    bottom = PermissibleValue(text="bottom")
    middle = PermissibleValue(text="middle")
    top = PermissibleValue(text="top")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="WindowVertPosEnum",
    )

class IndoorSurfEnum(EnumDefinitionImpl):

    cabinet = PermissibleValue(text="cabinet")
    ceiling = PermissibleValue(text="ceiling")
    door = PermissibleValue(text="door")
    shelving = PermissibleValue(text="shelving")
    window = PermissibleValue(text="window")
    wall = PermissibleValue(text="wall")

    _defn = EnumDefinition(
        name="IndoorSurfEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "counter top",
                PermissibleValue(text="counter top") )
        setattr(cls, "vent cover",
                PermissibleValue(text="vent cover") )

class CeilTextureEnum(EnumDefinitionImpl):

    knockdown = PermissibleValue(text="knockdown")
    popcorn = PermissibleValue(text="popcorn")
    smooth = PermissibleValue(text="smooth")
    swirl = PermissibleValue(text="swirl")

    _defn = EnumDefinition(
        name="CeilTextureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crows feet",
                PermissibleValue(text="crows feet") )
        setattr(cls, "crows-foot stomp",
                PermissibleValue(text="crows-foot stomp") )
        setattr(cls, "double skip",
                PermissibleValue(text="double skip") )
        setattr(cls, "hawk and trowel",
                PermissibleValue(text="hawk and trowel") )
        setattr(cls, "orange peel",
                PermissibleValue(text="orange peel") )
        setattr(cls, "rosebud stomp",
                PermissibleValue(text="rosebud stomp") )
        setattr(cls, "Santa-Fe texture",
                PermissibleValue(text="Santa-Fe texture") )
        setattr(cls, "skip trowel",
                PermissibleValue(text="skip trowel") )
        setattr(cls, "stomp knockdown",
                PermissibleValue(text="stomp knockdown") )

class TrainStopLocEnum(EnumDefinitionImpl):

    end = PermissibleValue(text="end")
    mid = PermissibleValue(text="mid")
    downtown = PermissibleValue(text="downtown")

    _defn = EnumDefinition(
        name="TrainStopLocEnum",
    )

class TrainLineEnum(EnumDefinitionImpl):

    red = PermissibleValue(text="red")
    green = PermissibleValue(text="green")
    orange = PermissibleValue(text="orange")

    _defn = EnumDefinition(
        name="TrainLineEnum",
    )

class RoomLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RoomLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "corner room",
                PermissibleValue(text="corner room") )
        setattr(cls, "interior room",
                PermissibleValue(text="interior room") )
        setattr(cls, "exterior wall",
                PermissibleValue(text="exterior wall") )

class ShadingDeviceTypeEnum(EnumDefinitionImpl):

    tree = PermissibleValue(text="tree")
    trellis = PermissibleValue(text="trellis")

    _defn = EnumDefinition(
        name="ShadingDeviceTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bahama shutters",
                PermissibleValue(text="bahama shutters") )
        setattr(cls, "exterior roll blind",
                PermissibleValue(text="exterior roll blind") )
        setattr(cls, "gambrel awning",
                PermissibleValue(text="gambrel awning") )
        setattr(cls, "hood awning",
                PermissibleValue(text="hood awning") )
        setattr(cls, "porchroller awning",
                PermissibleValue(text="porchroller awning") )
        setattr(cls, "sarasota shutters",
                PermissibleValue(text="sarasota shutters") )
        setattr(cls, "slatted aluminum",
                PermissibleValue(text="slatted aluminum") )
        setattr(cls, "solid aluminum awning",
                PermissibleValue(text="solid aluminum awning") )
        setattr(cls, "sun screen",
                PermissibleValue(text="sun screen") )
        setattr(cls, "venetian awning",
                PermissibleValue(text="venetian awning") )

class HandidnessEnum(EnumDefinitionImpl):

    ambidexterity = PermissibleValue(text="ambidexterity")

    _defn = EnumDefinition(
        name="HandidnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "left handedness",
                PermissibleValue(text="left handedness") )
        setattr(cls, "mixed-handedness",
                PermissibleValue(text="mixed-handedness") )
        setattr(cls, "right handedness",
                PermissibleValue(text="right handedness") )

class SampFloorEnum(EnumDefinitionImpl):

    basement = PermissibleValue(text="basement")
    lobby = PermissibleValue(text="lobby")

    _defn = EnumDefinition(
        name="SampFloorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1st floor",
                PermissibleValue(text="1st floor") )
        setattr(cls, "2nd floor",
                PermissibleValue(text="2nd floor") )

class WindowCoverEnum(EnumDefinitionImpl):

    blinds = PermissibleValue(text="blinds")
    curtains = PermissibleValue(text="curtains")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="WindowCoverEnum",
    )

class SampWeatherEnum(EnumDefinitionImpl):

    cloudy = PermissibleValue(text="cloudy")
    foggy = PermissibleValue(text="foggy")
    hail = PermissibleValue(text="hail")
    rain = PermissibleValue(text="rain")
    snow = PermissibleValue(text="snow")
    sleet = PermissibleValue(text="sleet")
    sunny = PermissibleValue(text="sunny")
    windy = PermissibleValue(text="windy")

    _defn = EnumDefinition(
        name="SampWeatherEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "clear sky",
                PermissibleValue(text="clear sky") )

class ShadingDeviceCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="ShadingDeviceCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class TrainStatLocEnum(EnumDefinitionImpl):

    riverside = PermissibleValue(text="riverside")

    _defn = EnumDefinition(
        name="TrainStatLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "south station above ground",
                PermissibleValue(text="south station above ground") )
        setattr(cls, "south station underground",
                PermissibleValue(text="south station underground") )
        setattr(cls, "south station amtrak",
                PermissibleValue(text="south station amtrak") )
        setattr(cls, "forest hills",
                PermissibleValue(text="forest hills") )

class SeasonUseEnum(EnumDefinitionImpl):

    Spring = PermissibleValue(text="Spring")
    Summer = PermissibleValue(text="Summer")
    Fall = PermissibleValue(text="Fall")
    Winter = PermissibleValue(text="Winter")

    _defn = EnumDefinition(
        name="SeasonUseEnum",
    )

class WindowMatEnum(EnumDefinitionImpl):

    clad = PermissibleValue(text="clad")
    fiberglass = PermissibleValue(text="fiberglass")
    metal = PermissibleValue(text="metal")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="WindowMatEnum",
    )

class HeatDelivLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="HeatDelivLocEnum",
    )

class QuadPosEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="QuadPosEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "North side",
                PermissibleValue(text="North side") )
        setattr(cls, "West side",
                PermissibleValue(text="West side") )
        setattr(cls, "South side",
                PermissibleValue(text="South side") )
        setattr(cls, "East side",
                PermissibleValue(text="East side") )

class MechStrucEnum(EnumDefinitionImpl):

    subway = PermissibleValue(text="subway")
    coach = PermissibleValue(text="coach")
    carriage = PermissibleValue(text="carriage")
    elevator = PermissibleValue(text="elevator")
    escalator = PermissibleValue(text="escalator")
    boat = PermissibleValue(text="boat")
    train = PermissibleValue(text="train")
    car = PermissibleValue(text="car")
    bus = PermissibleValue(text="bus")

    _defn = EnumDefinition(
        name="MechStrucEnum",
    )

class ExtWindowOrientEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")
    northeast = PermissibleValue(text="northeast")
    southeast = PermissibleValue(text="southeast")
    southwest = PermissibleValue(text="southwest")
    northwest = PermissibleValue(text="northwest")

    _defn = EnumDefinition(
        name="ExtWindowOrientEnum",
    )

class DoorTypeWoodEnum(EnumDefinitionImpl):

    battened = PermissibleValue(text="battened")
    flush = PermissibleValue(text="flush")
    louvered = PermissibleValue(text="louvered")

    _defn = EnumDefinition(
        name="DoorTypeWoodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bettened and ledged",
                PermissibleValue(text="bettened and ledged") )
        setattr(cls, "ledged and braced",
                PermissibleValue(text="ledged and braced") )
        setattr(cls, "ledged and framed",
                PermissibleValue(text="ledged and framed") )
        setattr(cls, "ledged, braced and frame",
                PermissibleValue(text="ledged, braced and frame") )
        setattr(cls, "framed and paneled",
                PermissibleValue(text="framed and paneled") )
        setattr(cls, "glashed or sash",
                PermissibleValue(text="glashed or sash") )
        setattr(cls, "wire gauged",
                PermissibleValue(text="wire gauged") )

class BuildOccupTypeEnum(EnumDefinitionImpl):

    office = PermissibleValue(text="office")
    market = PermissibleValue(text="market")
    restaurant = PermissibleValue(text="restaurant")
    residence = PermissibleValue(text="residence")
    school = PermissibleValue(text="school")
    residential = PermissibleValue(text="residential")
    commercial = PermissibleValue(text="commercial")
    airport = PermissibleValue(text="airport")

    _defn = EnumDefinition(
        name="BuildOccupTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low rise",
                PermissibleValue(text="low rise") )
        setattr(cls, "high rise",
                PermissibleValue(text="high rise") )
        setattr(cls, "wood framed",
                PermissibleValue(text="wood framed") )
        setattr(cls, "health care",
                PermissibleValue(text="health care") )
        setattr(cls, "sports complex",
                PermissibleValue(text="sports complex") )

class DoorMatEnum(EnumDefinitionImpl):

    aluminum = PermissibleValue(text="aluminum")
    fiberboard = PermissibleValue(text="fiberboard")
    fiberglass = PermissibleValue(text="fiberglass")
    metal = PermissibleValue(text="metal")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="DoorMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cellular PVC",
                PermissibleValue(text="cellular PVC") )
        setattr(cls, "engineered plastic",
                PermissibleValue(text="engineered plastic") )
        setattr(cls, "thermoplastic alloy",
                PermissibleValue(text="thermoplastic alloy") )
        setattr(cls, "wood/plastic composite",
                PermissibleValue(text="wood/plastic composite") )

class GenderRestroomEnum(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    male = PermissibleValue(text="male")
    unisex = PermissibleValue(text="unisex")

    _defn = EnumDefinition(
        name="GenderRestroomEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "all gender",
                PermissibleValue(text="all gender") )
        setattr(cls, "gender neurtral",
                PermissibleValue(text="gender neurtral") )
        setattr(cls, "male and female",
                PermissibleValue(text="male and female") )

class SurfMaterialEnum(EnumDefinitionImpl):

    adobe = PermissibleValue(text="adobe")
    carpet = PermissibleValue(text="carpet")
    concrete = PermissibleValue(text="concrete")
    glass = PermissibleValue(text="glass")
    metal = PermissibleValue(text="metal")
    paint = PermissibleValue(text="paint")
    plastic = PermissibleValue(text="plastic")
    stone = PermissibleValue(text="stone")
    stucco = PermissibleValue(text="stucco")
    tile = PermissibleValue(text="tile")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="SurfMaterialEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cinder blocks",
                PermissibleValue(text="cinder blocks") )
        setattr(cls, "hay bales",
                PermissibleValue(text="hay bales") )
        setattr(cls, "stainless steel",
                PermissibleValue(text="stainless steel") )

class WallTextureEnum(EnumDefinitionImpl):

    knockdown = PermissibleValue(text="knockdown")
    popcorn = PermissibleValue(text="popcorn")
    smooth = PermissibleValue(text="smooth")
    swirl = PermissibleValue(text="swirl")

    _defn = EnumDefinition(
        name="WallTextureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crows feet",
                PermissibleValue(text="crows feet") )
        setattr(cls, "crows-foot stomp",
                PermissibleValue(text="crows-foot stomp") )
        setattr(cls, "",
                PermissibleValue(text="") )
        setattr(cls, "double skip",
                PermissibleValue(text="double skip") )
        setattr(cls, "hawk and trowel",
                PermissibleValue(text="hawk and trowel") )
        setattr(cls, "orange peel",
                PermissibleValue(text="orange peel") )
        setattr(cls, "rosebud stomp",
                PermissibleValue(text="rosebud stomp") )
        setattr(cls, "Santa-Fe texture",
                PermissibleValue(text="Santa-Fe texture") )
        setattr(cls, "skip trowel",
                PermissibleValue(text="skip trowel") )
        setattr(cls, "stomp knockdown",
                PermissibleValue(text="stomp knockdown") )

class CeilFinishMatEnum(EnumDefinitionImpl):

    drywall = PermissibleValue(text="drywall")
    tiles = PermissibleValue(text="tiles")
    PVC = PermissibleValue(text="PVC")
    plasterboard = PermissibleValue(text="plasterboard")
    metal = PermissibleValue(text="metal")
    fiberglass = PermissibleValue(text="fiberglass")
    stucco = PermissibleValue(text="stucco")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="CeilFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mineral fibre",
                PermissibleValue(text="mineral fibre") )
        setattr(cls, "mineral wool/calcium silicate",
                PermissibleValue(text="mineral wool/calcium silicate") )

class DoorCompTypeEnum(EnumDefinitionImpl):

    revolving = PermissibleValue(text="revolving")
    sliding = PermissibleValue(text="sliding")
    telescopic = PermissibleValue(text="telescopic")

    _defn = EnumDefinition(
        name="DoorCompTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "metal covered",
                PermissibleValue(text="metal covered") )

class DrawingsEnum(EnumDefinitionImpl):

    operation = PermissibleValue(text="operation")
    construction = PermissibleValue(text="construction")
    bid = PermissibleValue(text="bid")
    design = PermissibleValue(text="design")
    diagram = PermissibleValue(text="diagram")
    sketch = PermissibleValue(text="sketch")

    _defn = EnumDefinition(
        name="DrawingsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as built",
                PermissibleValue(text="as built") )
        setattr(cls, "building navigation map",
                PermissibleValue(text="building navigation map") )

class RoomConnectedEnum(EnumDefinitionImpl):

    attic = PermissibleValue(text="attic")
    bathroom = PermissibleValue(text="bathroom")
    closet = PermissibleValue(text="closet")
    elevator = PermissibleValue(text="elevator")
    hallway = PermissibleValue(text="hallway")
    kitchen = PermissibleValue(text="kitchen")
    office = PermissibleValue(text="office")
    stairwell = PermissibleValue(text="stairwell")

    _defn = EnumDefinition(
        name="RoomConnectedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "conference room",
                PermissibleValue(text="conference room") )
        setattr(cls, "examining room",
                PermissibleValue(text="examining room") )
        setattr(cls, "mail room",
                PermissibleValue(text="mail room") )

class WindowLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WindowLocEnum",
    )

class IndoorSpaceEnum(EnumDefinitionImpl):

    bedroom = PermissibleValue(text="bedroom")
    office = PermissibleValue(text="office")
    bathroom = PermissibleValue(text="bathroom")
    foyer = PermissibleValue(text="foyer")
    kitchen = PermissibleValue(text="kitchen")
    hallway = PermissibleValue(text="hallway")
    elevator = PermissibleValue(text="elevator")

    _defn = EnumDefinition(
        name="IndoorSpaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "locker room",
                PermissibleValue(text="locker room") )

class DoorLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="DoorLocEnum",
    )

class WallLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WallLocEnum",
    )

class LightTypeEnum(EnumDefinitionImpl):

    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="LightTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural light",
                PermissibleValue(text="natural light") )
        setattr(cls, "electric light",
                PermissibleValue(text="electric light") )
        setattr(cls, "desk lamp",
                PermissibleValue(text="desk lamp") )
        setattr(cls, "flourescent lights",
                PermissibleValue(text="flourescent lights") )

class DoorDirectEnum(EnumDefinitionImpl):

    inward = PermissibleValue(text="inward")
    outward = PermissibleValue(text="outward")
    sideways = PermissibleValue(text="sideways")

    _defn = EnumDefinition(
        name="DoorDirectEnum",
    )

class OccupDocumentEnum(EnumDefinitionImpl):

    estimate = PermissibleValue(text="estimate")
    videos = PermissibleValue(text="videos")

    _defn = EnumDefinition(
        name="OccupDocumentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "automated count",
                PermissibleValue(text="automated count") )
        setattr(cls, "manual count",
                PermissibleValue(text="manual count") )

class CeilTypeEnum(EnumDefinitionImpl):

    cathedral = PermissibleValue(text="cathedral")
    dropped = PermissibleValue(text="dropped")
    concave = PermissibleValue(text="concave")
    coffered = PermissibleValue(text="coffered")
    cove = PermissibleValue(text="cove")
    stretched = PermissibleValue(text="stretched")

    _defn = EnumDefinition(
        name="CeilTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "barrel-shaped",
                PermissibleValue(text="barrel-shaped") )

class RoomSampPosEnum(EnumDefinitionImpl):

    center = PermissibleValue(text="center")

    _defn = EnumDefinition(
        name="RoomSampPosEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "north corner",
                PermissibleValue(text="north corner") )
        setattr(cls, "south corner",
                PermissibleValue(text="south corner") )
        setattr(cls, "west corner",
                PermissibleValue(text="west corner") )
        setattr(cls, "east corner",
                PermissibleValue(text="east corner") )
        setattr(cls, "northeast corner",
                PermissibleValue(text="northeast corner") )
        setattr(cls, "northwest corner",
                PermissibleValue(text="northwest corner") )
        setattr(cls, "southeast corner",
                PermissibleValue(text="southeast corner") )
        setattr(cls, "southwest corner",
                PermissibleValue(text="southwest corner") )

class WaterFeatTypeEnum(EnumDefinitionImpl):

    fountain = PermissibleValue(text="fountain")
    pool = PermissibleValue(text="pool")
    stream = PermissibleValue(text="stream")
    waterfall = PermissibleValue(text="waterfall")

    _defn = EnumDefinition(
        name="WaterFeatTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "standing feature",
                PermissibleValue(text="standing feature") )

class IntWallCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="IntWallCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class FloorWaterMoldEnum(EnumDefinitionImpl):

    condensation = PermissibleValue(text="condensation")

    _defn = EnumDefinition(
        name="FloorWaterMoldEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mold odor",
                PermissibleValue(text="mold odor") )
        setattr(cls, "wet floor",
                PermissibleValue(text="wet floor") )
        setattr(cls, "water stains",
                PermissibleValue(text="water stains") )
        setattr(cls, "wall discoloration",
                PermissibleValue(text="wall discoloration") )
        setattr(cls, "floor discoloration",
                PermissibleValue(text="floor discoloration") )
        setattr(cls, "ceiling discoloration",
                PermissibleValue(text="ceiling discoloration") )
        setattr(cls, "peeling paint or wallpaper",
                PermissibleValue(text="peeling paint or wallpaper") )
        setattr(cls, "bulging walls",
                PermissibleValue(text="bulging walls") )

class CeilCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="CeilCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class DoorCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="DoorCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class FurnitureEnum(EnumDefinitionImpl):

    cabinet = PermissibleValue(text="cabinet")
    chair = PermissibleValue(text="chair")
    desks = PermissibleValue(text="desks")

    _defn = EnumDefinition(
        name="FurnitureEnum",
    )

class FloorStrucEnum(EnumDefinitionImpl):

    balcony = PermissibleValue(text="balcony")
    concrete = PermissibleValue(text="concrete")

    _defn = EnumDefinition(
        name="FloorStrucEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "floating floor",
                PermissibleValue(text="floating floor") )
        setattr(cls, "glass floor",
                PermissibleValue(text="glass floor") )
        setattr(cls, "raised floor",
                PermissibleValue(text="raised floor") )
        setattr(cls, "sprung floor",
                PermissibleValue(text="sprung floor") )
        setattr(cls, "wood-framed",
                PermissibleValue(text="wood-framed") )

class WindowHorizPosEnum(EnumDefinitionImpl):

    left = PermissibleValue(text="left")
    middle = PermissibleValue(text="middle")
    right = PermissibleValue(text="right")

    _defn = EnumDefinition(
        name="WindowHorizPosEnum",
    )

class DoorTypeMetalEnum(EnumDefinitionImpl):

    collapsible = PermissibleValue(text="collapsible")
    hollow = PermissibleValue(text="hollow")

    _defn = EnumDefinition(
        name="DoorTypeMetalEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "corrugated steel",
                PermissibleValue(text="corrugated steel") )
        setattr(cls, "rolling shutters",
                PermissibleValue(text="rolling shutters") )
        setattr(cls, "steel plate",
                PermissibleValue(text="steel plate") )

class BuildDocsEnum(EnumDefinitionImpl):

    schedule = PermissibleValue(text="schedule")
    sections = PermissibleValue(text="sections")
    submittals = PermissibleValue(text="submittals")
    windows = PermissibleValue(text="windows")

    _defn = EnumDefinition(
        name="BuildDocsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "building information model",
                PermissibleValue(text="building information model") )
        setattr(cls, "commissioning report",
                PermissibleValue(text="commissioning report") )
        setattr(cls, "complaint logs",
                PermissibleValue(text="complaint logs") )
        setattr(cls, "contract administration",
                PermissibleValue(text="contract administration") )
        setattr(cls, "cost estimate",
                PermissibleValue(text="cost estimate") )
        setattr(cls, "janitorial schedules or logs",
                PermissibleValue(text="janitorial schedules or logs") )
        setattr(cls, "maintenance plans",
                PermissibleValue(text="maintenance plans") )
        setattr(cls, "shop drawings",
                PermissibleValue(text="shop drawings") )
        setattr(cls, "ventilation system",
                PermissibleValue(text="ventilation system") )

class SubstructureTypeEnum(EnumDefinitionImpl):

    crawlspace = PermissibleValue(text="crawlspace")
    basement = PermissibleValue(text="basement")

    _defn = EnumDefinition(
        name="SubstructureTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "slab on grade",
                PermissibleValue(text="slab on grade") )

class WallFinishMatEnum(EnumDefinitionImpl):

    plaster = PermissibleValue(text="plaster")
    tile = PermissibleValue(text="tile")
    terrazzo = PermissibleValue(text="terrazzo")
    wood = PermissibleValue(text="wood")
    metal = PermissibleValue(text="metal")
    masonry = PermissibleValue(text="masonry")

    _defn = EnumDefinition(
        name="WallFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gypsum plaster",
                PermissibleValue(text="gypsum plaster") )
        setattr(cls, "veneer plaster",
                PermissibleValue(text="veneer plaster") )
        setattr(cls, "gypsum board",
                PermissibleValue(text="gypsum board") )
        setattr(cls, "stone facing",
                PermissibleValue(text="stone facing") )
        setattr(cls, "acoustical treatment",
                PermissibleValue(text="acoustical treatment") )

class RelSampLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RelSampLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "edge of car",
                PermissibleValue(text="edge of car") )
        setattr(cls, "center of car",
                PermissibleValue(text="center of car") )
        setattr(cls, "under a seat",
                PermissibleValue(text="under a seat") )

class ExtWallOrientEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")
    northeast = PermissibleValue(text="northeast")
    southeast = PermissibleValue(text="southeast")
    southwest = PermissibleValue(text="southwest")
    northwest = PermissibleValue(text="northwest")

    _defn = EnumDefinition(
        name="ExtWallOrientEnum",
    )

class HeatCoolTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HeatCoolTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "radiant system",
                PermissibleValue(text="radiant system") )
        setattr(cls, "heat pump",
                PermissibleValue(text="heat pump") )
        setattr(cls, "forced air system",
                PermissibleValue(text="forced air system") )
        setattr(cls, "steam forced heat",
                PermissibleValue(text="steam forced heat") )
        setattr(cls, "wood stove",
                PermissibleValue(text="wood stove") )

class SurfAirContEnum(EnumDefinitionImpl):

    dust = PermissibleValue(text="dust")
    radon = PermissibleValue(text="radon")
    nutrients = PermissibleValue(text="nutrients")
    biocides = PermissibleValue(text="biocides")

    _defn = EnumDefinition(
        name="SurfAirContEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "organic matter",
                PermissibleValue(text="organic matter") )
        setattr(cls, "particulate matter",
                PermissibleValue(text="particulate matter") )
        setattr(cls, "volatile organic compounds",
                PermissibleValue(text="volatile organic compounds") )
        setattr(cls, "biological contaminants",
                PermissibleValue(text="biological contaminants") )

class FloorFinishMatEnum(EnumDefinitionImpl):

    tile = PermissibleValue(text="tile")
    carpet = PermissibleValue(text="carpet")
    rug = PermissibleValue(text="rug")
    lineoleum = PermissibleValue(text="lineoleum")
    stone = PermissibleValue(text="stone")
    bamboo = PermissibleValue(text="bamboo")
    cork = PermissibleValue(text="cork")
    terrazo = PermissibleValue(text="terrazo")
    concrete = PermissibleValue(text="concrete")
    none = PermissibleValue(text="none")
    sealed = PermissibleValue(text="sealed")
    paint = PermissibleValue(text="paint")

    _defn = EnumDefinition(
        name="FloorFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "wood strip or parquet",
                PermissibleValue(text="wood strip or parquet") )
        setattr(cls, "laminate wood",
                PermissibleValue(text="laminate wood") )
        setattr(cls, "vinyl composition tile",
                PermissibleValue(text="vinyl composition tile") )
        setattr(cls, "sheet vinyl",
                PermissibleValue(text="sheet vinyl") )
        setattr(cls, "clear finish",
                PermissibleValue(text="clear finish") )
        setattr(cls, "none or unfinished",
                PermissibleValue(text="none or unfinished") )

class VisMediaEnum(EnumDefinitionImpl):

    photos = PermissibleValue(text="photos")
    videos = PermissibleValue(text="videos")
    interiors = PermissibleValue(text="interiors")
    equipment = PermissibleValue(text="equipment")

    _defn = EnumDefinition(
        name="VisMediaEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "commonly of the building",
                PermissibleValue(text="commonly of the building") )
        setattr(cls, "site context (adjacent buildings, vegetation, terrain, streets)",
                PermissibleValue(text="site context (adjacent buildings, vegetation, terrain, streets)") )
        setattr(cls, "3D scans",
                PermissibleValue(text="3D scans") )

class RoomCondtEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="RoomCondtEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible signs of mold/mildew",
                PermissibleValue(text="visible signs of mold/mildew") )

class BuildingSettingEnum(EnumDefinitionImpl):

    urban = PermissibleValue(text="urban")
    suburban = PermissibleValue(text="suburban")
    exurban = PermissibleValue(text="exurban")
    rural = PermissibleValue(text="rural")

    _defn = EnumDefinition(
        name="BuildingSettingEnum",
    )

class WindowCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="WindowCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class ArchStrucEnum(EnumDefinitionImpl):

    building = PermissibleValue(text="building")
    shed = PermissibleValue(text="shed")
    home = PermissibleValue(text="home")

    _defn = EnumDefinition(
        name="ArchStrucEnum",
    )

class FloorCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="FloorCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class WeekdayEnum(EnumDefinitionImpl):

    Monday = PermissibleValue(text="Monday")
    Tuesday = PermissibleValue(text="Tuesday")
    Wednesday = PermissibleValue(text="Wednesday")
    Thursday = PermissibleValue(text="Thursday")
    Friday = PermissibleValue(text="Friday")
    Saturday = PermissibleValue(text="Saturday")
    Sunday = PermissibleValue(text="Sunday")

    _defn = EnumDefinition(
        name="WeekdayEnum",
    )

class RoomTypeEnum(EnumDefinitionImpl):

    attic = PermissibleValue(text="attic")
    bathroom = PermissibleValue(text="bathroom")
    closet = PermissibleValue(text="closet")
    elevator = PermissibleValue(text="elevator")
    hallway = PermissibleValue(text="hallway")
    kitchen = PermissibleValue(text="kitchen")
    stairwell = PermissibleValue(text="stairwell")
    lobby = PermissibleValue(text="lobby")
    vestibule = PermissibleValue(text="vestibule")
    laboratory_wet = PermissibleValue(text="laboratory_wet")
    laboratory_dry = PermissibleValue(text="laboratory_dry")
    gymnasium = PermissibleValue(text="gymnasium")
    natatorium = PermissibleValue(text="natatorium")
    auditorium = PermissibleValue(text="auditorium")
    lockers = PermissibleValue(text="lockers")
    cafe = PermissibleValue(text="cafe")
    warehouse = PermissibleValue(text="warehouse")

    _defn = EnumDefinition(
        name="RoomTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "conference room",
                PermissibleValue(text="conference room") )
        setattr(cls, "examining room",
                PermissibleValue(text="examining room") )
        setattr(cls, "mail room",
                PermissibleValue(text="mail room") )
        setattr(cls, "private office",
                PermissibleValue(text="private office") )
        setattr(cls, "open office",
                PermissibleValue(text="open office") )
        setattr(cls, ",restroom",
                PermissibleValue(text=",restroom") )
        setattr(cls, "mechanical or electrical room",
                PermissibleValue(text="mechanical or electrical room") )
        setattr(cls, "data center",
                PermissibleValue(text="data center") )

class DoorTypeEnum(EnumDefinitionImpl):

    composite = PermissibleValue(text="composite")
    metal = PermissibleValue(text="metal")
    wooden = PermissibleValue(text="wooden")

    _defn = EnumDefinition(
        name="DoorTypeEnum",
    )

class DoorMoveEnum(EnumDefinitionImpl):

    collapsible = PermissibleValue(text="collapsible")
    folding = PermissibleValue(text="folding")
    revolving = PermissibleValue(text="revolving")
    sliding = PermissibleValue(text="sliding")
    swinging = PermissibleValue(text="swinging")

    _defn = EnumDefinition(
        name="DoorMoveEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "rolling shutter",
                PermissibleValue(text="rolling shutter") )

class SampSubtypeEnum(EnumDefinitionImpl):

    biofilm = PermissibleValue(text="biofilm")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampSubtypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "oil phase",
                PermissibleValue(text="oil phase") )
        setattr(cls, "water phase",
                PermissibleValue(text="water phase") )
        setattr(cls, "not applicable",
                PermissibleValue(text="not applicable") )

class HcrEnum(EnumDefinitionImpl):

    Coalbed = PermissibleValue(text="Coalbed")
    Shale = PermissibleValue(text="Shale")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcrEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Oil Reservoir",
                PermissibleValue(text="Oil Reservoir") )
        setattr(cls, "Gas Reservoir",
                PermissibleValue(text="Gas Reservoir") )
        setattr(cls, "Oil Sand",
                PermissibleValue(text="Oil Sand") )
        setattr(cls, "Tight Oil Reservoir",
                PermissibleValue(text="Tight Oil Reservoir") )
        setattr(cls, "Tight Gas Reservoir",
                PermissibleValue(text="Tight Gas Reservoir") )

class HcProducedEnum(EnumDefinitionImpl):

    Oil = PermissibleValue(text="Oil")
    Gas = PermissibleValue(text="Gas")
    Bitumen = PermissibleValue(text="Bitumen")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcProducedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Gas-Condensate",
                PermissibleValue(text="Gas-Condensate") )
        setattr(cls, "Coalbed Methane",
                PermissibleValue(text="Coalbed Methane") )

class SampCollectPointEnum(EnumDefinitionImpl):

    well = PermissibleValue(text="well")
    wellhead = PermissibleValue(text="wellhead")
    separator = PermissibleValue(text="separator")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampCollectPointEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "test well",
                PermissibleValue(text="test well") )
        setattr(cls, "drilling rig",
                PermissibleValue(text="drilling rig") )
        setattr(cls, "storage tank",
                PermissibleValue(text="storage tank") )

class LithologyEnum(EnumDefinitionImpl):

    Basement = PermissibleValue(text="Basement")
    Chalk = PermissibleValue(text="Chalk")
    Chert = PermissibleValue(text="Chert")
    Coal = PermissibleValue(text="Coal")
    Conglomerate = PermissibleValue(text="Conglomerate")
    Diatomite = PermissibleValue(text="Diatomite")
    Dolomite = PermissibleValue(text="Dolomite")
    Limestone = PermissibleValue(text="Limestone")
    Sandstone = PermissibleValue(text="Sandstone")
    Shale = PermissibleValue(text="Shale")
    Siltstone = PermissibleValue(text="Siltstone")
    Volcanic = PermissibleValue(text="Volcanic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="LithologyEnum",
    )

class OxyStatSampEnum(EnumDefinitionImpl):

    aerobic = PermissibleValue(text="aerobic")
    anaerobic = PermissibleValue(text="anaerobic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="OxyStatSampEnum",
    )

class HcrGeolAgeEnum(EnumDefinitionImpl):

    Archean = PermissibleValue(text="Archean")
    Cambrian = PermissibleValue(text="Cambrian")
    Carboniferous = PermissibleValue(text="Carboniferous")
    Cenozoic = PermissibleValue(text="Cenozoic")
    Cretaceous = PermissibleValue(text="Cretaceous")
    Devonian = PermissibleValue(text="Devonian")
    Jurassic = PermissibleValue(text="Jurassic")
    Mesozoic = PermissibleValue(text="Mesozoic")
    Neogene = PermissibleValue(text="Neogene")
    Ordovician = PermissibleValue(text="Ordovician")
    Paleogene = PermissibleValue(text="Paleogene")
    Paleozoic = PermissibleValue(text="Paleozoic")
    Permian = PermissibleValue(text="Permian")
    Precambrian = PermissibleValue(text="Precambrian")
    Proterozoic = PermissibleValue(text="Proterozoic")
    Silurian = PermissibleValue(text="Silurian")
    Triassic = PermissibleValue(text="Triassic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcrGeolAgeEnum",
    )

class DeposEnvEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="DeposEnvEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Continental - Alluvial",
                PermissibleValue(text="Continental - Alluvial") )
        setattr(cls, "Continental - Aeolian",
                PermissibleValue(text="Continental - Aeolian") )
        setattr(cls, "Continental - Fluvial",
                PermissibleValue(text="Continental - Fluvial") )
        setattr(cls, "Continental - Lacustrine",
                PermissibleValue(text="Continental - Lacustrine") )
        setattr(cls, "Transitional - Deltaic",
                PermissibleValue(text="Transitional - Deltaic") )
        setattr(cls, "Transitional - Tidal",
                PermissibleValue(text="Transitional - Tidal") )
        setattr(cls, "Transitional - Lagoonal",
                PermissibleValue(text="Transitional - Lagoonal") )
        setattr(cls, "Transitional - Beach",
                PermissibleValue(text="Transitional - Beach") )
        setattr(cls, "Transitional - Lake",
                PermissibleValue(text="Transitional - Lake") )
        setattr(cls, "Marine - Shallow",
                PermissibleValue(text="Marine - Shallow") )
        setattr(cls, "Marine - Deep",
                PermissibleValue(text="Marine - Deep") )
        setattr(cls, "Marine - Reef",
                PermissibleValue(text="Marine - Reef") )
        setattr(cls, "Other - Evaporite",
                PermissibleValue(text="Other - Evaporite") )
        setattr(cls, "Other - Glacial",
                PermissibleValue(text="Other - Glacial") )
        setattr(cls, "Other - Volcanic",
                PermissibleValue(text="Other - Volcanic") )

class SrDepEnvEnum(EnumDefinitionImpl):

    Lacustine = PermissibleValue(text="Lacustine")
    Fluvioldeltaic = PermissibleValue(text="Fluvioldeltaic")
    Fluviomarine = PermissibleValue(text="Fluviomarine")
    Marine = PermissibleValue(text="Marine")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrDepEnvEnum",
    )

class SrLithologyEnum(EnumDefinitionImpl):

    Clastic = PermissibleValue(text="Clastic")
    Carbonate = PermissibleValue(text="Carbonate")
    Coal = PermissibleValue(text="Coal")
    Biosilicieous = PermissibleValue(text="Biosilicieous")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrLithologyEnum",
    )

class SrKerogTypeEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrKerogTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Type I",
                PermissibleValue(text="Type I") )
        setattr(cls, "Type II",
                PermissibleValue(text="Type II") )
        setattr(cls, "Type III",
                PermissibleValue(text="Type III") )
        setattr(cls, "Type IV",
                PermissibleValue(text="Type IV") )

class SrGeolAgeEnum(EnumDefinitionImpl):

    Archean = PermissibleValue(text="Archean")
    Cambrian = PermissibleValue(text="Cambrian")
    Carboniferous = PermissibleValue(text="Carboniferous")
    Cenozoic = PermissibleValue(text="Cenozoic")
    Cretaceous = PermissibleValue(text="Cretaceous")
    Devonian = PermissibleValue(text="Devonian")
    Jurassic = PermissibleValue(text="Jurassic")
    Mesozoic = PermissibleValue(text="Mesozoic")
    Neogene = PermissibleValue(text="Neogene")
    Ordovician = PermissibleValue(text="Ordovician")
    Paleogene = PermissibleValue(text="Paleogene")
    Paleozoic = PermissibleValue(text="Paleozoic")
    Permian = PermissibleValue(text="Permian")
    Precambrian = PermissibleValue(text="Precambrian")
    Proterozoic = PermissibleValue(text="Proterozoic")
    Silurian = PermissibleValue(text="Silurian")
    Triassic = PermissibleValue(text="Triassic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrGeolAgeEnum",
    )

class TillageEnum(EnumDefinitionImpl):

    drill = PermissibleValue(text="drill")
    chisel = PermissibleValue(text="chisel")
    tined = PermissibleValue(text="tined")
    mouldboard = PermissibleValue(text="mouldboard")

    _defn = EnumDefinition(
        name="TillageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cutting disc",
                PermissibleValue(text="cutting disc") )
        setattr(cls, "ridge till",
                PermissibleValue(text="ridge till") )
        setattr(cls, "strip tillage",
                PermissibleValue(text="strip tillage") )
        setattr(cls, "zonal tillage",
                PermissibleValue(text="zonal tillage") )
        setattr(cls, "disc plough",
                PermissibleValue(text="disc plough") )

class FaoClassEnum(EnumDefinitionImpl):

    Acrisols = PermissibleValue(text="Acrisols")
    Andosols = PermissibleValue(text="Andosols")
    Arenosols = PermissibleValue(text="Arenosols")
    Cambisols = PermissibleValue(text="Cambisols")
    Chernozems = PermissibleValue(text="Chernozems")
    Ferralsols = PermissibleValue(text="Ferralsols")
    Fluvisols = PermissibleValue(text="Fluvisols")
    Gleysols = PermissibleValue(text="Gleysols")
    Greyzems = PermissibleValue(text="Greyzems")
    Gypsisols = PermissibleValue(text="Gypsisols")
    Histosols = PermissibleValue(text="Histosols")
    Kastanozems = PermissibleValue(text="Kastanozems")
    Lithosols = PermissibleValue(text="Lithosols")
    Luvisols = PermissibleValue(text="Luvisols")
    Nitosols = PermissibleValue(text="Nitosols")
    Phaeozems = PermissibleValue(text="Phaeozems")
    Planosols = PermissibleValue(text="Planosols")
    Podzols = PermissibleValue(text="Podzols")
    Podzoluvisols = PermissibleValue(text="Podzoluvisols")
    Rankers = PermissibleValue(text="Rankers")
    Regosols = PermissibleValue(text="Regosols")
    Rendzinas = PermissibleValue(text="Rendzinas")
    Solonchaks = PermissibleValue(text="Solonchaks")
    Solonetz = PermissibleValue(text="Solonetz")
    Vertisols = PermissibleValue(text="Vertisols")
    Yermosols = PermissibleValue(text="Yermosols")

    _defn = EnumDefinition(
        name="FaoClassEnum",
    )

class CurLandUseEnum(EnumDefinitionImpl):

    cities = PermissibleValue(text="cities")
    farmstead = PermissibleValue(text="farmstead")
    rock = PermissibleValue(text="rock")
    sand = PermissibleValue(text="sand")
    gravel = PermissibleValue(text="gravel")
    mudflats = PermissibleValue(text="mudflats")
    badlands = PermissibleValue(text="badlands")
    rangeland = PermissibleValue(text="rangeland")
    hayland = PermissibleValue(text="hayland")

    _defn = EnumDefinition(
        name="CurLandUseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "industrial areas",
                PermissibleValue(text="industrial areas") )
        setattr(cls, "roads/railroads",
                PermissibleValue(text="roads/railroads") )
        setattr(cls, "salt flats",
                PermissibleValue(text="salt flats") )
        setattr(cls, "permanent snow or ice",
                PermissibleValue(text="permanent snow or ice") )
        setattr(cls, "saline seeps",
                PermissibleValue(text="saline seeps") )
        setattr(cls, "mines/quarries",
                PermissibleValue(text="mines/quarries") )
        setattr(cls, "oil waste areas",
                PermissibleValue(text="oil waste areas") )
        setattr(cls, "small grains",
                PermissibleValue(text="small grains") )
        setattr(cls, "row crops",
                PermissibleValue(text="row crops") )
        setattr(cls, "vegetable crops",
                PermissibleValue(text="vegetable crops") )
        setattr(cls, "horticultural plants (e.g. tulips)",
                PermissibleValue(text="horticultural plants (e.g. tulips)") )
        setattr(cls, "marshlands (grass,sedges,rushes)",
                PermissibleValue(text="marshlands (grass,sedges,rushes)") )
        setattr(cls, "tundra (mosses,lichens)",
                PermissibleValue(text="tundra (mosses,lichens)") )
        setattr(cls, "pastureland (grasslands used for livestock grazing)",
                PermissibleValue(text="pastureland (grasslands used for livestock grazing)") )
        setattr(cls, "meadows (grasses,alfalfa,fescue,bromegrass,timothy)",
                PermissibleValue(text="meadows (grasses,alfalfa,fescue,bromegrass,timothy)") )
        setattr(cls, "shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)",
                PermissibleValue(text="shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)") )
        setattr(cls, "successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)",
                PermissibleValue(text="successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)") )
        setattr(cls, "shrub crops (blueberries,nursery ornamentals,filberts)",
                PermissibleValue(text="shrub crops (blueberries,nursery ornamentals,filberts)") )
        setattr(cls, "vine crops (grapes)",
                PermissibleValue(text="vine crops (grapes)") )
        setattr(cls, "conifers (e.g. pine,spruce,fir,cypress)",
                PermissibleValue(text="conifers (e.g. pine,spruce,fir,cypress)") )
        setattr(cls, "hardwoods (e.g. oak,hickory,elm,aspen)",
                PermissibleValue(text="hardwoods (e.g. oak,hickory,elm,aspen)") )
        setattr(cls, "intermixed hardwood and conifers",
                PermissibleValue(text="intermixed hardwood and conifers") )
        setattr(cls, "tropical (e.g. mangrove,palms)",
                PermissibleValue(text="tropical (e.g. mangrove,palms)") )
        setattr(cls, "rainforest (evergreen forest receiving greater than 406 cm annual rainfall)",
                PermissibleValue(text="rainforest (evergreen forest receiving greater than 406 cm annual rainfall)") )
        setattr(cls, "swamp (permanent or semi-permanent water body dominated by woody plants)",
                PermissibleValue(text="swamp (permanent or semi-permanent water body dominated by woody plants)") )
        setattr(cls, "crop trees (nuts,fruit,christmas trees,nursery trees)",
                PermissibleValue(text="crop trees (nuts,fruit,christmas trees,nursery trees)") )

class SoilHorizonEnum(EnumDefinitionImpl):

    Permafrost = PermissibleValue(text="Permafrost")

    _defn = EnumDefinition(
        name="SoilHorizonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "O horizon",
                PermissibleValue(text="O horizon") )
        setattr(cls, "A horizon",
                PermissibleValue(text="A horizon") )
        setattr(cls, "E horizon",
                PermissibleValue(text="E horizon") )
        setattr(cls, "B horizon",
                PermissibleValue(text="B horizon") )
        setattr(cls, "C horizon",
                PermissibleValue(text="C horizon") )
        setattr(cls, "R layer",
                PermissibleValue(text="R layer") )

class DrainageClassEnum(EnumDefinitionImpl):

    poorly = PermissibleValue(text="poorly")
    well = PermissibleValue(text="well")

    _defn = EnumDefinition(
        name="DrainageClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "very poorly",
                PermissibleValue(text="very poorly") )
        setattr(cls, "somewhat poorly",
                PermissibleValue(text="somewhat poorly") )
        setattr(cls, "moderately well",
                PermissibleValue(text="moderately well") )
        setattr(cls, "excessively drained",
                PermissibleValue(text="excessively drained") )

class ProfilePositionEnum(EnumDefinitionImpl):

    summit = PermissibleValue(text="summit")
    shoulder = PermissibleValue(text="shoulder")
    backslope = PermissibleValue(text="backslope")
    footslope = PermissibleValue(text="footslope")
    toeslope = PermissibleValue(text="toeslope")

    _defn = EnumDefinition(
        name="ProfilePositionEnum",
    )

class PlantSexEnum(EnumDefinitionImpl):

    Androdioecious = PermissibleValue(text="Androdioecious")
    Androecious = PermissibleValue(text="Androecious")
    Androgynous = PermissibleValue(text="Androgynous")
    Androgynomonoecious = PermissibleValue(text="Androgynomonoecious")
    Andromonoecious = PermissibleValue(text="Andromonoecious")
    Bisexual = PermissibleValue(text="Bisexual")
    Dichogamous = PermissibleValue(text="Dichogamous")
    Diclinous = PermissibleValue(text="Diclinous")
    Dioecious = PermissibleValue(text="Dioecious")
    Gynodioecious = PermissibleValue(text="Gynodioecious")
    Gynoecious = PermissibleValue(text="Gynoecious")
    Gynomonoecious = PermissibleValue(text="Gynomonoecious")
    Hermaphroditic = PermissibleValue(text="Hermaphroditic")
    Imperfect = PermissibleValue(text="Imperfect")
    Monoclinous = PermissibleValue(text="Monoclinous")
    Monoecious = PermissibleValue(text="Monoecious")
    Perfect = PermissibleValue(text="Perfect")
    Polygamodioecious = PermissibleValue(text="Polygamodioecious")
    Polygamomonoecious = PermissibleValue(text="Polygamomonoecious")
    Polygamous = PermissibleValue(text="Polygamous")
    Protandrous = PermissibleValue(text="Protandrous")
    Protogynous = PermissibleValue(text="Protogynous")
    Subandroecious = PermissibleValue(text="Subandroecious")
    Subdioecious = PermissibleValue(text="Subdioecious")
    Subgynoecious = PermissibleValue(text="Subgynoecious")
    Synoecious = PermissibleValue(text="Synoecious")
    Trimonoecious = PermissibleValue(text="Trimonoecious")
    Trioecious = PermissibleValue(text="Trioecious")
    Unisexual = PermissibleValue(text="Unisexual")

    _defn = EnumDefinition(
        name="PlantSexEnum",
    )

class SampCaptStatusEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampCaptStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "active surveillance in response to an outbreak",
                PermissibleValue(text="active surveillance in response to an outbreak") )
        setattr(cls, "active surveillance not initiated by an outbreak",
                PermissibleValue(text="active surveillance not initiated by an outbreak") )
        setattr(cls, "farm sample",
                PermissibleValue(text="farm sample") )
        setattr(cls, "market sample",
                PermissibleValue(text="market sample") )

class SampDisStageEnum(EnumDefinitionImpl):

    dissemination = PermissibleValue(text="dissemination")
    infection = PermissibleValue(text="infection")
    inoculation = PermissibleValue(text="inoculation")
    penetration = PermissibleValue(text="penetration")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampDisStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "growth and reproduction",
                PermissibleValue(text="growth and reproduction") )

class GrowthHabitEnum(EnumDefinitionImpl):

    erect = PermissibleValue(text="erect")
    spreading = PermissibleValue(text="spreading")
    prostrate = PermissibleValue(text="prostrate")

    _defn = EnumDefinition(
        name="GrowthHabitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-erect",
                PermissibleValue(text="semi-erect") )

class BiolStatEnum(EnumDefinitionImpl):

    wild = PermissibleValue(text="wild")
    natural = PermissibleValue(text="natural")
    hybrid = PermissibleValue(text="hybrid")
    mutant = PermissibleValue(text="mutant")

    _defn = EnumDefinition(
        name="BiolStatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-natural",
                PermissibleValue(text="semi-natural") )
        setattr(cls, "inbred line",
                PermissibleValue(text="inbred line") )
        setattr(cls, "breeder's line",
                PermissibleValue(text="breeder's line") )
        setattr(cls, "clonal selection",
                PermissibleValue(text="clonal selection") )

class TidalStageEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TidalStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low tide",
                PermissibleValue(text="low tide") )
        setattr(cls, "ebb tide",
                PermissibleValue(text="ebb tide") )
        setattr(cls, "flood tide",
                PermissibleValue(text="flood tide") )
        setattr(cls, "high tide",
                PermissibleValue(text="high tide") )

class SedimentTypeEnum(EnumDefinitionImpl):

    biogenous = PermissibleValue(text="biogenous")
    cosmogenous = PermissibleValue(text="cosmogenous")
    hydrogenous = PermissibleValue(text="hydrogenous")
    lithogenous = PermissibleValue(text="lithogenous")

    _defn = EnumDefinition(
        name="SedimentTypeEnum",
    )

class HostSexEnum(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    male = PermissibleValue(text="male")
    neuter = PermissibleValue(text="neuter")

    _defn = EnumDefinition(
        name="HostSexEnum",
    )

# Slots
class slots:
    pass

slots.Bioscales = Slot(uri=NMDC_SUB_SCHEMA.Bioscales, name="Bioscales", curie=NMDC_SUB_SCHEMA.curie('Bioscales'),
                   model_uri=NMDC_SUB_SCHEMA.Bioscales, domain=None, range=Optional[str])

slots.EMSL = Slot(uri=NMDC_SUB_SCHEMA.EMSL, name="EMSL", curie=NMDC_SUB_SCHEMA.curie('EMSL'),
                   model_uri=NMDC_SUB_SCHEMA.EMSL, domain=None, range=Optional[str])

slots.EMSL_store_temp = Slot(uri=NMDC_SUB_SCHEMA.EMSL_store_temp, name="EMSL_store_temp", curie=NMDC_SUB_SCHEMA.curie('EMSL_store_temp'),
                   model_uri=NMDC_SUB_SCHEMA.EMSL_store_temp, domain=None, range=Optional[str])

slots.JGI_Metagenomics = Slot(uri=NMDC_SUB_SCHEMA.JGI_Metagenomics, name="JGI_Metagenomics", curie=NMDC_SUB_SCHEMA.curie('JGI_Metagenomics'),
                   model_uri=NMDC_SUB_SCHEMA.JGI_Metagenomics, domain=None, range=Optional[str])

slots.JGI_Metatranscriptomics = Slot(uri=NMDC_SUB_SCHEMA.JGI_Metatranscriptomics, name="JGI_Metatranscriptomics", curie=NMDC_SUB_SCHEMA.curie('JGI_Metatranscriptomics'),
                   model_uri=NMDC_SUB_SCHEMA.JGI_Metatranscriptomics, domain=None, range=Optional[str])

slots.MIxS = Slot(uri=NMDC_SUB_SCHEMA.MIxS, name="MIxS", curie=NMDC_SUB_SCHEMA.curie('MIxS'),
                   model_uri=NMDC_SUB_SCHEMA.MIxS, domain=None, range=Optional[str])

slots.MIxS_Inspired = Slot(uri=NMDC_SUB_SCHEMA.MIxS_Inspired, name="MIxS_Inspired", curie=NMDC_SUB_SCHEMA.curie('MIxS_Inspired'),
                   model_uri=NMDC_SUB_SCHEMA.MIxS_Inspired, domain=None, range=Optional[str])

slots.MIxS_NASSF = Slot(uri=NMDC_SUB_SCHEMA.MIxS_NASSF, name="MIxS_NASSF", curie=NMDC_SUB_SCHEMA.curie('MIxS_NASSF'),
                   model_uri=NMDC_SUB_SCHEMA.MIxS_NASSF, domain=None, range=Optional[str])

slots.MIxS_core = Slot(uri=NMDC_SUB_SCHEMA.MIxS_core, name="MIxS_core", curie=NMDC_SUB_SCHEMA.curie('MIxS_core'),
                   model_uri=NMDC_SUB_SCHEMA.MIxS_core, domain=None, range=Optional[str])

slots.MIxS_investigation = Slot(uri=NMDC_SUB_SCHEMA.MIxS_investigation, name="MIxS_investigation", curie=NMDC_SUB_SCHEMA.curie('MIxS_investigation'),
                   model_uri=NMDC_SUB_SCHEMA.MIxS_investigation, domain=None, range=Optional[str])

slots.MixS_Modified = Slot(uri=NMDC_SUB_SCHEMA.MixS_Modified, name="MixS_Modified", curie=NMDC_SUB_SCHEMA.curie('MixS_Modified'),
                   model_uri=NMDC_SUB_SCHEMA.MixS_Modified, domain=None, range=Optional[str])

slots.Sample_ID = Slot(uri=NMDC_SUB_SCHEMA.Sample_ID, name="Sample_ID", curie=NMDC_SUB_SCHEMA.curie('Sample_ID'),
                   model_uri=NMDC_SUB_SCHEMA.Sample_ID, domain=None, range=Optional[str])

slots.air_data = Slot(uri=NMDC_SUB_SCHEMA.air_data, name="air_data", curie=NMDC_SUB_SCHEMA.curie('air_data'),
                   model_uri=NMDC_SUB_SCHEMA.air_data, domain=None, range=Optional[Union[Union[dict, Air], List[Union[dict, Air]]]])

slots.analysis_type = Slot(uri=NMDC_SUB_SCHEMA.analysis_type, name="analysis_type", curie=NMDC_SUB_SCHEMA.curie('analysis_type'),
                   model_uri=NMDC_SUB_SCHEMA.analysis_type, domain=None, range=Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]])

slots.biofilm_data = Slot(uri=NMDC_SUB_SCHEMA.biofilm_data, name="biofilm_data", curie=NMDC_SUB_SCHEMA.curie('biofilm_data'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_data, domain=None, range=Optional[Union[Union[dict, Biofilm], List[Union[dict, Biofilm]]]])

slots.bioscales_data = Slot(uri=NMDC_SUB_SCHEMA.bioscales_data, name="bioscales_data", curie=NMDC_SUB_SCHEMA.curie('bioscales_data'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_data, domain=None, range=Optional[Union[Union[dict, Bioscales], List[Union[dict, Bioscales]]]])

slots.built_env_data = Slot(uri=NMDC_SUB_SCHEMA.built_env_data, name="built_env_data", curie=NMDC_SUB_SCHEMA.curie('built_env_data'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_data, domain=None, range=Optional[Union[Union[dict, BuiltEnv], List[Union[dict, BuiltEnv]]]])

slots.collection_date_inc = Slot(uri=NMDC_SUB_SCHEMA.collection_date_inc, name="collection_date_inc", curie=NMDC_SUB_SCHEMA.curie('collection_date_inc'),
                   model_uri=NMDC_SUB_SCHEMA.collection_date_inc, domain=None, range=Optional[str])

slots.collection_time = Slot(uri=NMDC_SUB_SCHEMA.collection_time, name="collection_time", curie=NMDC_SUB_SCHEMA.curie('collection_time'),
                   model_uri=NMDC_SUB_SCHEMA.collection_time, domain=None, range=Optional[str])

slots.collection_time_inc = Slot(uri=NMDC_SUB_SCHEMA.collection_time_inc, name="collection_time_inc", curie=NMDC_SUB_SCHEMA.curie('collection_time_inc'),
                   model_uri=NMDC_SUB_SCHEMA.collection_time_inc, domain=None, range=Optional[str])

slots.dh_section = Slot(uri=NMDC_SUB_SCHEMA.dh_section, name="dh_section", curie=NMDC_SUB_SCHEMA.curie('dh_section'),
                   model_uri=NMDC_SUB_SCHEMA.dh_section, domain=None, range=Optional[str])

slots.dna_absorb1 = Slot(uri=NMDC_SUB_SCHEMA.dna_absorb1, name="dna_absorb1", curie=NMDC_SUB_SCHEMA.curie('dna_absorb1'),
                   model_uri=NMDC_SUB_SCHEMA.dna_absorb1, domain=None, range=Optional[str])

slots.dna_absorb2 = Slot(uri=NMDC_SUB_SCHEMA.dna_absorb2, name="dna_absorb2", curie=NMDC_SUB_SCHEMA.curie('dna_absorb2'),
                   model_uri=NMDC_SUB_SCHEMA.dna_absorb2, domain=None, range=Optional[str])

slots.dna_collect_site = Slot(uri=NMDC_SUB_SCHEMA.dna_collect_site, name="dna_collect_site", curie=NMDC_SUB_SCHEMA.curie('dna_collect_site'),
                   model_uri=NMDC_SUB_SCHEMA.dna_collect_site, domain=None, range=Optional[str])

slots.dna_concentration = Slot(uri=NMDC_SUB_SCHEMA.dna_concentration, name="dna_concentration", curie=NMDC_SUB_SCHEMA.curie('dna_concentration'),
                   model_uri=NMDC_SUB_SCHEMA.dna_concentration, domain=None, range=Optional[str])

slots.dna_cont_type = Slot(uri=NMDC_SUB_SCHEMA.dna_cont_type, name="dna_cont_type", curie=NMDC_SUB_SCHEMA.curie('dna_cont_type'),
                   model_uri=NMDC_SUB_SCHEMA.dna_cont_type, domain=None, range=Optional[Union[str, "DnaContTypeEnum"]])

slots.dna_container_ID = Slot(uri=NMDC_SUB_SCHEMA.dna_container_ID, name="dna_container_ID", curie=NMDC_SUB_SCHEMA.curie('dna_container_ID'),
                   model_uri=NMDC_SUB_SCHEMA.dna_container_ID, domain=None, range=Optional[str])

slots.dna_dnase = Slot(uri=NMDC_SUB_SCHEMA.dna_dnase, name="dna_dnase", curie=NMDC_SUB_SCHEMA.curie('dna_dnase'),
                   model_uri=NMDC_SUB_SCHEMA.dna_dnase, domain=None, range=Optional[Union[str, "DnaDnaseEnum"]])

slots.dna_isolate_meth = Slot(uri=NMDC_SUB_SCHEMA.dna_isolate_meth, name="dna_isolate_meth", curie=NMDC_SUB_SCHEMA.curie('dna_isolate_meth'),
                   model_uri=NMDC_SUB_SCHEMA.dna_isolate_meth, domain=None, range=Optional[str])

slots.dna_organisms = Slot(uri=NMDC_SUB_SCHEMA.dna_organisms, name="dna_organisms", curie=NMDC_SUB_SCHEMA.curie('dna_organisms'),
                   model_uri=NMDC_SUB_SCHEMA.dna_organisms, domain=None, range=Optional[str])

slots.dna_project_contact = Slot(uri=NMDC_SUB_SCHEMA.dna_project_contact, name="dna_project_contact", curie=NMDC_SUB_SCHEMA.curie('dna_project_contact'),
                   model_uri=NMDC_SUB_SCHEMA.dna_project_contact, domain=None, range=Optional[str])

slots.dna_samp_ID = Slot(uri=NMDC_SUB_SCHEMA.dna_samp_ID, name="dna_samp_ID", curie=NMDC_SUB_SCHEMA.curie('dna_samp_ID'),
                   model_uri=NMDC_SUB_SCHEMA.dna_samp_ID, domain=None, range=Optional[str])

slots.dna_sample_format = Slot(uri=NMDC_SUB_SCHEMA.dna_sample_format, name="dna_sample_format", curie=NMDC_SUB_SCHEMA.curie('dna_sample_format'),
                   model_uri=NMDC_SUB_SCHEMA.dna_sample_format, domain=None, range=Optional[Union[str, "DnaSampleFormatEnum"]])

slots.dna_sample_name = Slot(uri=NMDC_SUB_SCHEMA.dna_sample_name, name="dna_sample_name", curie=NMDC_SUB_SCHEMA.curie('dna_sample_name'),
                   model_uri=NMDC_SUB_SCHEMA.dna_sample_name, domain=None, range=Optional[str])

slots.dna_seq_project = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project, name="dna_seq_project", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project, domain=None, range=Optional[str])

slots.dna_seq_project_PI = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project_PI, name="dna_seq_project_PI", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project_PI'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project_PI, domain=None, range=Optional[str])

slots.dna_seq_project_name = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project_name, name="dna_seq_project_name", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project_name'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project_name, domain=None, range=Optional[str])

slots.dna_volume = Slot(uri=NMDC_SUB_SCHEMA.dna_volume, name="dna_volume", curie=NMDC_SUB_SCHEMA.curie('dna_volume'),
                   model_uri=NMDC_SUB_SCHEMA.dna_volume, domain=None, range=Optional[str])

slots.dnase_rna = Slot(uri=NMDC_SUB_SCHEMA.dnase_rna, name="dnase_rna", curie=NMDC_SUB_SCHEMA.curie('dnase_rna'),
                   model_uri=NMDC_SUB_SCHEMA.dnase_rna, domain=None, range=Optional[Union[str, "DnaseRnaEnum"]])

slots.emsl_data = Slot(uri=NMDC_SUB_SCHEMA.emsl_data, name="emsl_data", curie=NMDC_SUB_SCHEMA.curie('emsl_data'),
                   model_uri=NMDC_SUB_SCHEMA.emsl_data, domain=None, range=Optional[Union[Union[dict, Emsl], List[Union[dict, Emsl]]]])

slots.env_package = Slot(uri=NMDC_SUB_SCHEMA.env_package, name="env_package", curie=NMDC_SUB_SCHEMA.curie('env_package'),
                   model_uri=NMDC_SUB_SCHEMA.env_package, domain=None, range=Optional[str])

slots.experimental_factor_other = Slot(uri=NMDC_SUB_SCHEMA.experimental_factor_other, name="experimental_factor_other", curie=NMDC_SUB_SCHEMA.curie('experimental_factor_other'),
                   model_uri=NMDC_SUB_SCHEMA.experimental_factor_other, domain=None, range=Optional[str])

slots.filter_method = Slot(uri=NMDC_SUB_SCHEMA.filter_method, name="filter_method", curie=NMDC_SUB_SCHEMA.curie('filter_method'),
                   model_uri=NMDC_SUB_SCHEMA.filter_method, domain=None, range=Optional[str])

slots.hcr_cores_data = Slot(uri=NMDC_SUB_SCHEMA.hcr_cores_data, name="hcr_cores_data", curie=NMDC_SUB_SCHEMA.curie('hcr_cores_data'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_data, domain=None, range=Optional[Union[Union[dict, HcrCores], List[Union[dict, HcrCores]]]])

slots.hcr_fluids_swabs_data = Slot(uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_data, name="hcr_fluids_swabs_data", curie=NMDC_SUB_SCHEMA.curie('hcr_fluids_swabs_data'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_data, domain=None, range=Optional[Union[Union[dict, HcrFluidsSwabs], List[Union[dict, HcrFluidsSwabs]]]])

slots.host_associated_data = Slot(uri=NMDC_SUB_SCHEMA.host_associated_data, name="host_associated_data", curie=NMDC_SUB_SCHEMA.curie('host_associated_data'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_data, domain=None, range=Optional[Union[Union[dict, HostAssociated], List[Union[dict, HostAssociated]]]])

slots.isotope_exposure = Slot(uri=NMDC_SUB_SCHEMA.isotope_exposure, name="isotope_exposure", curie=NMDC_SUB_SCHEMA.curie('isotope_exposure'),
                   model_uri=NMDC_SUB_SCHEMA.isotope_exposure, domain=None, range=Optional[str])

slots.jgi_mg_data = Slot(uri=NMDC_SUB_SCHEMA.jgi_mg_data, name="jgi_mg_data", curie=NMDC_SUB_SCHEMA.curie('jgi_mg_data'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_mg_data, domain=None, range=Optional[Union[Union[dict, JgiMg], List[Union[dict, JgiMg]]]])

slots.jgi_mt_data = Slot(uri=NMDC_SUB_SCHEMA.jgi_mt_data, name="jgi_mt_data", curie=NMDC_SUB_SCHEMA.curie('jgi_mt_data'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_mt_data, domain=None, range=Optional[Union[Union[dict, JgiMt], List[Union[dict, JgiMt]]]])

slots.micro_biomass_C_meth = Slot(uri=NMDC_SUB_SCHEMA.micro_biomass_C_meth, name="micro_biomass_C_meth", curie=NMDC_SUB_SCHEMA.curie('micro_biomass_C_meth'),
                   model_uri=NMDC_SUB_SCHEMA.micro_biomass_C_meth, domain=None, range=Optional[str])

slots.micro_biomass_N_meth = Slot(uri=NMDC_SUB_SCHEMA.micro_biomass_N_meth, name="micro_biomass_N_meth", curie=NMDC_SUB_SCHEMA.curie('micro_biomass_N_meth'),
                   model_uri=NMDC_SUB_SCHEMA.micro_biomass_N_meth, domain=None, range=Optional[str])

slots.microbial_biomass_C = Slot(uri=NMDC_SUB_SCHEMA.microbial_biomass_C, name="microbial_biomass_C", curie=NMDC_SUB_SCHEMA.curie('microbial_biomass_C'),
                   model_uri=NMDC_SUB_SCHEMA.microbial_biomass_C, domain=None, range=Optional[str])

slots.microbial_biomass_N = Slot(uri=NMDC_SUB_SCHEMA.microbial_biomass_N, name="microbial_biomass_N", curie=NMDC_SUB_SCHEMA.curie('microbial_biomass_N'),
                   model_uri=NMDC_SUB_SCHEMA.microbial_biomass_N, domain=None, range=Optional[str])

slots.misc_envs_data = Slot(uri=NMDC_SUB_SCHEMA.misc_envs_data, name="misc_envs_data", curie=NMDC_SUB_SCHEMA.curie('misc_envs_data'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_data, domain=None, range=Optional[Union[Union[dict, MiscEnvs], List[Union[dict, MiscEnvs]]]])

slots.non_microb_biomass = Slot(uri=NMDC_SUB_SCHEMA.non_microb_biomass, name="non_microb_biomass", curie=NMDC_SUB_SCHEMA.curie('non_microb_biomass'),
                   model_uri=NMDC_SUB_SCHEMA.non_microb_biomass, domain=None, range=Optional[str])

slots.non_microb_biomass_method = Slot(uri=NMDC_SUB_SCHEMA.non_microb_biomass_method, name="non_microb_biomass_method", curie=NMDC_SUB_SCHEMA.curie('non_microb_biomass_method'),
                   model_uri=NMDC_SUB_SCHEMA.non_microb_biomass_method, domain=None, range=Optional[str])

slots.org_nitro_method = Slot(uri=NMDC_SUB_SCHEMA.org_nitro_method, name="org_nitro_method", curie=NMDC_SUB_SCHEMA.curie('org_nitro_method'),
                   model_uri=NMDC_SUB_SCHEMA.org_nitro_method, domain=None, range=Optional[str])

slots.other_treatment = Slot(uri=NMDC_SUB_SCHEMA.other_treatment, name="other_treatment", curie=NMDC_SUB_SCHEMA.curie('other_treatment'),
                   model_uri=NMDC_SUB_SCHEMA.other_treatment, domain=None, range=Optional[str])

slots.plant_associated_data = Slot(uri=NMDC_SUB_SCHEMA.plant_associated_data, name="plant_associated_data", curie=NMDC_SUB_SCHEMA.curie('plant_associated_data'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_data, domain=None, range=Optional[Union[Union[dict, PlantAssociated], List[Union[dict, PlantAssociated]]]])

slots.project_ID = Slot(uri=NMDC_SUB_SCHEMA.project_ID, name="project_ID", curie=NMDC_SUB_SCHEMA.curie('project_ID'),
                   model_uri=NMDC_SUB_SCHEMA.project_ID, domain=None, range=Optional[str])

slots.proposal_dna = Slot(uri=NMDC_SUB_SCHEMA.proposal_dna, name="proposal_dna", curie=NMDC_SUB_SCHEMA.curie('proposal_dna'),
                   model_uri=NMDC_SUB_SCHEMA.proposal_dna, domain=None, range=Optional[str])

slots.proposal_rna = Slot(uri=NMDC_SUB_SCHEMA.proposal_rna, name="proposal_rna", curie=NMDC_SUB_SCHEMA.curie('proposal_rna'),
                   model_uri=NMDC_SUB_SCHEMA.proposal_rna, domain=None, range=Optional[str])

slots.replicate_number = Slot(uri=NMDC_SUB_SCHEMA.replicate_number, name="replicate_number", curie=NMDC_SUB_SCHEMA.curie('replicate_number'),
                   model_uri=NMDC_SUB_SCHEMA.replicate_number, domain=None, range=Optional[str])

slots.rna_absorb1 = Slot(uri=NMDC_SUB_SCHEMA.rna_absorb1, name="rna_absorb1", curie=NMDC_SUB_SCHEMA.curie('rna_absorb1'),
                   model_uri=NMDC_SUB_SCHEMA.rna_absorb1, domain=None, range=Optional[str])

slots.rna_absorb2 = Slot(uri=NMDC_SUB_SCHEMA.rna_absorb2, name="rna_absorb2", curie=NMDC_SUB_SCHEMA.curie('rna_absorb2'),
                   model_uri=NMDC_SUB_SCHEMA.rna_absorb2, domain=None, range=Optional[str])

slots.rna_collect_site = Slot(uri=NMDC_SUB_SCHEMA.rna_collect_site, name="rna_collect_site", curie=NMDC_SUB_SCHEMA.curie('rna_collect_site'),
                   model_uri=NMDC_SUB_SCHEMA.rna_collect_site, domain=None, range=Optional[str])

slots.rna_concentration = Slot(uri=NMDC_SUB_SCHEMA.rna_concentration, name="rna_concentration", curie=NMDC_SUB_SCHEMA.curie('rna_concentration'),
                   model_uri=NMDC_SUB_SCHEMA.rna_concentration, domain=None, range=Optional[str])

slots.rna_cont_type = Slot(uri=NMDC_SUB_SCHEMA.rna_cont_type, name="rna_cont_type", curie=NMDC_SUB_SCHEMA.curie('rna_cont_type'),
                   model_uri=NMDC_SUB_SCHEMA.rna_cont_type, domain=None, range=Optional[Union[str, "RnaContTypeEnum"]])

slots.rna_cont_well = Slot(uri=NMDC_SUB_SCHEMA.rna_cont_well, name="rna_cont_well", curie=NMDC_SUB_SCHEMA.curie('rna_cont_well'),
                   model_uri=NMDC_SUB_SCHEMA.rna_cont_well, domain=None, range=Optional[str])

slots.rna_container_ID = Slot(uri=NMDC_SUB_SCHEMA.rna_container_ID, name="rna_container_ID", curie=NMDC_SUB_SCHEMA.curie('rna_container_ID'),
                   model_uri=NMDC_SUB_SCHEMA.rna_container_ID, domain=None, range=Optional[str])

slots.rna_isolate_meth = Slot(uri=NMDC_SUB_SCHEMA.rna_isolate_meth, name="rna_isolate_meth", curie=NMDC_SUB_SCHEMA.curie('rna_isolate_meth'),
                   model_uri=NMDC_SUB_SCHEMA.rna_isolate_meth, domain=None, range=Optional[str])

slots.rna_organisms = Slot(uri=NMDC_SUB_SCHEMA.rna_organisms, name="rna_organisms", curie=NMDC_SUB_SCHEMA.curie('rna_organisms'),
                   model_uri=NMDC_SUB_SCHEMA.rna_organisms, domain=None, range=Optional[str])

slots.rna_project_contact = Slot(uri=NMDC_SUB_SCHEMA.rna_project_contact, name="rna_project_contact", curie=NMDC_SUB_SCHEMA.curie('rna_project_contact'),
                   model_uri=NMDC_SUB_SCHEMA.rna_project_contact, domain=None, range=Optional[str])

slots.rna_samp_ID = Slot(uri=NMDC_SUB_SCHEMA.rna_samp_ID, name="rna_samp_ID", curie=NMDC_SUB_SCHEMA.curie('rna_samp_ID'),
                   model_uri=NMDC_SUB_SCHEMA.rna_samp_ID, domain=None, range=Optional[str])

slots.rna_sample_format = Slot(uri=NMDC_SUB_SCHEMA.rna_sample_format, name="rna_sample_format", curie=NMDC_SUB_SCHEMA.curie('rna_sample_format'),
                   model_uri=NMDC_SUB_SCHEMA.rna_sample_format, domain=None, range=Optional[Union[str, "RnaSampleFormatEnum"]])

slots.rna_sample_name = Slot(uri=NMDC_SUB_SCHEMA.rna_sample_name, name="rna_sample_name", curie=NMDC_SUB_SCHEMA.curie('rna_sample_name'),
                   model_uri=NMDC_SUB_SCHEMA.rna_sample_name, domain=None, range=Optional[str])

slots.rna_seq_project = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project, name="rna_seq_project", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project, domain=None, range=Optional[str])

slots.rna_seq_project_PI = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project_PI, name="rna_seq_project_PI", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project_PI'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project_PI, domain=None, range=Optional[str])

slots.rna_seq_project_name = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project_name, name="rna_seq_project_name", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project_name'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project_name, domain=None, range=Optional[str])

slots.rna_volume = Slot(uri=NMDC_SUB_SCHEMA.rna_volume, name="rna_volume", curie=NMDC_SUB_SCHEMA.curie('rna_volume'),
                   model_uri=NMDC_SUB_SCHEMA.rna_volume, domain=None, range=Optional[str])

slots.sample_link = Slot(uri=NMDC_SUB_SCHEMA.sample_link, name="sample_link", curie=NMDC_SUB_SCHEMA.curie('sample_link'),
                   model_uri=NMDC_SUB_SCHEMA.sample_link, domain=None, range=Optional[str])

slots.sample_shipped = Slot(uri=NMDC_SUB_SCHEMA.sample_shipped, name="sample_shipped", curie=NMDC_SUB_SCHEMA.curie('sample_shipped'),
                   model_uri=NMDC_SUB_SCHEMA.sample_shipped, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=NMDC_SUB_SCHEMA.sample_type, name="sample_type", curie=NMDC_SUB_SCHEMA.curie('sample_type'),
                   model_uri=NMDC_SUB_SCHEMA.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.sediment_data = Slot(uri=NMDC_SUB_SCHEMA.sediment_data, name="sediment_data", curie=NMDC_SUB_SCHEMA.curie('sediment_data'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_data, domain=None, range=Optional[Union[Union[dict, Sediment], List[Union[dict, Sediment]]]])

slots.soil_data = Slot(uri=NMDC_SUB_SCHEMA.soil_data, name="soil_data", curie=NMDC_SUB_SCHEMA.curie('soil_data'),
                   model_uri=NMDC_SUB_SCHEMA.soil_data, domain=None, range=Optional[Union[Union[dict, Soil], List[Union[dict, Soil]]]])

slots.start_date_inc = Slot(uri=NMDC_SUB_SCHEMA.start_date_inc, name="start_date_inc", curie=NMDC_SUB_SCHEMA.curie('start_date_inc'),
                   model_uri=NMDC_SUB_SCHEMA.start_date_inc, domain=None, range=Optional[str])

slots.start_time_inc = Slot(uri=NMDC_SUB_SCHEMA.start_time_inc, name="start_time_inc", curie=NMDC_SUB_SCHEMA.curie('start_time_inc'),
                   model_uri=NMDC_SUB_SCHEMA.start_time_inc, domain=None, range=Optional[str])

slots.technical_reps = Slot(uri=NMDC_SUB_SCHEMA.technical_reps, name="technical_reps", curie=NMDC_SUB_SCHEMA.curie('technical_reps'),
                   model_uri=NMDC_SUB_SCHEMA.technical_reps, domain=None, range=Optional[str])

slots.type = Slot(uri=NMDC_SUB_SCHEMA.type, name="type", curie=NMDC_SUB_SCHEMA.curie('type'),
                   model_uri=NMDC_SUB_SCHEMA.type, domain=None, range=Optional[str])

slots.wastewater_sludge_data = Slot(uri=NMDC_SUB_SCHEMA.wastewater_sludge_data, name="wastewater_sludge_data", curie=NMDC_SUB_SCHEMA.curie('wastewater_sludge_data'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_data, domain=None, range=Optional[Union[Union[dict, WastewaterSludge], List[Union[dict, WastewaterSludge]]]])

slots.water_data = Slot(uri=NMDC_SUB_SCHEMA.water_data, name="water_data", curie=NMDC_SUB_SCHEMA.curie('water_data'),
                   model_uri=NMDC_SUB_SCHEMA.water_data, domain=None, range=Optional[Union[Union[dict, Water], List[Union[dict, Water]]]])

slots.abs_air_humidity = Slot(uri=MIXS['0000122'], name="abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=NMDC_SUB_SCHEMA.abs_air_humidity, domain=None, range=Optional[str])

slots.add_recov_method = Slot(uri=MIXS['0001009'], name="add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=NMDC_SUB_SCHEMA.add_recov_method, domain=None, range=Optional[str])

slots.additional_info = Slot(uri=MIXS['0000300'], name="additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC_SUB_SCHEMA.additional_info, domain=None, range=Optional[str])

slots.address = Slot(uri=MIXS['0000218'], name="address", curie=MIXS.curie('0000218'),
                   model_uri=NMDC_SUB_SCHEMA.address, domain=None, range=Optional[str])

slots.adj_room = Slot(uri=MIXS['0000219'], name="adj_room", curie=MIXS.curie('0000219'),
                   model_uri=NMDC_SUB_SCHEMA.adj_room, domain=None, range=Optional[str])

slots.aero_struc = Slot(uri=MIXS['0000773'], name="aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=NMDC_SUB_SCHEMA.aero_struc, domain=None, range=Optional[str])

slots.agrochem_addition = Slot(uri=MIXS['0000639'], name="agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_SUB_SCHEMA.agrochem_addition, domain=None, range=Optional[Union[str, List[str]]])

slots.air_PM_concen = Slot(uri=MIXS['0000108'], name="air_PM_concen", curie=MIXS.curie('0000108'),
                   model_uri=NMDC_SUB_SCHEMA.air_PM_concen, domain=None, range=Optional[Union[str, List[str]]])

slots.air_temp = Slot(uri=MIXS['0000113'], name="air_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.air_temp, domain=Air, range=Optional[str])

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.air_temp_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.al_sat = Slot(uri=MIXS['0000607'], name="al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_SUB_SCHEMA.al_sat, domain=None, range=Optional[str])

slots.al_sat_meth = Slot(uri=MIXS['0000324'], name="al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_SUB_SCHEMA.al_sat_meth, domain=None, range=Optional[str])

slots.alkalinity = Slot(uri=MIXS['0000421'], name="alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.alkalinity, domain=None, range=Optional[str])

slots.alkalinity_method = Slot(uri=MIXS['0000298'], name="alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.alkalinity_method, domain=None, range=Optional[str])

slots.alkyl_diethers = Slot(uri=MIXS['0000490'], name="alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.alkyl_diethers, domain=None, range=Optional[str])

slots.alt = Slot(uri=MIXS['0000094'], name="alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.alt, domain=None, range=Optional[str])

slots.aminopept_act = Slot(uri=MIXS['0000172'], name="aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.aminopept_act, domain=None, range=Optional[str])

slots.ammonium = Slot(uri=MIXS['0000427'], name="ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.ammonium, domain=None, range=Optional[str])

slots.ammonium_nitrogen = Slot(uri=NMDC_SUB_SCHEMA.ammonium_nitrogen, name="ammonium_nitrogen", curie=NMDC_SUB_SCHEMA.curie('ammonium_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.ammonium_nitrogen, domain=None, range=Optional[str])

slots.amount_light = Slot(uri=MIXS['0000140'], name="amount_light", curie=MIXS.curie('0000140'),
                   model_uri=NMDC_SUB_SCHEMA.amount_light, domain=None, range=Optional[str])

slots.ances_data = Slot(uri=MIXS['0000247'], name="ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC_SUB_SCHEMA.ances_data, domain=None, range=Optional[str])

slots.annual_precpt = Slot(uri=MIXS['0000644'], name="annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_SUB_SCHEMA.annual_precpt, domain=None, range=Optional[str])

slots.annual_temp = Slot(uri=MIXS['0000642'], name="annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_SUB_SCHEMA.annual_temp, domain=None, range=Optional[str])

slots.antibiotic_regm = Slot(uri=MIXS['0000553'], name="antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=NMDC_SUB_SCHEMA.antibiotic_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.api = Slot(uri=MIXS['0000157'], name="api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC_SUB_SCHEMA.api, domain=None, range=Optional[str])

slots.arch_struc = Slot(uri=MIXS['0000774'], name="arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=NMDC_SUB_SCHEMA.arch_struc, domain=None, range=Optional[Union[str, "ArchStrucEnum"]])

slots.aromatics_pc = Slot(uri=MIXS['0000133'], name="aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC_SUB_SCHEMA.aromatics_pc, domain=None, range=Optional[str])

slots.asphaltenes_pc = Slot(uri=MIXS['0000135'], name="asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC_SUB_SCHEMA.asphaltenes_pc, domain=None, range=Optional[str])

slots.atmospheric_data = Slot(uri=MIXS['0001097'], name="atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=NMDC_SUB_SCHEMA.atmospheric_data, domain=None, range=Optional[Union[str, List[str]]])

slots.avg_dew_point = Slot(uri=MIXS['0000141'], name="avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=NMDC_SUB_SCHEMA.avg_dew_point, domain=None, range=Optional[str])

slots.avg_occup = Slot(uri=MIXS['0000775'], name="avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=NMDC_SUB_SCHEMA.avg_occup, domain=None, range=Optional[str])

slots.avg_temp = Slot(uri=MIXS['0000142'], name="avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=NMDC_SUB_SCHEMA.avg_temp, domain=None, range=Optional[str])

slots.bac_prod = Slot(uri=MIXS['0000683'], name="bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=NMDC_SUB_SCHEMA.bac_prod, domain=None, range=Optional[str])

slots.bac_resp = Slot(uri=MIXS['0000684'], name="bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=NMDC_SUB_SCHEMA.bac_resp, domain=None, range=Optional[str])

slots.bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.bacteria_carb_prod, domain=None, range=Optional[str])

slots.barometric_press = Slot(uri=MIXS['0000096'], name="barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=NMDC_SUB_SCHEMA.barometric_press, domain=None, range=Optional[str])

slots.basin = Slot(uri=MIXS['0000290'], name="basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC_SUB_SCHEMA.basin, domain=None, range=Optional[str])

slots.bathroom_count = Slot(uri=MIXS['0000776'], name="bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=NMDC_SUB_SCHEMA.bathroom_count, domain=None, range=Optional[str])

slots.bedroom_count = Slot(uri=MIXS['0000777'], name="bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=NMDC_SUB_SCHEMA.bedroom_count, domain=None, range=Optional[str])

slots.benzene = Slot(uri=MIXS['0000153'], name="benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC_SUB_SCHEMA.benzene, domain=None, range=Optional[str])

slots.biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=NMDC_SUB_SCHEMA.biochem_oxygen_dem, domain=None, range=Optional[str])

slots.biocide = Slot(uri=MIXS['0001011'], name="biocide", curie=MIXS.curie('0001011'),
                   model_uri=NMDC_SUB_SCHEMA.biocide, domain=None, range=Optional[str])

slots.biocide_admin_method = Slot(uri=MIXS['0000456'], name="biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=NMDC_SUB_SCHEMA.biocide_admin_method, domain=None, range=Optional[str])

slots.biol_stat = Slot(uri=MIXS['0000858'], name="biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC_SUB_SCHEMA.biol_stat, domain=None, range=Optional[Union[str, "BiolStatEnum"]])

slots.biomass = Slot(uri=MIXS['0000174'], name="biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.biomass, domain=None, range=Optional[Union[str, List[str]]])

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.biotic_regm, domain=None, range=Optional[str])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_SUB_SCHEMA.biotic_relationship, domain=None, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.bishomohopanol = Slot(uri=MIXS['0000175'], name="bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.bishomohopanol, domain=None, range=Optional[str])

slots.blood_press_diast = Slot(uri=MIXS['0000258'], name="blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=NMDC_SUB_SCHEMA.blood_press_diast, domain=None, range=Optional[str])

slots.blood_press_syst = Slot(uri=MIXS['0000259'], name="blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=NMDC_SUB_SCHEMA.blood_press_syst, domain=None, range=Optional[str])

slots.bromide = Slot(uri=MIXS['0000176'], name="bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.bromide, domain=None, range=Optional[str])

slots.build_docs = Slot(uri=MIXS['0000787'], name="build_docs", curie=MIXS.curie('0000787'),
                   model_uri=NMDC_SUB_SCHEMA.build_docs, domain=None, range=Optional[Union[str, "BuildDocsEnum"]])

slots.build_occup_type = Slot(uri=MIXS['0000761'], name="build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=NMDC_SUB_SCHEMA.build_occup_type, domain=None, range=Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]])

slots.building_setting = Slot(uri=MIXS['0000768'], name="building_setting", curie=MIXS.curie('0000768'),
                   model_uri=NMDC_SUB_SCHEMA.building_setting, domain=None, range=Optional[Union[str, "BuildingSettingEnum"]])

slots.built_struc_age = Slot(uri=MIXS['0000145'], name="built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=NMDC_SUB_SCHEMA.built_struc_age, domain=None, range=Optional[str])

slots.built_struc_set = Slot(uri=MIXS['0000778'], name="built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=NMDC_SUB_SCHEMA.built_struc_set, domain=None, range=Optional[str])

slots.built_struc_type = Slot(uri=MIXS['0000721'], name="built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=NMDC_SUB_SCHEMA.built_struc_type, domain=None, range=Optional[str])

slots.calcium = Slot(uri=MIXS['0000432'], name="calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.calcium, domain=None, range=Optional[str])

slots.carb_dioxide = Slot(uri=MIXS['0000097'], name="carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC_SUB_SCHEMA.carb_dioxide, domain=None, range=Optional[str])

slots.carb_monoxide = Slot(uri=MIXS['0000098'], name="carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=NMDC_SUB_SCHEMA.carb_monoxide, domain=None, range=Optional[str])

slots.carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.carb_nitro_ratio, domain=None, range=Optional[str])

slots.ceil_area = Slot(uri=MIXS['0000148'], name="ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_area, domain=None, range=Optional[str])

slots.ceil_cond = Slot(uri=MIXS['0000779'], name="ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_cond, domain=None, range=Optional[Union[str, "CeilCondEnum"]])

slots.ceil_finish_mat = Slot(uri=MIXS['0000780'], name="ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_finish_mat, domain=None, range=Optional[Union[str, "CeilFinishMatEnum"]])

slots.ceil_struc = Slot(uri=MIXS['0000782'], name="ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_struc, domain=None, range=Optional[str])

slots.ceil_texture = Slot(uri=MIXS['0000783'], name="ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_texture, domain=None, range=Optional[Union[str, "CeilTextureEnum"]])

slots.ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_thermal_mass, domain=None, range=Optional[str])

slots.ceil_type = Slot(uri=MIXS['0000784'], name="ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_type, domain=None, range=Optional[Union[str, "CeilTypeEnum"]])

slots.ceil_water_mold = Slot(uri=MIXS['0000781'], name="ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=NMDC_SUB_SCHEMA.ceil_water_mold, domain=None, range=Optional[str])

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.chem_administration, domain=None, range=Optional[Union[str, List[str]]])

slots.chem_mutagen = Slot(uri=MIXS['0000555'], name="chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=NMDC_SUB_SCHEMA.chem_mutagen, domain=None, range=Optional[Union[str, List[str]]])

slots.chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=NMDC_SUB_SCHEMA.chem_oxygen_dem, domain=None, range=Optional[str])

slots.chem_treat_method = Slot(uri=MIXS['0000457'], name="chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=NMDC_SUB_SCHEMA.chem_treat_method, domain=None, range=Optional[str])

slots.chem_treatment = Slot(uri=MIXS['0001012'], name="chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=NMDC_SUB_SCHEMA.chem_treatment, domain=None, range=Optional[str])

slots.chloride = Slot(uri=MIXS['0000429'], name="chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.chloride, domain=None, range=Optional[str])

slots.chlorophyll = Slot(uri=MIXS['0000177'], name="chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.chlorophyll, domain=None, range=Optional[str])

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.climate_environment, domain=None, range=Optional[Union[str, List[str]]])

slots.collection_date = Slot(uri=MIXS['0000011'], name="collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.conduc = Slot(uri=MIXS['0000692'], name="conduc", curie=MIXS.curie('0000692'),
                   model_uri=NMDC_SUB_SCHEMA.conduc, domain=None, range=Optional[str])

slots.cool_syst_id = Slot(uri=MIXS['0000785'], name="cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=NMDC_SUB_SCHEMA.cool_syst_id, domain=None, range=Optional[str])

slots.crop_rotation = Slot(uri=MIXS['0000318'], name="crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_SUB_SCHEMA.crop_rotation, domain=None, range=Optional[str])

slots.cult_root_med = Slot(uri=MIXS['0001041'], name="cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=NMDC_SUB_SCHEMA.cult_root_med, domain=None, range=Optional[str])

slots.cur_land_use = Slot(uri=MIXS['0001080'], name="cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_SUB_SCHEMA.cur_land_use, domain=None, range=Optional[Union[str, "CurLandUseEnum"]])

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_SUB_SCHEMA.cur_vegetation, domain=None, range=Optional[str])

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_SUB_SCHEMA.cur_vegetation_meth, domain=None, range=Optional[str])

slots.date_last_rain = Slot(uri=MIXS['0000786'], name="date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=NMDC_SUB_SCHEMA.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.density = Slot(uri=MIXS['0000435'], name="density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.density, domain=None, range=Optional[str])

slots.depos_env = Slot(uri=MIXS['0000992'], name="depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC_SUB_SCHEMA.depos_env, domain=None, range=Optional[Union[str, "DeposEnvEnum"]])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.depth, domain=None, range=Optional[str])

slots.dew_point = Slot(uri=MIXS['0000129'], name="dew_point", curie=MIXS.curie('0000129'),
                   model_uri=NMDC_SUB_SCHEMA.dew_point, domain=None, range=Optional[str])

slots.diether_lipids = Slot(uri=MIXS['0000178'], name="diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.diether_lipids, domain=None, range=Optional[Union[str, List[str]]])

slots.diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.diss_carb_dioxide, domain=None, range=Optional[str])

slots.diss_hydrogen = Slot(uri=MIXS['0000179'], name="diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.diss_hydrogen, domain=None, range=Optional[str])

slots.diss_inorg_carb = Slot(uri=MIXS['0000434'], name="diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.diss_inorg_carb, domain=None, range=Optional[str])

slots.diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=NMDC_SUB_SCHEMA.diss_inorg_nitro, domain=None, range=Optional[str])

slots.diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.diss_inorg_phosp, domain=None, range=Optional[str])

slots.diss_iron = Slot(uri=MIXS['0000139'], name="diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC_SUB_SCHEMA.diss_iron, domain=None, range=Optional[str])

slots.diss_org_carb = Slot(uri=MIXS['0000433'], name="diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.diss_org_carb, domain=None, range=Optional[str])

slots.diss_org_nitro = Slot(uri=MIXS['0000162'], name="diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.diss_org_nitro, domain=None, range=Optional[str])

slots.diss_oxygen = Slot(uri=MIXS['0000119'], name="diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.diss_oxygen, domain=None, range=Optional[str])

slots.diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC_SUB_SCHEMA.diss_oxygen_fluid, domain=None, range=Optional[str])

slots.dna_cont_well = Slot(uri=NMDC_SUB_SCHEMA.dna_cont_well, name="dna_cont_well", curie=NMDC_SUB_SCHEMA.curie('dna_cont_well'),
                   model_uri=NMDC_SUB_SCHEMA.dna_cont_well, domain=None, range=Optional[str])

slots.door_comp_type = Slot(uri=MIXS['0000795'], name="door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=NMDC_SUB_SCHEMA.door_comp_type, domain=None, range=Optional[Union[str, "DoorCompTypeEnum"]])

slots.door_cond = Slot(uri=MIXS['0000788'], name="door_cond", curie=MIXS.curie('0000788'),
                   model_uri=NMDC_SUB_SCHEMA.door_cond, domain=None, range=Optional[Union[str, "DoorCondEnum"]])

slots.door_direct = Slot(uri=MIXS['0000789'], name="door_direct", curie=MIXS.curie('0000789'),
                   model_uri=NMDC_SUB_SCHEMA.door_direct, domain=None, range=Optional[Union[str, "DoorDirectEnum"]])

slots.door_loc = Slot(uri=MIXS['0000790'], name="door_loc", curie=MIXS.curie('0000790'),
                   model_uri=NMDC_SUB_SCHEMA.door_loc, domain=None, range=Optional[Union[str, "DoorLocEnum"]])

slots.door_mat = Slot(uri=MIXS['0000791'], name="door_mat", curie=MIXS.curie('0000791'),
                   model_uri=NMDC_SUB_SCHEMA.door_mat, domain=None, range=Optional[Union[str, "DoorMatEnum"]])

slots.door_move = Slot(uri=MIXS['0000792'], name="door_move", curie=MIXS.curie('0000792'),
                   model_uri=NMDC_SUB_SCHEMA.door_move, domain=None, range=Optional[Union[str, "DoorMoveEnum"]])

slots.door_size = Slot(uri=MIXS['0000158'], name="door_size", curie=MIXS.curie('0000158'),
                   model_uri=NMDC_SUB_SCHEMA.door_size, domain=None, range=Optional[str])

slots.door_type = Slot(uri=MIXS['0000794'], name="door_type", curie=MIXS.curie('0000794'),
                   model_uri=NMDC_SUB_SCHEMA.door_type, domain=None, range=Optional[Union[str, "DoorTypeEnum"]])

slots.door_type_metal = Slot(uri=MIXS['0000796'], name="door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=NMDC_SUB_SCHEMA.door_type_metal, domain=None, range=Optional[Union[str, "DoorTypeMetalEnum"]])

slots.door_type_wood = Slot(uri=MIXS['0000797'], name="door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=NMDC_SUB_SCHEMA.door_type_wood, domain=None, range=Optional[Union[str, "DoorTypeWoodEnum"]])

slots.door_water_mold = Slot(uri=MIXS['0000793'], name="door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=NMDC_SUB_SCHEMA.door_water_mold, domain=None, range=Optional[str])

slots.down_par = Slot(uri=MIXS['0000703'], name="down_par", curie=MIXS.curie('0000703'),
                   model_uri=NMDC_SUB_SCHEMA.down_par, domain=None, range=Optional[str])

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_SUB_SCHEMA.drainage_class, domain=None, range=Optional[Union[str, "DrainageClassEnum"]])

slots.drawings = Slot(uri=MIXS['0000798'], name="drawings", curie=MIXS.curie('0000798'),
                   model_uri=NMDC_SUB_SCHEMA.drawings, domain=None, range=Optional[Union[str, "DrawingsEnum"]])

slots.ecosystem = Slot(uri=NMDC_SUB_SCHEMA.ecosystem, name="ecosystem", curie=NMDC_SUB_SCHEMA.curie('ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.ecosystem, domain=None, range=Optional[str])

slots.ecosystem_category = Slot(uri=NMDC_SUB_SCHEMA.ecosystem_category, name="ecosystem_category", curie=NMDC_SUB_SCHEMA.curie('ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.ecosystem_category, domain=None, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=NMDC_SUB_SCHEMA.ecosystem_subtype, name="ecosystem_subtype", curie=NMDC_SUB_SCHEMA.curie('ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.ecosystem_subtype, domain=None, range=Optional[str])

slots.ecosystem_type = Slot(uri=NMDC_SUB_SCHEMA.ecosystem_type, name="ecosystem_type", curie=NMDC_SUB_SCHEMA.curie('ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.ecosystem_type, domain=None, range=Optional[str])

slots.efficiency_percent = Slot(uri=MIXS['0000657'], name="efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=NMDC_SUB_SCHEMA.efficiency_percent, domain=None, range=Optional[str])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.elev, domain=None, range=Optional[str])

slots.elevator = Slot(uri=MIXS['0000799'], name="elevator", curie=MIXS.curie('0000799'),
                   model_uri=NMDC_SUB_SCHEMA.elevator, domain=None, range=Optional[str])

slots.emulsions = Slot(uri=MIXS['0000660'], name="emulsions", curie=MIXS.curie('0000660'),
                   model_uri=NMDC_SUB_SCHEMA.emulsions, domain=None, range=Optional[Union[str, List[str]]])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.env_broad_scale, domain=None, range=Optional[str])

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.env_local_scale, domain=None, range=Optional[str])

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.env_medium, domain=None, range=Optional[str])

slots.escalator = Slot(uri=MIXS['0000800'], name="escalator", curie=MIXS.curie('0000800'),
                   model_uri=NMDC_SUB_SCHEMA.escalator, domain=None, range=Optional[str])

slots.ethylbenzene = Slot(uri=MIXS['0000155'], name="ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC_SUB_SCHEMA.ethylbenzene, domain=None, range=Optional[str])

slots.exp_duct = Slot(uri=MIXS['0000144'], name="exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=NMDC_SUB_SCHEMA.exp_duct, domain=None, range=Optional[str])

slots.exp_pipe = Slot(uri=MIXS['0000220'], name="exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=NMDC_SUB_SCHEMA.exp_pipe, domain=None, range=Optional[str])

slots.experimental_factor = Slot(uri=MIXS['0000008'], name="experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.experimental_factor, domain=None, range=Optional[str])

slots.ext_door = Slot(uri=MIXS['0000170'], name="ext_door", curie=MIXS.curie('0000170'),
                   model_uri=NMDC_SUB_SCHEMA.ext_door, domain=None, range=Optional[str])

slots.ext_wall_orient = Slot(uri=MIXS['0000817'], name="ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=NMDC_SUB_SCHEMA.ext_wall_orient, domain=None, range=Optional[Union[str, "ExtWallOrientEnum"]])

slots.ext_window_orient = Slot(uri=MIXS['0000818'], name="ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=NMDC_SUB_SCHEMA.ext_window_orient, domain=None, range=Optional[Union[str, "ExtWindowOrientEnum"]])

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_SUB_SCHEMA.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_SUB_SCHEMA.fao_class, domain=None, range=Optional[Union[str, "FaoClassEnum"]])

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC_SUB_SCHEMA.fertilizer_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.field, domain=None, range=Optional[str])

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC_SUB_SCHEMA.filter_type, domain=None, range=Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_SUB_SCHEMA.fire, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC_SUB_SCHEMA.fireplace_type, domain=None, range=Optional[str])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_SUB_SCHEMA.flooding, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.floor_age = Slot(uri=MIXS['0000164'], name="floor_age", curie=MIXS.curie('0000164'),
                   model_uri=NMDC_SUB_SCHEMA.floor_age, domain=None, range=Optional[str])

slots.floor_area = Slot(uri=MIXS['0000165'], name="floor_area", curie=MIXS.curie('0000165'),
                   model_uri=NMDC_SUB_SCHEMA.floor_area, domain=None, range=Optional[str])

slots.floor_cond = Slot(uri=MIXS['0000803'], name="floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=NMDC_SUB_SCHEMA.floor_cond, domain=None, range=Optional[Union[str, "FloorCondEnum"]])

slots.floor_count = Slot(uri=MIXS['0000225'], name="floor_count", curie=MIXS.curie('0000225'),
                   model_uri=NMDC_SUB_SCHEMA.floor_count, domain=None, range=Optional[str])

slots.floor_finish_mat = Slot(uri=MIXS['0000804'], name="floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=NMDC_SUB_SCHEMA.floor_finish_mat, domain=None, range=Optional[Union[str, "FloorFinishMatEnum"]])

slots.floor_struc = Slot(uri=MIXS['0000806'], name="floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=NMDC_SUB_SCHEMA.floor_struc, domain=None, range=Optional[Union[str, "FloorStrucEnum"]])

slots.floor_thermal_mass = Slot(uri=MIXS['0000166'], name="floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=NMDC_SUB_SCHEMA.floor_thermal_mass, domain=None, range=Optional[str])

slots.floor_water_mold = Slot(uri=MIXS['0000805'], name="floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=NMDC_SUB_SCHEMA.floor_water_mold, domain=None, range=Optional[Union[str, "FloorWaterMoldEnum"]])

slots.fluor = Slot(uri=MIXS['0000704'], name="fluor", curie=MIXS.curie('0000704'),
                   model_uri=NMDC_SUB_SCHEMA.fluor, domain=None, range=Optional[str])

slots.freq_clean = Slot(uri=MIXS['0000226'], name="freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=NMDC_SUB_SCHEMA.freq_clean, domain=None, range=Optional[str])

slots.freq_cook = Slot(uri=MIXS['0000227'], name="freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=NMDC_SUB_SCHEMA.freq_cook, domain=None, range=Optional[str])

slots.fungicide_regm = Slot(uri=MIXS['0000557'], name="fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=NMDC_SUB_SCHEMA.fungicide_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.furniture = Slot(uri=MIXS['0000807'], name="furniture", curie=MIXS.curie('0000807'),
                   model_uri=NMDC_SUB_SCHEMA.furniture, domain=None, range=Optional[Union[str, "FurnitureEnum"]])

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.gaseous_environment, domain=None, range=Optional[Union[str, List[str]]])

slots.gaseous_substances = Slot(uri=MIXS['0000661'], name="gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=NMDC_SUB_SCHEMA.gaseous_substances, domain=None, range=Optional[Union[str, List[str]]])

slots.gender_restroom = Slot(uri=MIXS['0000808'], name="gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=NMDC_SUB_SCHEMA.gender_restroom, domain=None, range=Optional[Union[str, "GenderRestroomEnum"]])

slots.genetic_mod = Slot(uri=MIXS['0000859'], name="genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC_SUB_SCHEMA.genetic_mod, domain=None, range=Optional[str])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.geo_loc_name, domain=None, range=Optional[str])

slots.glucosidase_act = Slot(uri=MIXS['0000137'], name="glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.glucosidase_act, domain=None, range=Optional[str])

slots.gravidity = Slot(uri=MIXS['0000875'], name="gravidity", curie=MIXS.curie('0000875'),
                   model_uri=NMDC_SUB_SCHEMA.gravidity, domain=None, range=Optional[str])

slots.gravity = Slot(uri=MIXS['0000559'], name="gravity", curie=MIXS.curie('0000559'),
                   model_uri=NMDC_SUB_SCHEMA.gravity, domain=None, range=Optional[Union[str, List[str]]])

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.growth_facil, domain=None, range=Optional[str])

slots.growth_habit = Slot(uri=MIXS['0001044'], name="growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=NMDC_SUB_SCHEMA.growth_habit, domain=None, range=Optional[Union[str, "GrowthHabitEnum"]])

slots.growth_hormone_regm = Slot(uri=MIXS['0000560'], name="growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=NMDC_SUB_SCHEMA.growth_hormone_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.hall_count = Slot(uri=MIXS['0000228'], name="hall_count", curie=MIXS.curie('0000228'),
                   model_uri=NMDC_SUB_SCHEMA.hall_count, domain=None, range=Optional[str])

slots.handidness = Slot(uri=MIXS['0000809'], name="handidness", curie=MIXS.curie('0000809'),
                   model_uri=NMDC_SUB_SCHEMA.handidness, domain=None, range=Optional[Union[str, "HandidnessEnum"]])

slots.hc_produced = Slot(uri=MIXS['0000989'], name="hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC_SUB_SCHEMA.hc_produced, domain=None, range=Optional[Union[str, "HcProducedEnum"]])

slots.hcr = Slot(uri=MIXS['0000988'], name="hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC_SUB_SCHEMA.hcr, domain=None, range=Optional[Union[str, "HcrEnum"]])

slots.hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fw_salinity, domain=None, range=Optional[str])

slots.hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_geol_age, domain=None, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_pressure, domain=None, range=Optional[str])

slots.hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_temp, domain=None, range=Optional[str])

slots.heat_cool_type = Slot(uri=MIXS['0000766'], name="heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=NMDC_SUB_SCHEMA.heat_cool_type, domain=None, range=Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]])

slots.heat_deliv_loc = Slot(uri=MIXS['0000810'], name="heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=NMDC_SUB_SCHEMA.heat_deliv_loc, domain=None, range=Optional[Union[str, "HeatDelivLocEnum"]])

slots.heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=NMDC_SUB_SCHEMA.heat_sys_deliv_meth, domain=None, range=Optional[str])

slots.heat_system_id = Slot(uri=MIXS['0000833'], name="heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=NMDC_SUB_SCHEMA.heat_system_id, domain=None, range=Optional[str])

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_SUB_SCHEMA.heavy_metals, domain=None, range=Optional[Union[str, List[str]]])

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_SUB_SCHEMA.heavy_metals_meth, domain=None, range=Optional[str])

slots.height_carper_fiber = Slot(uri=MIXS['0000167'], name="height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=NMDC_SUB_SCHEMA.height_carper_fiber, domain=None, range=Optional[str])

slots.herbicide_regm = Slot(uri=MIXS['0000561'], name="herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=NMDC_SUB_SCHEMA.herbicide_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.horizon_meth = Slot(uri=MIXS['0000321'], name="horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.horizon_meth, domain=None, range=Optional[str])

slots.host_age = Slot(uri=MIXS['0000255'], name="host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC_SUB_SCHEMA.host_age, domain=None, range=Optional[str])

slots.host_body_habitat = Slot(uri=MIXS['0000866'], name="host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=NMDC_SUB_SCHEMA.host_body_habitat, domain=None, range=Optional[str])

slots.host_body_product = Slot(uri=MIXS['0000888'], name="host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=NMDC_SUB_SCHEMA.host_body_product, domain=None, range=Optional[str])

slots.host_body_site = Slot(uri=MIXS['0000867'], name="host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=NMDC_SUB_SCHEMA.host_body_site, domain=None, range=Optional[str])

slots.host_body_temp = Slot(uri=MIXS['0000274'], name="host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=NMDC_SUB_SCHEMA.host_body_temp, domain=None, range=Optional[str])

slots.host_color = Slot(uri=MIXS['0000260'], name="host_color", curie=MIXS.curie('0000260'),
                   model_uri=NMDC_SUB_SCHEMA.host_color, domain=None, range=Optional[str])

slots.host_common_name = Slot(uri=MIXS['0000248'], name="host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC_SUB_SCHEMA.host_common_name, domain=None, range=Optional[str])

slots.host_diet = Slot(uri=MIXS['0000869'], name="host_diet", curie=MIXS.curie('0000869'),
                   model_uri=NMDC_SUB_SCHEMA.host_diet, domain=None, range=Optional[Union[str, List[str]]])

slots.host_dry_mass = Slot(uri=MIXS['0000257'], name="host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC_SUB_SCHEMA.host_dry_mass, domain=None, range=Optional[str])

slots.host_family_relation = Slot(uri=MIXS['0000872'], name="host_family_relation", curie=MIXS.curie('0000872'),
                   model_uri=NMDC_SUB_SCHEMA.host_family_relation, domain=None, range=Optional[Union[str, List[str]]])

slots.host_genotype = Slot(uri=MIXS['0000365'], name="host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC_SUB_SCHEMA.host_genotype, domain=None, range=Optional[str])

slots.host_growth_cond = Slot(uri=MIXS['0000871'], name="host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=NMDC_SUB_SCHEMA.host_growth_cond, domain=None, range=Optional[str])

slots.host_height = Slot(uri=MIXS['0000264'], name="host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC_SUB_SCHEMA.host_height, domain=None, range=Optional[str])

slots.host_last_meal = Slot(uri=MIXS['0000870'], name="host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=NMDC_SUB_SCHEMA.host_last_meal, domain=None, range=Optional[Union[str, List[str]]])

slots.host_length = Slot(uri=MIXS['0000256'], name="host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC_SUB_SCHEMA.host_length, domain=None, range=Optional[str])

slots.host_life_stage = Slot(uri=MIXS['0000251'], name="host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC_SUB_SCHEMA.host_life_stage, domain=None, range=Optional[str])

slots.host_phenotype = Slot(uri=MIXS['0000874'], name="host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC_SUB_SCHEMA.host_phenotype, domain=None, range=Optional[str])

slots.host_sex = Slot(uri=MIXS['0000811'], name="host_sex", curie=MIXS.curie('0000811'),
                   model_uri=NMDC_SUB_SCHEMA.host_sex, domain=None, range=Optional[Union[str, "HostSexEnum"]])

slots.host_shape = Slot(uri=MIXS['0000261'], name="host_shape", curie=MIXS.curie('0000261'),
                   model_uri=NMDC_SUB_SCHEMA.host_shape, domain=None, range=Optional[str])

slots.host_subject_id = Slot(uri=MIXS['0000861'], name="host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=NMDC_SUB_SCHEMA.host_subject_id, domain=None, range=Optional[str])

slots.host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC_SUB_SCHEMA.host_subspecf_genlin, domain=None, range=Optional[Union[str, List[str]]])

slots.host_substrate = Slot(uri=MIXS['0000252'], name="host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=NMDC_SUB_SCHEMA.host_substrate, domain=None, range=Optional[str])

slots.host_symbiont = Slot(uri=MIXS['0001298'], name="host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC_SUB_SCHEMA.host_symbiont, domain=None, range=Optional[Union[str, List[str]]])

slots.host_taxid = Slot(uri=MIXS['0000250'], name="host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC_SUB_SCHEMA.host_taxid, domain=None, range=Optional[str])

slots.host_tot_mass = Slot(uri=MIXS['0000263'], name="host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC_SUB_SCHEMA.host_tot_mass, domain=None, range=Optional[str])

slots.host_wet_mass = Slot(uri=MIXS['0000567'], name="host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=NMDC_SUB_SCHEMA.host_wet_mass, domain=None, range=Optional[str])

slots.humidity = Slot(uri=MIXS['0000100'], name="humidity", curie=MIXS.curie('0000100'),
                   model_uri=NMDC_SUB_SCHEMA.humidity, domain=None, range=Optional[str])

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.humidity_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.indoor_space = Slot(uri=MIXS['0000763'], name="indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=NMDC_SUB_SCHEMA.indoor_space, domain=None, range=Optional[Union[str, "IndoorSpaceEnum"]])

slots.indoor_surf = Slot(uri=MIXS['0000764'], name="indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=NMDC_SUB_SCHEMA.indoor_surf, domain=None, range=Optional[Union[str, "IndoorSurfEnum"]])

slots.indust_eff_percent = Slot(uri=MIXS['0000662'], name="indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=NMDC_SUB_SCHEMA.indust_eff_percent, domain=None, range=Optional[str])

slots.inorg_particles = Slot(uri=MIXS['0000664'], name="inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=NMDC_SUB_SCHEMA.inorg_particles, domain=None, range=Optional[Union[str, List[str]]])

slots.inside_lux = Slot(uri=MIXS['0000168'], name="inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=NMDC_SUB_SCHEMA.inside_lux, domain=None, range=Optional[str])

slots.int_wall_cond = Slot(uri=MIXS['0000813'], name="int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=NMDC_SUB_SCHEMA.int_wall_cond, domain=None, range=Optional[Union[str, "IntWallCondEnum"]])

slots.iw_bt_date_well = Slot(uri=MIXS['0001010'], name="iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=NMDC_SUB_SCHEMA.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.iwf = Slot(uri=MIXS['0000455'], name="iwf", curie=MIXS.curie('0000455'),
                   model_uri=NMDC_SUB_SCHEMA.iwf, domain=None, range=Optional[str])

slots.last_clean = Slot(uri=MIXS['0000814'], name="last_clean", curie=MIXS.curie('0000814'),
                   model_uri=NMDC_SUB_SCHEMA.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]])

slots.lbc_thirty = Slot(uri=NMDC_SUB_SCHEMA.lbc_thirty, name="lbc_thirty", curie=NMDC_SUB_SCHEMA.curie('lbc_thirty'),
                   model_uri=NMDC_SUB_SCHEMA.lbc_thirty, domain=None, range=Optional[str])

slots.lbceq = Slot(uri=NMDC_SUB_SCHEMA.lbceq, name="lbceq", curie=NMDC_SUB_SCHEMA.curie('lbceq'),
                   model_uri=NMDC_SUB_SCHEMA.lbceq, domain=None, range=Optional[str])

slots.light_intensity = Slot(uri=MIXS['0000706'], name="light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=NMDC_SUB_SCHEMA.light_intensity, domain=None, range=Optional[str])

slots.light_regm = Slot(uri=MIXS['0000569'], name="light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.light_regm, domain=None, range=Optional[str])

slots.light_type = Slot(uri=MIXS['0000769'], name="light_type", curie=MIXS.curie('0000769'),
                   model_uri=NMDC_SUB_SCHEMA.light_type, domain=None, range=Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]])

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_SUB_SCHEMA.link_class_info, domain=None, range=Optional[str])

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_SUB_SCHEMA.link_climate_info, domain=None, range=Optional[str])

slots.lithology = Slot(uri=MIXS['0000990'], name="lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC_SUB_SCHEMA.lithology, domain=None, range=Optional[Union[str, "LithologyEnum"]])

slots.local_class = Slot(uri=MIXS['0000330'], name="local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_SUB_SCHEMA.local_class, domain=None, range=Optional[str])

slots.local_class_meth = Slot(uri=MIXS['0000331'], name="local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_SUB_SCHEMA.local_class_meth, domain=None, range=Optional[str])

slots.magnesium = Slot(uri=MIXS['0000431'], name="magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.magnesium, domain=None, range=Optional[str])

slots.manganese = Slot(uri=NMDC_SUB_SCHEMA.manganese, name="manganese", curie=NMDC_SUB_SCHEMA.curie('manganese'),
                   model_uri=NMDC_SUB_SCHEMA.manganese, domain=None, range=Optional[str])

slots.max_occup = Slot(uri=MIXS['0000229'], name="max_occup", curie=MIXS.curie('0000229'),
                   model_uri=NMDC_SUB_SCHEMA.max_occup, domain=None, range=Optional[str])

slots.mean_frict_vel = Slot(uri=MIXS['0000498'], name="mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.mean_frict_vel, domain=None, range=Optional[str])

slots.mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.mean_peak_frict_vel, domain=None, range=Optional[str])

slots.mech_struc = Slot(uri=MIXS['0000815'], name="mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=NMDC_SUB_SCHEMA.mech_struc, domain=None, range=Optional[Union[str, "MechStrucEnum"]])

slots.mechanical_damage = Slot(uri=MIXS['0001052'], name="mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=NMDC_SUB_SCHEMA.mechanical_damage, domain=None, range=Optional[Union[str, List[str]]])

slots.methane = Slot(uri=MIXS['0000101'], name="methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.methane, domain=None, range=Optional[str])

slots.micro_biomass_meth = Slot(uri=MIXS['0000339'], name="micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_SUB_SCHEMA.micro_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_SUB_SCHEMA.microbial_biomass, domain=None, range=Optional[str])

slots.mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=NMDC_SUB_SCHEMA.mineral_nutr_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.misc_param, domain=None, range=Optional[Union[str, List[str]]])

slots.n_alkanes = Slot(uri=MIXS['0000503'], name="n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.n_alkanes, domain=None, range=Optional[Union[str, List[str]]])

slots.nitrate = Slot(uri=MIXS['0000425'], name="nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.nitrate, domain=None, range=Optional[str])

slots.nitrate_nitrogen = Slot(uri=NMDC_SUB_SCHEMA.nitrate_nitrogen, name="nitrate_nitrogen", curie=NMDC_SUB_SCHEMA.curie('nitrate_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.nitrate_nitrogen, domain=None, range=Optional[str])

slots.nitrite = Slot(uri=MIXS['0000426'], name="nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.nitrite, domain=None, range=Optional[str])

slots.nitrite_nitrogen = Slot(uri=NMDC_SUB_SCHEMA.nitrite_nitrogen, name="nitrite_nitrogen", curie=NMDC_SUB_SCHEMA.curie('nitrite_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.nitrite_nitrogen, domain=None, range=Optional[str])

slots.nitro = Slot(uri=MIXS['0000504'], name="nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.nitro, domain=None, range=Optional[str])

slots.non_min_nutr_regm = Slot(uri=MIXS['0000571'], name="non_min_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=NMDC_SUB_SCHEMA.non_min_nutr_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.number_pets = Slot(uri=MIXS['0000231'], name="number_pets", curie=MIXS.curie('0000231'),
                   model_uri=NMDC_SUB_SCHEMA.number_pets, domain=None, range=Optional[str])

slots.number_plants = Slot(uri=MIXS['0000230'], name="number_plants", curie=MIXS.curie('0000230'),
                   model_uri=NMDC_SUB_SCHEMA.number_plants, domain=None, range=Optional[str])

slots.number_resident = Slot(uri=MIXS['0000232'], name="number_resident", curie=MIXS.curie('0000232'),
                   model_uri=NMDC_SUB_SCHEMA.number_resident, domain=None, range=Optional[str])

slots.occup_density_samp = Slot(uri=MIXS['0000217'], name="occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=NMDC_SUB_SCHEMA.occup_density_samp, domain=None, range=Optional[str])

slots.occup_document = Slot(uri=MIXS['0000816'], name="occup_document", curie=MIXS.curie('0000816'),
                   model_uri=NMDC_SUB_SCHEMA.occup_document, domain=None, range=Optional[Union[str, "OccupDocumentEnum"]])

slots.occup_samp = Slot(uri=MIXS['0000772'], name="occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=NMDC_SUB_SCHEMA.occup_samp, domain=None, range=Optional[str])

slots.org_carb = Slot(uri=MIXS['0000508'], name="org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.org_carb, domain=None, range=Optional[str])

slots.org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC_SUB_SCHEMA.org_count_qpcr_info, domain=None, range=Optional[str])

slots.org_matter = Slot(uri=MIXS['0000204'], name="org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.org_matter, domain=None, range=Optional[str])

slots.org_nitro = Slot(uri=MIXS['0000205'], name="org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.org_nitro, domain=None, range=Optional[str])

slots.org_particles = Slot(uri=MIXS['0000665'], name="org_particles", curie=MIXS.curie('0000665'),
                   model_uri=NMDC_SUB_SCHEMA.org_particles, domain=None, range=Optional[Union[str, List[str]]])

slots.organism_count = Slot(uri=MIXS['0000103'], name="organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.organism_count, domain=None, range=Optional[Union[str, List[str]]])

slots.owc_tvdss = Slot(uri=MIXS['0000405'], name="owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=NMDC_SUB_SCHEMA.owc_tvdss, domain=None, range=Optional[str])

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.oxy_stat_samp, domain=None, range=Optional[Union[str, "OxyStatSampEnum"]])

slots.oxygen = Slot(uri=MIXS['0000104'], name="oxygen", curie=MIXS.curie('0000104'),
                   model_uri=NMDC_SUB_SCHEMA.oxygen, domain=None, range=Optional[str])

slots.part_org_carb = Slot(uri=MIXS['0000515'], name="part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.part_org_carb, domain=None, range=Optional[str])

slots.part_org_nitro = Slot(uri=MIXS['0000719'], name="part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=NMDC_SUB_SCHEMA.part_org_nitro, domain=None, range=Optional[str])

slots.particle_class = Slot(uri=MIXS['0000206'], name="particle_class", curie=MIXS.curie('0000206'),
                   model_uri=NMDC_SUB_SCHEMA.particle_class, domain=None, range=Optional[Union[str, List[str]]])

slots.permeability = Slot(uri=MIXS['0000404'], name="permeability", curie=MIXS.curie('0000404'),
                   model_uri=NMDC_SUB_SCHEMA.permeability, domain=None, range=Optional[str])

slots.perturbation = Slot(uri=MIXS['0000754'], name="perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.perturbation, domain=None, range=Optional[Union[str, List[str]]])

slots.pesticide_regm = Slot(uri=MIXS['0000573'], name="pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=NMDC_SUB_SCHEMA.pesticide_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.petroleum_hydrocarb, domain=None, range=Optional[str])

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.ph, domain=None, range=Optional[float])

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.ph_meth, domain=None, range=Optional[str])

slots.ph_regm = Slot(uri=MIXS['0001056'], name="ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=NMDC_SUB_SCHEMA.ph_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.phaeopigments = Slot(uri=MIXS['0000180'], name="phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.phaeopigments, domain=None, range=Optional[Union[str, List[str]]])

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.phosphate, domain=None, range=Optional[str])

slots.phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.phosplipid_fatt_acid, domain=None, range=Optional[Union[str, List[str]]])

slots.photon_flux = Slot(uri=MIXS['0000725'], name="photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=NMDC_SUB_SCHEMA.photon_flux, domain=None, range=Optional[str])

slots.plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=NMDC_SUB_SCHEMA.plant_growth_med, domain=None, range=Optional[str])

slots.plant_product = Slot(uri=MIXS['0001058'], name="plant_product", curie=MIXS.curie('0001058'),
                   model_uri=NMDC_SUB_SCHEMA.plant_product, domain=None, range=Optional[str])

slots.plant_sex = Slot(uri=MIXS['0001059'], name="plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=NMDC_SUB_SCHEMA.plant_sex, domain=None, range=Optional[Union[str, "PlantSexEnum"]])

slots.plant_struc = Slot(uri=MIXS['0001060'], name="plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=NMDC_SUB_SCHEMA.plant_struc, domain=None, range=Optional[str])

slots.pollutants = Slot(uri=MIXS['0000107'], name="pollutants", curie=MIXS.curie('0000107'),
                   model_uri=NMDC_SUB_SCHEMA.pollutants, domain=None, range=Optional[Union[str, List[str]]])

slots.porosity = Slot(uri=MIXS['0000211'], name="porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC_SUB_SCHEMA.porosity, domain=None, range=Optional[str])

slots.potassium = Slot(uri=MIXS['0000430'], name="potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.potassium, domain=None, range=Optional[str])

slots.pour_point = Slot(uri=MIXS['0000127'], name="pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC_SUB_SCHEMA.pour_point, domain=None, range=Optional[str])

slots.pre_treatment = Slot(uri=MIXS['0000348'], name="pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=NMDC_SUB_SCHEMA.pre_treatment, domain=None, range=Optional[str])

slots.pres_animal_insect = Slot(uri=MIXS['0000819'], name="pres_animal_insect", curie=MIXS.curie('0000819'),
                   model_uri=NMDC_SUB_SCHEMA.pres_animal_insect, domain=None, range=Optional[str])

slots.pressure = Slot(uri=MIXS['0000412'], name="pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.pressure, domain=None, range=Optional[str])

slots.prev_land_use_meth = Slot(uri=MIXS['0000316'], name="prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_SUB_SCHEMA.prev_land_use_meth, domain=None, range=Optional[str])

slots.previous_land_use = Slot(uri=MIXS['0000315'], name="previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_SUB_SCHEMA.previous_land_use, domain=None, range=Optional[str])

slots.primary_prod = Slot(uri=MIXS['0000728'], name="primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=NMDC_SUB_SCHEMA.primary_prod, domain=None, range=Optional[str])

slots.primary_treatment = Slot(uri=MIXS['0000349'], name="primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=NMDC_SUB_SCHEMA.primary_treatment, domain=None, range=Optional[str])

slots.prod_rate = Slot(uri=MIXS['0000452'], name="prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=NMDC_SUB_SCHEMA.prod_rate, domain=None, range=Optional[str])

slots.prod_start_date = Slot(uri=MIXS['0001008'], name="prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=NMDC_SUB_SCHEMA.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_SUB_SCHEMA.profile_position, domain=None, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.quad_pos = Slot(uri=MIXS['0000820'], name="quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=NMDC_SUB_SCHEMA.quad_pos, domain=None, range=Optional[Union[str, "QuadPosEnum"]])

slots.radiation_regm = Slot(uri=MIXS['0000575'], name="radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=NMDC_SUB_SCHEMA.radiation_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.rainfall_regm = Slot(uri=MIXS['0000576'], name="rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=NMDC_SUB_SCHEMA.rainfall_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.reactor_type = Slot(uri=MIXS['0000350'], name="reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=NMDC_SUB_SCHEMA.reactor_type, domain=None, range=Optional[str])

slots.redox_potential = Slot(uri=MIXS['0000182'], name="redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.redox_potential, domain=None, range=Optional[str])

slots.rel_air_humidity = Slot(uri=MIXS['0000121'], name="rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=NMDC_SUB_SCHEMA.rel_air_humidity, domain=None, range=Optional[str])

slots.rel_humidity_out = Slot(uri=MIXS['0000188'], name="rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=NMDC_SUB_SCHEMA.rel_humidity_out, domain=None, range=Optional[str])

slots.rel_samp_loc = Slot(uri=MIXS['0000821'], name="rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=NMDC_SUB_SCHEMA.rel_samp_loc, domain=None, range=Optional[Union[str, "RelSampLocEnum"]])

slots.rel_to_oxygen = Slot(uri=MIXS['0000015'], name="rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.rel_to_oxygen, domain=None, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.reservoir = Slot(uri=MIXS['0000303'], name="reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC_SUB_SCHEMA.reservoir, domain=None, range=Optional[str])

slots.resins_pc = Slot(uri=MIXS['0000134'], name="resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC_SUB_SCHEMA.resins_pc, domain=None, range=Optional[str])

slots.room_air_exch_rate = Slot(uri=MIXS['0000169'], name="room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=NMDC_SUB_SCHEMA.room_air_exch_rate, domain=None, range=Optional[str])

slots.room_architec_elem = Slot(uri=MIXS['0000233'], name="room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=NMDC_SUB_SCHEMA.room_architec_elem, domain=None, range=Optional[str])

slots.room_condt = Slot(uri=MIXS['0000822'], name="room_condt", curie=MIXS.curie('0000822'),
                   model_uri=NMDC_SUB_SCHEMA.room_condt, domain=None, range=Optional[Union[str, "RoomCondtEnum"]])

slots.room_connected = Slot(uri=MIXS['0000826'], name="room_connected", curie=MIXS.curie('0000826'),
                   model_uri=NMDC_SUB_SCHEMA.room_connected, domain=None, range=Optional[Union[str, "RoomConnectedEnum"]])

slots.room_count = Slot(uri=MIXS['0000234'], name="room_count", curie=MIXS.curie('0000234'),
                   model_uri=NMDC_SUB_SCHEMA.room_count, domain=None, range=Optional[str])

slots.room_dim = Slot(uri=MIXS['0000192'], name="room_dim", curie=MIXS.curie('0000192'),
                   model_uri=NMDC_SUB_SCHEMA.room_dim, domain=None, range=Optional[str])

slots.room_door_dist = Slot(uri=MIXS['0000193'], name="room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=NMDC_SUB_SCHEMA.room_door_dist, domain=None, range=Optional[str])

slots.room_door_share = Slot(uri=MIXS['0000242'], name="room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=NMDC_SUB_SCHEMA.room_door_share, domain=None, range=Optional[str])

slots.room_hallway = Slot(uri=MIXS['0000238'], name="room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=NMDC_SUB_SCHEMA.room_hallway, domain=None, range=Optional[str])

slots.room_loc = Slot(uri=MIXS['0000823'], name="room_loc", curie=MIXS.curie('0000823'),
                   model_uri=NMDC_SUB_SCHEMA.room_loc, domain=None, range=Optional[Union[str, "RoomLocEnum"]])

slots.room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=NMDC_SUB_SCHEMA.room_moist_dam_hist, domain=None, range=Optional[int])

slots.room_net_area = Slot(uri=MIXS['0000194'], name="room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=NMDC_SUB_SCHEMA.room_net_area, domain=None, range=Optional[str])

slots.room_occup = Slot(uri=MIXS['0000236'], name="room_occup", curie=MIXS.curie('0000236'),
                   model_uri=NMDC_SUB_SCHEMA.room_occup, domain=None, range=Optional[str])

slots.room_samp_pos = Slot(uri=MIXS['0000824'], name="room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=NMDC_SUB_SCHEMA.room_samp_pos, domain=None, range=Optional[Union[str, "RoomSampPosEnum"]])

slots.room_type = Slot(uri=MIXS['0000825'], name="room_type", curie=MIXS.curie('0000825'),
                   model_uri=NMDC_SUB_SCHEMA.room_type, domain=None, range=Optional[Union[str, "RoomTypeEnum"]])

slots.room_vol = Slot(uri=MIXS['0000195'], name="room_vol", curie=MIXS.curie('0000195'),
                   model_uri=NMDC_SUB_SCHEMA.room_vol, domain=None, range=Optional[str])

slots.room_wall_share = Slot(uri=MIXS['0000243'], name="room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=NMDC_SUB_SCHEMA.room_wall_share, domain=None, range=Optional[str])

slots.room_window_count = Slot(uri=MIXS['0000237'], name="room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=NMDC_SUB_SCHEMA.room_window_count, domain=None, range=Optional[int])

slots.root_cond = Slot(uri=MIXS['0001061'], name="root_cond", curie=MIXS.curie('0001061'),
                   model_uri=NMDC_SUB_SCHEMA.root_cond, domain=None, range=Optional[str])

slots.root_med_carbon = Slot(uri=MIXS['0000577'], name="root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_carbon, domain=None, range=Optional[str])

slots.root_med_macronutr = Slot(uri=MIXS['0000578'], name="root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_macronutr, domain=None, range=Optional[str])

slots.root_med_micronutr = Slot(uri=MIXS['0000579'], name="root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_micronutr, domain=None, range=Optional[str])

slots.root_med_ph = Slot(uri=MIXS['0001062'], name="root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_ph, domain=None, range=Optional[str])

slots.root_med_regl = Slot(uri=MIXS['0000581'], name="root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_regl, domain=None, range=Optional[str])

slots.root_med_solid = Slot(uri=MIXS['0001063'], name="root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_solid, domain=None, range=Optional[str])

slots.root_med_suppl = Slot(uri=MIXS['0000580'], name="root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=NMDC_SUB_SCHEMA.root_med_suppl, domain=None, range=Optional[str])

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.salinity, domain=None, range=Optional[str])

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_SUB_SCHEMA.salinity_meth, domain=None, range=Optional[str])

slots.salt_regm = Slot(uri=MIXS['0000582'], name="salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=NMDC_SUB_SCHEMA.salt_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.samp_capt_status = Slot(uri=MIXS['0000860'], name="samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC_SUB_SCHEMA.samp_capt_status, domain=None, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.samp_collec_method, domain=None, range=Optional[str])

slots.samp_collect_point = Slot(uri=MIXS['0001015'], name="samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=NMDC_SUB_SCHEMA.samp_collect_point, domain=None, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.samp_dis_stage = Slot(uri=MIXS['0000249'], name="samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC_SUB_SCHEMA.samp_dis_stage, domain=None, range=Optional[Union[str, "SampDisStageEnum"]])

slots.samp_floor = Slot(uri=MIXS['0000828'], name="samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=NMDC_SUB_SCHEMA.samp_floor, domain=None, range=Optional[Union[str, "SampFloorEnum"]])

slots.samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=NMDC_SUB_SCHEMA.samp_loc_corr_rate, domain=None, range=Optional[str])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.samp_mat_process, domain=None, range=Optional[str])

slots.samp_md = Slot(uri=MIXS['0000413'], name="samp_md", curie=MIXS.curie('0000413'),
                   model_uri=NMDC_SUB_SCHEMA.samp_md, domain=None, range=Optional[str])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC_SUB_SCHEMA.samp_name, domain=None, range=Optional[str])

slots.samp_preserv = Slot(uri=MIXS['0000463'], name="samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=NMDC_SUB_SCHEMA.samp_preserv, domain=None, range=Optional[str])

slots.samp_room_id = Slot(uri=MIXS['0000244'], name="samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=NMDC_SUB_SCHEMA.samp_room_id, domain=None, range=Optional[str])

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.samp_size, domain=None, range=Optional[str])

slots.samp_sort_meth = Slot(uri=MIXS['0000216'], name="samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=NMDC_SUB_SCHEMA.samp_sort_meth, domain=None, range=Optional[Union[str, List[str]]])

slots.samp_store_dur = Slot(uri=MIXS['0000116'], name="samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.samp_store_dur, domain=None, range=Optional[str])

slots.samp_store_loc = Slot(uri=MIXS['0000755'], name="samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.samp_store_loc, domain=None, range=Optional[str])

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.samp_store_temp, domain=None, range=Optional[str])

slots.samp_subtype = Slot(uri=MIXS['0000999'], name="samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC_SUB_SCHEMA.samp_subtype, domain=None, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.samp_time_out = Slot(uri=MIXS['0000196'], name="samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=NMDC_SUB_SCHEMA.samp_time_out, domain=None, range=Optional[str])

slots.samp_transport_cond = Slot(uri=MIXS['0000410'], name="samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC_SUB_SCHEMA.samp_transport_cond, domain=None, range=Optional[str])

slots.samp_tvdss = Slot(uri=MIXS['0000409'], name="samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=NMDC_SUB_SCHEMA.samp_tvdss, domain=None, range=Optional[str])

slots.samp_type = Slot(uri=MIXS['0000998'], name="samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC_SUB_SCHEMA.samp_type, domain=None, range=Optional[str])

slots.samp_weather = Slot(uri=MIXS['0000827'], name="samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=NMDC_SUB_SCHEMA.samp_weather, domain=None, range=Optional[Union[str, "SampWeatherEnum"]])

slots.samp_well_name = Slot(uri=MIXS['0000296'], name="samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC_SUB_SCHEMA.samp_well_name, domain=None, range=Optional[str])

slots.saturates_pc = Slot(uri=MIXS['0000131'], name="saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC_SUB_SCHEMA.saturates_pc, domain=None, range=Optional[str])

slots.season = Slot(uri=MIXS['0000829'], name="season", curie=MIXS.curie('0000829'),
                   model_uri=NMDC_SUB_SCHEMA.season, domain=None, range=Optional[str])

slots.season_environment = Slot(uri=MIXS['0001068'], name="season_environment", curie=MIXS.curie('0001068'),
                   model_uri=NMDC_SUB_SCHEMA.season_environment, domain=None, range=Optional[Union[str, List[str]]])

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_SUB_SCHEMA.season_precpt, domain=None, range=Optional[str])

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_SUB_SCHEMA.season_temp, domain=None, range=Optional[str])

slots.season_use = Slot(uri=MIXS['0000830'], name="season_use", curie=MIXS.curie('0000830'),
                   model_uri=NMDC_SUB_SCHEMA.season_use, domain=None, range=Optional[Union[str, "SeasonUseEnum"]])

slots.secondary_treatment = Slot(uri=MIXS['0000351'], name="secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=NMDC_SUB_SCHEMA.secondary_treatment, domain=None, range=Optional[str])

slots.sediment_type = Slot(uri=MIXS['0001078'], name="sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_type, domain=None, range=Optional[Union[str, "SedimentTypeEnum"]])

slots.sewage_type = Slot(uri=MIXS['0000215'], name="sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=NMDC_SUB_SCHEMA.sewage_type, domain=None, range=Optional[str])

slots.shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=NMDC_SUB_SCHEMA.shad_dev_water_mold, domain=None, range=Optional[str])

slots.shading_device_cond = Slot(uri=MIXS['0000831'], name="shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=NMDC_SUB_SCHEMA.shading_device_cond, domain=None, range=Optional[Union[str, "ShadingDeviceCondEnum"]])

slots.shading_device_loc = Slot(uri=MIXS['0000832'], name="shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=NMDC_SUB_SCHEMA.shading_device_loc, domain=None, range=Optional[str])

slots.shading_device_mat = Slot(uri=MIXS['0000245'], name="shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=NMDC_SUB_SCHEMA.shading_device_mat, domain=None, range=Optional[str])

slots.shading_device_type = Slot(uri=MIXS['0000835'], name="shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=NMDC_SUB_SCHEMA.shading_device_type, domain=None, range=Optional[Union[str, "ShadingDeviceTypeEnum"]])

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_SUB_SCHEMA.sieving, domain=None, range=Optional[str])

slots.silicate = Slot(uri=MIXS['0000184'], name="silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.silicate, domain=None, range=Optional[str])

slots.size_frac = Slot(uri=MIXS['0000017'], name="size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.size_frac, domain=None, range=Optional[str])

slots.size_frac_low = Slot(uri=MIXS['0000735'], name="size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.size_frac_low, domain=None, range=Optional[str])

slots.size_frac_up = Slot(uri=MIXS['0000736'], name="size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.size_frac_up, domain=None, range=Optional[str])

slots.slope_aspect = Slot(uri=MIXS['0000647'], name="slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_SUB_SCHEMA.slope_aspect, domain=None, range=Optional[str])

slots.slope_gradient = Slot(uri=MIXS['0000646'], name="slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_SUB_SCHEMA.slope_gradient, domain=None, range=Optional[str])

slots.sludge_retent_time = Slot(uri=MIXS['0000669'], name="sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=NMDC_SUB_SCHEMA.sludge_retent_time, domain=None, range=Optional[str])

slots.sodium = Slot(uri=MIXS['0000428'], name="sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.sodium, domain=None, range=Optional[str])

slots.soil_horizon = Slot(uri=MIXS['0001082'], name="soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_SUB_SCHEMA.soil_horizon, domain=None, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_SUB_SCHEMA.soil_text_measure, domain=None, range=Optional[str])

slots.soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_SUB_SCHEMA.soil_texture_meth, domain=None, range=Optional[str])

slots.soil_type = Slot(uri=MIXS['0000332'], name="soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_SUB_SCHEMA.soil_type, domain=None, range=Optional[str])

slots.soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_SUB_SCHEMA.soil_type_meth, domain=None, range=Optional[str])

slots.solar_irradiance = Slot(uri=MIXS['0000112'], name="solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=NMDC_SUB_SCHEMA.solar_irradiance, domain=None, range=Optional[str])

slots.soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=NMDC_SUB_SCHEMA.soluble_inorg_mat, domain=None, range=Optional[Union[str, List[str]]])

slots.soluble_org_mat = Slot(uri=MIXS['0000673'], name="soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=NMDC_SUB_SCHEMA.soluble_org_mat, domain=None, range=Optional[Union[str, List[str]]])

slots.soluble_react_phosp = Slot(uri=MIXS['0000738'], name="soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=NMDC_SUB_SCHEMA.soluble_react_phosp, domain=None, range=Optional[str])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC_SUB_SCHEMA.source_mat_id, domain=None, range=Optional[str])

slots.space_typ_state = Slot(uri=MIXS['0000770'], name="space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=NMDC_SUB_SCHEMA.space_typ_state, domain=None, range=Optional[str])

slots.specific = Slot(uri=MIXS['0000836'], name="specific", curie=MIXS.curie('0000836'),
                   model_uri=NMDC_SUB_SCHEMA.specific, domain=None, range=Optional[Union[str, "SpecificEnum"]])

slots.specific_ecosystem = Slot(uri=NMDC_SUB_SCHEMA.specific_ecosystem, name="specific_ecosystem", curie=NMDC_SUB_SCHEMA.curie('specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.specific_ecosystem, domain=None, range=Optional[str])

slots.specific_humidity = Slot(uri=MIXS['0000214'], name="specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=NMDC_SUB_SCHEMA.specific_humidity, domain=None, range=Optional[str])

slots.sr_dep_env = Slot(uri=MIXS['0000996'], name="sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=NMDC_SUB_SCHEMA.sr_dep_env, domain=None, range=Optional[Union[str, "SrDepEnvEnum"]])

slots.sr_geol_age = Slot(uri=MIXS['0000997'], name="sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=NMDC_SUB_SCHEMA.sr_geol_age, domain=None, range=Optional[Union[str, "SrGeolAgeEnum"]])

slots.sr_kerog_type = Slot(uri=MIXS['0000994'], name="sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=NMDC_SUB_SCHEMA.sr_kerog_type, domain=None, range=Optional[Union[str, "SrKerogTypeEnum"]])

slots.sr_lithology = Slot(uri=MIXS['0000995'], name="sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=NMDC_SUB_SCHEMA.sr_lithology, domain=None, range=Optional[Union[str, "SrLithologyEnum"]])

slots.standing_water_regm = Slot(uri=MIXS['0001069'], name="standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=NMDC_SUB_SCHEMA.standing_water_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_SUB_SCHEMA.store_cond, domain=None, range=Optional[str])

slots.substructure_type = Slot(uri=MIXS['0000767'], name="substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=NMDC_SUB_SCHEMA.substructure_type, domain=None, range=Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]])

slots.sulfate = Slot(uri=MIXS['0000423'], name="sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.sulfate, domain=None, range=Optional[str])

slots.sulfate_fw = Slot(uri=MIXS['0000407'], name="sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC_SUB_SCHEMA.sulfate_fw, domain=None, range=Optional[str])

slots.sulfide = Slot(uri=MIXS['0000424'], name="sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.sulfide, domain=None, range=Optional[str])

slots.surf_air_cont = Slot(uri=MIXS['0000759'], name="surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=NMDC_SUB_SCHEMA.surf_air_cont, domain=None, range=Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]])

slots.surf_humidity = Slot(uri=MIXS['0000123'], name="surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=NMDC_SUB_SCHEMA.surf_humidity, domain=None, range=Optional[str])

slots.surf_material = Slot(uri=MIXS['0000758'], name="surf_material", curie=MIXS.curie('0000758'),
                   model_uri=NMDC_SUB_SCHEMA.surf_material, domain=None, range=Optional[Union[str, "SurfMaterialEnum"]])

slots.surf_moisture = Slot(uri=MIXS['0000128'], name="surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=NMDC_SUB_SCHEMA.surf_moisture, domain=None, range=Optional[str])

slots.surf_moisture_ph = Slot(uri=MIXS['0000760'], name="surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=NMDC_SUB_SCHEMA.surf_moisture_ph, domain=None, range=Optional[float])

slots.surf_temp = Slot(uri=MIXS['0000125'], name="surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=NMDC_SUB_SCHEMA.surf_temp, domain=None, range=Optional[str])

slots.suspend_part_matter = Slot(uri=MIXS['0000741'], name="suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=NMDC_SUB_SCHEMA.suspend_part_matter, domain=None, range=Optional[str])

slots.suspend_solids = Slot(uri=MIXS['0000150'], name="suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.suspend_solids, domain=None, range=Optional[Union[str, List[str]]])

slots.tan = Slot(uri=MIXS['0000120'], name="tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC_SUB_SCHEMA.tan, domain=None, range=Optional[str])

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.temp, domain=None, range=Optional[str])

slots.temp_out = Slot(uri=MIXS['0000197'], name="temp_out", curie=MIXS.curie('0000197'),
                   model_uri=NMDC_SUB_SCHEMA.temp_out, domain=None, range=Optional[str])

slots.tertiary_treatment = Slot(uri=MIXS['0000352'], name="tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=NMDC_SUB_SCHEMA.tertiary_treatment, domain=None, range=Optional[str])

slots.tidal_stage = Slot(uri=MIXS['0000750'], name="tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC_SUB_SCHEMA.tidal_stage, domain=None, range=Optional[Union[str, "TidalStageEnum"]])

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_SUB_SCHEMA.tillage, domain=None, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=NMDC_SUB_SCHEMA.tiss_cult_growth_med, domain=None, range=Optional[str])

slots.toluene = Slot(uri=MIXS['0000154'], name="toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC_SUB_SCHEMA.toluene, domain=None, range=Optional[str])

slots.tot_carb = Slot(uri=MIXS['0000525'], name="tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.tot_carb, domain=None, range=Optional[str])

slots.tot_depth_water_col = Slot(uri=MIXS['0000634'], name="tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC_SUB_SCHEMA.tot_depth_water_col, domain=None, range=Optional[str])

slots.tot_diss_nitro = Slot(uri=MIXS['0000744'], name="tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=NMDC_SUB_SCHEMA.tot_diss_nitro, domain=None, range=Optional[str])

slots.tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=NMDC_SUB_SCHEMA.tot_inorg_nitro, domain=None, range=Optional[str])

slots.tot_iron = Slot(uri=MIXS['0000105'], name="tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC_SUB_SCHEMA.tot_iron, domain=None, range=Optional[str])

slots.tot_nitro = Slot(uri=MIXS['0000102'], name="tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.tot_nitro, domain=None, range=Optional[str])

slots.tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_SUB_SCHEMA.tot_nitro_cont_meth, domain=None, range=Optional[str])

slots.tot_nitro_content = Slot(uri=MIXS['0000530'], name="tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.tot_nitro_content, domain=None, range=Optional[str])

slots.tot_org_c_meth = Slot(uri=MIXS['0000337'], name="tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_SUB_SCHEMA.tot_org_c_meth, domain=None, range=Optional[str])

slots.tot_org_carb = Slot(uri=MIXS['0000533'], name="tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.tot_org_carb, domain=None, range=Optional[str])

slots.tot_part_carb = Slot(uri=MIXS['0000747'], name="tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=NMDC_SUB_SCHEMA.tot_part_carb, domain=None, range=Optional[str])

slots.tot_phosp = Slot(uri=MIXS['0000117'], name="tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.tot_phosp, domain=None, range=Optional[str])

slots.tot_phosphate = Slot(uri=MIXS['0000689'], name="tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=NMDC_SUB_SCHEMA.tot_phosphate, domain=None, range=Optional[str])

slots.tot_sulfur = Slot(uri=MIXS['0000419'], name="tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC_SUB_SCHEMA.tot_sulfur, domain=None, range=Optional[str])

slots.train_line = Slot(uri=MIXS['0000837'], name="train_line", curie=MIXS.curie('0000837'),
                   model_uri=NMDC_SUB_SCHEMA.train_line, domain=None, range=Optional[Union[str, "TrainLineEnum"]])

slots.train_stat_loc = Slot(uri=MIXS['0000838'], name="train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=NMDC_SUB_SCHEMA.train_stat_loc, domain=None, range=Optional[Union[str, "TrainStatLocEnum"]])

slots.train_stop_loc = Slot(uri=MIXS['0000839'], name="train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=NMDC_SUB_SCHEMA.train_stop_loc, domain=None, range=Optional[Union[str, "TrainStopLocEnum"]])

slots.turbidity = Slot(uri=MIXS['0000191'], name="turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.turbidity, domain=None, range=Optional[str])

slots.tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC_SUB_SCHEMA.tvdss_of_hcr_press, domain=None, range=Optional[str])

slots.tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC_SUB_SCHEMA.tvdss_of_hcr_temp, domain=None, range=Optional[str])

slots.typ_occup_density = Slot(uri=MIXS['0000771'], name="typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=NMDC_SUB_SCHEMA.typ_occup_density, domain=None, range=Optional[float])

slots.ventilation_rate = Slot(uri=MIXS['0000114'], name="ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=NMDC_SUB_SCHEMA.ventilation_rate, domain=None, range=Optional[str])

slots.ventilation_type = Slot(uri=MIXS['0000756'], name="ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC_SUB_SCHEMA.ventilation_type, domain=None, range=Optional[str])

slots.vfa = Slot(uri=MIXS['0000152'], name="vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC_SUB_SCHEMA.vfa, domain=None, range=Optional[str])

slots.vfa_fw = Slot(uri=MIXS['0000408'], name="vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC_SUB_SCHEMA.vfa_fw, domain=None, range=Optional[str])

slots.vis_media = Slot(uri=MIXS['0000840'], name="vis_media", curie=MIXS.curie('0000840'),
                   model_uri=NMDC_SUB_SCHEMA.vis_media, domain=None, range=Optional[Union[str, "VisMediaEnum"]])

slots.viscosity = Slot(uri=MIXS['0000126'], name="viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC_SUB_SCHEMA.viscosity, domain=None, range=Optional[str])

slots.volatile_org_comp = Slot(uri=MIXS['0000115'], name="volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=NMDC_SUB_SCHEMA.volatile_org_comp, domain=None, range=Optional[Union[str, List[str]]])

slots.wall_area = Slot(uri=MIXS['0000198'], name="wall_area", curie=MIXS.curie('0000198'),
                   model_uri=NMDC_SUB_SCHEMA.wall_area, domain=None, range=Optional[str])

slots.wall_const_type = Slot(uri=MIXS['0000841'], name="wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=NMDC_SUB_SCHEMA.wall_const_type, domain=None, range=Optional[Union[str, "WallConstTypeEnum"]])

slots.wall_finish_mat = Slot(uri=MIXS['0000842'], name="wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=NMDC_SUB_SCHEMA.wall_finish_mat, domain=None, range=Optional[Union[str, "WallFinishMatEnum"]])

slots.wall_height = Slot(uri=MIXS['0000221'], name="wall_height", curie=MIXS.curie('0000221'),
                   model_uri=NMDC_SUB_SCHEMA.wall_height, domain=None, range=Optional[str])

slots.wall_loc = Slot(uri=MIXS['0000843'], name="wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=NMDC_SUB_SCHEMA.wall_loc, domain=None, range=Optional[Union[str, "WallLocEnum"]])

slots.wall_surf_treatment = Slot(uri=MIXS['0000845'], name="wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=NMDC_SUB_SCHEMA.wall_surf_treatment, domain=None, range=Optional[Union[str, "WallSurfTreatmentEnum"]])

slots.wall_texture = Slot(uri=MIXS['0000846'], name="wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=NMDC_SUB_SCHEMA.wall_texture, domain=None, range=Optional[Union[str, "WallTextureEnum"]])

slots.wall_thermal_mass = Slot(uri=MIXS['0000222'], name="wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=NMDC_SUB_SCHEMA.wall_thermal_mass, domain=None, range=Optional[str])

slots.wall_water_mold = Slot(uri=MIXS['0000844'], name="wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=NMDC_SUB_SCHEMA.wall_water_mold, domain=None, range=Optional[str])

slots.wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_type, domain=None, range=Optional[str])

slots.water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_SUB_SCHEMA.water_cont_soil_meth, domain=None, range=Optional[str])

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.water_content, domain=None, range=Optional[str])

slots.water_current = Slot(uri=MIXS['0000203'], name="water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC_SUB_SCHEMA.water_current, domain=None, range=Optional[str])

slots.water_cut = Slot(uri=MIXS['0000454'], name="water_cut", curie=MIXS.curie('0000454'),
                   model_uri=NMDC_SUB_SCHEMA.water_cut, domain=None, range=Optional[str])

slots.water_feat_size = Slot(uri=MIXS['0000223'], name="water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=NMDC_SUB_SCHEMA.water_feat_size, domain=None, range=Optional[str])

slots.water_feat_type = Slot(uri=MIXS['0000847'], name="water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=NMDC_SUB_SCHEMA.water_feat_type, domain=None, range=Optional[Union[str, "WaterFeatTypeEnum"]])

slots.water_prod_rate = Slot(uri=MIXS['0000453'], name="water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=NMDC_SUB_SCHEMA.water_prod_rate, domain=None, range=Optional[str])

slots.water_temp_regm = Slot(uri=MIXS['0000590'], name="water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=NMDC_SUB_SCHEMA.water_temp_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.watering_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.weekday = Slot(uri=MIXS['0000848'], name="weekday", curie=MIXS.curie('0000848'),
                   model_uri=NMDC_SUB_SCHEMA.weekday, domain=None, range=Optional[Union[str, "WeekdayEnum"]])

slots.win = Slot(uri=MIXS['0000297'], name="win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC_SUB_SCHEMA.win, domain=None, range=Optional[str])

slots.wind_direction = Slot(uri=MIXS['0000757'], name="wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=NMDC_SUB_SCHEMA.wind_direction, domain=None, range=Optional[str])

slots.wind_speed = Slot(uri=MIXS['0000118'], name="wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=NMDC_SUB_SCHEMA.wind_speed, domain=None, range=Optional[str])

slots.window_cond = Slot(uri=MIXS['0000849'], name="window_cond", curie=MIXS.curie('0000849'),
                   model_uri=NMDC_SUB_SCHEMA.window_cond, domain=None, range=Optional[Union[str, "WindowCondEnum"]])

slots.window_cover = Slot(uri=MIXS['0000850'], name="window_cover", curie=MIXS.curie('0000850'),
                   model_uri=NMDC_SUB_SCHEMA.window_cover, domain=None, range=Optional[Union[str, "WindowCoverEnum"]])

slots.window_horiz_pos = Slot(uri=MIXS['0000851'], name="window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=NMDC_SUB_SCHEMA.window_horiz_pos, domain=None, range=Optional[Union[str, "WindowHorizPosEnum"]])

slots.window_loc = Slot(uri=MIXS['0000852'], name="window_loc", curie=MIXS.curie('0000852'),
                   model_uri=NMDC_SUB_SCHEMA.window_loc, domain=None, range=Optional[Union[str, "WindowLocEnum"]])

slots.window_mat = Slot(uri=MIXS['0000853'], name="window_mat", curie=MIXS.curie('0000853'),
                   model_uri=NMDC_SUB_SCHEMA.window_mat, domain=None, range=Optional[Union[str, "WindowMatEnum"]])

slots.window_open_freq = Slot(uri=MIXS['0000246'], name="window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=NMDC_SUB_SCHEMA.window_open_freq, domain=None, range=Optional[str])

slots.window_size = Slot(uri=MIXS['0000224'], name="window_size", curie=MIXS.curie('0000224'),
                   model_uri=NMDC_SUB_SCHEMA.window_size, domain=None, range=Optional[str])

slots.window_status = Slot(uri=MIXS['0000855'], name="window_status", curie=MIXS.curie('0000855'),
                   model_uri=NMDC_SUB_SCHEMA.window_status, domain=None, range=Optional[str])

slots.window_type = Slot(uri=MIXS['0000856'], name="window_type", curie=MIXS.curie('0000856'),
                   model_uri=NMDC_SUB_SCHEMA.window_type, domain=None, range=Optional[Union[str, "WindowTypeEnum"]])

slots.window_vert_pos = Slot(uri=MIXS['0000857'], name="window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=NMDC_SUB_SCHEMA.window_vert_pos, domain=None, range=Optional[Union[str, "WindowVertPosEnum"]])

slots.window_water_mold = Slot(uri=MIXS['0000854'], name="window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=NMDC_SUB_SCHEMA.window_water_mold, domain=None, range=Optional[str])

slots.xylene = Slot(uri=MIXS['0000156'], name="xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC_SUB_SCHEMA.xylene, domain=None, range=Optional[str])

slots.zinc = Slot(uri=NMDC_SUB_SCHEMA.zinc, name="zinc", curie=NMDC_SUB_SCHEMA.curie('zinc'),
                   model_uri=NMDC_SUB_SCHEMA.zinc, domain=None, range=Optional[str])

slots.gold_path_field = Slot(uri=NMDC_SUB_SCHEMA.gold_path_field, name="gold_path_field", curie=NMDC_SUB_SCHEMA.curie('gold_path_field'),
                   model_uri=NMDC_SUB_SCHEMA.gold_path_field, domain=None, range=Optional[str])

slots.alternative_identifiers = Slot(uri=NMDC_SUB_SCHEMA.alternative_identifiers, name="alternative_identifiers", curie=NMDC_SUB_SCHEMA.curie('alternative_identifiers'),
                   model_uri=NMDC_SUB_SCHEMA.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=NMDC_SUB_SCHEMA.longitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.longitude])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=NMDC_SUB_SCHEMA.latitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.latitude])

slots.has_minimum_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_minimum_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.id = Slot(uri=NMDC_SUB_SCHEMA.id, name="id", curie=NMDC_SUB_SCHEMA.curie('id'),
                   model_uri=NMDC_SUB_SCHEMA.id, domain=None, range=URIRef)

slots.was_informed_by = Slot(uri=NMDC_SUB_SCHEMA.was_informed_by, name="was_informed_by", curie=NMDC_SUB_SCHEMA.curie('was_informed_by'),
                   model_uri=NMDC_SUB_SCHEMA.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.environment_field = Slot(uri=NMDC_SUB_SCHEMA.environment_field, name="environment field", curie=NMDC_SUB_SCHEMA.curie('environment_field'),
                   model_uri=NMDC_SUB_SCHEMA.environment_field, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_numeric_value, name="has_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.language = Slot(uri=NMDC_SUB_SCHEMA.language, name="language", curie=NMDC_SUB_SCHEMA.curie('language'),
                   model_uri=NMDC_SUB_SCHEMA.language, domain=None, range=Optional[str])

slots.started_at_time = Slot(uri=NMDC_SUB_SCHEMA.started_at_time, name="started_at_time", curie=NMDC_SUB_SCHEMA.curie('started_at_time'),
                   model_uri=NMDC_SUB_SCHEMA.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.startedAtTime])

slots.nucleic_acid_sequence_source_field = Slot(uri=NMDC_SUB_SCHEMA.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=NMDC_SUB_SCHEMA.curie('nucleic_acid_sequence_source_field'),
                   model_uri=NMDC_SUB_SCHEMA.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.name = Slot(uri=NMDC_SUB_SCHEMA.name, name="name", curie=NMDC_SUB_SCHEMA.curie('name'),
                   model_uri=NMDC_SUB_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC_SUB_SCHEMA.description, domain=None, range=Optional[str])

slots.has_maximum_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_maximum_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.ended_at_time = Slot(uri=NMDC_SUB_SCHEMA.ended_at_time, name="ended_at_time", curie=NMDC_SUB_SCHEMA.curie('ended_at_time'),
                   model_uri=NMDC_SUB_SCHEMA.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.endedAtTime])

slots.was_associated_with = Slot(uri=NMDC_SUB_SCHEMA.was_associated_with, name="was_associated_with", curie=NMDC_SUB_SCHEMA.curie('was_associated_with'),
                   model_uri=NMDC_SUB_SCHEMA.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.has_unit = Slot(uri=NMDC_SUB_SCHEMA.has_unit, name="has_unit", curie=NMDC_SUB_SCHEMA.curie('has_unit'),
                   model_uri=NMDC_SUB_SCHEMA.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.core_field = Slot(uri=NMDC_SUB_SCHEMA.core_field, name="core field", curie=NMDC_SUB_SCHEMA.curie('core_field'),
                   model_uri=NMDC_SUB_SCHEMA.core_field, domain=None, range=Optional[str])

slots.term = Slot(uri=NMDC_SUB_SCHEMA.term, name="term", curie=NMDC_SUB_SCHEMA.curie('term'),
                   model_uri=NMDC_SUB_SCHEMA.term, domain=NamedThing, range=Optional[Union[dict, OntologyClass]])

slots.investigation_field = Slot(uri=NMDC_SUB_SCHEMA.investigation_field, name="investigation field", curie=NMDC_SUB_SCHEMA.curie('investigation_field'),
                   model_uri=NMDC_SUB_SCHEMA.investigation_field, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC_SUB_SCHEMA.has_raw_value, name="has_raw_value", curie=NMDC_SUB_SCHEMA.curie('has_raw_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.acted_on_behalf_of = Slot(uri=NMDC_SUB_SCHEMA.acted_on_behalf_of, name="acted_on_behalf_of", curie=NMDC_SUB_SCHEMA.curie('acted_on_behalf_of'),
                   model_uri=NMDC_SUB_SCHEMA.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.was_generated_by = Slot(uri=NMDC_SUB_SCHEMA.was_generated_by, name="was_generated_by", curie=NMDC_SUB_SCHEMA.curie('was_generated_by'),
                   model_uri=NMDC_SUB_SCHEMA.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.attribute = Slot(uri=NMDC_SUB_SCHEMA.attribute, name="attribute", curie=NMDC_SUB_SCHEMA.curie('attribute'),
                   model_uri=NMDC_SUB_SCHEMA.attribute, domain=None, range=Optional[str])

slots.used = Slot(uri=NMDC_SUB_SCHEMA.used, name="used", curie=NMDC_SUB_SCHEMA.curie('used'),
                   model_uri=NMDC_SUB_SCHEMA.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.air_air_PM_concen = Slot(uri=MIXS['0000108'], name="air_air_PM_concen", curie=MIXS.curie('0000108'),
                   model_uri=NMDC_SUB_SCHEMA.air_air_PM_concen, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_alt = Slot(uri=MIXS['0000094'], name="air_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.air_alt, domain=Air, range=Optional[str])

slots.air_barometric_press = Slot(uri=MIXS['0000096'], name="air_barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=NMDC_SUB_SCHEMA.air_barometric_press, domain=Air, range=Optional[str])

slots.air_carb_dioxide = Slot(uri=MIXS['0000097'], name="air_carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC_SUB_SCHEMA.air_carb_dioxide, domain=Air, range=Optional[str])

slots.air_carb_monoxide = Slot(uri=MIXS['0000098'], name="air_carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=NMDC_SUB_SCHEMA.air_carb_monoxide, domain=Air, range=Optional[str])

slots.air_chem_administration = Slot(uri=MIXS['0000751'], name="air_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.air_chem_administration, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_collection_date = Slot(uri=MIXS['0000011'], name="air_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.air_collection_date, domain=Air, range=Optional[str])

slots.air_depth = Slot(uri=MIXS['0000018'], name="air_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.air_depth, domain=Air, range=Optional[str])

slots.air_ecosystem = Slot(uri="str(uriorcurie)", name="air_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.air_ecosystem, domain=Air, range=Optional[str])

slots.air_ecosystem_category = Slot(uri="str(uriorcurie)", name="air_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.air_ecosystem_category, domain=Air, range=Optional[str])

slots.air_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="air_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.air_ecosystem_subtype, domain=Air, range=Optional[str])

slots.air_ecosystem_type = Slot(uri="str(uriorcurie)", name="air_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.air_ecosystem_type, domain=Air, range=Optional[str])

slots.air_elev = Slot(uri=MIXS['0000093'], name="air_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.air_elev, domain=Air, range=Optional[float])

slots.air_env_broad_scale = Slot(uri=MIXS['0000012'], name="air_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.air_env_broad_scale, domain=Air, range=Optional[str])

slots.air_env_local_scale = Slot(uri=MIXS['0000013'], name="air_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.air_env_local_scale, domain=Air, range=Optional[str])

slots.air_env_medium = Slot(uri=MIXS['0000014'], name="air_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.air_env_medium, domain=Air, range=Optional[str])

slots.air_experimental_factor = Slot(uri=MIXS['0000008'], name="air_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.air_experimental_factor, domain=Air, range=Optional[str])

slots.air_geo_loc_name = Slot(uri=MIXS['0000010'], name="air_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.air_geo_loc_name, domain=Air, range=Optional[str])

slots.air_humidity = Slot(uri=MIXS['0000100'], name="air_humidity", curie=MIXS.curie('0000100'),
                   model_uri=NMDC_SUB_SCHEMA.air_humidity, domain=Air, range=Optional[str])

slots.air_lat_lon = Slot(uri=MIXS['0000009'], name="air_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.air_lat_lon, domain=Air, range=Optional[str])

slots.air_methane = Slot(uri=MIXS['0000101'], name="air_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.air_methane, domain=Air, range=Optional[str])

slots.air_misc_param = Slot(uri=MIXS['0000752'], name="air_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.air_misc_param, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_organism_count = Slot(uri=MIXS['0000103'], name="air_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.air_organism_count, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="air_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.air_oxy_stat_samp, domain=Air, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.air_oxygen = Slot(uri=MIXS['0000104'], name="air_oxygen", curie=MIXS.curie('0000104'),
                   model_uri=NMDC_SUB_SCHEMA.air_oxygen, domain=Air, range=Optional[str])

slots.air_perturbation = Slot(uri=MIXS['0000754'], name="air_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.air_perturbation, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_pollutants = Slot(uri=MIXS['0000107'], name="air_pollutants", curie=MIXS.curie('0000107'),
                   model_uri=NMDC_SUB_SCHEMA.air_pollutants, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="air_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.air_rel_to_oxygen, domain=Air, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.air_salinity = Slot(uri=MIXS['0000183'], name="air_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.air_salinity, domain=Air, range=Optional[str])

slots.air_samp_collec_device = Slot(uri=MIXS['0000002'], name="air_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_collec_device, domain=Air, range=Optional[str])

slots.air_samp_collec_method = Slot(uri=MIXS['0001225'], name="air_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_collec_method, domain=Air, range=Optional[str])

slots.air_samp_mat_process = Slot(uri=MIXS['0000016'], name="air_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_mat_process, domain=Air, range=Optional[str])

slots.air_samp_size = Slot(uri=MIXS['0000001'], name="air_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_size, domain=Air, range=Optional[str])

slots.air_samp_store_dur = Slot(uri=MIXS['0000116'], name="air_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_store_dur, domain=Air, range=Optional[str])

slots.air_samp_store_loc = Slot(uri=MIXS['0000755'], name="air_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_store_loc, domain=Air, range=Optional[str])

slots.air_samp_store_temp = Slot(uri=MIXS['0000110'], name="air_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.air_samp_store_temp, domain=Air, range=Optional[str])

slots.air_size_frac = Slot(uri=MIXS['0000017'], name="air_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.air_size_frac, domain=Air, range=Optional[str])

slots.air_solar_irradiance = Slot(uri=MIXS['0000112'], name="air_solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=NMDC_SUB_SCHEMA.air_solar_irradiance, domain=Air, range=Optional[str])

slots.air_specific_ecosystem = Slot(uri="str(uriorcurie)", name="air_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.air_specific_ecosystem, domain=Air, range=Optional[str])

slots.air_ventilation_rate = Slot(uri=MIXS['0000114'], name="air_ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=NMDC_SUB_SCHEMA.air_ventilation_rate, domain=Air, range=Optional[str])

slots.air_ventilation_type = Slot(uri=MIXS['0000756'], name="air_ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC_SUB_SCHEMA.air_ventilation_type, domain=Air, range=Optional[str])

slots.air_volatile_org_comp = Slot(uri=MIXS['0000115'], name="air_volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=NMDC_SUB_SCHEMA.air_volatile_org_comp, domain=Air, range=Optional[Union[str, List[str]]])

slots.air_wind_direction = Slot(uri=MIXS['0000757'], name="air_wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=NMDC_SUB_SCHEMA.air_wind_direction, domain=Air, range=Optional[str])

slots.air_wind_speed = Slot(uri=MIXS['0000118'], name="air_wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=NMDC_SUB_SCHEMA.air_wind_speed, domain=Air, range=Optional[str])

slots.air_horizon_meth = Slot(uri=MIXS['0000321'], name="air_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.air_horizon_meth, domain=Air, range=Optional[str])

slots.biofilm_alkalinity = Slot(uri=MIXS['0000421'], name="biofilm_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_alkalinity, domain=Biofilm, range=Optional[str])

slots.biofilm_alkyl_diethers = Slot(uri=MIXS['0000490'], name="biofilm_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_alkyl_diethers, domain=Biofilm, range=Optional[str])

slots.biofilm_alt = Slot(uri=MIXS['0000094'], name="biofilm_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_alt, domain=Biofilm, range=Optional[str])

slots.biofilm_aminopept_act = Slot(uri=MIXS['0000172'], name="biofilm_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_aminopept_act, domain=Biofilm, range=Optional[str])

slots.biofilm_ammonium = Slot(uri=MIXS['0000427'], name="biofilm_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ammonium, domain=Biofilm, range=Optional[str])

slots.biofilm_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="biofilm_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_bacteria_carb_prod, domain=Biofilm, range=Optional[str])

slots.biofilm_biomass = Slot(uri=MIXS['0000174'], name="biofilm_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_biomass, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_bishomohopanol = Slot(uri=MIXS['0000175'], name="biofilm_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_bishomohopanol, domain=Biofilm, range=Optional[str])

slots.biofilm_bromide = Slot(uri=MIXS['0000176'], name="biofilm_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_bromide, domain=Biofilm, range=Optional[str])

slots.biofilm_calcium = Slot(uri=MIXS['0000432'], name="biofilm_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_calcium, domain=Biofilm, range=Optional[str])

slots.biofilm_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="biofilm_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_carb_nitro_ratio, domain=Biofilm, range=Optional[float])

slots.biofilm_chem_administration = Slot(uri=MIXS['0000751'], name="biofilm_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_chem_administration, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_chloride = Slot(uri=MIXS['0000429'], name="biofilm_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_chloride, domain=Biofilm, range=Optional[str])

slots.biofilm_chlorophyll = Slot(uri=MIXS['0000177'], name="biofilm_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_chlorophyll, domain=Biofilm, range=Optional[str])

slots.biofilm_collection_date = Slot(uri=MIXS['0000011'], name="biofilm_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_collection_date, domain=Biofilm, range=Optional[str])

slots.biofilm_depth = Slot(uri=MIXS['0000018'], name="biofilm_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_depth, domain=Biofilm, range=Optional[str])

slots.biofilm_diether_lipids = Slot(uri=MIXS['0000178'], name="biofilm_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diether_lipids, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="biofilm_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_carb_dioxide, domain=Biofilm, range=Optional[str])

slots.biofilm_diss_hydrogen = Slot(uri=MIXS['0000179'], name="biofilm_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_hydrogen, domain=Biofilm, range=Optional[str])

slots.biofilm_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="biofilm_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_inorg_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_diss_org_carb = Slot(uri=MIXS['0000433'], name="biofilm_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_org_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_diss_org_nitro = Slot(uri=MIXS['0000162'], name="biofilm_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_org_nitro, domain=Biofilm, range=Optional[str])

slots.biofilm_diss_oxygen = Slot(uri=MIXS['0000119'], name="biofilm_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_diss_oxygen, domain=Biofilm, range=Optional[str])

slots.biofilm_ecosystem = Slot(uri="str(uriorcurie)", name="biofilm_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ecosystem, domain=Biofilm, range=Optional[str])

slots.biofilm_ecosystem_category = Slot(uri="str(uriorcurie)", name="biofilm_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ecosystem_category, domain=Biofilm, range=Optional[str])

slots.biofilm_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="biofilm_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ecosystem_subtype, domain=Biofilm, range=Optional[str])

slots.biofilm_ecosystem_type = Slot(uri="str(uriorcurie)", name="biofilm_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ecosystem_type, domain=Biofilm, range=Optional[str])

slots.biofilm_elev = Slot(uri=MIXS['0000093'], name="biofilm_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_elev, domain=Biofilm, range=Optional[float])

slots.biofilm_env_broad_scale = Slot(uri=MIXS['0000012'], name="biofilm_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_env_broad_scale, domain=Biofilm, range=Optional[str])

slots.biofilm_env_local_scale = Slot(uri=MIXS['0000013'], name="biofilm_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_env_local_scale, domain=Biofilm, range=Optional[str])

slots.biofilm_env_medium = Slot(uri=MIXS['0000014'], name="biofilm_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_env_medium, domain=Biofilm, range=Optional[str])

slots.biofilm_experimental_factor = Slot(uri=MIXS['0000008'], name="biofilm_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_experimental_factor, domain=Biofilm, range=Optional[str])

slots.biofilm_geo_loc_name = Slot(uri=MIXS['0000010'], name="biofilm_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_geo_loc_name, domain=Biofilm, range=Optional[str])

slots.biofilm_glucosidase_act = Slot(uri=MIXS['0000137'], name="biofilm_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_glucosidase_act, domain=Biofilm, range=Optional[str])

slots.biofilm_lat_lon = Slot(uri=MIXS['0000009'], name="biofilm_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_lat_lon, domain=Biofilm, range=Optional[str])

slots.biofilm_magnesium = Slot(uri=MIXS['0000431'], name="biofilm_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_magnesium, domain=Biofilm, range=Optional[str])

slots.biofilm_mean_frict_vel = Slot(uri=MIXS['0000498'], name="biofilm_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_mean_frict_vel, domain=Biofilm, range=Optional[str])

slots.biofilm_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="biofilm_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_mean_peak_frict_vel, domain=Biofilm, range=Optional[str])

slots.biofilm_methane = Slot(uri=MIXS['0000101'], name="biofilm_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_methane, domain=Biofilm, range=Optional[str])

slots.biofilm_misc_param = Slot(uri=MIXS['0000752'], name="biofilm_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_misc_param, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_n_alkanes = Slot(uri=MIXS['0000503'], name="biofilm_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_n_alkanes, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_nitrate = Slot(uri=MIXS['0000425'], name="biofilm_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_nitrate, domain=Biofilm, range=Optional[str])

slots.biofilm_nitrite = Slot(uri=MIXS['0000426'], name="biofilm_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_nitrite, domain=Biofilm, range=Optional[str])

slots.biofilm_nitro = Slot(uri=MIXS['0000504'], name="biofilm_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_nitro, domain=Biofilm, range=Optional[str])

slots.biofilm_org_carb = Slot(uri=MIXS['0000508'], name="biofilm_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_org_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_org_matter = Slot(uri=MIXS['0000204'], name="biofilm_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_org_matter, domain=Biofilm, range=Optional[str])

slots.biofilm_org_nitro = Slot(uri=MIXS['0000205'], name="biofilm_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_org_nitro, domain=Biofilm, range=Optional[str])

slots.biofilm_organism_count = Slot(uri=MIXS['0000103'], name="biofilm_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_organism_count, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="biofilm_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_oxy_stat_samp, domain=Biofilm, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.biofilm_part_org_carb = Slot(uri=MIXS['0000515'], name="biofilm_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_part_org_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_perturbation = Slot(uri=MIXS['0000754'], name="biofilm_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_perturbation, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="biofilm_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_petroleum_hydrocarb, domain=Biofilm, range=Optional[str])

slots.biofilm_ph = Slot(uri=MIXS['0001001'], name="biofilm_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ph, domain=Biofilm, range=Optional[str])

slots.biofilm_phaeopigments = Slot(uri=MIXS['0000180'], name="biofilm_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_phaeopigments, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_phosphate = Slot(uri=MIXS['0000505'], name="biofilm_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_phosphate, domain=Biofilm, range=Optional[str])

slots.biofilm_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="biofilm_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_phosplipid_fatt_acid, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_potassium = Slot(uri=MIXS['0000430'], name="biofilm_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_potassium, domain=Biofilm, range=Optional[str])

slots.biofilm_pressure = Slot(uri=MIXS['0000412'], name="biofilm_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_pressure, domain=Biofilm, range=Optional[str])

slots.biofilm_redox_potential = Slot(uri=MIXS['0000182'], name="biofilm_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_redox_potential, domain=Biofilm, range=Optional[str])

slots.biofilm_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="biofilm_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_rel_to_oxygen, domain=Biofilm, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.biofilm_salinity = Slot(uri=MIXS['0000183'], name="biofilm_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_salinity, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_collec_device = Slot(uri=MIXS['0000002'], name="biofilm_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_collec_device, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_collec_method = Slot(uri=MIXS['0001225'], name="biofilm_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_collec_method, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_mat_process = Slot(uri=MIXS['0000016'], name="biofilm_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_mat_process, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_size = Slot(uri=MIXS['0000001'], name="biofilm_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_size, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_store_dur = Slot(uri=MIXS['0000116'], name="biofilm_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_store_dur, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_store_loc = Slot(uri=MIXS['0000755'], name="biofilm_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_store_loc, domain=Biofilm, range=Optional[str])

slots.biofilm_samp_store_temp = Slot(uri=MIXS['0000110'], name="biofilm_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_samp_store_temp, domain=Biofilm, range=Optional[str])

slots.biofilm_silicate = Slot(uri=MIXS['0000184'], name="biofilm_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_silicate, domain=Biofilm, range=Optional[str])

slots.biofilm_size_frac = Slot(uri=MIXS['0000017'], name="biofilm_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_size_frac, domain=Biofilm, range=Optional[str])

slots.biofilm_sodium = Slot(uri=MIXS['0000428'], name="biofilm_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_sodium, domain=Biofilm, range=Optional[str])

slots.biofilm_specific_ecosystem = Slot(uri="str(uriorcurie)", name="biofilm_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.biofilm_specific_ecosystem, domain=Biofilm, range=Optional[str])

slots.biofilm_sulfate = Slot(uri=MIXS['0000423'], name="biofilm_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_sulfate, domain=Biofilm, range=Optional[str])

slots.biofilm_sulfide = Slot(uri=MIXS['0000424'], name="biofilm_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_sulfide, domain=Biofilm, range=Optional[str])

slots.biofilm_temp = Slot(uri=MIXS['0000113'], name="biofilm_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_temp, domain=Biofilm, range=Optional[str])

slots.biofilm_tot_carb = Slot(uri=MIXS['0000525'], name="biofilm_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_tot_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_tot_nitro_content = Slot(uri=MIXS['0000530'], name="biofilm_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_tot_nitro_content, domain=Biofilm, range=Optional[str])

slots.biofilm_tot_org_carb = Slot(uri=MIXS['0000533'], name="biofilm_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_tot_org_carb, domain=Biofilm, range=Optional[str])

slots.biofilm_turbidity = Slot(uri=MIXS['0000191'], name="biofilm_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_turbidity, domain=Biofilm, range=Optional[str])

slots.biofilm_water_content = Slot(uri=MIXS['0000185'], name="biofilm_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_water_content, domain=Biofilm, range=Optional[Union[str, List[str]]])

slots.biofilm_horizon_meth = Slot(uri=MIXS['0000321'], name="biofilm_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_horizon_meth, domain=Biofilm, range=Optional[str])

slots.biofilm_ph_meth = Slot(uri=MIXS['0001106'], name="biofilm_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_ph_meth, domain=Biofilm, range=Optional[str])

slots.bioscales_agrochem_addition = Slot(uri=MIXS['0000639'], name="bioscales_agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_agrochem_addition, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_air_temp_regm = Slot(uri=MIXS['0000551'], name="bioscales_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_air_temp_regm, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_al_sat = Slot(uri=MIXS['0000607'], name="bioscales_al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_al_sat, domain=Bioscales, range=Optional[str])

slots.bioscales_al_sat_meth = Slot(uri=MIXS['0000324'], name="bioscales_al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_al_sat_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_alt = Slot(uri=MIXS['0000094'], name="bioscales_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_alt, domain=Bioscales, range=Optional[str])

slots.bioscales_ammonium_nitrogen = Slot(uri="str(uriorcurie)", name="bioscales_ammonium_nitrogen", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ammonium_nitrogen, domain=Bioscales, range=Optional[str])

slots.bioscales_annual_precpt = Slot(uri=MIXS['0000644'], name="bioscales_annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_annual_precpt, domain=Bioscales, range=Optional[str])

slots.bioscales_annual_temp = Slot(uri=MIXS['0000642'], name="bioscales_annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_annual_temp, domain=Bioscales, range=Optional[str])

slots.bioscales_biotic_regm = Slot(uri=MIXS['0001038'], name="bioscales_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_biotic_regm, domain=Bioscales, range=Optional[str])

slots.bioscales_biotic_relationship = Slot(uri=MIXS['0000028'], name="bioscales_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_biotic_relationship, domain=Bioscales, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.bioscales_calcium = Slot(uri=MIXS['0000432'], name="bioscales_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_calcium, domain=Bioscales, range=Optional[str])

slots.bioscales_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="bioscales_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_carb_nitro_ratio, domain=Bioscales, range=Optional[float])

slots.bioscales_chem_administration = Slot(uri=MIXS['0000751'], name="bioscales_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_chem_administration, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_climate_environment = Slot(uri=MIXS['0001040'], name="bioscales_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_climate_environment, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_collection_date = Slot(uri=MIXS['0000011'], name="bioscales_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_collection_date, domain=Bioscales, range=Optional[str])

slots.bioscales_crop_rotation = Slot(uri=MIXS['0000318'], name="bioscales_crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_crop_rotation, domain=Bioscales, range=Optional[str])

slots.bioscales_cur_land_use = Slot(uri=MIXS['0001080'], name="bioscales_cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_cur_land_use, domain=Bioscales, range=Optional[Union[str, "CurLandUseEnum"]])

slots.bioscales_cur_vegetation = Slot(uri=MIXS['0000312'], name="bioscales_cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_cur_vegetation, domain=Bioscales, range=Optional[str])

slots.bioscales_cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="bioscales_cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_cur_vegetation_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_depth = Slot(uri=MIXS['0000018'], name="bioscales_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_depth, domain=Bioscales, range=Optional[str])

slots.bioscales_drainage_class = Slot(uri=MIXS['0001085'], name="bioscales_drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_drainage_class, domain=Bioscales, range=Optional[Union[str, "DrainageClassEnum"]])

slots.bioscales_ecosystem = Slot(uri="str(uriorcurie)", name="bioscales_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ecosystem, domain=Bioscales, range=Optional[Union[str, "EcosystemEnum"]])

slots.bioscales_ecosystem_category = Slot(uri="str(uriorcurie)", name="bioscales_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ecosystem_category, domain=Bioscales, range=Optional[Union[str, "EcosystemCategoryEnum"]])

slots.bioscales_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="bioscales_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ecosystem_subtype, domain=Bioscales, range=Optional[Union[str, "EcosystemSubtypeEnum"]])

slots.bioscales_ecosystem_type = Slot(uri="str(uriorcurie)", name="bioscales_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ecosystem_type, domain=Bioscales, range=Optional[Union[str, "EcosystemTypeEnum"]])

slots.bioscales_elev = Slot(uri=MIXS['0000093'], name="bioscales_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_elev, domain=Bioscales, range=Optional[float])

slots.bioscales_env_broad_scale = Slot(uri=MIXS['0000012'], name="bioscales_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_env_broad_scale, domain=Bioscales, range=Optional[Union[str, "EnvBroadScaleSoilEnum"]])

slots.bioscales_env_local_scale = Slot(uri=MIXS['0000013'], name="bioscales_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_env_local_scale, domain=Bioscales, range=Optional[Union[str, "EnvLocalScaleSoilEnum"]])

slots.bioscales_env_medium = Slot(uri=MIXS['0000014'], name="bioscales_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_env_medium, domain=Bioscales, range=Optional[Union[str, "EnvMediumSoilEnum"]])

slots.bioscales_experimental_factor = Slot(uri=MIXS['0000008'], name="bioscales_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_experimental_factor, domain=Bioscales, range=Optional[str])

slots.bioscales_extreme_event = Slot(uri=MIXS['0000320'], name="bioscales_extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_extreme_event, domain=Bioscales, range=Optional[str])

slots.bioscales_fao_class = Slot(uri=MIXS['0001083'], name="bioscales_fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_fao_class, domain=Bioscales, range=Optional[Union[str, "FaoClassEnum"]])

slots.bioscales_fire = Slot(uri=MIXS['0001086'], name="bioscales_fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_fire, domain=Bioscales, range=Optional[str])

slots.bioscales_flooding = Slot(uri=MIXS['0000319'], name="bioscales_flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_flooding, domain=Bioscales, range=Optional[str])

slots.bioscales_gaseous_environment = Slot(uri=MIXS['0000558'], name="bioscales_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_gaseous_environment, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_geo_loc_name = Slot(uri=MIXS['0000010'], name="bioscales_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_geo_loc_name, domain=Bioscales, range=Optional[str])

slots.bioscales_growth_facil = Slot(uri=MIXS['0001043'], name="bioscales_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_growth_facil, domain=Bioscales, range=Optional[Union[str, "GrowthFacilEnum"]])

slots.bioscales_heavy_metals = Slot(uri=MIXS['0000652'], name="bioscales_heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_heavy_metals, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_heavy_metals_meth = Slot(uri=MIXS['0000343'], name="bioscales_heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_heavy_metals_meth, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_horizon_meth = Slot(uri=MIXS['0000321'], name="bioscales_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_horizon_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_humidity_regm = Slot(uri=MIXS['0000568'], name="bioscales_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_humidity_regm, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_lat_lon = Slot(uri=MIXS['0000009'], name="bioscales_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_lat_lon, domain=Bioscales, range=Optional[str])

slots.bioscales_lbc_thirty = Slot(uri="str(uriorcurie)", name="bioscales_lbc_thirty", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_lbc_thirty, domain=Bioscales, range=Optional[str])

slots.bioscales_lbceq = Slot(uri="str(uriorcurie)", name="bioscales_lbceq", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_lbceq, domain=Bioscales, range=Optional[str])

slots.bioscales_light_regm = Slot(uri=MIXS['0000569'], name="bioscales_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_light_regm, domain=Bioscales, range=Optional[str])

slots.bioscales_link_class_info = Slot(uri=MIXS['0000329'], name="bioscales_link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_link_class_info, domain=Bioscales, range=Optional[str])

slots.bioscales_link_climate_info = Slot(uri=MIXS['0000328'], name="bioscales_link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_link_climate_info, domain=Bioscales, range=Optional[str])

slots.bioscales_local_class = Slot(uri=MIXS['0000330'], name="bioscales_local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_local_class, domain=Bioscales, range=Optional[str])

slots.bioscales_local_class_meth = Slot(uri=MIXS['0000331'], name="bioscales_local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_local_class_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_magnesium = Slot(uri=MIXS['0000431'], name="bioscales_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_magnesium, domain=Bioscales, range=Optional[str])

slots.bioscales_manganese = Slot(uri="str(uriorcurie)", name="bioscales_manganese", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_manganese, domain=Bioscales, range=Optional[str])

slots.bioscales_micro_biomass_meth = Slot(uri=MIXS['0000339'], name="bioscales_micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_micro_biomass_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_microbial_biomass = Slot(uri=MIXS['0000650'], name="bioscales_microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_microbial_biomass, domain=Bioscales, range=Optional[str])

slots.bioscales_misc_param = Slot(uri=MIXS['0000752'], name="bioscales_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_misc_param, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_nitrate_nitrogen = Slot(uri="str(uriorcurie)", name="bioscales_nitrate_nitrogen", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_nitrate_nitrogen, domain=Bioscales, range=Optional[str])

slots.bioscales_nitrite_nitrogen = Slot(uri="str(uriorcurie)", name="bioscales_nitrite_nitrogen", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_nitrite_nitrogen, domain=Bioscales, range=Optional[str])

slots.bioscales_org_matter = Slot(uri=MIXS['0000204'], name="bioscales_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_org_matter, domain=Bioscales, range=Optional[str])

slots.bioscales_org_nitro = Slot(uri=MIXS['0000205'], name="bioscales_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_org_nitro, domain=Bioscales, range=Optional[str])

slots.bioscales_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="bioscales_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_oxy_stat_samp, domain=Bioscales, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.bioscales_ph = Slot(uri=MIXS['0001001'], name="bioscales_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ph, domain=Bioscales, range=Optional[str])

slots.bioscales_ph_meth = Slot(uri=MIXS['0001106'], name="bioscales_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_ph_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_phosphate = Slot(uri=MIXS['0000505'], name="bioscales_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_phosphate, domain=Bioscales, range=Optional[str])

slots.bioscales_potassium = Slot(uri=MIXS['0000430'], name="bioscales_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_potassium, domain=Bioscales, range=Optional[str])

slots.bioscales_prev_land_use_meth = Slot(uri=MIXS['0000316'], name="bioscales_prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_prev_land_use_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_previous_land_use = Slot(uri=MIXS['0000315'], name="bioscales_previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_previous_land_use, domain=Bioscales, range=Optional[str])

slots.bioscales_profile_position = Slot(uri=MIXS['0001084'], name="bioscales_profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_profile_position, domain=Bioscales, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.bioscales_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="bioscales_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_rel_to_oxygen, domain=Bioscales, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.bioscales_salinity = Slot(uri=MIXS['0000183'], name="bioscales_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_salinity, domain=Bioscales, range=Optional[str])

slots.bioscales_salinity_meth = Slot(uri=MIXS['0000341'], name="bioscales_salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_salinity_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_samp_collec_device = Slot(uri=MIXS['0000002'], name="bioscales_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_samp_collec_device, domain=Bioscales, range=Optional[str])

slots.bioscales_samp_collec_method = Slot(uri=MIXS['0001225'], name="bioscales_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_samp_collec_method, domain=Bioscales, range=Optional[str])

slots.bioscales_samp_mat_process = Slot(uri=MIXS['0000016'], name="bioscales_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_samp_mat_process, domain=Bioscales, range=Optional[str])

slots.bioscales_samp_size = Slot(uri=MIXS['0000001'], name="bioscales_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_samp_size, domain=Bioscales, range=Optional[str])

slots.bioscales_samp_store_temp = Slot(uri=MIXS['0000110'], name="bioscales_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_samp_store_temp, domain=Bioscales, range=Optional[str])

slots.bioscales_season_precpt = Slot(uri=MIXS['0000645'], name="bioscales_season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_season_precpt, domain=Bioscales, range=Optional[str])

slots.bioscales_season_temp = Slot(uri=MIXS['0000643'], name="bioscales_season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_season_temp, domain=Bioscales, range=Optional[str])

slots.bioscales_sieving = Slot(uri=MIXS['0000322'], name="bioscales_sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_sieving, domain=Bioscales, range=Optional[str])

slots.bioscales_size_frac_low = Slot(uri=MIXS['0000735'], name="bioscales_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_size_frac_low, domain=Bioscales, range=Optional[str])

slots.bioscales_size_frac_up = Slot(uri=MIXS['0000736'], name="bioscales_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_size_frac_up, domain=Bioscales, range=Optional[str])

slots.bioscales_slope_aspect = Slot(uri=MIXS['0000647'], name="bioscales_slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_slope_aspect, domain=Bioscales, range=Optional[str])

slots.bioscales_slope_gradient = Slot(uri=MIXS['0000646'], name="bioscales_slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_slope_gradient, domain=Bioscales, range=Optional[str])

slots.bioscales_soil_horizon = Slot(uri=MIXS['0001082'], name="bioscales_soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_soil_horizon, domain=Bioscales, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.bioscales_soil_text_measure = Slot(uri=MIXS['0000335'], name="bioscales_soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_soil_text_measure, domain=Bioscales, range=Optional[str])

slots.bioscales_soil_texture_meth = Slot(uri=MIXS['0000336'], name="bioscales_soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_soil_texture_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_soil_type = Slot(uri=MIXS['0000332'], name="bioscales_soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_soil_type, domain=Bioscales, range=Optional[str])

slots.bioscales_soil_type_meth = Slot(uri=MIXS['0000334'], name="bioscales_soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_soil_type_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_specific_ecosystem = Slot(uri="str(uriorcurie)", name="bioscales_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_specific_ecosystem, domain=Bioscales, range=Optional[Union[str, "SpecificEcosystemEnum"]])

slots.bioscales_store_cond = Slot(uri=MIXS['0000327'], name="bioscales_store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_store_cond, domain=Bioscales, range=Optional[Union[str, "StoreCondEnum"]])

slots.bioscales_temp = Slot(uri=MIXS['0000113'], name="bioscales_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_temp, domain=Bioscales, range=Optional[str])

slots.bioscales_tillage = Slot(uri=MIXS['0001081'], name="bioscales_tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tillage, domain=Bioscales, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.bioscales_tot_carb = Slot(uri=MIXS['0000525'], name="bioscales_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_carb, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_nitro = Slot(uri=MIXS['0000102'], name="bioscales_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_nitro, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="bioscales_tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_nitro_cont_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_nitro_content = Slot(uri=MIXS['0000530'], name="bioscales_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_nitro_content, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_org_c_meth = Slot(uri=MIXS['0000337'], name="bioscales_tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_org_c_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_org_carb = Slot(uri=MIXS['0000533'], name="bioscales_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_org_carb, domain=Bioscales, range=Optional[str])

slots.bioscales_tot_phosp = Slot(uri=MIXS['0000117'], name="bioscales_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_tot_phosp, domain=Bioscales, range=Optional[str])

slots.bioscales_water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="bioscales_water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_water_cont_soil_meth, domain=Bioscales, range=Optional[str])

slots.bioscales_water_content = Slot(uri=MIXS['0000185'], name="bioscales_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_water_content, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_watering_regm = Slot(uri=MIXS['0000591'], name="bioscales_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.bioscales_watering_regm, domain=Bioscales, range=Optional[Union[str, List[str]]])

slots.bioscales_zinc = Slot(uri="str(uriorcurie)", name="bioscales_zinc", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.bioscales_zinc, domain=Bioscales, range=Optional[str])

slots.built_env_abs_air_humidity = Slot(uri=MIXS['0000122'], name="built_env_abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_abs_air_humidity, domain=BuiltEnv, range=Optional[str])

slots.built_env_address = Slot(uri=MIXS['0000218'], name="built_env_address", curie=MIXS.curie('0000218'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_address, domain=BuiltEnv, range=Optional[str])

slots.built_env_adj_room = Slot(uri=MIXS['0000219'], name="built_env_adj_room", curie=MIXS.curie('0000219'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_adj_room, domain=BuiltEnv, range=Optional[str])

slots.built_env_aero_struc = Slot(uri=MIXS['0000773'], name="built_env_aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_aero_struc, domain=BuiltEnv, range=Optional[str])

slots.built_env_air_temp = Slot(uri=MIXS['0000124'], name="built_env_air_temp", curie=MIXS.curie('0000124'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_air_temp, domain=BuiltEnv, range=Optional[str])

slots.built_env_alt = Slot(uri=MIXS['0000094'], name="built_env_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_alt, domain=BuiltEnv, range=Optional[str])

slots.built_env_amount_light = Slot(uri=MIXS['0000140'], name="built_env_amount_light", curie=MIXS.curie('0000140'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_amount_light, domain=BuiltEnv, range=Optional[str])

slots.built_env_arch_struc = Slot(uri=MIXS['0000774'], name="built_env_arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_arch_struc, domain=BuiltEnv, range=Optional[Union[str, "ArchStrucEnum"]])

slots.built_env_avg_dew_point = Slot(uri=MIXS['0000141'], name="built_env_avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_avg_dew_point, domain=BuiltEnv, range=Optional[str])

slots.built_env_avg_occup = Slot(uri=MIXS['0000775'], name="built_env_avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_avg_occup, domain=BuiltEnv, range=Optional[str])

slots.built_env_avg_temp = Slot(uri=MIXS['0000142'], name="built_env_avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_avg_temp, domain=BuiltEnv, range=Optional[str])

slots.built_env_bathroom_count = Slot(uri=MIXS['0000776'], name="built_env_bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_bathroom_count, domain=BuiltEnv, range=Optional[str])

slots.built_env_bedroom_count = Slot(uri=MIXS['0000777'], name="built_env_bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_bedroom_count, domain=BuiltEnv, range=Optional[str])

slots.built_env_build_docs = Slot(uri=MIXS['0000787'], name="built_env_build_docs", curie=MIXS.curie('0000787'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_build_docs, domain=BuiltEnv, range=Optional[Union[str, "BuildDocsEnum"]])

slots.built_env_build_occup_type = Slot(uri=MIXS['0000761'], name="built_env_build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_build_occup_type, domain=BuiltEnv, range=Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]])

slots.built_env_building_setting = Slot(uri=MIXS['0000768'], name="built_env_building_setting", curie=MIXS.curie('0000768'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_building_setting, domain=BuiltEnv, range=Optional[Union[str, "BuildingSettingEnum"]])

slots.built_env_built_struc_age = Slot(uri=MIXS['0000145'], name="built_env_built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_built_struc_age, domain=BuiltEnv, range=Optional[str])

slots.built_env_built_struc_set = Slot(uri=MIXS['0000778'], name="built_env_built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_built_struc_set, domain=BuiltEnv, range=Optional[str])

slots.built_env_built_struc_type = Slot(uri=MIXS['0000721'], name="built_env_built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_built_struc_type, domain=BuiltEnv, range=Optional[str])

slots.built_env_carb_dioxide = Slot(uri=MIXS['0000097'], name="built_env_carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_carb_dioxide, domain=BuiltEnv, range=Optional[str])

slots.built_env_ceil_area = Slot(uri=MIXS['0000148'], name="built_env_ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_area, domain=BuiltEnv, range=Optional[str])

slots.built_env_ceil_cond = Slot(uri=MIXS['0000779'], name="built_env_ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_cond, domain=BuiltEnv, range=Optional[Union[str, "CeilCondEnum"]])

slots.built_env_ceil_finish_mat = Slot(uri=MIXS['0000780'], name="built_env_ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_finish_mat, domain=BuiltEnv, range=Optional[Union[str, "CeilFinishMatEnum"]])

slots.built_env_ceil_struc = Slot(uri=MIXS['0000782'], name="built_env_ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_struc, domain=BuiltEnv, range=Optional[str])

slots.built_env_ceil_texture = Slot(uri=MIXS['0000783'], name="built_env_ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_texture, domain=BuiltEnv, range=Optional[Union[str, "CeilTextureEnum"]])

slots.built_env_ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="built_env_ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_thermal_mass, domain=BuiltEnv, range=Optional[str])

slots.built_env_ceil_type = Slot(uri=MIXS['0000784'], name="built_env_ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_type, domain=BuiltEnv, range=Optional[Union[str, "CeilTypeEnum"]])

slots.built_env_ceil_water_mold = Slot(uri=MIXS['0000781'], name="built_env_ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ceil_water_mold, domain=BuiltEnv, range=Optional[str])

slots.built_env_collection_date = Slot(uri=MIXS['0000011'], name="built_env_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_collection_date, domain=BuiltEnv, range=Optional[str])

slots.built_env_cool_syst_id = Slot(uri=MIXS['0000785'], name="built_env_cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_cool_syst_id, domain=BuiltEnv, range=Optional[str])

slots.built_env_date_last_rain = Slot(uri=MIXS['0000786'], name="built_env_date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_date_last_rain, domain=BuiltEnv, range=Optional[Union[dict, "TimestampValue"]])

slots.built_env_depth = Slot(uri=MIXS['0000018'], name="built_env_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_depth, domain=BuiltEnv, range=Optional[str])

slots.built_env_dew_point = Slot(uri=MIXS['0000129'], name="built_env_dew_point", curie=MIXS.curie('0000129'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_dew_point, domain=BuiltEnv, range=Optional[str])

slots.built_env_door_comp_type = Slot(uri=MIXS['0000795'], name="built_env_door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_comp_type, domain=BuiltEnv, range=Optional[Union[str, "DoorCompTypeEnum"]])

slots.built_env_door_cond = Slot(uri=MIXS['0000788'], name="built_env_door_cond", curie=MIXS.curie('0000788'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_cond, domain=BuiltEnv, range=Optional[Union[str, "DoorCondEnum"]])

slots.built_env_door_direct = Slot(uri=MIXS['0000789'], name="built_env_door_direct", curie=MIXS.curie('0000789'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_direct, domain=BuiltEnv, range=Optional[Union[str, "DoorDirectEnum"]])

slots.built_env_door_loc = Slot(uri=MIXS['0000790'], name="built_env_door_loc", curie=MIXS.curie('0000790'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_loc, domain=BuiltEnv, range=Optional[Union[str, "DoorLocEnum"]])

slots.built_env_door_mat = Slot(uri=MIXS['0000791'], name="built_env_door_mat", curie=MIXS.curie('0000791'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_mat, domain=BuiltEnv, range=Optional[Union[str, "DoorMatEnum"]])

slots.built_env_door_move = Slot(uri=MIXS['0000792'], name="built_env_door_move", curie=MIXS.curie('0000792'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_move, domain=BuiltEnv, range=Optional[Union[str, "DoorMoveEnum"]])

slots.built_env_door_size = Slot(uri=MIXS['0000158'], name="built_env_door_size", curie=MIXS.curie('0000158'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_size, domain=BuiltEnv, range=Optional[str])

slots.built_env_door_type = Slot(uri=MIXS['0000794'], name="built_env_door_type", curie=MIXS.curie('0000794'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_type, domain=BuiltEnv, range=Optional[Union[str, "DoorTypeEnum"]])

slots.built_env_door_type_metal = Slot(uri=MIXS['0000796'], name="built_env_door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_type_metal, domain=BuiltEnv, range=Optional[Union[str, "DoorTypeMetalEnum"]])

slots.built_env_door_type_wood = Slot(uri=MIXS['0000797'], name="built_env_door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_type_wood, domain=BuiltEnv, range=Optional[Union[str, "DoorTypeWoodEnum"]])

slots.built_env_door_water_mold = Slot(uri=MIXS['0000793'], name="built_env_door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_door_water_mold, domain=BuiltEnv, range=Optional[str])

slots.built_env_drawings = Slot(uri=MIXS['0000798'], name="built_env_drawings", curie=MIXS.curie('0000798'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_drawings, domain=BuiltEnv, range=Optional[Union[str, "DrawingsEnum"]])

slots.built_env_ecosystem = Slot(uri="str(uriorcurie)", name="built_env_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.built_env_ecosystem, domain=BuiltEnv, range=Optional[str])

slots.built_env_ecosystem_category = Slot(uri="str(uriorcurie)", name="built_env_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.built_env_ecosystem_category, domain=BuiltEnv, range=Optional[str])

slots.built_env_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="built_env_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.built_env_ecosystem_subtype, domain=BuiltEnv, range=Optional[str])

slots.built_env_ecosystem_type = Slot(uri="str(uriorcurie)", name="built_env_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.built_env_ecosystem_type, domain=BuiltEnv, range=Optional[str])

slots.built_env_elev = Slot(uri=MIXS['0000093'], name="built_env_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_elev, domain=BuiltEnv, range=Optional[float])

slots.built_env_elevator = Slot(uri=MIXS['0000799'], name="built_env_elevator", curie=MIXS.curie('0000799'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_elevator, domain=BuiltEnv, range=Optional[str])

slots.built_env_env_broad_scale = Slot(uri=MIXS['0000012'], name="built_env_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_env_broad_scale, domain=BuiltEnv, range=Optional[str])

slots.built_env_env_local_scale = Slot(uri=MIXS['0000013'], name="built_env_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_env_local_scale, domain=BuiltEnv, range=Optional[str])

slots.built_env_env_medium = Slot(uri=MIXS['0000014'], name="built_env_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_env_medium, domain=BuiltEnv, range=Optional[str])

slots.built_env_escalator = Slot(uri=MIXS['0000800'], name="built_env_escalator", curie=MIXS.curie('0000800'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_escalator, domain=BuiltEnv, range=Optional[str])

slots.built_env_exp_duct = Slot(uri=MIXS['0000144'], name="built_env_exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_exp_duct, domain=BuiltEnv, range=Optional[str])

slots.built_env_exp_pipe = Slot(uri=MIXS['0000220'], name="built_env_exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_exp_pipe, domain=BuiltEnv, range=Optional[str])

slots.built_env_experimental_factor = Slot(uri=MIXS['0000008'], name="built_env_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_experimental_factor, domain=BuiltEnv, range=Optional[str])

slots.built_env_ext_door = Slot(uri=MIXS['0000170'], name="built_env_ext_door", curie=MIXS.curie('0000170'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ext_door, domain=BuiltEnv, range=Optional[str])

slots.built_env_ext_wall_orient = Slot(uri=MIXS['0000817'], name="built_env_ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ext_wall_orient, domain=BuiltEnv, range=Optional[Union[str, "ExtWallOrientEnum"]])

slots.built_env_ext_window_orient = Slot(uri=MIXS['0000818'], name="built_env_ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ext_window_orient, domain=BuiltEnv, range=Optional[Union[str, "ExtWindowOrientEnum"]])

slots.built_env_filter_type = Slot(uri=MIXS['0000765'], name="built_env_filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_filter_type, domain=BuiltEnv, range=Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]])

slots.built_env_fireplace_type = Slot(uri=MIXS['0000802'], name="built_env_fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_fireplace_type, domain=BuiltEnv, range=Optional[str])

slots.built_env_floor_age = Slot(uri=MIXS['0000164'], name="built_env_floor_age", curie=MIXS.curie('0000164'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_age, domain=BuiltEnv, range=Optional[str])

slots.built_env_floor_area = Slot(uri=MIXS['0000165'], name="built_env_floor_area", curie=MIXS.curie('0000165'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_area, domain=BuiltEnv, range=Optional[str])

slots.built_env_floor_cond = Slot(uri=MIXS['0000803'], name="built_env_floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_cond, domain=BuiltEnv, range=Optional[Union[str, "FloorCondEnum"]])

slots.built_env_floor_count = Slot(uri=MIXS['0000225'], name="built_env_floor_count", curie=MIXS.curie('0000225'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_count, domain=BuiltEnv, range=Optional[str])

slots.built_env_floor_finish_mat = Slot(uri=MIXS['0000804'], name="built_env_floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_finish_mat, domain=BuiltEnv, range=Optional[Union[str, "FloorFinishMatEnum"]])

slots.built_env_floor_struc = Slot(uri=MIXS['0000806'], name="built_env_floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_struc, domain=BuiltEnv, range=Optional[Union[str, "FloorStrucEnum"]])

slots.built_env_floor_thermal_mass = Slot(uri=MIXS['0000166'], name="built_env_floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_thermal_mass, domain=BuiltEnv, range=Optional[str])

slots.built_env_floor_water_mold = Slot(uri=MIXS['0000805'], name="built_env_floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_floor_water_mold, domain=BuiltEnv, range=Optional[Union[str, "FloorWaterMoldEnum"]])

slots.built_env_freq_clean = Slot(uri=MIXS['0000226'], name="built_env_freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_freq_clean, domain=BuiltEnv, range=Optional[str])

slots.built_env_freq_cook = Slot(uri=MIXS['0000227'], name="built_env_freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_freq_cook, domain=BuiltEnv, range=Optional[str])

slots.built_env_furniture = Slot(uri=MIXS['0000807'], name="built_env_furniture", curie=MIXS.curie('0000807'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_furniture, domain=BuiltEnv, range=Optional[Union[str, "FurnitureEnum"]])

slots.built_env_gender_restroom = Slot(uri=MIXS['0000808'], name="built_env_gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_gender_restroom, domain=BuiltEnv, range=Optional[Union[str, "GenderRestroomEnum"]])

slots.built_env_geo_loc_name = Slot(uri=MIXS['0000010'], name="built_env_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_geo_loc_name, domain=BuiltEnv, range=Optional[str])

slots.built_env_hall_count = Slot(uri=MIXS['0000228'], name="built_env_hall_count", curie=MIXS.curie('0000228'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_hall_count, domain=BuiltEnv, range=Optional[str])

slots.built_env_handidness = Slot(uri=MIXS['0000809'], name="built_env_handidness", curie=MIXS.curie('0000809'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_handidness, domain=BuiltEnv, range=Optional[Union[str, "HandidnessEnum"]])

slots.built_env_heat_cool_type = Slot(uri=MIXS['0000766'], name="built_env_heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_heat_cool_type, domain=BuiltEnv, range=Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]])

slots.built_env_heat_deliv_loc = Slot(uri=MIXS['0000810'], name="built_env_heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_heat_deliv_loc, domain=BuiltEnv, range=Optional[Union[str, "HeatDelivLocEnum"]])

slots.built_env_heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="built_env_heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_heat_sys_deliv_meth, domain=BuiltEnv, range=Optional[str])

slots.built_env_heat_system_id = Slot(uri=MIXS['0000833'], name="built_env_heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_heat_system_id, domain=BuiltEnv, range=Optional[str])

slots.built_env_height_carper_fiber = Slot(uri=MIXS['0000167'], name="built_env_height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_height_carper_fiber, domain=BuiltEnv, range=Optional[str])

slots.built_env_indoor_space = Slot(uri=MIXS['0000763'], name="built_env_indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_indoor_space, domain=BuiltEnv, range=Optional[Union[str, "IndoorSpaceEnum"]])

slots.built_env_indoor_surf = Slot(uri=MIXS['0000764'], name="built_env_indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_indoor_surf, domain=BuiltEnv, range=Optional[Union[str, "IndoorSurfEnum"]])

slots.built_env_inside_lux = Slot(uri=MIXS['0000168'], name="built_env_inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_inside_lux, domain=BuiltEnv, range=Optional[str])

slots.built_env_int_wall_cond = Slot(uri=MIXS['0000813'], name="built_env_int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_int_wall_cond, domain=BuiltEnv, range=Optional[Union[str, "IntWallCondEnum"]])

slots.built_env_last_clean = Slot(uri=MIXS['0000814'], name="built_env_last_clean", curie=MIXS.curie('0000814'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_last_clean, domain=BuiltEnv, range=Optional[Union[dict, "TimestampValue"]])

slots.built_env_lat_lon = Slot(uri=MIXS['0000009'], name="built_env_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_lat_lon, domain=BuiltEnv, range=Optional[str])

slots.built_env_light_type = Slot(uri=MIXS['0000769'], name="built_env_light_type", curie=MIXS.curie('0000769'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_light_type, domain=BuiltEnv, range=Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]])

slots.built_env_max_occup = Slot(uri=MIXS['0000229'], name="built_env_max_occup", curie=MIXS.curie('0000229'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_max_occup, domain=BuiltEnv, range=Optional[str])

slots.built_env_mech_struc = Slot(uri=MIXS['0000815'], name="built_env_mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_mech_struc, domain=BuiltEnv, range=Optional[Union[str, "MechStrucEnum"]])

slots.built_env_number_pets = Slot(uri=MIXS['0000231'], name="built_env_number_pets", curie=MIXS.curie('0000231'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_number_pets, domain=BuiltEnv, range=Optional[str])

slots.built_env_number_plants = Slot(uri=MIXS['0000230'], name="built_env_number_plants", curie=MIXS.curie('0000230'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_number_plants, domain=BuiltEnv, range=Optional[str])

slots.built_env_number_resident = Slot(uri=MIXS['0000232'], name="built_env_number_resident", curie=MIXS.curie('0000232'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_number_resident, domain=BuiltEnv, range=Optional[str])

slots.built_env_occup_density_samp = Slot(uri=MIXS['0000217'], name="built_env_occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_occup_density_samp, domain=BuiltEnv, range=Optional[str])

slots.built_env_occup_document = Slot(uri=MIXS['0000816'], name="built_env_occup_document", curie=MIXS.curie('0000816'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_occup_document, domain=BuiltEnv, range=Optional[Union[str, "OccupDocumentEnum"]])

slots.built_env_occup_samp = Slot(uri=MIXS['0000772'], name="built_env_occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_occup_samp, domain=BuiltEnv, range=Optional[str])

slots.built_env_organism_count = Slot(uri=MIXS['0000103'], name="built_env_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_organism_count, domain=BuiltEnv, range=Optional[Union[str, List[str]]])

slots.built_env_pres_animal_insect = Slot(uri=MIXS['0000819'], name="built_env_pres_animal_insect", curie=MIXS.curie('0000819'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_pres_animal_insect, domain=BuiltEnv, range=Optional[str])

slots.built_env_quad_pos = Slot(uri=MIXS['0000820'], name="built_env_quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_quad_pos, domain=BuiltEnv, range=Optional[Union[str, "QuadPosEnum"]])

slots.built_env_rel_air_humidity = Slot(uri=MIXS['0000121'], name="built_env_rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_rel_air_humidity, domain=BuiltEnv, range=Optional[str])

slots.built_env_rel_humidity_out = Slot(uri=MIXS['0000188'], name="built_env_rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_rel_humidity_out, domain=BuiltEnv, range=Optional[str])

slots.built_env_rel_samp_loc = Slot(uri=MIXS['0000821'], name="built_env_rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_rel_samp_loc, domain=BuiltEnv, range=Optional[Union[str, "RelSampLocEnum"]])

slots.built_env_room_air_exch_rate = Slot(uri=MIXS['0000169'], name="built_env_room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_air_exch_rate, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_architec_elem = Slot(uri=MIXS['0000233'], name="built_env_room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_architec_elem, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_condt = Slot(uri=MIXS['0000822'], name="built_env_room_condt", curie=MIXS.curie('0000822'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_condt, domain=BuiltEnv, range=Optional[Union[str, "RoomCondtEnum"]])

slots.built_env_room_connected = Slot(uri=MIXS['0000826'], name="built_env_room_connected", curie=MIXS.curie('0000826'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_connected, domain=BuiltEnv, range=Optional[Union[str, "RoomConnectedEnum"]])

slots.built_env_room_count = Slot(uri=MIXS['0000234'], name="built_env_room_count", curie=MIXS.curie('0000234'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_count, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_dim = Slot(uri=MIXS['0000192'], name="built_env_room_dim", curie=MIXS.curie('0000192'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_dim, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_door_dist = Slot(uri=MIXS['0000193'], name="built_env_room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_door_dist, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_door_share = Slot(uri=MIXS['0000242'], name="built_env_room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_door_share, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_hallway = Slot(uri=MIXS['0000238'], name="built_env_room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_hallway, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_loc = Slot(uri=MIXS['0000823'], name="built_env_room_loc", curie=MIXS.curie('0000823'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_loc, domain=BuiltEnv, range=Optional[Union[str, "RoomLocEnum"]])

slots.built_env_room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="built_env_room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_moist_dam_hist, domain=BuiltEnv, range=Optional[int])

slots.built_env_room_net_area = Slot(uri=MIXS['0000194'], name="built_env_room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_net_area, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_occup = Slot(uri=MIXS['0000236'], name="built_env_room_occup", curie=MIXS.curie('0000236'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_occup, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_samp_pos = Slot(uri=MIXS['0000824'], name="built_env_room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_samp_pos, domain=BuiltEnv, range=Optional[Union[str, "RoomSampPosEnum"]])

slots.built_env_room_type = Slot(uri=MIXS['0000825'], name="built_env_room_type", curie=MIXS.curie('0000825'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_type, domain=BuiltEnv, range=Optional[Union[str, "RoomTypeEnum"]])

slots.built_env_room_vol = Slot(uri=MIXS['0000195'], name="built_env_room_vol", curie=MIXS.curie('0000195'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_vol, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_wall_share = Slot(uri=MIXS['0000243'], name="built_env_room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_wall_share, domain=BuiltEnv, range=Optional[str])

slots.built_env_room_window_count = Slot(uri=MIXS['0000237'], name="built_env_room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_room_window_count, domain=BuiltEnv, range=Optional[int])

slots.built_env_samp_floor = Slot(uri=MIXS['0000828'], name="built_env_samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_samp_floor, domain=BuiltEnv, range=Optional[Union[str, "SampFloorEnum"]])

slots.built_env_samp_room_id = Slot(uri=MIXS['0000244'], name="built_env_samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_samp_room_id, domain=BuiltEnv, range=Optional[str])

slots.built_env_samp_sort_meth = Slot(uri=MIXS['0000216'], name="built_env_samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_samp_sort_meth, domain=BuiltEnv, range=Optional[Union[str, List[str]]])

slots.built_env_samp_time_out = Slot(uri=MIXS['0000196'], name="built_env_samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_samp_time_out, domain=BuiltEnv, range=Optional[str])

slots.built_env_samp_weather = Slot(uri=MIXS['0000827'], name="built_env_samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_samp_weather, domain=BuiltEnv, range=Optional[Union[str, "SampWeatherEnum"]])

slots.built_env_season = Slot(uri=MIXS['0000829'], name="built_env_season", curie=MIXS.curie('0000829'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_season, domain=BuiltEnv, range=Optional[str])

slots.built_env_season_use = Slot(uri=MIXS['0000830'], name="built_env_season_use", curie=MIXS.curie('0000830'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_season_use, domain=BuiltEnv, range=Optional[Union[str, "SeasonUseEnum"]])

slots.built_env_shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="built_env_shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_shad_dev_water_mold, domain=BuiltEnv, range=Optional[str])

slots.built_env_shading_device_cond = Slot(uri=MIXS['0000831'], name="built_env_shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_shading_device_cond, domain=BuiltEnv, range=Optional[Union[str, "ShadingDeviceCondEnum"]])

slots.built_env_shading_device_loc = Slot(uri=MIXS['0000832'], name="built_env_shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_shading_device_loc, domain=BuiltEnv, range=Optional[str])

slots.built_env_shading_device_mat = Slot(uri=MIXS['0000245'], name="built_env_shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_shading_device_mat, domain=BuiltEnv, range=Optional[str])

slots.built_env_shading_device_type = Slot(uri=MIXS['0000835'], name="built_env_shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_shading_device_type, domain=BuiltEnv, range=Optional[Union[str, "ShadingDeviceTypeEnum"]])

slots.built_env_size_frac = Slot(uri=MIXS['0000017'], name="built_env_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_size_frac, domain=BuiltEnv, range=Optional[str])

slots.built_env_space_typ_state = Slot(uri=MIXS['0000770'], name="built_env_space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_space_typ_state, domain=BuiltEnv, range=Optional[str])

slots.built_env_specific = Slot(uri=MIXS['0000836'], name="built_env_specific", curie=MIXS.curie('0000836'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_specific, domain=BuiltEnv, range=Optional[Union[str, "SpecificEnum"]])

slots.built_env_specific_ecosystem = Slot(uri="str(uriorcurie)", name="built_env_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.built_env_specific_ecosystem, domain=BuiltEnv, range=Optional[str])

slots.built_env_specific_humidity = Slot(uri=MIXS['0000214'], name="built_env_specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_specific_humidity, domain=BuiltEnv, range=Optional[str])

slots.built_env_substructure_type = Slot(uri=MIXS['0000767'], name="built_env_substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_substructure_type, domain=BuiltEnv, range=Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]])

slots.built_env_surf_air_cont = Slot(uri=MIXS['0000759'], name="built_env_surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_air_cont, domain=BuiltEnv, range=Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]])

slots.built_env_surf_humidity = Slot(uri=MIXS['0000123'], name="built_env_surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_humidity, domain=BuiltEnv, range=Optional[str])

slots.built_env_surf_material = Slot(uri=MIXS['0000758'], name="built_env_surf_material", curie=MIXS.curie('0000758'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_material, domain=BuiltEnv, range=Optional[Union[str, "SurfMaterialEnum"]])

slots.built_env_surf_moisture = Slot(uri=MIXS['0000128'], name="built_env_surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_moisture, domain=BuiltEnv, range=Optional[str])

slots.built_env_surf_moisture_ph = Slot(uri=MIXS['0000760'], name="built_env_surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_moisture_ph, domain=BuiltEnv, range=Optional[float])

slots.built_env_surf_temp = Slot(uri=MIXS['0000125'], name="built_env_surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_surf_temp, domain=BuiltEnv, range=Optional[str])

slots.built_env_temp = Slot(uri=MIXS['0000113'], name="built_env_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_temp, domain=BuiltEnv, range=Optional[str])

slots.built_env_temp_out = Slot(uri=MIXS['0000197'], name="built_env_temp_out", curie=MIXS.curie('0000197'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_temp_out, domain=BuiltEnv, range=Optional[str])

slots.built_env_train_line = Slot(uri=MIXS['0000837'], name="built_env_train_line", curie=MIXS.curie('0000837'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_train_line, domain=BuiltEnv, range=Optional[Union[str, "TrainLineEnum"]])

slots.built_env_train_stat_loc = Slot(uri=MIXS['0000838'], name="built_env_train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_train_stat_loc, domain=BuiltEnv, range=Optional[Union[str, "TrainStatLocEnum"]])

slots.built_env_train_stop_loc = Slot(uri=MIXS['0000839'], name="built_env_train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_train_stop_loc, domain=BuiltEnv, range=Optional[Union[str, "TrainStopLocEnum"]])

slots.built_env_typ_occup_density = Slot(uri=MIXS['0000771'], name="built_env_typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_typ_occup_density, domain=BuiltEnv, range=Optional[float])

slots.built_env_ventilation_type = Slot(uri=MIXS['0000756'], name="built_env_ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_ventilation_type, domain=BuiltEnv, range=Optional[str])

slots.built_env_vis_media = Slot(uri=MIXS['0000840'], name="built_env_vis_media", curie=MIXS.curie('0000840'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_vis_media, domain=BuiltEnv, range=Optional[Union[str, "VisMediaEnum"]])

slots.built_env_wall_area = Slot(uri=MIXS['0000198'], name="built_env_wall_area", curie=MIXS.curie('0000198'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_area, domain=BuiltEnv, range=Optional[str])

slots.built_env_wall_const_type = Slot(uri=MIXS['0000841'], name="built_env_wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_const_type, domain=BuiltEnv, range=Optional[Union[str, "WallConstTypeEnum"]])

slots.built_env_wall_finish_mat = Slot(uri=MIXS['0000842'], name="built_env_wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_finish_mat, domain=BuiltEnv, range=Optional[Union[str, "WallFinishMatEnum"]])

slots.built_env_wall_height = Slot(uri=MIXS['0000221'], name="built_env_wall_height", curie=MIXS.curie('0000221'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_height, domain=BuiltEnv, range=Optional[str])

slots.built_env_wall_loc = Slot(uri=MIXS['0000843'], name="built_env_wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_loc, domain=BuiltEnv, range=Optional[Union[str, "WallLocEnum"]])

slots.built_env_wall_surf_treatment = Slot(uri=MIXS['0000845'], name="built_env_wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_surf_treatment, domain=BuiltEnv, range=Optional[Union[str, "WallSurfTreatmentEnum"]])

slots.built_env_wall_texture = Slot(uri=MIXS['0000846'], name="built_env_wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_texture, domain=BuiltEnv, range=Optional[Union[str, "WallTextureEnum"]])

slots.built_env_wall_thermal_mass = Slot(uri=MIXS['0000222'], name="built_env_wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_thermal_mass, domain=BuiltEnv, range=Optional[str])

slots.built_env_wall_water_mold = Slot(uri=MIXS['0000844'], name="built_env_wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_wall_water_mold, domain=BuiltEnv, range=Optional[str])

slots.built_env_water_feat_size = Slot(uri=MIXS['0000223'], name="built_env_water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_water_feat_size, domain=BuiltEnv, range=Optional[str])

slots.built_env_water_feat_type = Slot(uri=MIXS['0000847'], name="built_env_water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_water_feat_type, domain=BuiltEnv, range=Optional[Union[str, "WaterFeatTypeEnum"]])

slots.built_env_weekday = Slot(uri=MIXS['0000848'], name="built_env_weekday", curie=MIXS.curie('0000848'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_weekday, domain=BuiltEnv, range=Optional[Union[str, "WeekdayEnum"]])

slots.built_env_window_cond = Slot(uri=MIXS['0000849'], name="built_env_window_cond", curie=MIXS.curie('0000849'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_cond, domain=BuiltEnv, range=Optional[Union[str, "WindowCondEnum"]])

slots.built_env_window_cover = Slot(uri=MIXS['0000850'], name="built_env_window_cover", curie=MIXS.curie('0000850'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_cover, domain=BuiltEnv, range=Optional[Union[str, "WindowCoverEnum"]])

slots.built_env_window_horiz_pos = Slot(uri=MIXS['0000851'], name="built_env_window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_horiz_pos, domain=BuiltEnv, range=Optional[Union[str, "WindowHorizPosEnum"]])

slots.built_env_window_loc = Slot(uri=MIXS['0000852'], name="built_env_window_loc", curie=MIXS.curie('0000852'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_loc, domain=BuiltEnv, range=Optional[Union[str, "WindowLocEnum"]])

slots.built_env_window_mat = Slot(uri=MIXS['0000853'], name="built_env_window_mat", curie=MIXS.curie('0000853'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_mat, domain=BuiltEnv, range=Optional[Union[str, "WindowMatEnum"]])

slots.built_env_window_open_freq = Slot(uri=MIXS['0000246'], name="built_env_window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_open_freq, domain=BuiltEnv, range=Optional[str])

slots.built_env_window_size = Slot(uri=MIXS['0000224'], name="built_env_window_size", curie=MIXS.curie('0000224'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_size, domain=BuiltEnv, range=Optional[str])

slots.built_env_window_status = Slot(uri=MIXS['0000855'], name="built_env_window_status", curie=MIXS.curie('0000855'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_status, domain=BuiltEnv, range=Optional[str])

slots.built_env_window_type = Slot(uri=MIXS['0000856'], name="built_env_window_type", curie=MIXS.curie('0000856'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_type, domain=BuiltEnv, range=Optional[Union[str, "WindowTypeEnum"]])

slots.built_env_window_vert_pos = Slot(uri=MIXS['0000857'], name="built_env_window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_vert_pos, domain=BuiltEnv, range=Optional[Union[str, "WindowVertPosEnum"]])

slots.built_env_window_water_mold = Slot(uri=MIXS['0000854'], name="built_env_window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_window_water_mold, domain=BuiltEnv, range=Optional[str])

slots.built_env_horizon_meth = Slot(uri=MIXS['0000321'], name="built_env_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_horizon_meth, domain=BuiltEnv, range=Optional[str])

slots.dh_mutliview_common_columns_samp_name = Slot(uri=MIXS['0001107'], name="dh_mutliview_common_columns_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC_SUB_SCHEMA.dh_mutliview_common_columns_samp_name, domain=None, range=Optional[str])

slots.dh_mutliview_common_columns_source_mat_id = Slot(uri=MIXS['0000026'], name="dh_mutliview_common_columns_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC_SUB_SCHEMA.dh_mutliview_common_columns_source_mat_id, domain=None, range=Union[str, DhMutliviewCommonColumnsSourceMatId])

slots.hcr_cores_additional_info = Slot(uri=MIXS['0000300'], name="hcr_cores_additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_additional_info, domain=HcrCores, range=Optional[str])

slots.hcr_cores_alkalinity = Slot(uri=MIXS['0000421'], name="hcr_cores_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_alkalinity, domain=HcrCores, range=Optional[str])

slots.hcr_cores_alkalinity_method = Slot(uri=MIXS['0000298'], name="hcr_cores_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_alkalinity_method, domain=HcrCores, range=Optional[str])

slots.hcr_cores_alt = Slot(uri=MIXS['0000094'], name="hcr_cores_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_alt, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ammonium = Slot(uri=MIXS['0000427'], name="hcr_cores_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ammonium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_api = Slot(uri=MIXS['0000157'], name="hcr_cores_api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_api, domain=HcrCores, range=Optional[str])

slots.hcr_cores_aromatics_pc = Slot(uri=MIXS['0000133'], name="hcr_cores_aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_aromatics_pc, domain=HcrCores, range=Optional[str])

slots.hcr_cores_asphaltenes_pc = Slot(uri=MIXS['0000135'], name="hcr_cores_asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_asphaltenes_pc, domain=HcrCores, range=Optional[str])

slots.hcr_cores_basin = Slot(uri=MIXS['0000290'], name="hcr_cores_basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_basin, domain=HcrCores, range=Optional[str])

slots.hcr_cores_benzene = Slot(uri=MIXS['0000153'], name="hcr_cores_benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_benzene, domain=HcrCores, range=Optional[str])

slots.hcr_cores_calcium = Slot(uri=MIXS['0000432'], name="hcr_cores_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_calcium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_chloride = Slot(uri=MIXS['0000429'], name="hcr_cores_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_chloride, domain=HcrCores, range=Optional[str])

slots.hcr_cores_collection_date = Slot(uri=MIXS['0000011'], name="hcr_cores_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_collection_date, domain=HcrCores, range=Optional[str])

slots.hcr_cores_density = Slot(uri=MIXS['0000435'], name="hcr_cores_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_density, domain=HcrCores, range=Optional[str])

slots.hcr_cores_depos_env = Slot(uri=MIXS['0000992'], name="hcr_cores_depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_depos_env, domain=HcrCores, range=Optional[Union[str, "DeposEnvEnum"]])

slots.hcr_cores_depth = Slot(uri=MIXS['0000018'], name="hcr_cores_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_depth, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="hcr_cores_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_carb_dioxide, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="hcr_cores_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_inorg_carb, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="hcr_cores_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_inorg_phosp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_iron = Slot(uri=MIXS['0000139'], name="hcr_cores_diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_iron, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_org_carb = Slot(uri=MIXS['0000433'], name="hcr_cores_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_org_carb, domain=HcrCores, range=Optional[str])

slots.hcr_cores_diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="hcr_cores_diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_diss_oxygen_fluid, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ecosystem = Slot(uri="str(uriorcurie)", name="hcr_cores_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ecosystem, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ecosystem_category = Slot(uri="str(uriorcurie)", name="hcr_cores_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ecosystem_category, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="hcr_cores_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ecosystem_subtype, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ecosystem_type = Slot(uri="str(uriorcurie)", name="hcr_cores_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ecosystem_type, domain=HcrCores, range=Optional[str])

slots.hcr_cores_elev = Slot(uri=MIXS['0000093'], name="hcr_cores_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_elev, domain=HcrCores, range=Optional[float])

slots.hcr_cores_env_broad_scale = Slot(uri=MIXS['0000012'], name="hcr_cores_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_env_broad_scale, domain=HcrCores, range=Optional[str])

slots.hcr_cores_env_local_scale = Slot(uri=MIXS['0000013'], name="hcr_cores_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_env_local_scale, domain=HcrCores, range=Optional[str])

slots.hcr_cores_env_medium = Slot(uri=MIXS['0000014'], name="hcr_cores_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_env_medium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ethylbenzene = Slot(uri=MIXS['0000155'], name="hcr_cores_ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ethylbenzene, domain=HcrCores, range=Optional[str])

slots.hcr_cores_experimental_factor = Slot(uri=MIXS['0000008'], name="hcr_cores_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_experimental_factor, domain=HcrCores, range=Optional[str])

slots.hcr_cores_field = Slot(uri=MIXS['0000291'], name="hcr_cores_field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_field, domain=HcrCores, range=Optional[str])

slots.hcr_cores_geo_loc_name = Slot(uri=MIXS['0000010'], name="hcr_cores_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_geo_loc_name, domain=HcrCores, range=Optional[str])

slots.hcr_cores_hc_produced = Slot(uri=MIXS['0000989'], name="hcr_cores_hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hc_produced, domain=HcrCores, range=Optional[Union[str, "HcProducedEnum"]])

slots.hcr_cores_hcr = Slot(uri=MIXS['0000988'], name="hcr_cores_hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hcr, domain=HcrCores, range=Optional[Union[str, "HcrEnum"]])

slots.hcr_cores_hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_cores_hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hcr_fw_salinity, domain=HcrCores, range=Optional[str])

slots.hcr_cores_hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_cores_hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hcr_geol_age, domain=HcrCores, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.hcr_cores_hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_cores_hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hcr_pressure, domain=HcrCores, range=Optional[str])

slots.hcr_cores_hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_cores_hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_hcr_temp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_lat_lon = Slot(uri=MIXS['0000009'], name="hcr_cores_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_lat_lon, domain=HcrCores, range=Optional[str])

slots.hcr_cores_lithology = Slot(uri=MIXS['0000990'], name="hcr_cores_lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_lithology, domain=HcrCores, range=Optional[Union[str, "LithologyEnum"]])

slots.hcr_cores_magnesium = Slot(uri=MIXS['0000431'], name="hcr_cores_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_magnesium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_misc_param = Slot(uri=MIXS['0000752'], name="hcr_cores_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_misc_param, domain=HcrCores, range=Optional[Union[str, List[str]]])

slots.hcr_cores_nitrate = Slot(uri=MIXS['0000425'], name="hcr_cores_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_nitrate, domain=HcrCores, range=Optional[str])

slots.hcr_cores_nitrite = Slot(uri=MIXS['0000426'], name="hcr_cores_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_nitrite, domain=HcrCores, range=Optional[str])

slots.hcr_cores_org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="hcr_cores_org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_org_count_qpcr_info, domain=HcrCores, range=Optional[str])

slots.hcr_cores_organism_count = Slot(uri=MIXS['0000103'], name="hcr_cores_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_organism_count, domain=HcrCores, range=Optional[Union[str, List[str]]])

slots.hcr_cores_owc_tvdss = Slot(uri=MIXS['0000405'], name="hcr_cores_owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_owc_tvdss, domain=HcrCores, range=Optional[str])

slots.hcr_cores_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="hcr_cores_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_oxy_stat_samp, domain=HcrCores, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.hcr_cores_permeability = Slot(uri=MIXS['0000404'], name="hcr_cores_permeability", curie=MIXS.curie('0000404'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_permeability, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ph = Slot(uri=MIXS['0001001'], name="hcr_cores_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ph, domain=HcrCores, range=Optional[str])

slots.hcr_cores_porosity = Slot(uri=MIXS['0000211'], name="hcr_cores_porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_porosity, domain=HcrCores, range=Optional[str])

slots.hcr_cores_potassium = Slot(uri=MIXS['0000430'], name="hcr_cores_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_potassium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_pour_point = Slot(uri=MIXS['0000127'], name="hcr_cores_pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_pour_point, domain=HcrCores, range=Optional[str])

slots.hcr_cores_pressure = Slot(uri=MIXS['0000412'], name="hcr_cores_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_pressure, domain=HcrCores, range=Optional[str])

slots.hcr_cores_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="hcr_cores_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_rel_to_oxygen, domain=HcrCores, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.hcr_cores_reservoir = Slot(uri=MIXS['0000303'], name="hcr_cores_reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_reservoir, domain=HcrCores, range=Optional[str])

slots.hcr_cores_resins_pc = Slot(uri=MIXS['0000134'], name="hcr_cores_resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_resins_pc, domain=HcrCores, range=Optional[str])

slots.hcr_cores_salinity = Slot(uri=MIXS['0000183'], name="hcr_cores_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_salinity, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_collec_device = Slot(uri=MIXS['0000002'], name="hcr_cores_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_collec_device, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_collec_method = Slot(uri=MIXS['0001225'], name="hcr_cores_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_collec_method, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_mat_process = Slot(uri=MIXS['0000016'], name="hcr_cores_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_mat_process, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_md = Slot(uri=MIXS['0000413'], name="hcr_cores_samp_md", curie=MIXS.curie('0000413'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_md, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_size = Slot(uri=MIXS['0000001'], name="hcr_cores_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_size, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_store_dur = Slot(uri=MIXS['0000116'], name="hcr_cores_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_store_dur, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_store_loc = Slot(uri=MIXS['0000755'], name="hcr_cores_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_store_loc, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_store_temp = Slot(uri=MIXS['0000110'], name="hcr_cores_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_store_temp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_subtype = Slot(uri=MIXS['0000999'], name="hcr_cores_samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_subtype, domain=HcrCores, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.hcr_cores_samp_transport_cond = Slot(uri=MIXS['0000410'], name="hcr_cores_samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_transport_cond, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_tvdss = Slot(uri=MIXS['0000409'], name="hcr_cores_samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_tvdss, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_type = Slot(uri=MIXS['0000998'], name="hcr_cores_samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_type, domain=HcrCores, range=Optional[str])

slots.hcr_cores_samp_well_name = Slot(uri=MIXS['0000296'], name="hcr_cores_samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_samp_well_name, domain=HcrCores, range=Optional[str])

slots.hcr_cores_saturates_pc = Slot(uri=MIXS['0000131'], name="hcr_cores_saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_saturates_pc, domain=HcrCores, range=Optional[str])

slots.hcr_cores_size_frac = Slot(uri=MIXS['0000017'], name="hcr_cores_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_size_frac, domain=HcrCores, range=Optional[str])

slots.hcr_cores_sodium = Slot(uri=MIXS['0000428'], name="hcr_cores_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sodium, domain=HcrCores, range=Optional[str])

slots.hcr_cores_specific_ecosystem = Slot(uri="str(uriorcurie)", name="hcr_cores_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_specific_ecosystem, domain=HcrCores, range=Optional[str])

slots.hcr_cores_sr_dep_env = Slot(uri=MIXS['0000996'], name="hcr_cores_sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sr_dep_env, domain=HcrCores, range=Optional[Union[str, "SrDepEnvEnum"]])

slots.hcr_cores_sr_geol_age = Slot(uri=MIXS['0000997'], name="hcr_cores_sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sr_geol_age, domain=HcrCores, range=Optional[Union[str, "SrGeolAgeEnum"]])

slots.hcr_cores_sr_kerog_type = Slot(uri=MIXS['0000994'], name="hcr_cores_sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sr_kerog_type, domain=HcrCores, range=Optional[Union[str, "SrKerogTypeEnum"]])

slots.hcr_cores_sr_lithology = Slot(uri=MIXS['0000995'], name="hcr_cores_sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sr_lithology, domain=HcrCores, range=Optional[Union[str, "SrLithologyEnum"]])

slots.hcr_cores_sulfate = Slot(uri=MIXS['0000423'], name="hcr_cores_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sulfate, domain=HcrCores, range=Optional[str])

slots.hcr_cores_sulfate_fw = Slot(uri=MIXS['0000407'], name="hcr_cores_sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sulfate_fw, domain=HcrCores, range=Optional[str])

slots.hcr_cores_sulfide = Slot(uri=MIXS['0000424'], name="hcr_cores_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_sulfide, domain=HcrCores, range=Optional[str])

slots.hcr_cores_suspend_solids = Slot(uri=MIXS['0000150'], name="hcr_cores_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_suspend_solids, domain=HcrCores, range=Optional[Union[str, List[str]]])

slots.hcr_cores_tan = Slot(uri=MIXS['0000120'], name="hcr_cores_tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tan, domain=HcrCores, range=Optional[str])

slots.hcr_cores_temp = Slot(uri=MIXS['0000113'], name="hcr_cores_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_temp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_toluene = Slot(uri=MIXS['0000154'], name="hcr_cores_toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_toluene, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tot_iron = Slot(uri=MIXS['0000105'], name="hcr_cores_tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tot_iron, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tot_nitro = Slot(uri=MIXS['0000102'], name="hcr_cores_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tot_nitro, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tot_phosp = Slot(uri=MIXS['0000117'], name="hcr_cores_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tot_phosp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tot_sulfur = Slot(uri=MIXS['0000419'], name="hcr_cores_tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tot_sulfur, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="hcr_cores_tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tvdss_of_hcr_press, domain=HcrCores, range=Optional[str])

slots.hcr_cores_tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="hcr_cores_tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_tvdss_of_hcr_temp, domain=HcrCores, range=Optional[str])

slots.hcr_cores_vfa = Slot(uri=MIXS['0000152'], name="hcr_cores_vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_vfa, domain=HcrCores, range=Optional[str])

slots.hcr_cores_vfa_fw = Slot(uri=MIXS['0000408'], name="hcr_cores_vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_vfa_fw, domain=HcrCores, range=Optional[str])

slots.hcr_cores_viscosity = Slot(uri=MIXS['0000126'], name="hcr_cores_viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_viscosity, domain=HcrCores, range=Optional[str])

slots.hcr_cores_win = Slot(uri=MIXS['0000297'], name="hcr_cores_win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_win, domain=HcrCores, range=Optional[str])

slots.hcr_cores_xylene = Slot(uri=MIXS['0000156'], name="hcr_cores_xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_xylene, domain=HcrCores, range=Optional[str])

slots.hcr_cores_horizon_meth = Slot(uri=MIXS['0000321'], name="hcr_cores_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_horizon_meth, domain=HcrCores, range=Optional[str])

slots.hcr_cores_ph_meth = Slot(uri=MIXS['0001106'], name="hcr_cores_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_ph_meth, domain=HcrCores, range=Optional[str])

slots.hcr_fluids_swabs_add_recov_method = Slot(uri=MIXS['0001009'], name="hcr_fluids_swabs_add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_add_recov_method, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_additional_info = Slot(uri=MIXS['0000300'], name="hcr_fluids_swabs_additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_additional_info, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_alkalinity = Slot(uri=MIXS['0000421'], name="hcr_fluids_swabs_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_alkalinity, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_alkalinity_method = Slot(uri=MIXS['0000298'], name="hcr_fluids_swabs_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_alkalinity_method, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_alt = Slot(uri=MIXS['0000094'], name="hcr_fluids_swabs_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_alt, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ammonium = Slot(uri=MIXS['0000427'], name="hcr_fluids_swabs_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ammonium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_api = Slot(uri=MIXS['0000157'], name="hcr_fluids_swabs_api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_api, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_aromatics_pc = Slot(uri=MIXS['0000133'], name="hcr_fluids_swabs_aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_aromatics_pc, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_asphaltenes_pc = Slot(uri=MIXS['0000135'], name="hcr_fluids_swabs_asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_asphaltenes_pc, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_basin = Slot(uri=MIXS['0000290'], name="hcr_fluids_swabs_basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_basin, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_benzene = Slot(uri=MIXS['0000153'], name="hcr_fluids_swabs_benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_benzene, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_biocide = Slot(uri=MIXS['0001011'], name="hcr_fluids_swabs_biocide", curie=MIXS.curie('0001011'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_biocide, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_biocide_admin_method = Slot(uri=MIXS['0000456'], name="hcr_fluids_swabs_biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_biocide_admin_method, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_calcium = Slot(uri=MIXS['0000432'], name="hcr_fluids_swabs_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_calcium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_chem_treat_method = Slot(uri=MIXS['0000457'], name="hcr_fluids_swabs_chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_chem_treat_method, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_chem_treatment = Slot(uri=MIXS['0001012'], name="hcr_fluids_swabs_chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_chem_treatment, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_chloride = Slot(uri=MIXS['0000429'], name="hcr_fluids_swabs_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_chloride, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_collection_date = Slot(uri=MIXS['0000011'], name="hcr_fluids_swabs_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_collection_date, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_density = Slot(uri=MIXS['0000435'], name="hcr_fluids_swabs_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_density, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_depos_env = Slot(uri=MIXS['0000992'], name="hcr_fluids_swabs_depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_depos_env, domain=HcrFluidsSwabs, range=Optional[Union[str, "DeposEnvEnum"]])

slots.hcr_fluids_swabs_depth = Slot(uri=MIXS['0000018'], name="hcr_fluids_swabs_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_depth, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="hcr_fluids_swabs_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_carb_dioxide, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="hcr_fluids_swabs_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_inorg_carb, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="hcr_fluids_swabs_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_inorg_phosp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_iron = Slot(uri=MIXS['0000139'], name="hcr_fluids_swabs_diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_iron, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_org_carb = Slot(uri=MIXS['0000433'], name="hcr_fluids_swabs_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_org_carb, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="hcr_fluids_swabs_diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_diss_oxygen_fluid, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ecosystem = Slot(uri="str(uriorcurie)", name="hcr_fluids_swabs_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ecosystem, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ecosystem_category = Slot(uri="str(uriorcurie)", name="hcr_fluids_swabs_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ecosystem_category, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="hcr_fluids_swabs_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ecosystem_subtype, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ecosystem_type = Slot(uri="str(uriorcurie)", name="hcr_fluids_swabs_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ecosystem_type, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_elev = Slot(uri=MIXS['0000093'], name="hcr_fluids_swabs_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_elev, domain=HcrFluidsSwabs, range=Optional[float])

slots.hcr_fluids_swabs_env_broad_scale = Slot(uri=MIXS['0000012'], name="hcr_fluids_swabs_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_env_broad_scale, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_env_local_scale = Slot(uri=MIXS['0000013'], name="hcr_fluids_swabs_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_env_local_scale, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_env_medium = Slot(uri=MIXS['0000014'], name="hcr_fluids_swabs_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_env_medium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ethylbenzene = Slot(uri=MIXS['0000155'], name="hcr_fluids_swabs_ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ethylbenzene, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_experimental_factor = Slot(uri=MIXS['0000008'], name="hcr_fluids_swabs_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_experimental_factor, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_field = Slot(uri=MIXS['0000291'], name="hcr_fluids_swabs_field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_field, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_geo_loc_name = Slot(uri=MIXS['0000010'], name="hcr_fluids_swabs_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_geo_loc_name, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_hc_produced = Slot(uri=MIXS['0000989'], name="hcr_fluids_swabs_hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hc_produced, domain=HcrFluidsSwabs, range=Optional[Union[str, "HcProducedEnum"]])

slots.hcr_fluids_swabs_hcr = Slot(uri=MIXS['0000988'], name="hcr_fluids_swabs_hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hcr, domain=HcrFluidsSwabs, range=Optional[Union[str, "HcrEnum"]])

slots.hcr_fluids_swabs_hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fluids_swabs_hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hcr_fw_salinity, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_fluids_swabs_hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hcr_geol_age, domain=HcrFluidsSwabs, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.hcr_fluids_swabs_hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_fluids_swabs_hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hcr_pressure, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_fluids_swabs_hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_hcr_temp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_iw_bt_date_well = Slot(uri=MIXS['0001010'], name="hcr_fluids_swabs_iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_iw_bt_date_well, domain=HcrFluidsSwabs, range=Optional[Union[dict, "TimestampValue"]])

slots.hcr_fluids_swabs_iwf = Slot(uri=MIXS['0000455'], name="hcr_fluids_swabs_iwf", curie=MIXS.curie('0000455'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_iwf, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_lat_lon = Slot(uri=MIXS['0000009'], name="hcr_fluids_swabs_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_lat_lon, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_lithology = Slot(uri=MIXS['0000990'], name="hcr_fluids_swabs_lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_lithology, domain=HcrFluidsSwabs, range=Optional[Union[str, "LithologyEnum"]])

slots.hcr_fluids_swabs_magnesium = Slot(uri=MIXS['0000431'], name="hcr_fluids_swabs_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_magnesium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_misc_param = Slot(uri=MIXS['0000752'], name="hcr_fluids_swabs_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_misc_param, domain=HcrFluidsSwabs, range=Optional[Union[str, List[str]]])

slots.hcr_fluids_swabs_nitrate = Slot(uri=MIXS['0000425'], name="hcr_fluids_swabs_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_nitrate, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_nitrite = Slot(uri=MIXS['0000426'], name="hcr_fluids_swabs_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_nitrite, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="hcr_fluids_swabs_org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_org_count_qpcr_info, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_organism_count = Slot(uri=MIXS['0000103'], name="hcr_fluids_swabs_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_organism_count, domain=HcrFluidsSwabs, range=Optional[Union[str, List[str]]])

slots.hcr_fluids_swabs_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="hcr_fluids_swabs_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_oxy_stat_samp, domain=HcrFluidsSwabs, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.hcr_fluids_swabs_ph = Slot(uri=MIXS['0001001'], name="hcr_fluids_swabs_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ph, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_potassium = Slot(uri=MIXS['0000430'], name="hcr_fluids_swabs_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_potassium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_pour_point = Slot(uri=MIXS['0000127'], name="hcr_fluids_swabs_pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_pour_point, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_pressure = Slot(uri=MIXS['0000412'], name="hcr_fluids_swabs_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_pressure, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_prod_rate = Slot(uri=MIXS['0000452'], name="hcr_fluids_swabs_prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_prod_rate, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_prod_start_date = Slot(uri=MIXS['0001008'], name="hcr_fluids_swabs_prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_prod_start_date, domain=HcrFluidsSwabs, range=Optional[Union[dict, "TimestampValue"]])

slots.hcr_fluids_swabs_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="hcr_fluids_swabs_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_rel_to_oxygen, domain=HcrFluidsSwabs, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.hcr_fluids_swabs_reservoir = Slot(uri=MIXS['0000303'], name="hcr_fluids_swabs_reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_reservoir, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_resins_pc = Slot(uri=MIXS['0000134'], name="hcr_fluids_swabs_resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_resins_pc, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_salinity = Slot(uri=MIXS['0000183'], name="hcr_fluids_swabs_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_salinity, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_collec_device = Slot(uri=MIXS['0000002'], name="hcr_fluids_swabs_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_collec_device, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_collec_method = Slot(uri=MIXS['0001225'], name="hcr_fluids_swabs_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_collec_method, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_collect_point = Slot(uri=MIXS['0001015'], name="hcr_fluids_swabs_samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_collect_point, domain=HcrFluidsSwabs, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.hcr_fluids_swabs_samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="hcr_fluids_swabs_samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_loc_corr_rate, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_mat_process = Slot(uri=MIXS['0000016'], name="hcr_fluids_swabs_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_mat_process, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_preserv = Slot(uri=MIXS['0000463'], name="hcr_fluids_swabs_samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_preserv, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_size = Slot(uri=MIXS['0000001'], name="hcr_fluids_swabs_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_size, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_store_dur = Slot(uri=MIXS['0000116'], name="hcr_fluids_swabs_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_store_dur, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_store_loc = Slot(uri=MIXS['0000755'], name="hcr_fluids_swabs_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_store_loc, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_store_temp = Slot(uri=MIXS['0000110'], name="hcr_fluids_swabs_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_store_temp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_subtype = Slot(uri=MIXS['0000999'], name="hcr_fluids_swabs_samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_subtype, domain=HcrFluidsSwabs, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.hcr_fluids_swabs_samp_transport_cond = Slot(uri=MIXS['0000410'], name="hcr_fluids_swabs_samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_transport_cond, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_type = Slot(uri=MIXS['0000998'], name="hcr_fluids_swabs_samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_type, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_samp_well_name = Slot(uri=MIXS['0000296'], name="hcr_fluids_swabs_samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_samp_well_name, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_saturates_pc = Slot(uri=MIXS['0000131'], name="hcr_fluids_swabs_saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_saturates_pc, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_size_frac = Slot(uri=MIXS['0000017'], name="hcr_fluids_swabs_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_size_frac, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_sodium = Slot(uri=MIXS['0000428'], name="hcr_fluids_swabs_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_sodium, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_specific_ecosystem = Slot(uri="str(uriorcurie)", name="hcr_fluids_swabs_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_specific_ecosystem, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_sulfate = Slot(uri=MIXS['0000423'], name="hcr_fluids_swabs_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_sulfate, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_sulfate_fw = Slot(uri=MIXS['0000407'], name="hcr_fluids_swabs_sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_sulfate_fw, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_sulfide = Slot(uri=MIXS['0000424'], name="hcr_fluids_swabs_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_sulfide, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_suspend_solids = Slot(uri=MIXS['0000150'], name="hcr_fluids_swabs_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_suspend_solids, domain=HcrFluidsSwabs, range=Optional[Union[str, List[str]]])

slots.hcr_fluids_swabs_tan = Slot(uri=MIXS['0000120'], name="hcr_fluids_swabs_tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tan, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_temp = Slot(uri=MIXS['0000113'], name="hcr_fluids_swabs_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_temp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_toluene = Slot(uri=MIXS['0000154'], name="hcr_fluids_swabs_toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_toluene, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tot_iron = Slot(uri=MIXS['0000105'], name="hcr_fluids_swabs_tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tot_iron, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tot_nitro = Slot(uri=MIXS['0000102'], name="hcr_fluids_swabs_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tot_nitro, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tot_phosp = Slot(uri=MIXS['0000117'], name="hcr_fluids_swabs_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tot_phosp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tot_sulfur = Slot(uri=MIXS['0000419'], name="hcr_fluids_swabs_tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tot_sulfur, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="hcr_fluids_swabs_tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tvdss_of_hcr_press, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="hcr_fluids_swabs_tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_tvdss_of_hcr_temp, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_vfa = Slot(uri=MIXS['0000152'], name="hcr_fluids_swabs_vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_vfa, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_vfa_fw = Slot(uri=MIXS['0000408'], name="hcr_fluids_swabs_vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_vfa_fw, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_viscosity = Slot(uri=MIXS['0000126'], name="hcr_fluids_swabs_viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_viscosity, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_water_cut = Slot(uri=MIXS['0000454'], name="hcr_fluids_swabs_water_cut", curie=MIXS.curie('0000454'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_water_cut, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_water_prod_rate = Slot(uri=MIXS['0000453'], name="hcr_fluids_swabs_water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_water_prod_rate, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_win = Slot(uri=MIXS['0000297'], name="hcr_fluids_swabs_win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_win, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_xylene = Slot(uri=MIXS['0000156'], name="hcr_fluids_swabs_xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_xylene, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_horizon_meth = Slot(uri=MIXS['0000321'], name="hcr_fluids_swabs_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_horizon_meth, domain=HcrFluidsSwabs, range=Optional[str])

slots.hcr_fluids_swabs_ph_meth = Slot(uri=MIXS['0001106'], name="hcr_fluids_swabs_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_ph_meth, domain=HcrFluidsSwabs, range=Optional[str])

slots.host_associated_alt = Slot(uri=MIXS['0000094'], name="host_associated_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_alt, domain=HostAssociated, range=Optional[str])

slots.host_associated_ances_data = Slot(uri=MIXS['0000247'], name="host_associated_ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_ances_data, domain=HostAssociated, range=Optional[str])

slots.host_associated_biol_stat = Slot(uri=MIXS['0000858'], name="host_associated_biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_biol_stat, domain=HostAssociated, range=Optional[Union[str, "BiolStatEnum"]])

slots.host_associated_blood_press_diast = Slot(uri=MIXS['0000258'], name="host_associated_blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_blood_press_diast, domain=HostAssociated, range=Optional[str])

slots.host_associated_blood_press_syst = Slot(uri=MIXS['0000259'], name="host_associated_blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_blood_press_syst, domain=HostAssociated, range=Optional[str])

slots.host_associated_chem_administration = Slot(uri=MIXS['0000751'], name="host_associated_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_chem_administration, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_collection_date = Slot(uri=MIXS['0000011'], name="host_associated_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_collection_date, domain=HostAssociated, range=Optional[str])

slots.host_associated_depth = Slot(uri=MIXS['0000018'], name="host_associated_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_depth, domain=HostAssociated, range=Optional[str])

slots.host_associated_ecosystem = Slot(uri="str(uriorcurie)", name="host_associated_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.host_associated_ecosystem, domain=HostAssociated, range=Optional[str])

slots.host_associated_ecosystem_category = Slot(uri="str(uriorcurie)", name="host_associated_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.host_associated_ecosystem_category, domain=HostAssociated, range=Optional[str])

slots.host_associated_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="host_associated_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.host_associated_ecosystem_subtype, domain=HostAssociated, range=Optional[str])

slots.host_associated_ecosystem_type = Slot(uri="str(uriorcurie)", name="host_associated_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.host_associated_ecosystem_type, domain=HostAssociated, range=Optional[str])

slots.host_associated_elev = Slot(uri=MIXS['0000093'], name="host_associated_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_elev, domain=HostAssociated, range=Optional[float])

slots.host_associated_env_broad_scale = Slot(uri=MIXS['0000012'], name="host_associated_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_env_broad_scale, domain=HostAssociated, range=Optional[str])

slots.host_associated_env_local_scale = Slot(uri=MIXS['0000013'], name="host_associated_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_env_local_scale, domain=HostAssociated, range=Optional[str])

slots.host_associated_env_medium = Slot(uri=MIXS['0000014'], name="host_associated_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_env_medium, domain=HostAssociated, range=Optional[str])

slots.host_associated_experimental_factor = Slot(uri=MIXS['0000008'], name="host_associated_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_experimental_factor, domain=HostAssociated, range=Optional[str])

slots.host_associated_genetic_mod = Slot(uri=MIXS['0000859'], name="host_associated_genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_genetic_mod, domain=HostAssociated, range=Optional[str])

slots.host_associated_geo_loc_name = Slot(uri=MIXS['0000010'], name="host_associated_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_geo_loc_name, domain=HostAssociated, range=Optional[str])

slots.host_associated_gravidity = Slot(uri=MIXS['0000875'], name="host_associated_gravidity", curie=MIXS.curie('0000875'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_gravidity, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_age = Slot(uri=MIXS['0000255'], name="host_associated_host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_age, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_body_habitat = Slot(uri=MIXS['0000866'], name="host_associated_host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_body_habitat, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_body_product = Slot(uri=MIXS['0000888'], name="host_associated_host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_body_product, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_body_site = Slot(uri=MIXS['0000867'], name="host_associated_host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_body_site, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_body_temp = Slot(uri=MIXS['0000274'], name="host_associated_host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_body_temp, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_color = Slot(uri=MIXS['0000260'], name="host_associated_host_color", curie=MIXS.curie('0000260'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_color, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_common_name = Slot(uri=MIXS['0000248'], name="host_associated_host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_common_name, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_diet = Slot(uri=MIXS['0000869'], name="host_associated_host_diet", curie=MIXS.curie('0000869'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_diet, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_host_dry_mass = Slot(uri=MIXS['0000257'], name="host_associated_host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_dry_mass, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_family_relation = Slot(uri=MIXS['0000872'], name="host_associated_host_family_relation", curie=MIXS.curie('0000872'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_family_relation, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_host_genotype = Slot(uri=MIXS['0000365'], name="host_associated_host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_genotype, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_growth_cond = Slot(uri=MIXS['0000871'], name="host_associated_host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_growth_cond, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_height = Slot(uri=MIXS['0000264'], name="host_associated_host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_height, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_last_meal = Slot(uri=MIXS['0000870'], name="host_associated_host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_last_meal, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_host_length = Slot(uri=MIXS['0000256'], name="host_associated_host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_length, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_life_stage = Slot(uri=MIXS['0000251'], name="host_associated_host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_life_stage, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_phenotype = Slot(uri=MIXS['0000874'], name="host_associated_host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_phenotype, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_sex = Slot(uri=MIXS['0000811'], name="host_associated_host_sex", curie=MIXS.curie('0000811'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_sex, domain=HostAssociated, range=Optional[Union[str, "HostSexEnum"]])

slots.host_associated_host_shape = Slot(uri=MIXS['0000261'], name="host_associated_host_shape", curie=MIXS.curie('0000261'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_shape, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_subject_id = Slot(uri=MIXS['0000861'], name="host_associated_host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_subject_id, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="host_associated_host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_subspecf_genlin, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_host_substrate = Slot(uri=MIXS['0000252'], name="host_associated_host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_substrate, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_symbiont = Slot(uri=MIXS['0001298'], name="host_associated_host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_symbiont, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_host_taxid = Slot(uri=MIXS['0000250'], name="host_associated_host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_taxid, domain=HostAssociated, range=Optional[str])

slots.host_associated_host_tot_mass = Slot(uri=MIXS['0000263'], name="host_associated_host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_host_tot_mass, domain=HostAssociated, range=Optional[str])

slots.host_associated_lat_lon = Slot(uri=MIXS['0000009'], name="host_associated_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_lat_lon, domain=HostAssociated, range=Optional[str])

slots.host_associated_misc_param = Slot(uri=MIXS['0000752'], name="host_associated_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_misc_param, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_organism_count = Slot(uri=MIXS['0000103'], name="host_associated_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_organism_count, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="host_associated_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_oxy_stat_samp, domain=HostAssociated, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.host_associated_perturbation = Slot(uri=MIXS['0000754'], name="host_associated_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_perturbation, domain=HostAssociated, range=Optional[Union[str, List[str]]])

slots.host_associated_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="host_associated_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_rel_to_oxygen, domain=HostAssociated, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.host_associated_salinity = Slot(uri=MIXS['0000183'], name="host_associated_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_salinity, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_capt_status = Slot(uri=MIXS['0000860'], name="host_associated_samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_capt_status, domain=HostAssociated, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.host_associated_samp_collec_device = Slot(uri=MIXS['0000002'], name="host_associated_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_collec_device, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_collec_method = Slot(uri=MIXS['0001225'], name="host_associated_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_collec_method, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_dis_stage = Slot(uri=MIXS['0000249'], name="host_associated_samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_dis_stage, domain=HostAssociated, range=Optional[Union[str, "SampDisStageEnum"]])

slots.host_associated_samp_mat_process = Slot(uri=MIXS['0000016'], name="host_associated_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_mat_process, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_size = Slot(uri=MIXS['0000001'], name="host_associated_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_size, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_store_dur = Slot(uri=MIXS['0000116'], name="host_associated_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_store_dur, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_store_loc = Slot(uri=MIXS['0000755'], name="host_associated_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_store_loc, domain=HostAssociated, range=Optional[str])

slots.host_associated_samp_store_temp = Slot(uri=MIXS['0000110'], name="host_associated_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_samp_store_temp, domain=HostAssociated, range=Optional[str])

slots.host_associated_size_frac = Slot(uri=MIXS['0000017'], name="host_associated_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_size_frac, domain=HostAssociated, range=Optional[str])

slots.host_associated_specific_ecosystem = Slot(uri="str(uriorcurie)", name="host_associated_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.host_associated_specific_ecosystem, domain=HostAssociated, range=Optional[str])

slots.host_associated_temp = Slot(uri=MIXS['0000113'], name="host_associated_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_temp, domain=HostAssociated, range=Optional[str])

slots.host_associated_horizon_meth = Slot(uri=MIXS['0000321'], name="host_associated_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_horizon_meth, domain=HostAssociated, range=Optional[str])

slots.jgi_mg_dna_cont_well = Slot(uri="str(uriorcurie)", name="jgi_mg_dna_cont_well", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.jgi_mg_dna_cont_well, domain=JgiMg, range=Optional[str])

slots.misc_envs_alkalinity = Slot(uri=MIXS['0000421'], name="misc_envs_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_alkalinity, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_alt = Slot(uri=MIXS['0000094'], name="misc_envs_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_alt, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ammonium = Slot(uri=MIXS['0000427'], name="misc_envs_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ammonium, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_biomass = Slot(uri=MIXS['0000174'], name="misc_envs_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_biomass, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_bromide = Slot(uri=MIXS['0000176'], name="misc_envs_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_bromide, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_calcium = Slot(uri=MIXS['0000432'], name="misc_envs_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_calcium, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_chem_administration = Slot(uri=MIXS['0000751'], name="misc_envs_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_chem_administration, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_chloride = Slot(uri=MIXS['0000429'], name="misc_envs_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_chloride, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_chlorophyll = Slot(uri=MIXS['0000177'], name="misc_envs_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_chlorophyll, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_collection_date = Slot(uri=MIXS['0000011'], name="misc_envs_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_collection_date, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_density = Slot(uri=MIXS['0000435'], name="misc_envs_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_density, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_depth = Slot(uri=MIXS['0000018'], name="misc_envs_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_depth, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_diether_lipids = Slot(uri=MIXS['0000178'], name="misc_envs_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diether_lipids, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="misc_envs_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diss_carb_dioxide, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_diss_hydrogen = Slot(uri=MIXS['0000179'], name="misc_envs_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diss_hydrogen, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="misc_envs_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diss_inorg_carb, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_diss_org_nitro = Slot(uri=MIXS['0000162'], name="misc_envs_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diss_org_nitro, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_diss_oxygen = Slot(uri=MIXS['0000119'], name="misc_envs_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_diss_oxygen, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ecosystem = Slot(uri="str(uriorcurie)", name="misc_envs_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ecosystem, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ecosystem_category = Slot(uri="str(uriorcurie)", name="misc_envs_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ecosystem_category, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="misc_envs_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ecosystem_subtype, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ecosystem_type = Slot(uri="str(uriorcurie)", name="misc_envs_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ecosystem_type, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_elev = Slot(uri=MIXS['0000093'], name="misc_envs_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_elev, domain=MiscEnvs, range=Optional[float])

slots.misc_envs_env_broad_scale = Slot(uri=MIXS['0000012'], name="misc_envs_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_env_broad_scale, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_env_local_scale = Slot(uri=MIXS['0000013'], name="misc_envs_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_env_local_scale, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_env_medium = Slot(uri=MIXS['0000014'], name="misc_envs_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_env_medium, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_experimental_factor = Slot(uri=MIXS['0000008'], name="misc_envs_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_experimental_factor, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_geo_loc_name = Slot(uri=MIXS['0000010'], name="misc_envs_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_geo_loc_name, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_lat_lon = Slot(uri=MIXS['0000009'], name="misc_envs_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_lat_lon, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_misc_param = Slot(uri=MIXS['0000752'], name="misc_envs_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_misc_param, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_nitrate = Slot(uri=MIXS['0000425'], name="misc_envs_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_nitrate, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_nitrite = Slot(uri=MIXS['0000426'], name="misc_envs_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_nitrite, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_nitro = Slot(uri=MIXS['0000504'], name="misc_envs_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_nitro, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_org_carb = Slot(uri=MIXS['0000508'], name="misc_envs_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_org_carb, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_org_matter = Slot(uri=MIXS['0000204'], name="misc_envs_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_org_matter, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_org_nitro = Slot(uri=MIXS['0000205'], name="misc_envs_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_org_nitro, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_organism_count = Slot(uri=MIXS['0000103'], name="misc_envs_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_organism_count, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="misc_envs_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_oxy_stat_samp, domain=MiscEnvs, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.misc_envs_perturbation = Slot(uri=MIXS['0000754'], name="misc_envs_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_perturbation, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_ph = Slot(uri=MIXS['0001001'], name="misc_envs_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ph, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_phosphate = Slot(uri=MIXS['0000505'], name="misc_envs_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_phosphate, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="misc_envs_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_phosplipid_fatt_acid, domain=MiscEnvs, range=Optional[Union[str, List[str]]])

slots.misc_envs_potassium = Slot(uri=MIXS['0000430'], name="misc_envs_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_potassium, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_pressure = Slot(uri=MIXS['0000412'], name="misc_envs_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_pressure, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="misc_envs_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_rel_to_oxygen, domain=MiscEnvs, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.misc_envs_salinity = Slot(uri=MIXS['0000183'], name="misc_envs_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_salinity, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_collec_device = Slot(uri=MIXS['0000002'], name="misc_envs_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_collec_device, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_collec_method = Slot(uri=MIXS['0001225'], name="misc_envs_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_collec_method, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_mat_process = Slot(uri=MIXS['0000016'], name="misc_envs_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_mat_process, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_size = Slot(uri=MIXS['0000001'], name="misc_envs_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_size, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_store_dur = Slot(uri=MIXS['0000116'], name="misc_envs_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_store_dur, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_store_loc = Slot(uri=MIXS['0000755'], name="misc_envs_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_store_loc, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_samp_store_temp = Slot(uri=MIXS['0000110'], name="misc_envs_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_samp_store_temp, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_silicate = Slot(uri=MIXS['0000184'], name="misc_envs_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_silicate, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_size_frac = Slot(uri=MIXS['0000017'], name="misc_envs_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_size_frac, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_sodium = Slot(uri=MIXS['0000428'], name="misc_envs_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_sodium, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_specific_ecosystem = Slot(uri="str(uriorcurie)", name="misc_envs_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_specific_ecosystem, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_sulfate = Slot(uri=MIXS['0000423'], name="misc_envs_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_sulfate, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_sulfide = Slot(uri=MIXS['0000424'], name="misc_envs_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_sulfide, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_temp = Slot(uri=MIXS['0000113'], name="misc_envs_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_temp, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_water_current = Slot(uri=MIXS['0000203'], name="misc_envs_water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_water_current, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_horizon_meth = Slot(uri=MIXS['0000321'], name="misc_envs_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_horizon_meth, domain=MiscEnvs, range=Optional[str])

slots.misc_envs_ph_meth = Slot(uri=MIXS['0001106'], name="misc_envs_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_ph_meth, domain=MiscEnvs, range=Optional[str])

slots.plant_associated_air_temp_regm = Slot(uri=MIXS['0000551'], name="plant_associated_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_air_temp_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_alt = Slot(uri=MIXS['0000094'], name="plant_associated_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_alt, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_ances_data = Slot(uri=MIXS['0000247'], name="plant_associated_ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ances_data, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_antibiotic_regm = Slot(uri=MIXS['0000553'], name="plant_associated_antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_antibiotic_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_biol_stat = Slot(uri=MIXS['0000858'], name="plant_associated_biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_biol_stat, domain=PlantAssociated, range=Optional[Union[str, "BiolStatEnum"]])

slots.plant_associated_biotic_regm = Slot(uri=MIXS['0001038'], name="plant_associated_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_biotic_regm, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_chem_administration = Slot(uri=MIXS['0000751'], name="plant_associated_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_chem_administration, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_chem_mutagen = Slot(uri=MIXS['0000555'], name="plant_associated_chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_chem_mutagen, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_climate_environment = Slot(uri=MIXS['0001040'], name="plant_associated_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_climate_environment, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_collection_date = Slot(uri=MIXS['0000011'], name="plant_associated_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_collection_date, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_cult_root_med = Slot(uri=MIXS['0001041'], name="plant_associated_cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_cult_root_med, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_depth = Slot(uri=MIXS['0000018'], name="plant_associated_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_depth, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_ecosystem = Slot(uri="str(uriorcurie)", name="plant_associated_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ecosystem, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_ecosystem_category = Slot(uri="str(uriorcurie)", name="plant_associated_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ecosystem_category, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="plant_associated_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ecosystem_subtype, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_ecosystem_type = Slot(uri="str(uriorcurie)", name="plant_associated_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ecosystem_type, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_elev = Slot(uri=MIXS['0000093'], name="plant_associated_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_elev, domain=PlantAssociated, range=Optional[float])

slots.plant_associated_env_broad_scale = Slot(uri=MIXS['0000012'], name="plant_associated_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_env_broad_scale, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_env_local_scale = Slot(uri=MIXS['0000013'], name="plant_associated_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_env_local_scale, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_env_medium = Slot(uri=MIXS['0000014'], name="plant_associated_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_env_medium, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_experimental_factor = Slot(uri=MIXS['0000008'], name="plant_associated_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_experimental_factor, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_fertilizer_regm = Slot(uri=MIXS['0000556'], name="plant_associated_fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_fertilizer_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_fungicide_regm = Slot(uri=MIXS['0000557'], name="plant_associated_fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_fungicide_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_gaseous_environment = Slot(uri=MIXS['0000558'], name="plant_associated_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_gaseous_environment, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_genetic_mod = Slot(uri=MIXS['0000859'], name="plant_associated_genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_genetic_mod, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_geo_loc_name = Slot(uri=MIXS['0000010'], name="plant_associated_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_geo_loc_name, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_gravity = Slot(uri=MIXS['0000559'], name="plant_associated_gravity", curie=MIXS.curie('0000559'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_gravity, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_growth_facil = Slot(uri=MIXS['0001043'], name="plant_associated_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_growth_facil, domain=PlantAssociated, range=Optional[Union[str, "GrowthFacilEnum"]])

slots.plant_associated_growth_habit = Slot(uri=MIXS['0001044'], name="plant_associated_growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_growth_habit, domain=PlantAssociated, range=Optional[Union[str, "GrowthHabitEnum"]])

slots.plant_associated_growth_hormone_regm = Slot(uri=MIXS['0000560'], name="plant_associated_growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_growth_hormone_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_herbicide_regm = Slot(uri=MIXS['0000561'], name="plant_associated_herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_herbicide_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_host_age = Slot(uri=MIXS['0000255'], name="plant_associated_host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_age, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_common_name = Slot(uri=MIXS['0000248'], name="plant_associated_host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_common_name, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_dry_mass = Slot(uri=MIXS['0000257'], name="plant_associated_host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_dry_mass, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_genotype = Slot(uri=MIXS['0000365'], name="plant_associated_host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_genotype, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_height = Slot(uri=MIXS['0000264'], name="plant_associated_host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_height, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_length = Slot(uri=MIXS['0000256'], name="plant_associated_host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_length, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_life_stage = Slot(uri=MIXS['0000251'], name="plant_associated_host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_life_stage, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_phenotype = Slot(uri=MIXS['0000874'], name="plant_associated_host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_phenotype, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="plant_associated_host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_subspecf_genlin, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_host_symbiont = Slot(uri=MIXS['0001298'], name="plant_associated_host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_symbiont, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_host_taxid = Slot(uri=MIXS['0000250'], name="plant_associated_host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_taxid, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_tot_mass = Slot(uri=MIXS['0000263'], name="plant_associated_host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_tot_mass, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_host_wet_mass = Slot(uri=MIXS['0000567'], name="plant_associated_host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_host_wet_mass, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_humidity_regm = Slot(uri=MIXS['0000568'], name="plant_associated_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_humidity_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_lat_lon = Slot(uri=MIXS['0000009'], name="plant_associated_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_lat_lon, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_light_regm = Slot(uri=MIXS['0000569'], name="plant_associated_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_light_regm, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_mechanical_damage = Slot(uri=MIXS['0001052'], name="plant_associated_mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_mechanical_damage, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="plant_associated_mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_mineral_nutr_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_misc_param = Slot(uri=MIXS['0000752'], name="plant_associated_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_misc_param, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_non_min_nutr_regm = Slot(uri=MIXS['0000571'], name="plant_associated_non_min_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_non_min_nutr_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_organism_count = Slot(uri=MIXS['0000103'], name="plant_associated_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_organism_count, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="plant_associated_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_oxy_stat_samp, domain=PlantAssociated, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.plant_associated_perturbation = Slot(uri=MIXS['0000754'], name="plant_associated_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_perturbation, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_pesticide_regm = Slot(uri=MIXS['0000573'], name="plant_associated_pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_pesticide_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_ph_regm = Slot(uri=MIXS['0001056'], name="plant_associated_ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_ph_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_associated_plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_plant_growth_med, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_plant_product = Slot(uri=MIXS['0001058'], name="plant_associated_plant_product", curie=MIXS.curie('0001058'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_plant_product, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_plant_sex = Slot(uri=MIXS['0001059'], name="plant_associated_plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_plant_sex, domain=PlantAssociated, range=Optional[Union[str, "PlantSexEnum"]])

slots.plant_associated_plant_struc = Slot(uri=MIXS['0001060'], name="plant_associated_plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_plant_struc, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_radiation_regm = Slot(uri=MIXS['0000575'], name="plant_associated_radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_radiation_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_rainfall_regm = Slot(uri=MIXS['0000576'], name="plant_associated_rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_rainfall_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="plant_associated_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_rel_to_oxygen, domain=PlantAssociated, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.plant_associated_root_cond = Slot(uri=MIXS['0001061'], name="plant_associated_root_cond", curie=MIXS.curie('0001061'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_cond, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_carbon = Slot(uri=MIXS['0000577'], name="plant_associated_root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_carbon, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_macronutr = Slot(uri=MIXS['0000578'], name="plant_associated_root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_macronutr, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_micronutr = Slot(uri=MIXS['0000579'], name="plant_associated_root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_micronutr, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_ph = Slot(uri=MIXS['0001062'], name="plant_associated_root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_ph, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_regl = Slot(uri=MIXS['0000581'], name="plant_associated_root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_regl, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_solid = Slot(uri=MIXS['0001063'], name="plant_associated_root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_solid, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_root_med_suppl = Slot(uri=MIXS['0000580'], name="plant_associated_root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_root_med_suppl, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_salinity = Slot(uri=MIXS['0000183'], name="plant_associated_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_salinity, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_salt_regm = Slot(uri=MIXS['0000582'], name="plant_associated_salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_salt_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_samp_capt_status = Slot(uri=MIXS['0000860'], name="plant_associated_samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_capt_status, domain=PlantAssociated, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.plant_associated_samp_collec_device = Slot(uri=MIXS['0000002'], name="plant_associated_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_collec_device, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_collec_method = Slot(uri=MIXS['0001225'], name="plant_associated_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_collec_method, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_dis_stage = Slot(uri=MIXS['0000249'], name="plant_associated_samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_dis_stage, domain=PlantAssociated, range=Optional[Union[str, "SampDisStageEnum"]])

slots.plant_associated_samp_mat_process = Slot(uri=MIXS['0000016'], name="plant_associated_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_mat_process, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_size = Slot(uri=MIXS['0000001'], name="plant_associated_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_size, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_store_dur = Slot(uri=MIXS['0000116'], name="plant_associated_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_store_dur, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_store_loc = Slot(uri=MIXS['0000755'], name="plant_associated_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_store_loc, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_samp_store_temp = Slot(uri=MIXS['0000110'], name="plant_associated_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_samp_store_temp, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_season_environment = Slot(uri=MIXS['0001068'], name="plant_associated_season_environment", curie=MIXS.curie('0001068'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_season_environment, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_size_frac = Slot(uri=MIXS['0000017'], name="plant_associated_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_size_frac, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_specific_ecosystem = Slot(uri="str(uriorcurie)", name="plant_associated_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_specific_ecosystem, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_standing_water_regm = Slot(uri=MIXS['0001069'], name="plant_associated_standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_standing_water_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_temp = Slot(uri=MIXS['0000113'], name="plant_associated_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_temp, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="plant_associated_tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_tiss_cult_growth_med, domain=PlantAssociated, range=Optional[str])

slots.plant_associated_water_temp_regm = Slot(uri=MIXS['0000590'], name="plant_associated_water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_water_temp_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_watering_regm = Slot(uri=MIXS['0000591'], name="plant_associated_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_watering_regm, domain=PlantAssociated, range=Optional[Union[str, List[str]]])

slots.plant_associated_horizon_meth = Slot(uri=MIXS['0000321'], name="plant_associated_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_horizon_meth, domain=PlantAssociated, range=Optional[str])

slots.sediment_alkalinity = Slot(uri=MIXS['0000421'], name="sediment_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_alkalinity, domain=Sediment, range=Optional[str])

slots.sediment_alkyl_diethers = Slot(uri=MIXS['0000490'], name="sediment_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_alkyl_diethers, domain=Sediment, range=Optional[str])

slots.sediment_alt = Slot(uri=MIXS['0000094'], name="sediment_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_alt, domain=Sediment, range=Optional[str])

slots.sediment_aminopept_act = Slot(uri=MIXS['0000172'], name="sediment_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_aminopept_act, domain=Sediment, range=Optional[str])

slots.sediment_ammonium = Slot(uri=MIXS['0000427'], name="sediment_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_ammonium, domain=Sediment, range=Optional[str])

slots.sediment_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="sediment_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_bacteria_carb_prod, domain=Sediment, range=Optional[str])

slots.sediment_biomass = Slot(uri=MIXS['0000174'], name="sediment_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_biomass, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_bishomohopanol = Slot(uri=MIXS['0000175'], name="sediment_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_bishomohopanol, domain=Sediment, range=Optional[str])

slots.sediment_bromide = Slot(uri=MIXS['0000176'], name="sediment_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_bromide, domain=Sediment, range=Optional[str])

slots.sediment_calcium = Slot(uri=MIXS['0000432'], name="sediment_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_calcium, domain=Sediment, range=Optional[str])

slots.sediment_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="sediment_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_carb_nitro_ratio, domain=Sediment, range=Optional[float])

slots.sediment_chem_administration = Slot(uri=MIXS['0000751'], name="sediment_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_chem_administration, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_chloride = Slot(uri=MIXS['0000429'], name="sediment_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_chloride, domain=Sediment, range=Optional[str])

slots.sediment_chlorophyll = Slot(uri=MIXS['0000177'], name="sediment_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_chlorophyll, domain=Sediment, range=Optional[str])

slots.sediment_collection_date = Slot(uri=MIXS['0000011'], name="sediment_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_collection_date, domain=Sediment, range=Optional[str])

slots.sediment_density = Slot(uri=MIXS['0000435'], name="sediment_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_density, domain=Sediment, range=Optional[str])

slots.sediment_depth = Slot(uri=MIXS['0000018'], name="sediment_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_depth, domain=Sediment, range=Optional[str])

slots.sediment_diether_lipids = Slot(uri=MIXS['0000178'], name="sediment_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diether_lipids, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="sediment_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_carb_dioxide, domain=Sediment, range=Optional[str])

slots.sediment_diss_hydrogen = Slot(uri=MIXS['0000179'], name="sediment_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_hydrogen, domain=Sediment, range=Optional[str])

slots.sediment_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="sediment_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_inorg_carb, domain=Sediment, range=Optional[str])

slots.sediment_diss_org_carb = Slot(uri=MIXS['0000433'], name="sediment_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_org_carb, domain=Sediment, range=Optional[str])

slots.sediment_diss_org_nitro = Slot(uri=MIXS['0000162'], name="sediment_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_org_nitro, domain=Sediment, range=Optional[str])

slots.sediment_diss_oxygen = Slot(uri=MIXS['0000119'], name="sediment_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_diss_oxygen, domain=Sediment, range=Optional[str])

slots.sediment_ecosystem = Slot(uri="str(uriorcurie)", name="sediment_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.sediment_ecosystem, domain=Sediment, range=Optional[str])

slots.sediment_ecosystem_category = Slot(uri="str(uriorcurie)", name="sediment_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.sediment_ecosystem_category, domain=Sediment, range=Optional[str])

slots.sediment_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="sediment_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.sediment_ecosystem_subtype, domain=Sediment, range=Optional[str])

slots.sediment_ecosystem_type = Slot(uri="str(uriorcurie)", name="sediment_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.sediment_ecosystem_type, domain=Sediment, range=Optional[str])

slots.sediment_elev = Slot(uri=MIXS['0000093'], name="sediment_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_elev, domain=Sediment, range=Optional[float])

slots.sediment_env_broad_scale = Slot(uri=MIXS['0000012'], name="sediment_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_env_broad_scale, domain=Sediment, range=Optional[str])

slots.sediment_env_local_scale = Slot(uri=MIXS['0000013'], name="sediment_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_env_local_scale, domain=Sediment, range=Optional[str])

slots.sediment_env_medium = Slot(uri=MIXS['0000014'], name="sediment_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_env_medium, domain=Sediment, range=Optional[str])

slots.sediment_experimental_factor = Slot(uri=MIXS['0000008'], name="sediment_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_experimental_factor, domain=Sediment, range=Optional[str])

slots.sediment_geo_loc_name = Slot(uri=MIXS['0000010'], name="sediment_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_geo_loc_name, domain=Sediment, range=Optional[str])

slots.sediment_glucosidase_act = Slot(uri=MIXS['0000137'], name="sediment_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_glucosidase_act, domain=Sediment, range=Optional[str])

slots.sediment_lat_lon = Slot(uri=MIXS['0000009'], name="sediment_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_lat_lon, domain=Sediment, range=Optional[str])

slots.sediment_magnesium = Slot(uri=MIXS['0000431'], name="sediment_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_magnesium, domain=Sediment, range=Optional[str])

slots.sediment_mean_frict_vel = Slot(uri=MIXS['0000498'], name="sediment_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_mean_frict_vel, domain=Sediment, range=Optional[str])

slots.sediment_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="sediment_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_mean_peak_frict_vel, domain=Sediment, range=Optional[str])

slots.sediment_methane = Slot(uri=MIXS['0000101'], name="sediment_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_methane, domain=Sediment, range=Optional[str])

slots.sediment_misc_param = Slot(uri=MIXS['0000752'], name="sediment_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_misc_param, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_n_alkanes = Slot(uri=MIXS['0000503'], name="sediment_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_n_alkanes, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_nitrate = Slot(uri=MIXS['0000425'], name="sediment_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_nitrate, domain=Sediment, range=Optional[str])

slots.sediment_nitrite = Slot(uri=MIXS['0000426'], name="sediment_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_nitrite, domain=Sediment, range=Optional[str])

slots.sediment_nitro = Slot(uri=MIXS['0000504'], name="sediment_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_nitro, domain=Sediment, range=Optional[str])

slots.sediment_org_carb = Slot(uri=MIXS['0000508'], name="sediment_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_org_carb, domain=Sediment, range=Optional[str])

slots.sediment_org_matter = Slot(uri=MIXS['0000204'], name="sediment_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_org_matter, domain=Sediment, range=Optional[str])

slots.sediment_org_nitro = Slot(uri=MIXS['0000205'], name="sediment_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_org_nitro, domain=Sediment, range=Optional[str])

slots.sediment_organism_count = Slot(uri=MIXS['0000103'], name="sediment_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_organism_count, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="sediment_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_oxy_stat_samp, domain=Sediment, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.sediment_part_org_carb = Slot(uri=MIXS['0000515'], name="sediment_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_part_org_carb, domain=Sediment, range=Optional[str])

slots.sediment_particle_class = Slot(uri=MIXS['0000206'], name="sediment_particle_class", curie=MIXS.curie('0000206'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_particle_class, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_perturbation = Slot(uri=MIXS['0000754'], name="sediment_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_perturbation, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="sediment_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_petroleum_hydrocarb, domain=Sediment, range=Optional[str])

slots.sediment_ph = Slot(uri=MIXS['0001001'], name="sediment_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_ph, domain=Sediment, range=Optional[str])

slots.sediment_phaeopigments = Slot(uri=MIXS['0000180'], name="sediment_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_phaeopigments, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_phosphate = Slot(uri=MIXS['0000505'], name="sediment_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_phosphate, domain=Sediment, range=Optional[str])

slots.sediment_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="sediment_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_phosplipid_fatt_acid, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_porosity = Slot(uri=MIXS['0000211'], name="sediment_porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_porosity, domain=Sediment, range=Optional[str])

slots.sediment_potassium = Slot(uri=MIXS['0000430'], name="sediment_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_potassium, domain=Sediment, range=Optional[str])

slots.sediment_pressure = Slot(uri=MIXS['0000412'], name="sediment_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_pressure, domain=Sediment, range=Optional[str])

slots.sediment_redox_potential = Slot(uri=MIXS['0000182'], name="sediment_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_redox_potential, domain=Sediment, range=Optional[str])

slots.sediment_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="sediment_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_rel_to_oxygen, domain=Sediment, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.sediment_salinity = Slot(uri=MIXS['0000183'], name="sediment_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_salinity, domain=Sediment, range=Optional[str])

slots.sediment_samp_collec_device = Slot(uri=MIXS['0000002'], name="sediment_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_collec_device, domain=Sediment, range=Optional[str])

slots.sediment_samp_collec_method = Slot(uri=MIXS['0001225'], name="sediment_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_collec_method, domain=Sediment, range=Optional[str])

slots.sediment_samp_mat_process = Slot(uri=MIXS['0000016'], name="sediment_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_mat_process, domain=Sediment, range=Optional[str])

slots.sediment_samp_size = Slot(uri=MIXS['0000001'], name="sediment_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_size, domain=Sediment, range=Optional[str])

slots.sediment_samp_store_dur = Slot(uri=MIXS['0000116'], name="sediment_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_store_dur, domain=Sediment, range=Optional[str])

slots.sediment_samp_store_loc = Slot(uri=MIXS['0000755'], name="sediment_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_store_loc, domain=Sediment, range=Optional[str])

slots.sediment_samp_store_temp = Slot(uri=MIXS['0000110'], name="sediment_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_samp_store_temp, domain=Sediment, range=Optional[str])

slots.sediment_sediment_type = Slot(uri=MIXS['0001078'], name="sediment_sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_sediment_type, domain=Sediment, range=Optional[Union[str, "SedimentTypeEnum"]])

slots.sediment_silicate = Slot(uri=MIXS['0000184'], name="sediment_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_silicate, domain=Sediment, range=Optional[str])

slots.sediment_size_frac = Slot(uri=MIXS['0000017'], name="sediment_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_size_frac, domain=Sediment, range=Optional[str])

slots.sediment_sodium = Slot(uri=MIXS['0000428'], name="sediment_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_sodium, domain=Sediment, range=Optional[str])

slots.sediment_specific_ecosystem = Slot(uri="str(uriorcurie)", name="sediment_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.sediment_specific_ecosystem, domain=Sediment, range=Optional[str])

slots.sediment_sulfate = Slot(uri=MIXS['0000423'], name="sediment_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_sulfate, domain=Sediment, range=Optional[str])

slots.sediment_sulfide = Slot(uri=MIXS['0000424'], name="sediment_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_sulfide, domain=Sediment, range=Optional[str])

slots.sediment_temp = Slot(uri=MIXS['0000113'], name="sediment_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_temp, domain=Sediment, range=Optional[str])

slots.sediment_tidal_stage = Slot(uri=MIXS['0000750'], name="sediment_tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_tidal_stage, domain=Sediment, range=Optional[Union[str, "TidalStageEnum"]])

slots.sediment_tot_carb = Slot(uri=MIXS['0000525'], name="sediment_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_tot_carb, domain=Sediment, range=Optional[str])

slots.sediment_tot_depth_water_col = Slot(uri=MIXS['0000634'], name="sediment_tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_tot_depth_water_col, domain=Sediment, range=Optional[str])

slots.sediment_tot_nitro_content = Slot(uri=MIXS['0000530'], name="sediment_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_tot_nitro_content, domain=Sediment, range=Optional[str])

slots.sediment_tot_org_carb = Slot(uri=MIXS['0000533'], name="sediment_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_tot_org_carb, domain=Sediment, range=Optional[str])

slots.sediment_turbidity = Slot(uri=MIXS['0000191'], name="sediment_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_turbidity, domain=Sediment, range=Optional[str])

slots.sediment_water_content = Slot(uri=MIXS['0000185'], name="sediment_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_water_content, domain=Sediment, range=Optional[Union[str, List[str]]])

slots.sediment_horizon_meth = Slot(uri=MIXS['0000321'], name="sediment_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_horizon_meth, domain=Sediment, range=Optional[str])

slots.sediment_ph_meth = Slot(uri=MIXS['0001106'], name="sediment_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_ph_meth, domain=Sediment, range=Optional[str])

slots.soil_agrochem_addition = Slot(uri=MIXS['0000639'], name="soil_agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_SUB_SCHEMA.soil_agrochem_addition, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_air_temp_regm = Slot(uri=MIXS['0000551'], name="soil_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.soil_air_temp_regm, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_al_sat = Slot(uri=MIXS['0000607'], name="soil_al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_SUB_SCHEMA.soil_al_sat, domain=Soil, range=Optional[str])

slots.soil_al_sat_meth = Slot(uri=MIXS['0000324'], name="soil_al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_SUB_SCHEMA.soil_al_sat_meth, domain=Soil, range=Optional[str])

slots.soil_alt = Slot(uri=MIXS['0000094'], name="soil_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.soil_alt, domain=Soil, range=Optional[str])

slots.soil_annual_precpt = Slot(uri=MIXS['0000644'], name="soil_annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_SUB_SCHEMA.soil_annual_precpt, domain=Soil, range=Optional[str])

slots.soil_annual_temp = Slot(uri=MIXS['0000642'], name="soil_annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_SUB_SCHEMA.soil_annual_temp, domain=Soil, range=Optional[str])

slots.soil_biotic_regm = Slot(uri=MIXS['0001038'], name="soil_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.soil_biotic_regm, domain=Soil, range=Optional[str])

slots.soil_biotic_relationship = Slot(uri=MIXS['0000028'], name="soil_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_SUB_SCHEMA.soil_biotic_relationship, domain=Soil, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.soil_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="soil_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.soil_carb_nitro_ratio, domain=Soil, range=Optional[float])

slots.soil_chem_administration = Slot(uri=MIXS['0000751'], name="soil_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.soil_chem_administration, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_climate_environment = Slot(uri=MIXS['0001040'], name="soil_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.soil_climate_environment, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_collection_date = Slot(uri=MIXS['0000011'], name="soil_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.soil_collection_date, domain=Soil, range=Optional[str])

slots.soil_crop_rotation = Slot(uri=MIXS['0000318'], name="soil_crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_SUB_SCHEMA.soil_crop_rotation, domain=Soil, range=Optional[str])

slots.soil_cur_land_use = Slot(uri=MIXS['0001080'], name="soil_cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_SUB_SCHEMA.soil_cur_land_use, domain=Soil, range=Optional[Union[str, "CurLandUseEnum"]])

slots.soil_cur_vegetation = Slot(uri=MIXS['0000312'], name="soil_cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_SUB_SCHEMA.soil_cur_vegetation, domain=Soil, range=Optional[str])

slots.soil_cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="soil_cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_SUB_SCHEMA.soil_cur_vegetation_meth, domain=Soil, range=Optional[str])

slots.soil_depth = Slot(uri=MIXS['0000018'], name="soil_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.soil_depth, domain=Soil, range=Optional[str])

slots.soil_drainage_class = Slot(uri=MIXS['0001085'], name="soil_drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_SUB_SCHEMA.soil_drainage_class, domain=Soil, range=Optional[Union[str, "DrainageClassEnum"]])

slots.soil_ecosystem = Slot(uri="str(uriorcurie)", name="soil_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.soil_ecosystem, domain=Soil, range=Optional[Union[str, "EcosystemEnum"]])

slots.soil_ecosystem_category = Slot(uri="str(uriorcurie)", name="soil_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.soil_ecosystem_category, domain=Soil, range=Optional[Union[str, "EcosystemCategoryEnum"]])

slots.soil_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="soil_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.soil_ecosystem_subtype, domain=Soil, range=Optional[Union[str, "EcosystemSubtypeEnum"]])

slots.soil_ecosystem_type = Slot(uri="str(uriorcurie)", name="soil_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.soil_ecosystem_type, domain=Soil, range=Optional[Union[str, "EcosystemTypeEnum"]])

slots.soil_elev = Slot(uri=MIXS['0000093'], name="soil_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.soil_elev, domain=Soil, range=Optional[float])

slots.soil_env_broad_scale = Slot(uri=MIXS['0000012'], name="soil_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.soil_env_broad_scale, domain=Soil, range=Optional[Union[str, "EnvBroadScaleSoilEnum"]])

slots.soil_env_local_scale = Slot(uri=MIXS['0000013'], name="soil_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.soil_env_local_scale, domain=Soil, range=Optional[Union[str, "EnvLocalScaleSoilEnum"]])

slots.soil_env_medium = Slot(uri=MIXS['0000014'], name="soil_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.soil_env_medium, domain=Soil, range=Optional[Union[str, "EnvMediumSoilEnum"]])

slots.soil_experimental_factor = Slot(uri=MIXS['0000008'], name="soil_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.soil_experimental_factor, domain=Soil, range=Optional[str])

slots.soil_extreme_event = Slot(uri=MIXS['0000320'], name="soil_extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_SUB_SCHEMA.soil_extreme_event, domain=Soil, range=Optional[str])

slots.soil_fao_class = Slot(uri=MIXS['0001083'], name="soil_fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_SUB_SCHEMA.soil_fao_class, domain=Soil, range=Optional[Union[str, "FaoClassEnum"]])

slots.soil_fire = Slot(uri=MIXS['0001086'], name="soil_fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_SUB_SCHEMA.soil_fire, domain=Soil, range=Optional[str])

slots.soil_flooding = Slot(uri=MIXS['0000319'], name="soil_flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_SUB_SCHEMA.soil_flooding, domain=Soil, range=Optional[str])

slots.soil_gaseous_environment = Slot(uri=MIXS['0000558'], name="soil_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.soil_gaseous_environment, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_geo_loc_name = Slot(uri=MIXS['0000010'], name="soil_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.soil_geo_loc_name, domain=Soil, range=Optional[str])

slots.soil_growth_facil = Slot(uri=MIXS['0001043'], name="soil_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.soil_growth_facil, domain=Soil, range=Optional[Union[str, "GrowthFacilEnum"]])

slots.soil_heavy_metals = Slot(uri=MIXS['0000652'], name="soil_heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_SUB_SCHEMA.soil_heavy_metals, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_heavy_metals_meth = Slot(uri=MIXS['0000343'], name="soil_heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_SUB_SCHEMA.soil_heavy_metals_meth, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_horizon_meth = Slot(uri=MIXS['0000321'], name="soil_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.soil_horizon_meth, domain=Soil, range=Optional[str])

slots.soil_humidity_regm = Slot(uri=MIXS['0000568'], name="soil_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.soil_humidity_regm, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_lat_lon = Slot(uri=MIXS['0000009'], name="soil_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.soil_lat_lon, domain=Soil, range=Optional[str])

slots.soil_light_regm = Slot(uri=MIXS['0000569'], name="soil_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.soil_light_regm, domain=Soil, range=Optional[str])

slots.soil_link_class_info = Slot(uri=MIXS['0000329'], name="soil_link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_SUB_SCHEMA.soil_link_class_info, domain=Soil, range=Optional[str])

slots.soil_link_climate_info = Slot(uri=MIXS['0000328'], name="soil_link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_SUB_SCHEMA.soil_link_climate_info, domain=Soil, range=Optional[str])

slots.soil_local_class = Slot(uri=MIXS['0000330'], name="soil_local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_SUB_SCHEMA.soil_local_class, domain=Soil, range=Optional[str])

slots.soil_local_class_meth = Slot(uri=MIXS['0000331'], name="soil_local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_SUB_SCHEMA.soil_local_class_meth, domain=Soil, range=Optional[str])

slots.soil_micro_biomass_meth = Slot(uri=MIXS['0000339'], name="soil_micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_SUB_SCHEMA.soil_micro_biomass_meth, domain=Soil, range=Optional[str])

slots.soil_microbial_biomass = Slot(uri=MIXS['0000650'], name="soil_microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_SUB_SCHEMA.soil_microbial_biomass, domain=Soil, range=Optional[str])

slots.soil_misc_param = Slot(uri=MIXS['0000752'], name="soil_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.soil_misc_param, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_org_matter = Slot(uri=MIXS['0000204'], name="soil_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.soil_org_matter, domain=Soil, range=Optional[str])

slots.soil_org_nitro = Slot(uri=MIXS['0000205'], name="soil_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.soil_org_nitro, domain=Soil, range=Optional[str])

slots.soil_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="soil_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.soil_oxy_stat_samp, domain=Soil, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.soil_ph = Slot(uri=MIXS['0001001'], name="soil_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.soil_ph, domain=Soil, range=Optional[str])

slots.soil_ph_meth = Slot(uri=MIXS['0001106'], name="soil_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.soil_ph_meth, domain=Soil, range=Optional[str])

slots.soil_phosphate = Slot(uri=MIXS['0000505'], name="soil_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.soil_phosphate, domain=Soil, range=Optional[str])

slots.soil_prev_land_use_meth = Slot(uri=MIXS['0000316'], name="soil_prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_SUB_SCHEMA.soil_prev_land_use_meth, domain=Soil, range=Optional[str])

slots.soil_previous_land_use = Slot(uri=MIXS['0000315'], name="soil_previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_SUB_SCHEMA.soil_previous_land_use, domain=Soil, range=Optional[str])

slots.soil_profile_position = Slot(uri=MIXS['0001084'], name="soil_profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_SUB_SCHEMA.soil_profile_position, domain=Soil, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.soil_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="soil_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.soil_rel_to_oxygen, domain=Soil, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.soil_salinity = Slot(uri=MIXS['0000183'], name="soil_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.soil_salinity, domain=Soil, range=Optional[str])

slots.soil_salinity_meth = Slot(uri=MIXS['0000341'], name="soil_salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_SUB_SCHEMA.soil_salinity_meth, domain=Soil, range=Optional[str])

slots.soil_samp_collec_device = Slot(uri=MIXS['0000002'], name="soil_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.soil_samp_collec_device, domain=Soil, range=Optional[str])

slots.soil_samp_collec_method = Slot(uri=MIXS['0001225'], name="soil_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.soil_samp_collec_method, domain=Soil, range=Optional[str])

slots.soil_samp_mat_process = Slot(uri=MIXS['0000016'], name="soil_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.soil_samp_mat_process, domain=Soil, range=Optional[str])

slots.soil_samp_size = Slot(uri=MIXS['0000001'], name="soil_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.soil_samp_size, domain=Soil, range=Optional[str])

slots.soil_samp_store_temp = Slot(uri=MIXS['0000110'], name="soil_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.soil_samp_store_temp, domain=Soil, range=Optional[str])

slots.soil_season_precpt = Slot(uri=MIXS['0000645'], name="soil_season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_SUB_SCHEMA.soil_season_precpt, domain=Soil, range=Optional[str])

slots.soil_season_temp = Slot(uri=MIXS['0000643'], name="soil_season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_SUB_SCHEMA.soil_season_temp, domain=Soil, range=Optional[str])

slots.soil_sieving = Slot(uri=MIXS['0000322'], name="soil_sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_SUB_SCHEMA.soil_sieving, domain=Soil, range=Optional[str])

slots.soil_size_frac_low = Slot(uri=MIXS['0000735'], name="soil_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.soil_size_frac_low, domain=Soil, range=Optional[str])

slots.soil_size_frac_up = Slot(uri=MIXS['0000736'], name="soil_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.soil_size_frac_up, domain=Soil, range=Optional[str])

slots.soil_slope_aspect = Slot(uri=MIXS['0000647'], name="soil_slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_SUB_SCHEMA.soil_slope_aspect, domain=Soil, range=Optional[str])

slots.soil_slope_gradient = Slot(uri=MIXS['0000646'], name="soil_slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_SUB_SCHEMA.soil_slope_gradient, domain=Soil, range=Optional[str])

slots.soil_soil_horizon = Slot(uri=MIXS['0001082'], name="soil_soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_SUB_SCHEMA.soil_soil_horizon, domain=Soil, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_SUB_SCHEMA.soil_soil_text_measure, domain=Soil, range=Optional[str])

slots.soil_soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_SUB_SCHEMA.soil_soil_texture_meth, domain=Soil, range=Optional[str])

slots.soil_soil_type = Slot(uri=MIXS['0000332'], name="soil_soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_SUB_SCHEMA.soil_soil_type, domain=Soil, range=Optional[str])

slots.soil_soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_SUB_SCHEMA.soil_soil_type_meth, domain=Soil, range=Optional[str])

slots.soil_specific_ecosystem = Slot(uri="str(uriorcurie)", name="soil_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.soil_specific_ecosystem, domain=Soil, range=Optional[Union[str, "SpecificEcosystemEnum"]])

slots.soil_store_cond = Slot(uri=MIXS['0000327'], name="soil_store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_SUB_SCHEMA.soil_store_cond, domain=Soil, range=Optional[Union[str, "StoreCondEnum"]])

slots.soil_temp = Slot(uri=MIXS['0000113'], name="soil_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.soil_temp, domain=Soil, range=Optional[str])

slots.soil_tillage = Slot(uri=MIXS['0001081'], name="soil_tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tillage, domain=Soil, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.soil_tot_carb = Slot(uri=MIXS['0000525'], name="soil_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_carb, domain=Soil, range=Optional[str])

slots.soil_tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="soil_tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_nitro_cont_meth, domain=Soil, range=Optional[str])

slots.soil_tot_nitro_content = Slot(uri=MIXS['0000530'], name="soil_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_nitro_content, domain=Soil, range=Optional[str])

slots.soil_tot_org_c_meth = Slot(uri=MIXS['0000337'], name="soil_tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_org_c_meth, domain=Soil, range=Optional[str])

slots.soil_tot_org_carb = Slot(uri=MIXS['0000533'], name="soil_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_org_carb, domain=Soil, range=Optional[str])

slots.soil_tot_phosp = Slot(uri=MIXS['0000117'], name="soil_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.soil_tot_phosp, domain=Soil, range=Optional[str])

slots.soil_water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="soil_water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_SUB_SCHEMA.soil_water_cont_soil_meth, domain=Soil, range=Optional[str])

slots.soil_water_content = Slot(uri=MIXS['0000185'], name="soil_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.soil_water_content, domain=Soil, range=Optional[Union[str, List[str]]])

slots.soil_watering_regm = Slot(uri=MIXS['0000591'], name="soil_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.soil_watering_regm, domain=Soil, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_alkalinity = Slot(uri=MIXS['0000421'], name="wastewater_sludge_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_alkalinity, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_alt = Slot(uri=MIXS['0000094'], name="wastewater_sludge_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_alt, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="wastewater_sludge_biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_biochem_oxygen_dem, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_chem_administration = Slot(uri=MIXS['0000751'], name="wastewater_sludge_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_chem_administration, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="wastewater_sludge_chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_chem_oxygen_dem, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_collection_date = Slot(uri=MIXS['0000011'], name="wastewater_sludge_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_collection_date, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_depth = Slot(uri=MIXS['0000018'], name="wastewater_sludge_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_depth, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_ecosystem = Slot(uri="str(uriorcurie)", name="wastewater_sludge_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ecosystem, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_ecosystem_category = Slot(uri="str(uriorcurie)", name="wastewater_sludge_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ecosystem_category, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="wastewater_sludge_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ecosystem_subtype, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_ecosystem_type = Slot(uri="str(uriorcurie)", name="wastewater_sludge_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ecosystem_type, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_efficiency_percent = Slot(uri=MIXS['0000657'], name="wastewater_sludge_efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_efficiency_percent, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_elev = Slot(uri=MIXS['0000093'], name="wastewater_sludge_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_elev, domain=WastewaterSludge, range=Optional[float])

slots.wastewater_sludge_emulsions = Slot(uri=MIXS['0000660'], name="wastewater_sludge_emulsions", curie=MIXS.curie('0000660'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_emulsions, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_env_broad_scale = Slot(uri=MIXS['0000012'], name="wastewater_sludge_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_env_broad_scale, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_env_local_scale = Slot(uri=MIXS['0000013'], name="wastewater_sludge_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_env_local_scale, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_env_medium = Slot(uri=MIXS['0000014'], name="wastewater_sludge_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_env_medium, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_experimental_factor = Slot(uri=MIXS['0000008'], name="wastewater_sludge_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_experimental_factor, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_gaseous_substances = Slot(uri=MIXS['0000661'], name="wastewater_sludge_gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_gaseous_substances, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_geo_loc_name = Slot(uri=MIXS['0000010'], name="wastewater_sludge_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_geo_loc_name, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_indust_eff_percent = Slot(uri=MIXS['0000662'], name="wastewater_sludge_indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_indust_eff_percent, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_inorg_particles = Slot(uri=MIXS['0000664'], name="wastewater_sludge_inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_inorg_particles, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_lat_lon = Slot(uri=MIXS['0000009'], name="wastewater_sludge_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_lat_lon, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_misc_param = Slot(uri=MIXS['0000752'], name="wastewater_sludge_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_misc_param, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_nitrate = Slot(uri=MIXS['0000425'], name="wastewater_sludge_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_nitrate, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_org_particles = Slot(uri=MIXS['0000665'], name="wastewater_sludge_org_particles", curie=MIXS.curie('0000665'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_org_particles, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_organism_count = Slot(uri=MIXS['0000103'], name="wastewater_sludge_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_organism_count, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="wastewater_sludge_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_oxy_stat_samp, domain=WastewaterSludge, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.wastewater_sludge_perturbation = Slot(uri=MIXS['0000754'], name="wastewater_sludge_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_perturbation, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_ph = Slot(uri=MIXS['0001001'], name="wastewater_sludge_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ph, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_phosphate = Slot(uri=MIXS['0000505'], name="wastewater_sludge_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_phosphate, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_pre_treatment = Slot(uri=MIXS['0000348'], name="wastewater_sludge_pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_pre_treatment, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_primary_treatment = Slot(uri=MIXS['0000349'], name="wastewater_sludge_primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_primary_treatment, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_reactor_type = Slot(uri=MIXS['0000350'], name="wastewater_sludge_reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_reactor_type, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="wastewater_sludge_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_rel_to_oxygen, domain=WastewaterSludge, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.wastewater_sludge_salinity = Slot(uri=MIXS['0000183'], name="wastewater_sludge_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_salinity, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_collec_device = Slot(uri=MIXS['0000002'], name="wastewater_sludge_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_collec_device, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_collec_method = Slot(uri=MIXS['0001225'], name="wastewater_sludge_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_collec_method, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_mat_process = Slot(uri=MIXS['0000016'], name="wastewater_sludge_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_mat_process, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_size = Slot(uri=MIXS['0000001'], name="wastewater_sludge_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_size, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_store_dur = Slot(uri=MIXS['0000116'], name="wastewater_sludge_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_store_dur, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_store_loc = Slot(uri=MIXS['0000755'], name="wastewater_sludge_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_store_loc, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_samp_store_temp = Slot(uri=MIXS['0000110'], name="wastewater_sludge_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_samp_store_temp, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_secondary_treatment = Slot(uri=MIXS['0000351'], name="wastewater_sludge_secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_secondary_treatment, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_sewage_type = Slot(uri=MIXS['0000215'], name="wastewater_sludge_sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_sewage_type, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_size_frac = Slot(uri=MIXS['0000017'], name="wastewater_sludge_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_size_frac, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_sludge_retent_time = Slot(uri=MIXS['0000669'], name="wastewater_sludge_sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_sludge_retent_time, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_sodium = Slot(uri=MIXS['0000428'], name="wastewater_sludge_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_sodium, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="wastewater_sludge_soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_soluble_inorg_mat, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_soluble_org_mat = Slot(uri=MIXS['0000673'], name="wastewater_sludge_soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_soluble_org_mat, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_specific_ecosystem = Slot(uri="str(uriorcurie)", name="wastewater_sludge_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_specific_ecosystem, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_suspend_solids = Slot(uri=MIXS['0000150'], name="wastewater_sludge_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_suspend_solids, domain=WastewaterSludge, range=Optional[Union[str, List[str]]])

slots.wastewater_sludge_temp = Slot(uri=MIXS['0000113'], name="wastewater_sludge_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_temp, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_tertiary_treatment = Slot(uri=MIXS['0000352'], name="wastewater_sludge_tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_tertiary_treatment, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_tot_nitro = Slot(uri=MIXS['0000102'], name="wastewater_sludge_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_tot_nitro, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_tot_phosphate = Slot(uri=MIXS['0000689'], name="wastewater_sludge_tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_tot_phosphate, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_sludge_wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_wastewater_type, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_horizon_meth = Slot(uri=MIXS['0000321'], name="wastewater_sludge_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_horizon_meth, domain=WastewaterSludge, range=Optional[str])

slots.wastewater_sludge_ph_meth = Slot(uri=MIXS['0001106'], name="wastewater_sludge_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_ph_meth, domain=WastewaterSludge, range=Optional[str])

slots.water_alkalinity = Slot(uri=MIXS['0000421'], name="water_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.water_alkalinity, domain=Water, range=Optional[str])

slots.water_alkalinity_method = Slot(uri=MIXS['0000298'], name="water_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.water_alkalinity_method, domain=Water, range=Optional[str])

slots.water_alkyl_diethers = Slot(uri=MIXS['0000490'], name="water_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.water_alkyl_diethers, domain=Water, range=Optional[str])

slots.water_alt = Slot(uri=MIXS['0000094'], name="water_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.water_alt, domain=Water, range=Optional[str])

slots.water_aminopept_act = Slot(uri=MIXS['0000172'], name="water_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.water_aminopept_act, domain=Water, range=Optional[str])

slots.water_ammonium = Slot(uri=MIXS['0000427'], name="water_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.water_ammonium, domain=Water, range=Optional[str])

slots.water_atmospheric_data = Slot(uri=MIXS['0001097'], name="water_atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=NMDC_SUB_SCHEMA.water_atmospheric_data, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_bac_prod = Slot(uri=MIXS['0000683'], name="water_bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=NMDC_SUB_SCHEMA.water_bac_prod, domain=Water, range=Optional[str])

slots.water_bac_resp = Slot(uri=MIXS['0000684'], name="water_bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=NMDC_SUB_SCHEMA.water_bac_resp, domain=Water, range=Optional[str])

slots.water_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="water_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.water_bacteria_carb_prod, domain=Water, range=Optional[str])

slots.water_biomass = Slot(uri=MIXS['0000174'], name="water_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.water_biomass, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_bishomohopanol = Slot(uri=MIXS['0000175'], name="water_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.water_bishomohopanol, domain=Water, range=Optional[str])

slots.water_bromide = Slot(uri=MIXS['0000176'], name="water_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.water_bromide, domain=Water, range=Optional[str])

slots.water_calcium = Slot(uri=MIXS['0000432'], name="water_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.water_calcium, domain=Water, range=Optional[str])

slots.water_chem_administration = Slot(uri=MIXS['0000751'], name="water_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.water_chem_administration, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_chloride = Slot(uri=MIXS['0000429'], name="water_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.water_chloride, domain=Water, range=Optional[str])

slots.water_chlorophyll = Slot(uri=MIXS['0000177'], name="water_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.water_chlorophyll, domain=Water, range=Optional[str])

slots.water_collection_date = Slot(uri=MIXS['0000011'], name="water_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.water_collection_date, domain=Water, range=Optional[str])

slots.water_conduc = Slot(uri=MIXS['0000692'], name="water_conduc", curie=MIXS.curie('0000692'),
                   model_uri=NMDC_SUB_SCHEMA.water_conduc, domain=Water, range=Optional[str])

slots.water_density = Slot(uri=MIXS['0000435'], name="water_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.water_density, domain=Water, range=Optional[str])

slots.water_depth = Slot(uri=MIXS['0000018'], name="water_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.water_depth, domain=Water, range=Optional[str])

slots.water_diether_lipids = Slot(uri=MIXS['0000178'], name="water_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.water_diether_lipids, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="water_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_carb_dioxide, domain=Water, range=Optional[str])

slots.water_diss_hydrogen = Slot(uri=MIXS['0000179'], name="water_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_hydrogen, domain=Water, range=Optional[str])

slots.water_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="water_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_inorg_carb, domain=Water, range=Optional[str])

slots.water_diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="water_diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_inorg_nitro, domain=Water, range=Optional[str])

slots.water_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="water_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_inorg_phosp, domain=Water, range=Optional[str])

slots.water_diss_org_carb = Slot(uri=MIXS['0000433'], name="water_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_org_carb, domain=Water, range=Optional[str])

slots.water_diss_org_nitro = Slot(uri=MIXS['0000162'], name="water_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_org_nitro, domain=Water, range=Optional[str])

slots.water_diss_oxygen = Slot(uri=MIXS['0000119'], name="water_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.water_diss_oxygen, domain=Water, range=Optional[str])

slots.water_down_par = Slot(uri=MIXS['0000703'], name="water_down_par", curie=MIXS.curie('0000703'),
                   model_uri=NMDC_SUB_SCHEMA.water_down_par, domain=Water, range=Optional[str])

slots.water_ecosystem = Slot(uri="str(uriorcurie)", name="water_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.water_ecosystem, domain=Water, range=Optional[str])

slots.water_ecosystem_category = Slot(uri="str(uriorcurie)", name="water_ecosystem_category", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.water_ecosystem_category, domain=Water, range=Optional[str])

slots.water_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="water_ecosystem_subtype", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.water_ecosystem_subtype, domain=Water, range=Optional[str])

slots.water_ecosystem_type = Slot(uri="str(uriorcurie)", name="water_ecosystem_type", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.water_ecosystem_type, domain=Water, range=Optional[str])

slots.water_elev = Slot(uri=MIXS['0000093'], name="water_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.water_elev, domain=Water, range=Optional[float])

slots.water_env_broad_scale = Slot(uri=MIXS['0000012'], name="water_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.water_env_broad_scale, domain=Water, range=Optional[str])

slots.water_env_local_scale = Slot(uri=MIXS['0000013'], name="water_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.water_env_local_scale, domain=Water, range=Optional[str])

slots.water_env_medium = Slot(uri=MIXS['0000014'], name="water_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.water_env_medium, domain=Water, range=Optional[str])

slots.water_experimental_factor = Slot(uri=MIXS['0000008'], name="water_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.water_experimental_factor, domain=Water, range=Optional[str])

slots.water_fluor = Slot(uri=MIXS['0000704'], name="water_fluor", curie=MIXS.curie('0000704'),
                   model_uri=NMDC_SUB_SCHEMA.water_fluor, domain=Water, range=Optional[str])

slots.water_geo_loc_name = Slot(uri=MIXS['0000010'], name="water_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.water_geo_loc_name, domain=Water, range=Optional[str])

slots.water_glucosidase_act = Slot(uri=MIXS['0000137'], name="water_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.water_glucosidase_act, domain=Water, range=Optional[str])

slots.water_lat_lon = Slot(uri=MIXS['0000009'], name="water_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.water_lat_lon, domain=Water, range=Optional[str])

slots.water_light_intensity = Slot(uri=MIXS['0000706'], name="water_light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=NMDC_SUB_SCHEMA.water_light_intensity, domain=Water, range=Optional[str])

slots.water_mean_frict_vel = Slot(uri=MIXS['0000498'], name="water_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.water_mean_frict_vel, domain=Water, range=Optional[str])

slots.water_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="water_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.water_mean_peak_frict_vel, domain=Water, range=Optional[str])

slots.water_misc_param = Slot(uri=MIXS['0000752'], name="water_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.water_misc_param, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_n_alkanes = Slot(uri=MIXS['0000503'], name="water_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.water_n_alkanes, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_nitrate = Slot(uri=MIXS['0000425'], name="water_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.water_nitrate, domain=Water, range=Optional[str])

slots.water_nitrite = Slot(uri=MIXS['0000426'], name="water_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.water_nitrite, domain=Water, range=Optional[str])

slots.water_nitro = Slot(uri=MIXS['0000504'], name="water_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.water_nitro, domain=Water, range=Optional[str])

slots.water_org_carb = Slot(uri=MIXS['0000508'], name="water_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.water_org_carb, domain=Water, range=Optional[str])

slots.water_org_matter = Slot(uri=MIXS['0000204'], name="water_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.water_org_matter, domain=Water, range=Optional[str])

slots.water_org_nitro = Slot(uri=MIXS['0000205'], name="water_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.water_org_nitro, domain=Water, range=Optional[str])

slots.water_organism_count = Slot(uri=MIXS['0000103'], name="water_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.water_organism_count, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="water_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.water_oxy_stat_samp, domain=Water, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.water_part_org_carb = Slot(uri=MIXS['0000515'], name="water_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.water_part_org_carb, domain=Water, range=Optional[str])

slots.water_part_org_nitro = Slot(uri=MIXS['0000719'], name="water_part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=NMDC_SUB_SCHEMA.water_part_org_nitro, domain=Water, range=Optional[str])

slots.water_perturbation = Slot(uri=MIXS['0000754'], name="water_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.water_perturbation, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="water_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.water_petroleum_hydrocarb, domain=Water, range=Optional[str])

slots.water_ph = Slot(uri=MIXS['0001001'], name="water_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.water_ph, domain=Water, range=Optional[str])

slots.water_phaeopigments = Slot(uri=MIXS['0000180'], name="water_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.water_phaeopigments, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_phosphate = Slot(uri=MIXS['0000505'], name="water_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.water_phosphate, domain=Water, range=Optional[str])

slots.water_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="water_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.water_phosplipid_fatt_acid, domain=Water, range=Optional[Union[str, List[str]]])

slots.water_photon_flux = Slot(uri=MIXS['0000725'], name="water_photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=NMDC_SUB_SCHEMA.water_photon_flux, domain=Water, range=Optional[str])

slots.water_potassium = Slot(uri=MIXS['0000430'], name="water_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.water_potassium, domain=Water, range=Optional[str])

slots.water_pressure = Slot(uri=MIXS['0000412'], name="water_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.water_pressure, domain=Water, range=Optional[str])

slots.water_primary_prod = Slot(uri=MIXS['0000728'], name="water_primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=NMDC_SUB_SCHEMA.water_primary_prod, domain=Water, range=Optional[str])

slots.water_redox_potential = Slot(uri=MIXS['0000182'], name="water_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.water_redox_potential, domain=Water, range=Optional[str])

slots.water_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="water_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.water_rel_to_oxygen, domain=Water, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.water_salinity = Slot(uri=MIXS['0000183'], name="water_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.water_salinity, domain=Water, range=Optional[str])

slots.water_samp_collec_device = Slot(uri=MIXS['0000002'], name="water_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_collec_device, domain=Water, range=Optional[str])

slots.water_samp_collec_method = Slot(uri=MIXS['0001225'], name="water_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_collec_method, domain=Water, range=Optional[str])

slots.water_samp_mat_process = Slot(uri=MIXS['0000016'], name="water_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_mat_process, domain=Water, range=Optional[str])

slots.water_samp_size = Slot(uri=MIXS['0000001'], name="water_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_size, domain=Water, range=Optional[str])

slots.water_samp_store_dur = Slot(uri=MIXS['0000116'], name="water_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_store_dur, domain=Water, range=Optional[str])

slots.water_samp_store_loc = Slot(uri=MIXS['0000755'], name="water_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_store_loc, domain=Water, range=Optional[str])

slots.water_samp_store_temp = Slot(uri=MIXS['0000110'], name="water_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.water_samp_store_temp, domain=Water, range=Optional[str])

slots.water_silicate = Slot(uri=MIXS['0000184'], name="water_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.water_silicate, domain=Water, range=Optional[str])

slots.water_size_frac = Slot(uri=MIXS['0000017'], name="water_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.water_size_frac, domain=Water, range=Optional[str])

slots.water_size_frac_low = Slot(uri=MIXS['0000735'], name="water_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.water_size_frac_low, domain=Water, range=Optional[str])

slots.water_size_frac_up = Slot(uri=MIXS['0000736'], name="water_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.water_size_frac_up, domain=Water, range=Optional[str])

slots.water_sodium = Slot(uri=MIXS['0000428'], name="water_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.water_sodium, domain=Water, range=Optional[str])

slots.water_soluble_react_phosp = Slot(uri=MIXS['0000738'], name="water_soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=NMDC_SUB_SCHEMA.water_soluble_react_phosp, domain=Water, range=Optional[str])

slots.water_specific_ecosystem = Slot(uri="str(uriorcurie)", name="water_specific_ecosystem", curie=None,
                   model_uri=NMDC_SUB_SCHEMA.water_specific_ecosystem, domain=Water, range=Optional[str])

slots.water_sulfate = Slot(uri=MIXS['0000423'], name="water_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.water_sulfate, domain=Water, range=Optional[str])

slots.water_sulfide = Slot(uri=MIXS['0000424'], name="water_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.water_sulfide, domain=Water, range=Optional[str])

slots.water_suspend_part_matter = Slot(uri=MIXS['0000741'], name="water_suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=NMDC_SUB_SCHEMA.water_suspend_part_matter, domain=Water, range=Optional[str])

slots.water_temp = Slot(uri=MIXS['0000113'], name="water_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.water_temp, domain=Water, range=Optional[str])

slots.water_tidal_stage = Slot(uri=MIXS['0000750'], name="water_tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC_SUB_SCHEMA.water_tidal_stage, domain=Water, range=Optional[Union[str, "TidalStageEnum"]])

slots.water_tot_depth_water_col = Slot(uri=MIXS['0000634'], name="water_tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC_SUB_SCHEMA.water_tot_depth_water_col, domain=Water, range=Optional[str])

slots.water_tot_diss_nitro = Slot(uri=MIXS['0000744'], name="water_tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=NMDC_SUB_SCHEMA.water_tot_diss_nitro, domain=Water, range=Optional[str])

slots.water_tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="water_tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=NMDC_SUB_SCHEMA.water_tot_inorg_nitro, domain=Water, range=Optional[str])

slots.water_tot_nitro = Slot(uri=MIXS['0000102'], name="water_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.water_tot_nitro, domain=Water, range=Optional[str])

slots.water_tot_part_carb = Slot(uri=MIXS['0000747'], name="water_tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=NMDC_SUB_SCHEMA.water_tot_part_carb, domain=Water, range=Optional[str])

slots.water_turbidity = Slot(uri=MIXS['0000191'], name="water_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.water_turbidity, domain=Water, range=Optional[str])

slots.water_water_current = Slot(uri=MIXS['0000203'], name="water_water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC_SUB_SCHEMA.water_water_current, domain=Water, range=Optional[str])

slots.water_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="water_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.water_carb_nitro_ratio, domain=Water, range=Optional[float])

slots.water_horizon_meth = Slot(uri=MIXS['0000321'], name="water_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.water_horizon_meth, domain=Water, range=Optional[str])

slots.water_ph_meth = Slot(uri=MIXS['0001106'], name="water_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.water_ph_meth, domain=Water, range=Optional[str])

slots.GeolocationValue_has_raw_value = Slot(uri=NMDC_SUB_SCHEMA.has_raw_value, name="GeolocationValue_has_raw_value", curie=NMDC_SUB_SCHEMA.curie('has_raw_value'),
                   model_uri=NMDC_SUB_SCHEMA.GeolocationValue_has_raw_value, domain=GeolocationValue, range=Optional[str])

slots.Activity_id = Slot(uri=NMDC_SUB_SCHEMA.id, name="Activity_id", curie=NMDC_SUB_SCHEMA.curie('id'),
                   model_uri=NMDC_SUB_SCHEMA.Activity_id, domain=Activity, range=Union[str, ActivityId])

slots.AttributeValue_type = Slot(uri=NMDC_SUB_SCHEMA.type, name="AttributeValue_type", curie=NMDC_SUB_SCHEMA.curie('type'),
                   model_uri=NMDC_SUB_SCHEMA.AttributeValue_type, domain=AttributeValue, range=Optional[str])