# Auto generated from submission_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-07T14:43:21
# Schema: nmdc_submission_schema
#
# id: https://example.com/nmdc_submission_schema
# description: Schema for creating Data Harmonizer interfaces for biosamples based on MIxS and other standards
# license:

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
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

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
ISA = CurieNamespace('ISA', 'https://unknown.to.linter.org/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'http://identifiers.org/kegg.orthology/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'http://identifiers.org/kegg.pathway/')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/')
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
GTPO = CurieNamespace('gtpo', 'https://unknown.to.linter.org/')
JGI = CurieNamespace('jgi', 'https://unknown.to.linter.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
NMDC_SUB_SCHEMA = CurieNamespace('nmdc_sub_schema', 'https://example.com/nmdc_sub_schema/')
NMDC_YAML = CurieNamespace('nmdc_yaml', 'https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/')
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
    """ a float representation of a degree of rotation """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = NMDC_SUB_SCHEMA.DecimalDegree


class LanguageCode(str):
    """ a string representation of a language """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = NMDC_SUB_SCHEMA.LanguageCode


class Unit(str):
    """ a string representation of a unit """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = NMDC_SUB_SCHEMA.Unit


class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = NMDC_SUB_SCHEMA.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = NMDC_SUB_SCHEMA.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = NMDC_SUB_SCHEMA.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = NMDC_SUB_SCHEMA.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = NMDC_SUB_SCHEMA.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = NMDC_SUB_SCHEMA.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = NMDC_SUB_SCHEMA.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = NMDC_SUB_SCHEMA.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = NMDC_SUB_SCHEMA.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = NMDC_SUB_SCHEMA.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = NMDC_SUB_SCHEMA.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = NMDC_SUB_SCHEMA.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = NMDC_SUB_SCHEMA.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = NMDC_SUB_SCHEMA.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = NMDC_SUB_SCHEMA.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = NMDC_SUB_SCHEMA.Nodeidentifier


# Class references
class DhMultiviewCommonColumnsSourceMatId(extended_str):
    pass


class NamedThingId(extended_str):
    pass


class OntologyClassId(NamedThingId):
    pass


class ActivityId(extended_str):
    pass


class DhInterface(YAMLRoot):
    """
    One DataHarmonizer interface, for the specified combination of a checklist, enviornmental_package, and various
    standards, user facilities or analysis types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:DhInterface"
    class_name: ClassVar[str] = "DhInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhInterface


@dataclass
class AirInterface(DhInterface):
    """
    air dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.AirInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:AirInterface"
    class_name: ClassVar[str] = "AirInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.AirInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
    air_PM_concen: Optional[Union[str, List[str]]] = empty_list()
    alt: Optional[str] = None
    barometric_press: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    humidity: Optional[str] = None
    lat_lon: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class BiofilmInterface(DhInterface):
    """
    biofilm dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BiofilmInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:BiofilmInterface"
    class_name: ClassVar[str] = "BiofilmInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BiofilmInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
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
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    lat_lon: Optional[str] = None
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
    ph_meth: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class BuiltEnvInterface(DhInterface):
    """
    built_env dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BuiltEnvInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:BuiltEnvInterface"
    class_name: ClassVar[str] = "BuiltEnvInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.BuiltEnvInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
    abs_air_humidity: Optional[str] = None
    address: Optional[str] = None
    adj_room: Optional[str] = None
    aero_struc: Optional[str] = None
    air_temp: Optional[str] = None
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
    collection_date: Optional[str] = None
    cool_syst_id: Optional[str] = None
    date_last_rain: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    indoor_space: Optional[Union[str, "IndoorSpaceEnum"]] = None
    indoor_surf: Optional[Union[str, "IndoorSurfEnum"]] = None
    inside_lux: Optional[str] = None
    int_wall_cond: Optional[Union[str, "IntWallCondEnum"]] = None
    last_clean: Optional[str] = None
    lat_lon: Optional[str] = None
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
    temp: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, str):
            self.date_last_rain = str(self.date_last_rain)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.indoor_space is not None and not isinstance(self.indoor_space, IndoorSpaceEnum):
            self.indoor_space = IndoorSpaceEnum(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, IndoorSurfEnum):
            self.indoor_surf = IndoorSurfEnum(self.indoor_surf)

        if self.inside_lux is not None and not isinstance(self.inside_lux, str):
            self.inside_lux = str(self.inside_lux)

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, IntWallCondEnum):
            self.int_wall_cond = IntWallCondEnum(self.int_wall_cond)

        if self.last_clean is not None and not isinstance(self.last_clean, str):
            self.last_clean = str(self.last_clean)

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

        if self.cool_syst_id is not None and not isinstance(self.cool_syst_id, str):
            self.cool_syst_id = str(self.cool_syst_id)

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, str):
            self.date_last_rain = str(self.date_last_rain)

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

        if self.elevator is not None and not isinstance(self.elevator, str):
            self.elevator = str(self.elevator)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.indoor_space is not None and not isinstance(self.indoor_space, IndoorSpaceEnum):
            self.indoor_space = IndoorSpaceEnum(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, IndoorSurfEnum):
            self.indoor_surf = IndoorSurfEnum(self.indoor_surf)

        if self.inside_lux is not None and not isinstance(self.inside_lux, str):
            self.inside_lux = str(self.inside_lux)

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, IntWallCondEnum):
            self.int_wall_cond = IntWallCondEnum(self.int_wall_cond)

        if self.last_clean is not None and not isinstance(self.last_clean, str):
            self.last_clean = str(self.last_clean)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class DhMutliviewCommonColumnsMixin(YAMLRoot):
    """
    Mixin with DhMutliviewCommon Columns
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMutliviewCommonColumnsMixin
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:DhMutliviewCommonColumnsMixin"
    class_name: ClassVar[str] = "DhMutliviewCommonColumnsMixin"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMutliviewCommonColumnsMixin

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        super().__post_init__(**kwargs)


@dataclass
class EmslInterface(DhInterface):
    """
    emsl dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.EmslInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:EmslInterface"
    class_name: ClassVar[str] = "EmslInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.EmslInterface

    emsl_store_temp: str = None
    project_id: str = None
    sample_shipped: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    replicate_number: Optional[str] = None
    technical_reps: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.emsl_store_temp):
            self.MissingRequiredField("emsl_store_temp")
        if not isinstance(self.emsl_store_temp, str):
            self.emsl_store_temp = str(self.emsl_store_temp)

        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self._is_empty(self.sample_shipped):
            self.MissingRequiredField("sample_shipped")
        if not isinstance(self.sample_shipped, str):
            self.sample_shipped = str(self.sample_shipped)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.replicate_number is not None and not isinstance(self.replicate_number, str):
            self.replicate_number = str(self.replicate_number)

        if self.technical_reps is not None and not isinstance(self.technical_reps, str):
            self.technical_reps = str(self.technical_reps)

        super().__post_init__(**kwargs)


@dataclass
class HcrCoresInterface(DhInterface):
    """
    hcr_cores dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrCoresInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HcrCoresInterface"
    class_name: ClassVar[str] = "HcrCoresInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrCoresInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
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
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    lat_lon: Optional[str] = None
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
    ph_meth: Optional[str] = None
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

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

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.permeability is not None and not isinstance(self.permeability, str):
            self.permeability = str(self.permeability)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        super().__post_init__(**kwargs)


@dataclass
class HcrFluidsSwabsInterface(DhInterface):
    """
    hcr_fluids_swabs dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HcrFluidsSwabsInterface"
    class_name: ClassVar[str] = "HcrFluidsSwabsInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
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
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chem_treat_method: Optional[str] = None
    chem_treatment: Optional[str] = None
    chloride: Optional[str] = None
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    iw_bt_date_well: Optional[str] = None
    iwf: Optional[str] = None
    lat_lon: Optional[str] = None
    lithology: Optional[Union[str, "LithologyEnum"]] = None
    magnesium: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    org_count_qpcr_info: Optional[str] = None
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    potassium: Optional[str] = None
    pour_point: Optional[str] = None
    pressure: Optional[str] = None
    prod_rate: Optional[str] = None
    prod_start_date: Optional[str] = None
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

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

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, str):
            self.iw_bt_date_well = str(self.iw_bt_date_well)

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

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.prod_rate is not None and not isinstance(self.prod_rate, str):
            self.prod_rate = str(self.prod_rate)

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, str):
            self.prod_start_date = str(self.prod_start_date)

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

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chem_treat_method is not None and not isinstance(self.chem_treat_method, str):
            self.chem_treat_method = str(self.chem_treat_method)

        if self.chem_treatment is not None and not isinstance(self.chem_treatment, str):
            self.chem_treatment = str(self.chem_treatment)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, str):
            self.iw_bt_date_well = str(self.iw_bt_date_well)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.prod_rate is not None and not isinstance(self.prod_rate, str):
            self.prod_rate = str(self.prod_rate)

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, str):
            self.prod_start_date = str(self.prod_start_date)

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

        super().__post_init__(**kwargs)


@dataclass
class HostAssociatedInterface(DhInterface):
    """
    host_associated dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HostAssociatedInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:HostAssociatedInterface"
    class_name: ClassVar[str] = "HostAssociatedInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.HostAssociatedInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
    alt: Optional[str] = None
    ances_data: Optional[str] = None
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    blood_press_diast: Optional[str] = None
    blood_press_syst: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
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
    lat_lon: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.gravidity is not None and not isinstance(self.gravidity, str):
            self.gravidity = str(self.gravidity)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class JgiMgInterface(DhInterface):
    """
    jgi_mg dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMgInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:JgiMgInterface"
    class_name: ClassVar[str] = "JgiMgInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMgInterface

    dna_collect_site: str = None
    dna_concentration: str = None
    dna_cont_type: Union[str, "DnaContTypeEnum"] = None
    dna_cont_well: str = None
    dna_container_id: str = None
    dna_dnase: Union[str, "DnaDnaseEnum"] = None
    dna_isolate_meth: str = None
    dna_project_contact: str = None
    dna_samp_id: str = None
    dna_sample_format: Union[str, "DnaSampleFormatEnum"] = None
    dna_sample_name: str = None
    dna_seq_project: str = None
    dna_seq_project_name: str = None
    dna_seq_project_pi: str = None
    dna_volume: str = None
    proposal_dna: str = None
    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    dna_absorb1: Optional[str] = None
    dna_absorb2: Optional[str] = None
    dna_organisms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dna_collect_site):
            self.MissingRequiredField("dna_collect_site")
        if not isinstance(self.dna_collect_site, str):
            self.dna_collect_site = str(self.dna_collect_site)

        if self._is_empty(self.dna_concentration):
            self.MissingRequiredField("dna_concentration")
        if not isinstance(self.dna_concentration, str):
            self.dna_concentration = str(self.dna_concentration)

        if self._is_empty(self.dna_cont_type):
            self.MissingRequiredField("dna_cont_type")
        if not isinstance(self.dna_cont_type, DnaContTypeEnum):
            self.dna_cont_type = DnaContTypeEnum(self.dna_cont_type)

        if self._is_empty(self.dna_cont_well):
            self.MissingRequiredField("dna_cont_well")
        if not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if self._is_empty(self.dna_container_id):
            self.MissingRequiredField("dna_container_id")
        if not isinstance(self.dna_container_id, str):
            self.dna_container_id = str(self.dna_container_id)

        if self._is_empty(self.dna_dnase):
            self.MissingRequiredField("dna_dnase")
        if not isinstance(self.dna_dnase, DnaDnaseEnum):
            self.dna_dnase = DnaDnaseEnum(self.dna_dnase)

        if self._is_empty(self.dna_isolate_meth):
            self.MissingRequiredField("dna_isolate_meth")
        if not isinstance(self.dna_isolate_meth, str):
            self.dna_isolate_meth = str(self.dna_isolate_meth)

        if self._is_empty(self.dna_project_contact):
            self.MissingRequiredField("dna_project_contact")
        if not isinstance(self.dna_project_contact, str):
            self.dna_project_contact = str(self.dna_project_contact)

        if self._is_empty(self.dna_samp_id):
            self.MissingRequiredField("dna_samp_id")
        if not isinstance(self.dna_samp_id, str):
            self.dna_samp_id = str(self.dna_samp_id)

        if self._is_empty(self.dna_sample_format):
            self.MissingRequiredField("dna_sample_format")
        if not isinstance(self.dna_sample_format, DnaSampleFormatEnum):
            self.dna_sample_format = DnaSampleFormatEnum(self.dna_sample_format)

        if self._is_empty(self.dna_sample_name):
            self.MissingRequiredField("dna_sample_name")
        if not isinstance(self.dna_sample_name, str):
            self.dna_sample_name = str(self.dna_sample_name)

        if self._is_empty(self.dna_seq_project):
            self.MissingRequiredField("dna_seq_project")
        if not isinstance(self.dna_seq_project, str):
            self.dna_seq_project = str(self.dna_seq_project)

        if self._is_empty(self.dna_seq_project_name):
            self.MissingRequiredField("dna_seq_project_name")
        if not isinstance(self.dna_seq_project_name, str):
            self.dna_seq_project_name = str(self.dna_seq_project_name)

        if self._is_empty(self.dna_seq_project_pi):
            self.MissingRequiredField("dna_seq_project_pi")
        if not isinstance(self.dna_seq_project_pi, str):
            self.dna_seq_project_pi = str(self.dna_seq_project_pi)

        if self._is_empty(self.dna_volume):
            self.MissingRequiredField("dna_volume")
        if not isinstance(self.dna_volume, str):
            self.dna_volume = str(self.dna_volume)

        if self._is_empty(self.proposal_dna):
            self.MissingRequiredField("proposal_dna")
        if not isinstance(self.proposal_dna, str):
            self.proposal_dna = str(self.proposal_dna)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.dna_absorb1 is not None and not isinstance(self.dna_absorb1, str):
            self.dna_absorb1 = str(self.dna_absorb1)

        if self.dna_absorb2 is not None and not isinstance(self.dna_absorb2, str):
            self.dna_absorb2 = str(self.dna_absorb2)

        if self.dna_organisms is not None and not isinstance(self.dna_organisms, str):
            self.dna_organisms = str(self.dna_organisms)

        super().__post_init__(**kwargs)


@dataclass
class JgiMtInterface(DhInterface):
    """
    jgi_mt dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMtInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:JgiMtInterface"
    class_name: ClassVar[str] = "JgiMtInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.JgiMtInterface

    dnase_rna: Union[str, "DnaseRnaEnum"] = None
    proposal_rna: str = None
    rna_collect_site: str = None
    rna_concentration: str = None
    rna_cont_type: Union[str, "RnaContTypeEnum"] = None
    rna_cont_well: str = None
    rna_container_id: str = None
    rna_isolate_meth: str = None
    rna_project_contact: str = None
    rna_samp_id: str = None
    rna_sample_format: Union[str, "RnaSampleFormatEnum"] = None
    rna_sample_name: str = None
    rna_seq_project: str = None
    rna_seq_project_name: str = None
    rna_seq_project_pi: str = None
    rna_volume: str = None
    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    rna_absorb1: Optional[str] = None
    rna_absorb2: Optional[str] = None
    rna_organisms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dnase_rna):
            self.MissingRequiredField("dnase_rna")
        if not isinstance(self.dnase_rna, DnaseRnaEnum):
            self.dnase_rna = DnaseRnaEnum(self.dnase_rna)

        if self._is_empty(self.proposal_rna):
            self.MissingRequiredField("proposal_rna")
        if not isinstance(self.proposal_rna, str):
            self.proposal_rna = str(self.proposal_rna)

        if self._is_empty(self.rna_collect_site):
            self.MissingRequiredField("rna_collect_site")
        if not isinstance(self.rna_collect_site, str):
            self.rna_collect_site = str(self.rna_collect_site)

        if self._is_empty(self.rna_concentration):
            self.MissingRequiredField("rna_concentration")
        if not isinstance(self.rna_concentration, str):
            self.rna_concentration = str(self.rna_concentration)

        if self._is_empty(self.rna_cont_type):
            self.MissingRequiredField("rna_cont_type")
        if not isinstance(self.rna_cont_type, RnaContTypeEnum):
            self.rna_cont_type = RnaContTypeEnum(self.rna_cont_type)

        if self._is_empty(self.rna_cont_well):
            self.MissingRequiredField("rna_cont_well")
        if not isinstance(self.rna_cont_well, str):
            self.rna_cont_well = str(self.rna_cont_well)

        if self._is_empty(self.rna_container_id):
            self.MissingRequiredField("rna_container_id")
        if not isinstance(self.rna_container_id, str):
            self.rna_container_id = str(self.rna_container_id)

        if self._is_empty(self.rna_isolate_meth):
            self.MissingRequiredField("rna_isolate_meth")
        if not isinstance(self.rna_isolate_meth, str):
            self.rna_isolate_meth = str(self.rna_isolate_meth)

        if self._is_empty(self.rna_project_contact):
            self.MissingRequiredField("rna_project_contact")
        if not isinstance(self.rna_project_contact, str):
            self.rna_project_contact = str(self.rna_project_contact)

        if self._is_empty(self.rna_samp_id):
            self.MissingRequiredField("rna_samp_id")
        if not isinstance(self.rna_samp_id, str):
            self.rna_samp_id = str(self.rna_samp_id)

        if self._is_empty(self.rna_sample_format):
            self.MissingRequiredField("rna_sample_format")
        if not isinstance(self.rna_sample_format, RnaSampleFormatEnum):
            self.rna_sample_format = RnaSampleFormatEnum(self.rna_sample_format)

        if self._is_empty(self.rna_sample_name):
            self.MissingRequiredField("rna_sample_name")
        if not isinstance(self.rna_sample_name, str):
            self.rna_sample_name = str(self.rna_sample_name)

        if self._is_empty(self.rna_seq_project):
            self.MissingRequiredField("rna_seq_project")
        if not isinstance(self.rna_seq_project, str):
            self.rna_seq_project = str(self.rna_seq_project)

        if self._is_empty(self.rna_seq_project_name):
            self.MissingRequiredField("rna_seq_project_name")
        if not isinstance(self.rna_seq_project_name, str):
            self.rna_seq_project_name = str(self.rna_seq_project_name)

        if self._is_empty(self.rna_seq_project_pi):
            self.MissingRequiredField("rna_seq_project_pi")
        if not isinstance(self.rna_seq_project_pi, str):
            self.rna_seq_project_pi = str(self.rna_seq_project_pi)

        if self._is_empty(self.rna_volume):
            self.MissingRequiredField("rna_volume")
        if not isinstance(self.rna_volume, str):
            self.rna_volume = str(self.rna_volume)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self.rna_absorb1 is not None and not isinstance(self.rna_absorb1, str):
            self.rna_absorb1 = str(self.rna_absorb1)

        if self.rna_absorb2 is not None and not isinstance(self.rna_absorb2, str):
            self.rna_absorb2 = str(self.rna_absorb2)

        if self.rna_organisms is not None and not isinstance(self.rna_organisms, str):
            self.rna_organisms = str(self.rna_organisms)

        super().__post_init__(**kwargs)


@dataclass
class MiscEnvsInterface(DhInterface):
    """
    misc_envs dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.MiscEnvsInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:MiscEnvsInterface"
    class_name: ClassVar[str] = "MiscEnvsInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.MiscEnvsInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    alkalinity: Optional[str] = None
    alt: Optional[str] = None
    ammonium: Optional[str] = None
    biomass: Optional[Union[str, List[str]]] = empty_list()
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    lat_lon: Optional[str] = None
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
    ph_meth: Optional[str] = None
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        super().__post_init__(**kwargs)


@dataclass
class PlantAssociatedInterface(DhInterface):
    """
    plant_associated dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.PlantAssociatedInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:PlantAssociatedInterface"
    class_name: ClassVar[str] = "PlantAssociatedInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.PlantAssociatedInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
    air_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    alt: Optional[str] = None
    ances_data: Optional[str] = None
    antibiotic_regm: Optional[Union[str, List[str]]] = empty_list()
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chem_mutagen: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
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
    lat_lon: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.growth_facil):
            self.MissingRequiredField("growth_facil")
        if not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

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

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if not isinstance(self.growth_hormone_regm, list):
            self.growth_hormone_regm = [self.growth_hormone_regm] if self.growth_hormone_regm is not None else []
        self.growth_hormone_regm = [v if isinstance(v, str) else str(v) for v in self.growth_hormone_regm]

        if not isinstance(self.herbicide_regm, list):
            self.herbicide_regm = [self.herbicide_regm] if self.herbicide_regm is not None else []
        self.herbicide_regm = [v if isinstance(v, str) else str(v) for v in self.herbicide_regm]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if not isinstance(self.season_environment, list):
            self.season_environment = [self.season_environment] if self.season_environment is not None else []
        self.season_environment = [v if isinstance(v, str) else str(v) for v in self.season_environment]

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class SampIdNewTermsMixin(YAMLRoot):
    """
    Mixin with SampIdNew Terms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampIdNewTermsMixin
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SampIdNewTermsMixin"
    class_name: ClassVar[str] = "SampIdNewTermsMixin"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SampIdNewTermsMixin

    env_package: str = None
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


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

    air_data: Optional[Union[Union[dict, AirInterface], List[Union[dict, AirInterface]]]] = empty_list()
    biofilm_data: Optional[Union[Union[dict, BiofilmInterface], List[Union[dict, BiofilmInterface]]]] = empty_list()
    built_env_data: Optional[Union[Union[dict, BuiltEnvInterface], List[Union[dict, BuiltEnvInterface]]]] = empty_list()
    host_associated_data: Optional[Union[Union[dict, HostAssociatedInterface], List[Union[dict, HostAssociatedInterface]]]] = empty_list()
    plant_associated_data: Optional[Union[Union[dict, PlantAssociatedInterface], List[Union[dict, PlantAssociatedInterface]]]] = empty_list()
    sediment_data: Optional[Union[Union[dict, "SedimentInterface"], List[Union[dict, "SedimentInterface"]]]] = empty_list()
    soil_data: Optional[Union[Union[dict, "SoilInterface"], List[Union[dict, "SoilInterface"]]]] = empty_list()
    wastewater_sludge_data: Optional[Union[Union[dict, "WastewaterSludgeInterface"], List[Union[dict, "WastewaterSludgeInterface"]]]] = empty_list()
    water_data: Optional[Union[Union[dict, "WaterInterface"], List[Union[dict, "WaterInterface"]]]] = empty_list()
    emsl_data: Optional[Union[Union[dict, EmslInterface], List[Union[dict, EmslInterface]]]] = empty_list()
    jgi_mg_data: Optional[Union[Union[dict, JgiMgInterface], List[Union[dict, JgiMgInterface]]]] = empty_list()
    jgi_mt_data: Optional[Union[Union[dict, JgiMtInterface], List[Union[dict, JgiMtInterface]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.air_data, list):
            self.air_data = [self.air_data] if self.air_data is not None else []
        self.air_data = [v if isinstance(v, AirInterface) else AirInterface(**as_dict(v)) for v in self.air_data]

        if not isinstance(self.biofilm_data, list):
            self.biofilm_data = [self.biofilm_data] if self.biofilm_data is not None else []
        self.biofilm_data = [v if isinstance(v, BiofilmInterface) else BiofilmInterface(**as_dict(v)) for v in self.biofilm_data]

        if not isinstance(self.built_env_data, list):
            self.built_env_data = [self.built_env_data] if self.built_env_data is not None else []
        self.built_env_data = [v if isinstance(v, BuiltEnvInterface) else BuiltEnvInterface(**as_dict(v)) for v in self.built_env_data]

        if not isinstance(self.host_associated_data, list):
            self.host_associated_data = [self.host_associated_data] if self.host_associated_data is not None else []
        self.host_associated_data = [v if isinstance(v, HostAssociatedInterface) else HostAssociatedInterface(**as_dict(v)) for v in self.host_associated_data]

        if not isinstance(self.plant_associated_data, list):
            self.plant_associated_data = [self.plant_associated_data] if self.plant_associated_data is not None else []
        self.plant_associated_data = [v if isinstance(v, PlantAssociatedInterface) else PlantAssociatedInterface(**as_dict(v)) for v in self.plant_associated_data]

        if not isinstance(self.sediment_data, list):
            self.sediment_data = [self.sediment_data] if self.sediment_data is not None else []
        self.sediment_data = [v if isinstance(v, SedimentInterface) else SedimentInterface(**as_dict(v)) for v in self.sediment_data]

        if not isinstance(self.soil_data, list):
            self.soil_data = [self.soil_data] if self.soil_data is not None else []
        self.soil_data = [v if isinstance(v, SoilInterface) else SoilInterface(**as_dict(v)) for v in self.soil_data]

        if not isinstance(self.wastewater_sludge_data, list):
            self.wastewater_sludge_data = [self.wastewater_sludge_data] if self.wastewater_sludge_data is not None else []
        self.wastewater_sludge_data = [v if isinstance(v, WastewaterSludgeInterface) else WastewaterSludgeInterface(**as_dict(v)) for v in self.wastewater_sludge_data]

        if not isinstance(self.water_data, list):
            self.water_data = [self.water_data] if self.water_data is not None else []
        self.water_data = [v if isinstance(v, WaterInterface) else WaterInterface(**as_dict(v)) for v in self.water_data]

        if not isinstance(self.emsl_data, list):
            self.emsl_data = [self.emsl_data] if self.emsl_data is not None else []
        self.emsl_data = [v if isinstance(v, EmslInterface) else EmslInterface(**as_dict(v)) for v in self.emsl_data]

        if not isinstance(self.jgi_mg_data, list):
            self.jgi_mg_data = [self.jgi_mg_data] if self.jgi_mg_data is not None else []
        self.jgi_mg_data = [v if isinstance(v, JgiMgInterface) else JgiMgInterface(**as_dict(v)) for v in self.jgi_mg_data]

        if not isinstance(self.jgi_mt_data, list):
            self.jgi_mt_data = [self.jgi_mt_data] if self.jgi_mt_data is not None else []
        self.jgi_mt_data = [v if isinstance(v, JgiMtInterface) else JgiMtInterface(**as_dict(v)) for v in self.jgi_mt_data]

        super().__post_init__(**kwargs)


@dataclass
class SedimentInterface(DhInterface):
    """
    sediment dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SedimentInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SedimentInterface"
    class_name: ClassVar[str] = "SedimentInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SedimentInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
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
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    lat_lon: Optional[str] = None
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
    ph_meth: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.sediment_type is not None and not isinstance(self.sediment_type, SedimentTypeEnum):
            self.sediment_type = SedimentTypeEnum(self.sediment_type)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class SoilInterface(DhInterface):
    """
    soil dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SoilInterface"
    class_name: ClassVar[str] = "SoilInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
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
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    collection_date: Optional[str] = None
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
    extreme_event: Optional[str] = None
    fao_class: Optional[Union[str, "FaoClassEnum"]] = None
    fire: Optional[str] = None
    flooding: Optional[str] = None
    gaseous_environment: Optional[Union[str, List[str]]] = empty_list()
    geo_loc_name: Optional[str] = None
    growth_facil: Optional[str] = None
    heavy_metals: Optional[Union[str, List[str]]] = empty_list()
    heavy_metals_meth: Optional[str] = None
    humidity_regm: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[str] = None
    lbc_thirty: Optional[str] = None
    lbceq: Optional[str] = None
    light_regm: Optional[str] = None
    link_class_info: Optional[str] = None
    link_climate_info: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
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
    zinc: Optional[str] = None
    sample_link: Optional[str] = None
    collection_date_inc: Optional[str] = None
    collection_time: Optional[str] = None
    collection_time_inc: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    filter_method: Optional[str] = None
    isotope_exposure: Optional[str] = None
    micro_biomass_c_meth: Optional[str] = None
    micro_biomass_n_meth: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other_treatment: Optional[str] = None
    start_date_inc: Optional[str] = None
    start_time_inc: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, EnvBroadScaleSoilEnum):
            self.env_broad_scale = EnvBroadScaleSoilEnum(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, EnvLocalScaleSoilEnum):
            self.env_local_scale = EnvLocalScaleSoilEnum(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, EnvMediumSoilEnum):
            self.env_medium = EnvMediumSoilEnum(self.env_medium)

        if self._is_empty(self.growth_facil):
            self.MissingRequiredField("growth_facil")
        if not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.store_cond):
            self.MissingRequiredField("store_cond")
        if not isinstance(self.store_cond, StoreCondEnum):
            self.store_cond = StoreCondEnum(self.store_cond)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

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

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

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

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

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

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if not isinstance(self.heavy_metals_meth, list):
            self.heavy_metals_meth = [self.heavy_metals_meth] if self.heavy_metals_meth is not None else []
        self.heavy_metals_meth = [v if isinstance(v, str) else str(v) for v in self.heavy_metals_meth]

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

        if self.zinc is not None and not isinstance(self.zinc, str):
            self.zinc = str(self.zinc)

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

        if self.micro_biomass_c_meth is not None and not isinstance(self.micro_biomass_c_meth, str):
            self.micro_biomass_c_meth = str(self.micro_biomass_c_meth)

        if self.micro_biomass_n_meth is not None and not isinstance(self.micro_biomass_n_meth, str):
            self.micro_biomass_n_meth = str(self.micro_biomass_n_meth)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

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
class SoilMixsInspiredMixin(YAMLRoot):
    """
    Mixin with SoilMixsInspired Terms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilMixsInspiredMixin
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:SoilMixsInspiredMixin"
    class_name: ClassVar[str] = "SoilMixsInspiredMixin"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.SoilMixsInspiredMixin

    collection_date_inc: Optional[str] = None
    collection_time: Optional[str] = None
    collection_time_inc: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    filter_method: Optional[str] = None
    isotope_exposure: Optional[str] = None
    micro_biomass_c_meth: Optional[str] = None
    micro_biomass_n_meth: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
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

        if self.micro_biomass_c_meth is not None and not isinstance(self.micro_biomass_c_meth, str):
            self.micro_biomass_c_meth = str(self.micro_biomass_c_meth)

        if self.micro_biomass_n_meth is not None and not isinstance(self.micro_biomass_n_meth, str):
            self.micro_biomass_n_meth = str(self.micro_biomass_n_meth)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

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
class WastewaterSludgeInterface(DhInterface):
    """
    wastewater_sludge dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WastewaterSludgeInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:WastewaterSludgeInterface"
    class_name: ClassVar[str] = "WastewaterSludgeInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WastewaterSludgeInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
    alkalinity: Optional[str] = None
    alt: Optional[str] = None
    biochem_oxygen_dem: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chem_oxygen_dem: Optional[str] = None
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    indust_eff_percent: Optional[str] = None
    inorg_particles: Optional[Union[str, List[str]]] = empty_list()
    lat_lon: Optional[str] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    nitrate: Optional[str] = None
    org_particles: Optional[Union[str, List[str]]] = empty_list()
    organism_count: Optional[Union[str, List[str]]] = empty_list()
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    perturbation: Optional[Union[str, List[str]]] = empty_list()
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, str) else str(v) for v in self.perturbation]

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, str):
            self.efficiency_percent = str(self.efficiency_percent)

        if not isinstance(self.emulsions, list):
            self.emulsions = [self.emulsions] if self.emulsions is not None else []
        self.emulsions = [v if isinstance(v, str) else str(v) for v in self.emulsions]

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if not isinstance(self.gaseous_substances, list):
            self.gaseous_substances = [self.gaseous_substances] if self.gaseous_substances is not None else []
        self.gaseous_substances = [v if isinstance(v, str) else str(v) for v in self.gaseous_substances]

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class WaterInterface(DhInterface):
    """
    water dh_interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WaterInterface
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:WaterInterface"
    class_name: ClassVar[str] = "WaterInterface"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.WaterInterface

    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: str = None
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
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    collection_date: Optional[str] = None
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
    horizon_meth: Optional[str] = None
    lat_lon: Optional[str] = None
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
    ph_meth: Optional[str] = None
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
    sample_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

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

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

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

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, float):
            self.carb_nitro_ratio = float(self.carb_nitro_ratio)

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

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

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

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

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

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

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        super().__post_init__(**kwargs)


@dataclass
class DhMultiviewCommonColumns(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMultiviewCommonColumns
    class_class_curie: ClassVar[str] = "nmdc_sub_schema:DhMultiviewCommonColumns"
    class_name: ClassVar[str] = "DhMultiviewCommonColumns"
    class_model_uri: ClassVar[URIRef] = NMDC_SUB_SCHEMA.DhMultiviewCommonColumns

    source_mat_id: Optional[str] = None
    samp_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_mat_id):
            self.MissingRequiredField("source_mat_id")
        if not isinstance(self.source_mat_id, DhMultiviewCommonColumnsSourceMatId):
            self.source_mat_id = DhMultiviewCommonColumnsSourceMatId(self.source_mat_id)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

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
    was_associated_with: Optional[Union[dict, Agent]] = None
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


# Enumerations
class AnalysisTypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    metabolomics = PermissibleValue(text="metabolomics",
                                               description="placeholder PV descr")
    metagenomics = PermissibleValue(text="metagenomics",
                                               description="placeholder PV descr")
    metaproteomics = PermissibleValue(text="metaproteomics",
                                                   description="placeholder PV descr")
    metatranscriptomics = PermissibleValue(text="metatranscriptomics",
                                                             description="placeholder PV descr")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
        description="placeholder enum descr",
    )

class BioticRelationshipEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    commensalism = PermissibleValue(text="commensalism",
                                               description="placeholder PV descr")
    mutualism = PermissibleValue(text="mutualism",
                                         description="placeholder PV descr")
    parasitism = PermissibleValue(text="parasitism",
                                           description="placeholder PV descr")

    _defn = EnumDefinition(
        name="BioticRelationshipEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "free living",
                PermissibleValue(text="free living",
                                 description="placeholder PV descr") )
        setattr(cls, "natural organic matter",
                PermissibleValue(text="natural organic matter",
                                 description="placeholder PV descr") )

class DnaContTypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    plate = PermissibleValue(text="plate",
                                 description="placeholder PV descr")
    symbiotic = PermissibleValue(text="symbiotic",
                                         description="placeholder PV descr")

    _defn = EnumDefinition(
        name="DnaContTypeEnum",
        description="placeholder enum descr",
    )

class DnaDnaseEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    no = PermissibleValue(text="no",
                           description="placeholder PV descr")
    tube = PermissibleValue(text="tube",
                               description="placeholder PV descr")

    _defn = EnumDefinition(
        name="DnaDnaseEnum",
        description="placeholder enum descr",
    )

class DnaSampleFormatEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    DNAStable = PermissibleValue(text="DNAStable",
                                         description="placeholder PV descr")
    Ethanol = PermissibleValue(text="Ethanol",
                                     description="placeholder PV descr")
    PBS = PermissibleValue(text="PBS",
                             description="placeholder PV descr")
    Pellet = PermissibleValue(text="Pellet",
                                   description="placeholder PV descr")
    RNAStable = PermissibleValue(text="RNAStable",
                                         description="placeholder PV descr")
    TE = PermissibleValue(text="TE",
                           description="placeholder PV descr")
    Water = PermissibleValue(text="Water",
                                 description="placeholder PV descr")
    yes = PermissibleValue(text="yes",
                             description="placeholder PV descr")

    _defn = EnumDefinition(
        name="DnaSampleFormatEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl",
                                 description="placeholder PV descr") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE",
                                 description="placeholder PV descr") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer",
                                 description="placeholder PV descr") )

class DnaseRnaEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    no = PermissibleValue(text="no",
                           description="placeholder PV descr")
    yes = PermissibleValue(text="yes",
                             description="placeholder PV descr")

    _defn = EnumDefinition(
        name="DnaseRnaEnum",
        description="placeholder enum descr",
    )

class EcosystemCategoryEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    Terrestrial = PermissibleValue(text="Terrestrial",
                                             description="placeholder PV descr")

    _defn = EnumDefinition(
        name="EcosystemCategoryEnum",
        description="placeholder enum descr",
    )

class EcosystemEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    Environmental = PermissibleValue(text="Environmental",
                                                 description="placeholder PV descr")

    _defn = EnumDefinition(
        name="EcosystemEnum",
        description="placeholder enum descr",
    )

class EcosystemSubtypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    Biocrust = PermissibleValue(text="Biocrust",
                                       description="placeholder PV descr")
    Biofilm = PermissibleValue(text="Biofilm",
                                     description="placeholder PV descr")
    Clay = PermissibleValue(text="Clay",
                               description="placeholder PV descr")
    Floodplain = PermissibleValue(text="Floodplain",
                                           description="placeholder PV descr")
    Fossil = PermissibleValue(text="Fossil",
                                   description="placeholder PV descr")
    Glacier = PermissibleValue(text="Glacier",
                                     description="placeholder PV descr")
    Loam = PermissibleValue(text="Loam",
                               description="placeholder PV descr")
    Pasture = PermissibleValue(text="Pasture",
                                     description="placeholder PV descr")
    Peat = PermissibleValue(text="Peat",
                               description="placeholder PV descr")
    Ranch = PermissibleValue(text="Ranch",
                                 description="placeholder PV descr")
    Sand = PermissibleValue(text="Sand",
                               description="placeholder PV descr")
    Silt = PermissibleValue(text="Silt",
                               description="placeholder PV descr")
    Unclassified = PermissibleValue(text="Unclassified",
                                               description="placeholder PV descr")
    Watershed = PermissibleValue(text="Watershed",
                                         description="placeholder PV descr")
    Wetlands = PermissibleValue(text="Wetlands",
                                       description="placeholder PV descr")

    _defn = EnumDefinition(
        name="EcosystemSubtypeEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bulk soil",
                PermissibleValue(text="Bulk soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Mineral horizon",
                PermissibleValue(text="Mineral horizon",
                                 description="placeholder PV descr") )
        setattr(cls, "Nature reserve",
                PermissibleValue(text="Nature reserve",
                                 description="placeholder PV descr") )
        setattr(cls, "Organic layer",
                PermissibleValue(text="Organic layer",
                                 description="placeholder PV descr") )
        setattr(cls, "Paddy field/soil",
                PermissibleValue(text="Paddy field/soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Soil crust",
                PermissibleValue(text="Soil crust",
                                 description="placeholder PV descr") )

class EcosystemTypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    Soil = PermissibleValue(text="Soil",
                               description="placeholder PV descr")

    _defn = EnumDefinition(
        name="EcosystemTypeEnum",
        description="placeholder enum descr",
    )

class EnvBroadScaleSoilEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    _defn = EnumDefinition(
        name="EnvBroadScaleSoilEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "______mediterranean savanna biome [ENVO:01000229]",
                PermissibleValue(text="______mediterranean savanna biome [ENVO:01000229]",
                                 description="placeholder PV descr") )
        setattr(cls, "____flooded savanna biome [ENVO:01000190]",
                PermissibleValue(text="____flooded savanna biome [ENVO:01000190]",
                                 description="placeholder PV descr") )
        setattr(cls, "____mediterranean savanna biome [ENVO:01000229]",
                PermissibleValue(text="____mediterranean savanna biome [ENVO:01000229]",
                                 description="placeholder PV descr") )
        setattr(cls, "____mediterranean shrubland biome [ENVO:01000217]",
                PermissibleValue(text="____mediterranean shrubland biome [ENVO:01000217]",
                                 description="placeholder PV descr") )
        setattr(cls, "____mediterranean woodland biome [ENVO:01000208]",
                PermissibleValue(text="____mediterranean woodland biome [ENVO:01000208]",
                                 description="placeholder PV descr") )
        setattr(cls, "____montane savanna biome [ENVO:01000223]",
                PermissibleValue(text="____montane savanna biome [ENVO:01000223]",
                                 description="placeholder PV descr") )
        setattr(cls, "____subtropical savanna biome [ENVO:01000187]",
                PermissibleValue(text="____subtropical savanna biome [ENVO:01000187]",
                                 description="placeholder PV descr") )
        setattr(cls, "____temperate savanna biome [ENVO:01000189]",
                PermissibleValue(text="____temperate savanna biome [ENVO:01000189]",
                                 description="placeholder PV descr") )
        setattr(cls, "____tropical savanna biome [ENVO:01000188]",
                PermissibleValue(text="____tropical savanna biome [ENVO:01000188]",
                                 description="placeholder PV descr") )
        setattr(cls, "__alpine tundra biome [ENVO:01001505]",
                PermissibleValue(text="__alpine tundra biome [ENVO:01001505]",
                                 description="placeholder PV descr") )
        setattr(cls, "__mediterranean biome [ENVO:01001833]",
                PermissibleValue(text="__mediterranean biome [ENVO:01001833]",
                                 description="placeholder PV descr") )
        setattr(cls, "__montane savanna biome [ENVO:01000223]",
                PermissibleValue(text="__montane savanna biome [ENVO:01000223]",
                                 description="placeholder PV descr") )
        setattr(cls, "__montane shrubland biome [ENVO:01000216]",
                PermissibleValue(text="__montane shrubland biome [ENVO:01000216]",
                                 description="placeholder PV descr") )
        setattr(cls, "__rangeland biome [ENVO:01000247]",
                PermissibleValue(text="__rangeland biome [ENVO:01000247]",
                                 description="placeholder PV descr") )
        setattr(cls, "__savanna biome [ENVO:01000178]",
                PermissibleValue(text="__savanna biome [ENVO:01000178]",
                                 description="placeholder PV descr") )
        setattr(cls, "__subtropical savanna biome [ENVO:01000187]",
                PermissibleValue(text="__subtropical savanna biome [ENVO:01000187]",
                                 description="placeholder PV descr") )
        setattr(cls, "__subtropical shrubland biome [ENVO:01000213]",
                PermissibleValue(text="__subtropical shrubland biome [ENVO:01000213]",
                                 description="placeholder PV descr") )
        setattr(cls, "__subtropical woodland biome [ENVO:01000222]",
                PermissibleValue(text="__subtropical woodland biome [ENVO:01000222]",
                                 description="placeholder PV descr") )
        setattr(cls, "__temperate savanna biome [ENVO:01000189]",
                PermissibleValue(text="__temperate savanna biome [ENVO:01000189]",
                                 description="placeholder PV descr") )
        setattr(cls, "__temperate shrubland biome [ENVO:01000215]",
                PermissibleValue(text="__temperate shrubland biome [ENVO:01000215]",
                                 description="placeholder PV descr") )
        setattr(cls, "__temperate woodland biome [ENVO:01000221]",
                PermissibleValue(text="__temperate woodland biome [ENVO:01000221]",
                                 description="placeholder PV descr") )
        setattr(cls, "__tropical savanna biome [ENVO:01000188]",
                PermissibleValue(text="__tropical savanna biome [ENVO:01000188]",
                                 description="placeholder PV descr") )
        setattr(cls, "__tropical shrubland biome [ENVO:01000214]",
                PermissibleValue(text="__tropical shrubland biome [ENVO:01000214]",
                                 description="placeholder PV descr") )
        setattr(cls, "__tropical woodland biome [ENVO:01000220]",
                PermissibleValue(text="__tropical woodland biome [ENVO:01000220]",
                                 description="placeholder PV descr") )
        setattr(cls, "__village biome [ENVO:01000246]",
                PermissibleValue(text="__village biome [ENVO:01000246]",
                                 description="placeholder PV descr") )
        setattr(cls, "alpine biome [ENVO:01001835]",
                PermissibleValue(text="alpine biome [ENVO:01001835]",
                                 description="placeholder PV descr") )
        setattr(cls, "anthropogenic terrestrial biome [ENVO:01000219]",
                PermissibleValue(text="anthropogenic terrestrial biome [ENVO:01000219]",
                                 description="placeholder PV descr") )
        setattr(cls, "arid biome [ENVO:01001838]",
                PermissibleValue(text="arid biome [ENVO:01001838]",
                                 description="placeholder PV descr") )
        setattr(cls, "mangrove biome [ENVO:01000181]",
                PermissibleValue(text="mangrove biome [ENVO:01000181]",
                                 description="placeholder PV descr") )
        setattr(cls, "montane biome [ENVO:01001836]",
                PermissibleValue(text="montane biome [ENVO:01001836]",
                                 description="placeholder PV descr") )
        setattr(cls, "polar biome [ENVO:01000339]",
                PermissibleValue(text="polar biome [ENVO:01000339]",
                                 description="placeholder PV descr") )
        setattr(cls, "shrubland biome [ENVO:01000176]",
                PermissibleValue(text="shrubland biome [ENVO:01000176]",
                                 description="placeholder PV descr") )
        setattr(cls, "subalpine biome [ENVO:01001837]",
                PermissibleValue(text="subalpine biome [ENVO:01001837]",
                                 description="placeholder PV descr") )
        setattr(cls, "subpolar biome [ENVO:01001834]",
                PermissibleValue(text="subpolar biome [ENVO:01001834]",
                                 description="placeholder PV descr") )
        setattr(cls, "subtropical biome [ENVO:01001832]",
                PermissibleValue(text="subtropical biome [ENVO:01001832]",
                                 description="placeholder PV descr") )
        setattr(cls, "temperate biome [ENVO:01001831]",
                PermissibleValue(text="temperate biome [ENVO:01001831]",
                                 description="placeholder PV descr") )
        setattr(cls, "tropical biome [ENVO:01001830]",
                PermissibleValue(text="tropical biome [ENVO:01001830]",
                                 description="placeholder PV descr") )
        setattr(cls, "tundra biome [ENVO:01000180]",
                PermissibleValue(text="tundra biome [ENVO:01000180]",
                                 description="placeholder PV descr") )
        setattr(cls, "urban biome [ENVO:01000249]",
                PermissibleValue(text="urban biome [ENVO:01000249]",
                                 description="placeholder PV descr") )
        setattr(cls, "woodland biome [ENVO:01000175]",
                PermissibleValue(text="woodland biome [ENVO:01000175]",
                                 description="placeholder PV descr") )

class EnvLocalScaleSoilEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    _defn = EnumDefinition(
        name="EnvLocalScaleSoilEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "__canyon [ENVO:00000169]",
                PermissibleValue(text="__canyon [ENVO:00000169]",
                                 description="placeholder PV descr") )
        setattr(cls, "__cliff [ENVO:00000087]",
                PermissibleValue(text="__cliff [ENVO:00000087]",
                                 description="placeholder PV descr") )
        setattr(cls, "__dry valley [ENVO:00000128]",
                PermissibleValue(text="__dry valley [ENVO:00000128]",
                                 description="placeholder PV descr") )
        setattr(cls, "__dune [ENVO:00000170]",
                PermissibleValue(text="__dune [ENVO:00000170]",
                                 description="placeholder PV descr") )
        setattr(cls, "__glacial valley [ENVO:00000248]",
                PermissibleValue(text="__glacial valley [ENVO:00000248]",
                                 description="placeholder PV descr") )
        setattr(cls, "__hillside [ENVO:01000333]",
                PermissibleValue(text="__hillside [ENVO:01000333]",
                                 description="placeholder PV descr") )
        setattr(cls, "__tunnel [ENVO:00000068]",
                PermissibleValue(text="__tunnel [ENVO:00000068]",
                                 description="placeholder PV descr") )
        setattr(cls, "active geological fault [ENVO:01000669]",
                PermissibleValue(text="active geological fault [ENVO:01000669]",
                                 description="placeholder PV descr") )
        setattr(cls, "agricultural field [ENVO:00000114]",
                PermissibleValue(text="agricultural field [ENVO:00000114]",
                                 description="placeholder PV descr") )
        setattr(cls, "beach [ENVO:00000091]",
                PermissibleValue(text="beach [ENVO:00000091]",
                                 description="placeholder PV descr") )
        setattr(cls, "cave [ENVO:00000067]",
                PermissibleValue(text="cave [ENVO:00000067]",
                                 description="placeholder PV descr") )
        setattr(cls, "channel [ENVO:03000117]",
                PermissibleValue(text="channel [ENVO:03000117]",
                                 description="placeholder PV descr") )
        setattr(cls, "coast [ENVO:01000687]",
                PermissibleValue(text="coast [ENVO:01000687]",
                                 description="placeholder PV descr") )
        setattr(cls, "dry lake [ENVO:00000277]",
                PermissibleValue(text="dry lake [ENVO:00000277]",
                                 description="placeholder PV descr") )
        setattr(cls, "dry river [ENVO:01000995]",
                PermissibleValue(text="dry river [ENVO:01000995]",
                                 description="placeholder PV descr") )
        setattr(cls, "garden [ENVO:00000011]",
                PermissibleValue(text="garden [ENVO:00000011]",
                                 description="placeholder PV descr") )
        setattr(cls, "hill [ENVO:00000083]",
                PermissibleValue(text="hill [ENVO:00000083]",
                                 description="placeholder PV descr") )
        setattr(cls, "hummock [ENVO:00000516]",
                PermissibleValue(text="hummock [ENVO:00000516]",
                                 description="placeholder PV descr") )
        setattr(cls, "impact crater [ENVO:01001071]",
                PermissibleValue(text="impact crater [ENVO:01001071]",
                                 description="placeholder PV descr") )
        setattr(cls, "isthmus [ENVO:00000174]",
                PermissibleValue(text="isthmus [ENVO:00000174]",
                                 description="placeholder PV descr") )
        setattr(cls, "karst [ENVO:00000175]",
                PermissibleValue(text="karst [ENVO:00000175]",
                                 description="placeholder PV descr") )
        setattr(cls, "lake shore [ENVO:00000382]",
                PermissibleValue(text="lake shore [ENVO:00000382]",
                                 description="placeholder PV descr") )
        setattr(cls, "lava field [ENVO:01000437]",
                PermissibleValue(text="lava field [ENVO:01000437]",
                                 description="placeholder PV descr") )
        setattr(cls, "mesa [ENVO:00000179]",
                PermissibleValue(text="mesa [ENVO:00000179]",
                                 description="placeholder PV descr") )
        setattr(cls, "mountain [ENVO:00000081]",
                PermissibleValue(text="mountain [ENVO:00000081]",
                                 description="placeholder PV descr") )
        setattr(cls, "peatland [ENVO:00000044]",
                PermissibleValue(text="peatland [ENVO:00000044]",
                                 description="placeholder PV descr") )
        setattr(cls, "peninsula [ENVO:00000305]",
                PermissibleValue(text="peninsula [ENVO:00000305]",
                                 description="placeholder PV descr") )
        setattr(cls, "plain [ENVO:00000086]",
                PermissibleValue(text="plain [ENVO:00000086]",
                                 description="placeholder PV descr") )
        setattr(cls, "plateau [ENVO:00000182]",
                PermissibleValue(text="plateau [ENVO:00000182]",
                                 description="placeholder PV descr") )
        setattr(cls, "ridge [ENVO:00000283]",
                PermissibleValue(text="ridge [ENVO:00000283]",
                                 description="placeholder PV descr") )
        setattr(cls, "slope [ENVO:00002000]",
                PermissibleValue(text="slope [ENVO:00002000]",
                                 description="placeholder PV descr") )
        setattr(cls, "snow field [ENVO:00000146]",
                PermissibleValue(text="snow field [ENVO:00000146]",
                                 description="placeholder PV descr") )
        setattr(cls, "tombolo [ENVO:00000420]",
                PermissibleValue(text="tombolo [ENVO:00000420]",
                                 description="placeholder PV descr") )
        setattr(cls, "tuff cone [ENVO:01000664]",
                PermissibleValue(text="tuff cone [ENVO:01000664]",
                                 description="placeholder PV descr") )
        setattr(cls, "valley [ENVO:00000100]",
                PermissibleValue(text="valley [ENVO:00000100]",
                                 description="placeholder PV descr") )
        setattr(cls, "vein [ENVO:01000670]",
                PermissibleValue(text="vein [ENVO:01000670]",
                                 description="placeholder PV descr") )
        setattr(cls, "volcano [ENVO:00000247]",
                PermissibleValue(text="volcano [ENVO:00000247]",
                                 description="placeholder PV descr") )
        setattr(cls, "woodland clearing [ENVO:00000444]",
                PermissibleValue(text="woodland clearing [ENVO:00000444]",
                                 description="placeholder PV descr") )

class EnvMediumSoilEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    _defn = EnumDefinition(
        name="EnvMediumSoilEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "____peaty paddy field soil [ENVO:00005776]",
                PermissibleValue(text="____peaty paddy field soil [ENVO:00005776]",
                                 description="placeholder PV descr") )
        setattr(cls, "__acrisol [ENVO:00002234]",
                PermissibleValue(text="__acrisol [ENVO:00002234]",
                                 description="placeholder PV descr") )
        setattr(cls, "__alluvial swamp soil [ENVO:00005758]",
                PermissibleValue(text="__alluvial swamp soil [ENVO:00005758]",
                                 description="placeholder PV descr") )
        setattr(cls, "__beech forest soil [ENVO:00005770]",
                PermissibleValue(text="__beech forest soil [ENVO:00005770]",
                                 description="placeholder PV descr") )
        setattr(cls, "__bluegrass field soil [ENVO:00005789]",
                PermissibleValue(text="__bluegrass field soil [ENVO:00005789]",
                                 description="placeholder PV descr") )
        setattr(cls, "__cryosol [ENVO:00002236]",
                PermissibleValue(text="__cryosol [ENVO:00002236]",
                                 description="placeholder PV descr") )
        setattr(cls, "__eucalyptus forest soil [ENVO:00005787]",
                PermissibleValue(text="__eucalyptus forest soil [ENVO:00005787]",
                                 description="placeholder PV descr") )
        setattr(cls, "__friable-frozen soil [ENVO:01001528]",
                PermissibleValue(text="__friable-frozen soil [ENVO:01001528]",
                                 description="placeholder PV descr") )
        setattr(cls, "__frozen compost soil [ENVO:00005765]",
                PermissibleValue(text="__frozen compost soil [ENVO:00005765]",
                                 description="placeholder PV descr") )
        setattr(cls, "__mountain forest soil [ENVO:00005769]",
                PermissibleValue(text="__mountain forest soil [ENVO:00005769]",
                                 description="placeholder PV descr") )
        setattr(cls, "__paddy field soil [ENVO:00005740]",
                PermissibleValue(text="__paddy field soil [ENVO:00005740]",
                                 description="placeholder PV descr") )
        setattr(cls, "__plastic-frozen soil [ENVO:01001527]",
                PermissibleValue(text="__plastic-frozen soil [ENVO:01001527]",
                                 description="placeholder PV descr") )
        setattr(cls, "__rubber plantation soil [ENVO:00005788]",
                PermissibleValue(text="__rubber plantation soil [ENVO:00005788]",
                                 description="placeholder PV descr") )
        setattr(cls, "__savanna soil [ENVO:00005746]",
                PermissibleValue(text="__savanna soil [ENVO:00005746]",
                                 description="placeholder PV descr") )
        setattr(cls, "__steppe soil [ENVO:00005777]",
                PermissibleValue(text="__steppe soil [ENVO:00005777]",
                                 description="placeholder PV descr") )
        setattr(cls, "__volcanic soil [ENVO:01001841]",
                PermissibleValue(text="__volcanic soil [ENVO:01001841]",
                                 description="placeholder PV descr") )
        setattr(cls, "__xylene contaminated soil [ENVO:00002146]",
                PermissibleValue(text="__xylene contaminated soil [ENVO:00002146]",
                                 description="placeholder PV descr") )
        setattr(cls, "agricultural soil [ENVO:00002259]",
                PermissibleValue(text="agricultural soil [ENVO:00002259]",
                                 description="placeholder PV descr") )
        setattr(cls, "albeluvisol [ENVO:00002233]",
                PermissibleValue(text="albeluvisol [ENVO:00002233]",
                                 description="placeholder PV descr") )
        setattr(cls, "alisol [ENVO:00002231]",
                PermissibleValue(text="alisol [ENVO:00002231]",
                                 description="placeholder PV descr") )
        setattr(cls, "alluvial soil [ENVO:00002871]",
                PermissibleValue(text="alluvial soil [ENVO:00002871]",
                                 description="placeholder PV descr") )
        setattr(cls, "alpine soil [ENVO:00005741]",
                PermissibleValue(text="alpine soil [ENVO:00005741]",
                                 description="placeholder PV descr") )
        setattr(cls, "andosol [ENVO:00002232]",
                PermissibleValue(text="andosol [ENVO:00002232]",
                                 description="placeholder PV descr") )
        setattr(cls, "anthrosol [ENVO:00002230]",
                PermissibleValue(text="anthrosol [ENVO:00002230]",
                                 description="placeholder PV descr") )
        setattr(cls, "arenosol [ENVO:00002229]",
                PermissibleValue(text="arenosol [ENVO:00002229]",
                                 description="placeholder PV descr") )
        setattr(cls, "bare soil [ENVO:01001616]",
                PermissibleValue(text="bare soil [ENVO:01001616]",
                                 description="placeholder PV descr") )
        setattr(cls, "burned soil [ENVO:00005760]",
                PermissibleValue(text="burned soil [ENVO:00005760]",
                                 description="placeholder PV descr") )
        setattr(cls, "calcisol [ENVO:00002239]",
                PermissibleValue(text="calcisol [ENVO:00002239]",
                                 description="placeholder PV descr") )
        setattr(cls, "cambisol [ENVO:00002235]",
                PermissibleValue(text="cambisol [ENVO:00002235]",
                                 description="placeholder PV descr") )
        setattr(cls, "carbon nanotube enriched soil [ENVO:01000427]",
                PermissibleValue(text="carbon nanotube enriched soil [ENVO:01000427]",
                                 description="placeholder PV descr") )
        setattr(cls, "chernozem [ENVO:00002237]",
                PermissibleValue(text="chernozem [ENVO:00002237]",
                                 description="placeholder PV descr") )
        setattr(cls, "compost soil [ENVO:00005747]",
                PermissibleValue(text="compost soil [ENVO:00005747]",
                                 description="placeholder PV descr") )
        setattr(cls, "contaminated soil [ENVO:00002116]",
                PermissibleValue(text="contaminated soil [ENVO:00002116]",
                                 description="placeholder PV descr") )
        setattr(cls, "dune soil [ENVO:00002260]",
                PermissibleValue(text="dune soil [ENVO:00002260]",
                                 description="placeholder PV descr") )
        setattr(cls, "durisol [ENVO:00002238]",
                PermissibleValue(text="durisol [ENVO:00002238]",
                                 description="placeholder PV descr") )
        setattr(cls, "ferralsol [ENVO:00002246]",
                PermissibleValue(text="ferralsol [ENVO:00002246]",
                                 description="placeholder PV descr") )
        setattr(cls, "fluvisol [ENVO:00002273]",
                PermissibleValue(text="fluvisol [ENVO:00002273]",
                                 description="placeholder PV descr") )
        setattr(cls, "forest soil [ENVO:00002261]",
                PermissibleValue(text="forest soil [ENVO:00002261]",
                                 description="placeholder PV descr") )
        setattr(cls, "frost-susceptible soil [ENVO:01001638]",
                PermissibleValue(text="frost-susceptible soil [ENVO:01001638]",
                                 description="placeholder PV descr") )
        setattr(cls, "frozen soil [ENVO:01001526]",
                PermissibleValue(text="frozen soil [ENVO:01001526]",
                                 description="placeholder PV descr") )
        setattr(cls, "gleysol [ENVO:00002244]",
                PermissibleValue(text="gleysol [ENVO:00002244]",
                                 description="placeholder PV descr") )
        setattr(cls, "grassland soil [ENVO:00005750]",
                PermissibleValue(text="grassland soil [ENVO:00005750]",
                                 description="placeholder PV descr") )
        setattr(cls, "greenhouse soil [ENVO:00005780]",
                PermissibleValue(text="greenhouse soil [ENVO:00005780]",
                                 description="placeholder PV descr") )
        setattr(cls, "gypsisol [ENVO:00002245]",
                PermissibleValue(text="gypsisol [ENVO:00002245]",
                                 description="placeholder PV descr") )
        setattr(cls, "histosol [ENVO:00002243]",
                PermissibleValue(text="histosol [ENVO:00002243]",
                                 description="placeholder PV descr") )
        setattr(cls, "humus-rich acidic ash soil [ENVO:00005763]",
                PermissibleValue(text="humus-rich acidic ash soil [ENVO:00005763]",
                                 description="placeholder PV descr") )
        setattr(cls, "jungle soil [ENVO:00005751]",
                PermissibleValue(text="jungle soil [ENVO:00005751]",
                                 description="placeholder PV descr") )
        setattr(cls, "kastanozem [ENVO:00002240]",
                PermissibleValue(text="kastanozem [ENVO:00002240]",
                                 description="placeholder PV descr") )
        setattr(cls, "leptosol [ENVO:00002241]",
                PermissibleValue(text="leptosol [ENVO:00002241]",
                                 description="placeholder PV descr") )
        setattr(cls, "limed soil [ENVO:00005766]",
                PermissibleValue(text="limed soil [ENVO:00005766]",
                                 description="placeholder PV descr") )
        setattr(cls, "lixisol [ENVO:00002242]",
                PermissibleValue(text="lixisol [ENVO:00002242]",
                                 description="placeholder PV descr") )
        setattr(cls, "loam [ENVO:00002258]",
                PermissibleValue(text="loam [ENVO:00002258]",
                                 description="placeholder PV descr") )
        setattr(cls, "luvisol [ENVO:00002248]",
                PermissibleValue(text="luvisol [ENVO:00002248]",
                                 description="placeholder PV descr") )
        setattr(cls, "manured soil [ENVO:00005767]",
                PermissibleValue(text="manured soil [ENVO:00005767]",
                                 description="placeholder PV descr") )
        setattr(cls, "meadow soil [ENVO:00005761]",
                PermissibleValue(text="meadow soil [ENVO:00005761]",
                                 description="placeholder PV descr") )
        setattr(cls, "muddy soil [ENVO:00005771]",
                PermissibleValue(text="muddy soil [ENVO:00005771]",
                                 description="placeholder PV descr") )
        setattr(cls, "nitisol [ENVO:00002247]",
                PermissibleValue(text="nitisol [ENVO:00002247]",
                                 description="placeholder PV descr") )
        setattr(cls, "orchard soil [ENVO:00005772]",
                PermissibleValue(text="orchard soil [ENVO:00005772]",
                                 description="placeholder PV descr") )
        setattr(cls, "ornithogenic soil [ENVO:00005782]",
                PermissibleValue(text="ornithogenic soil [ENVO:00005782]",
                                 description="placeholder PV descr") )
        setattr(cls, "pantothenate enriched soil [ENVO:00003088]",
                PermissibleValue(text="pantothenate enriched soil [ENVO:00003088]",
                                 description="placeholder PV descr") )
        setattr(cls, "pasture soil [ENVO:00005773]",
                PermissibleValue(text="pasture soil [ENVO:00005773]",
                                 description="placeholder PV descr") )
        setattr(cls, "peat soil [ENVO:00005774]",
                PermissibleValue(text="peat soil [ENVO:00005774]",
                                 description="placeholder PV descr") )
        setattr(cls, "phaeozem [ENVO:00002249]",
                PermissibleValue(text="phaeozem [ENVO:00002249]",
                                 description="placeholder PV descr") )
        setattr(cls, "planosol [ENVO:00002251]",
                PermissibleValue(text="planosol [ENVO:00002251]",
                                 description="placeholder PV descr") )
        setattr(cls, "plinthosol [ENVO:00002250]",
                PermissibleValue(text="plinthosol [ENVO:00002250]",
                                 description="placeholder PV descr") )
        setattr(cls, "podzol [ENVO:00002257]",
                PermissibleValue(text="podzol [ENVO:00002257]",
                                 description="placeholder PV descr") )
        setattr(cls, "poly-beta-hydroxybutyrate enriched soil [ENVO:00003093]",
                PermissibleValue(text="poly-beta-hydroxybutyrate enriched soil [ENVO:00003093]",
                                 description="placeholder PV descr") )
        setattr(cls, "pond soil [ENVO:00005764]",
                PermissibleValue(text="pond soil [ENVO:00005764]",
                                 description="placeholder PV descr") )
        setattr(cls, "quinate enriched soil [ENVO:00003095]",
                PermissibleValue(text="quinate enriched soil [ENVO:00003095]",
                                 description="placeholder PV descr") )
        setattr(cls, "regosol [ENVO:00002256]",
                PermissibleValue(text="regosol [ENVO:00002256]",
                                 description="placeholder PV descr") )
        setattr(cls, "sarcosine enriched soil [ENVO:00003083]",
                PermissibleValue(text="sarcosine enriched soil [ENVO:00003083]",
                                 description="placeholder PV descr") )
        setattr(cls, "skatole enriched soil [ENVO:00003085]",
                PermissibleValue(text="skatole enriched soil [ENVO:00003085]",
                                 description="placeholder PV descr") )
        setattr(cls, "solonchak [ENVO:00002252]",
                PermissibleValue(text="solonchak [ENVO:00002252]",
                                 description="placeholder PV descr") )
        setattr(cls, "solonetz [ENVO:00002255]",
                PermissibleValue(text="solonetz [ENVO:00002255]",
                                 description="placeholder PV descr") )
        setattr(cls, "stagnosol [ENVO:00002274]",
                PermissibleValue(text="stagnosol [ENVO:00002274]",
                                 description="placeholder PV descr") )
        setattr(cls, "surface soil [ENVO:02000059]",
                PermissibleValue(text="surface soil [ENVO:02000059]",
                                 description="placeholder PV descr") )
        setattr(cls, "technosol [ENVO:00002275]",
                PermissibleValue(text="technosol [ENVO:00002275]",
                                 description="placeholder PV descr") )
        setattr(cls, "threonine enriched soil [ENVO:00003091]",
                PermissibleValue(text="threonine enriched soil [ENVO:00003091]",
                                 description="placeholder PV descr") )
        setattr(cls, "trimethylamine enriched soil [ENVO:00003084]",
                PermissibleValue(text="trimethylamine enriched soil [ENVO:00003084]",
                                 description="placeholder PV descr") )
        setattr(cls, "tropical soil [ENVO:00005778]",
                PermissibleValue(text="tropical soil [ENVO:00005778]",
                                 description="placeholder PV descr") )
        setattr(cls, "ultisol [ENVO:01001397]",
                PermissibleValue(text="ultisol [ENVO:01001397]",
                                 description="placeholder PV descr") )
        setattr(cls, "umbrisol [ENVO:00002253]",
                PermissibleValue(text="umbrisol [ENVO:00002253]",
                                 description="placeholder PV descr") )
        setattr(cls, "upland soil [ENVO:00005786]",
                PermissibleValue(text="upland soil [ENVO:00005786]",
                                 description="placeholder PV descr") )
        setattr(cls, "urea enriched soil [ENVO:00005753]",
                PermissibleValue(text="urea enriched soil [ENVO:00005753]",
                                 description="placeholder PV descr") )
        setattr(cls, "vertisol [ENVO:00002254]",
                PermissibleValue(text="vertisol [ENVO:00002254]",
                                 description="placeholder PV descr") )

class EnvPackageEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    soil = PermissibleValue(text="soil",
                               description="placeholder PV descr")

    _defn = EnumDefinition(
        name="EnvPackageEnum",
        description="placeholder enum descr",
    )

class GrowthFacilEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    experimental_garden = PermissibleValue(text="experimental_garden",
                                                             description="placeholder PV descr")
    field = PermissibleValue(text="field",
                                 description="placeholder PV descr")
    field_incubation = PermissibleValue(text="field_incubation",
                                                       description="placeholder PV descr")
    glasshouse = PermissibleValue(text="glasshouse",
                                           description="placeholder PV descr")
    greenhouse = PermissibleValue(text="greenhouse",
                                           description="placeholder PV descr")
    growth_chamber = PermissibleValue(text="growth_chamber",
                                                   description="placeholder PV descr")
    lab_incubation = PermissibleValue(text="lab_incubation",
                                                   description="placeholder PV descr")
    open_top_chamber = PermissibleValue(text="open_top_chamber",
                                                       description="placeholder PV descr")
    other = PermissibleValue(text="other",
                                 description="placeholder PV descr")

    _defn = EnumDefinition(
        name="GrowthFacilEnum",
        description="placeholder enum descr",
    )

class RelToOxygenEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    aerobe = PermissibleValue(text="aerobe",
                                   description="placeholder PV descr")
    anaerobe = PermissibleValue(text="anaerobe",
                                       description="placeholder PV descr")
    facultative = PermissibleValue(text="facultative",
                                             description="placeholder PV descr")
    microaerophilic = PermissibleValue(text="microaerophilic",
                                                     description="placeholder PV descr")
    microanaerobe = PermissibleValue(text="microanaerobe",
                                                 description="placeholder PV descr")

    _defn = EnumDefinition(
        name="RelToOxygenEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "obligate aerobe",
                PermissibleValue(text="obligate aerobe",
                                 description="placeholder PV descr") )
        setattr(cls, "obligate anaerobe",
                PermissibleValue(text="obligate anaerobe",
                                 description="placeholder PV descr") )

class RnaContTypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    plate = PermissibleValue(text="plate",
                                 description="placeholder PV descr")
    tube = PermissibleValue(text="tube",
                               description="placeholder PV descr")

    _defn = EnumDefinition(
        name="RnaContTypeEnum",
        description="placeholder enum descr",
    )

class RnaSampleFormatEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    DNAStable = PermissibleValue(text="DNAStable",
                                         description="placeholder PV descr")
    Ethanol = PermissibleValue(text="Ethanol",
                                     description="placeholder PV descr")
    PBS = PermissibleValue(text="PBS",
                             description="placeholder PV descr")
    Pellet = PermissibleValue(text="Pellet",
                                   description="placeholder PV descr")
    RNAStable = PermissibleValue(text="RNAStable",
                                         description="placeholder PV descr")
    TE = PermissibleValue(text="TE",
                           description="placeholder PV descr")
    Water = PermissibleValue(text="Water",
                                 description="placeholder PV descr")

    _defn = EnumDefinition(
        name="RnaSampleFormatEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl",
                                 description="placeholder PV descr") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE",
                                 description="placeholder PV descr") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer",
                                 description="placeholder PV descr") )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    soil = PermissibleValue(text="soil",
                               description="placeholder PV descr")
    water_extract_soil = PermissibleValue(text="water_extract_soil",
                                                           description="placeholder PV descr")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="placeholder enum descr",
    )

class SpecificEcosystemEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    Agricultural = PermissibleValue(text="Agricultural",
                                               description="placeholder PV descr")
    Alpine = PermissibleValue(text="Alpine",
                                   description="placeholder PV descr")
    Bog = PermissibleValue(text="Bog",
                             description="placeholder PV descr")
    Contaminated = PermissibleValue(text="Contaminated",
                                               description="placeholder PV descr")
    Desert = PermissibleValue(text="Desert",
                                   description="placeholder PV descr")
    Farm = PermissibleValue(text="Farm",
                               description="placeholder PV descr")
    Grasslands = PermissibleValue(text="Grasslands",
                                           description="placeholder PV descr")
    Meadow = PermissibleValue(text="Meadow",
                                   description="placeholder PV descr")
    Mine = PermissibleValue(text="Mine",
                               description="placeholder PV descr")
    Permafrost = PermissibleValue(text="Permafrost",
                                           description="placeholder PV descr")
    River = PermissibleValue(text="River",
                                 description="placeholder PV descr")
    Shrubland = PermissibleValue(text="Shrubland",
                                         description="placeholder PV descr")
    Unclassified = PermissibleValue(text="Unclassified",
                                               description="placeholder PV descr")

    _defn = EnumDefinition(
        name="SpecificEcosystemEnum",
        description="placeholder enum descr",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Agricultural land",
                PermissibleValue(text="Agricultural land",
                                 description="placeholder PV descr") )
        setattr(cls, "Agricultural soil",
                PermissibleValue(text="Agricultural soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Boreal forest",
                PermissibleValue(text="Boreal forest",
                                 description="placeholder PV descr") )
        setattr(cls, "Forest Soil",
                PermissibleValue(text="Forest Soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Forest soil",
                PermissibleValue(text="Forest soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Mine drainage",
                PermissibleValue(text="Mine drainage",
                                 description="placeholder PV descr") )
        setattr(cls, "Oil-contaminated",
                PermissibleValue(text="Oil-contaminated",
                                 description="placeholder PV descr") )
        setattr(cls, "Orchard soil",
                PermissibleValue(text="Orchard soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Riparian soil",
                PermissibleValue(text="Riparian soil",
                                 description="placeholder PV descr") )
        setattr(cls, "Tropical rainforest",
                PermissibleValue(text="Tropical rainforest",
                                 description="placeholder PV descr") )
        setattr(cls, "Uranium contaminated",
                PermissibleValue(text="Uranium contaminated",
                                 description="placeholder PV descr") )

class StoreCondEnum(EnumDefinitionImpl):
    """
    placeholder enum descr
    """
    fresh = PermissibleValue(text="fresh",
                                 description="placeholder PV descr")
    frozen = PermissibleValue(text="frozen",
                                   description="placeholder PV descr")
    lyophilized = PermissibleValue(text="lyophilized",
                                             description="placeholder PV descr")
    other = PermissibleValue(text="other",
                                 description="placeholder PV descr")

    _defn = EnumDefinition(
        name="StoreCondEnum",
        description="placeholder enum descr",
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

class HeatDelivLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="HeatDelivLocEnum",
    )

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

class FurnitureEnum(EnumDefinitionImpl):

    cabinet = PermissibleValue(text="cabinet")
    chair = PermissibleValue(text="chair")
    desks = PermissibleValue(text="desks")

    _defn = EnumDefinition(
        name="FurnitureEnum",
    )

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

class WindowMatEnum(EnumDefinitionImpl):

    clad = PermissibleValue(text="clad")
    fiberglass = PermissibleValue(text="fiberglass")
    metal = PermissibleValue(text="metal")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="WindowMatEnum",
    )

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

class DoorLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="DoorLocEnum",
    )

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

class SeasonUseEnum(EnumDefinitionImpl):

    Spring = PermissibleValue(text="Spring")
    Summer = PermissibleValue(text="Summer")
    Fall = PermissibleValue(text="Fall")
    Winter = PermissibleValue(text="Winter")

    _defn = EnumDefinition(
        name="SeasonUseEnum",
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

class WindowVertPosEnum(EnumDefinitionImpl):

    bottom = PermissibleValue(text="bottom")
    middle = PermissibleValue(text="middle")
    top = PermissibleValue(text="top")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="WindowVertPosEnum",
    )

class WallLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WallLocEnum",
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

class TrainStopLocEnum(EnumDefinitionImpl):

    end = PermissibleValue(text="end")
    mid = PermissibleValue(text="mid")
    downtown = PermissibleValue(text="downtown")

    _defn = EnumDefinition(
        name="TrainStopLocEnum",
    )

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

class ArchStrucEnum(EnumDefinitionImpl):

    building = PermissibleValue(text="building")
    shed = PermissibleValue(text="shed")
    home = PermissibleValue(text="home")

    _defn = EnumDefinition(
        name="ArchStrucEnum",
    )

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

class DoorDirectEnum(EnumDefinitionImpl):

    inward = PermissibleValue(text="inward")
    outward = PermissibleValue(text="outward")
    sideways = PermissibleValue(text="sideways")

    _defn = EnumDefinition(
        name="DoorDirectEnum",
    )

class WindowCoverEnum(EnumDefinitionImpl):

    blinds = PermissibleValue(text="blinds")
    curtains = PermissibleValue(text="curtains")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="WindowCoverEnum",
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

class DoorTypeEnum(EnumDefinitionImpl):

    composite = PermissibleValue(text="composite")
    metal = PermissibleValue(text="metal")
    wooden = PermissibleValue(text="wooden")

    _defn = EnumDefinition(
        name="DoorTypeEnum",
    )

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

class TrainLineEnum(EnumDefinitionImpl):

    red = PermissibleValue(text="red")
    green = PermissibleValue(text="green")
    orange = PermissibleValue(text="orange")

    _defn = EnumDefinition(
        name="TrainLineEnum",
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

class BuildingSettingEnum(EnumDefinitionImpl):

    urban = PermissibleValue(text="urban")
    suburban = PermissibleValue(text="suburban")
    exurban = PermissibleValue(text="exurban")
    rural = PermissibleValue(text="rural")

    _defn = EnumDefinition(
        name="BuildingSettingEnum",
    )

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

class WindowHorizPosEnum(EnumDefinitionImpl):

    left = PermissibleValue(text="left")
    middle = PermissibleValue(text="middle")
    right = PermissibleValue(text="right")

    _defn = EnumDefinition(
        name="WindowHorizPosEnum",
    )

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

class WindowLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WindowLocEnum",
    )

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

class SrLithologyEnum(EnumDefinitionImpl):

    Clastic = PermissibleValue(text="Clastic")
    Carbonate = PermissibleValue(text="Carbonate")
    Coal = PermissibleValue(text="Coal")
    Biosilicieous = PermissibleValue(text="Biosilicieous")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrLithologyEnum",
    )

class SrDepEnvEnum(EnumDefinitionImpl):

    Lacustine = PermissibleValue(text="Lacustine")
    Fluvioldeltaic = PermissibleValue(text="Fluvioldeltaic")
    Fluviomarine = PermissibleValue(text="Fluviomarine")
    Marine = PermissibleValue(text="Marine")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrDepEnvEnum",
    )

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

class ProfilePositionEnum(EnumDefinitionImpl):

    summit = PermissibleValue(text="summit")
    shoulder = PermissibleValue(text="shoulder")
    backslope = PermissibleValue(text="backslope")
    footslope = PermissibleValue(text="footslope")
    toeslope = PermissibleValue(text="toeslope")

    _defn = EnumDefinition(
        name="ProfilePositionEnum",
    )

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

class SedimentTypeEnum(EnumDefinitionImpl):

    biogenous = PermissibleValue(text="biogenous")
    cosmogenous = PermissibleValue(text="cosmogenous")
    hydrogenous = PermissibleValue(text="hydrogenous")
    lithogenous = PermissibleValue(text="lithogenous")

    _defn = EnumDefinition(
        name="SedimentTypeEnum",
    )

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

slots.air_data = Slot(uri=NMDC_SUB_SCHEMA.air_data, name="air_data", curie=NMDC_SUB_SCHEMA.curie('air_data'),
                   model_uri=NMDC_SUB_SCHEMA.air_data, domain=None, range=Optional[Union[Union[dict, AirInterface], List[Union[dict, AirInterface]]]])

slots.analysis_type = Slot(uri=NMDC_SUB_SCHEMA.analysis_type, name="analysis_type", curie=NMDC_SUB_SCHEMA.curie('analysis_type'),
                   model_uri=NMDC_SUB_SCHEMA.analysis_type, domain=None, range=Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]])

slots.biofilm_data = Slot(uri=NMDC_SUB_SCHEMA.biofilm_data, name="biofilm_data", curie=NMDC_SUB_SCHEMA.curie('biofilm_data'),
                   model_uri=NMDC_SUB_SCHEMA.biofilm_data, domain=None, range=Optional[Union[Union[dict, BiofilmInterface], List[Union[dict, BiofilmInterface]]]])

slots.built_env_data = Slot(uri=NMDC_SUB_SCHEMA.built_env_data, name="built_env_data", curie=NMDC_SUB_SCHEMA.curie('built_env_data'),
                   model_uri=NMDC_SUB_SCHEMA.built_env_data, domain=None, range=Optional[Union[Union[dict, BuiltEnvInterface], List[Union[dict, BuiltEnvInterface]]]])

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
                   model_uri=NMDC_SUB_SCHEMA.dna_collect_site, domain=None, range=str)

slots.dna_concentration = Slot(uri=NMDC_SUB_SCHEMA.dna_concentration, name="dna_concentration", curie=NMDC_SUB_SCHEMA.curie('dna_concentration'),
                   model_uri=NMDC_SUB_SCHEMA.dna_concentration, domain=None, range=str)

slots.dna_cont_type = Slot(uri=NMDC_SUB_SCHEMA.dna_cont_type, name="dna_cont_type", curie=NMDC_SUB_SCHEMA.curie('dna_cont_type'),
                   model_uri=NMDC_SUB_SCHEMA.dna_cont_type, domain=None, range=Union[str, "DnaContTypeEnum"])

slots.dna_cont_well = Slot(uri=NMDC_SUB_SCHEMA.dna_cont_well, name="dna_cont_well", curie=NMDC_SUB_SCHEMA.curie('dna_cont_well'),
                   model_uri=NMDC_SUB_SCHEMA.dna_cont_well, domain=None, range=str)

slots.dna_container_id = Slot(uri=NMDC_SUB_SCHEMA.dna_container_id, name="dna_container_id", curie=NMDC_SUB_SCHEMA.curie('dna_container_id'),
                   model_uri=NMDC_SUB_SCHEMA.dna_container_id, domain=None, range=str)

slots.dna_dnase = Slot(uri=NMDC_SUB_SCHEMA.dna_dnase, name="dna_dnase", curie=NMDC_SUB_SCHEMA.curie('dna_dnase'),
                   model_uri=NMDC_SUB_SCHEMA.dna_dnase, domain=None, range=Union[str, "DnaDnaseEnum"])

slots.dna_isolate_meth = Slot(uri=NMDC_SUB_SCHEMA.dna_isolate_meth, name="dna_isolate_meth", curie=NMDC_SUB_SCHEMA.curie('dna_isolate_meth'),
                   model_uri=NMDC_SUB_SCHEMA.dna_isolate_meth, domain=None, range=str)

slots.dna_organisms = Slot(uri=NMDC_SUB_SCHEMA.dna_organisms, name="dna_organisms", curie=NMDC_SUB_SCHEMA.curie('dna_organisms'),
                   model_uri=NMDC_SUB_SCHEMA.dna_organisms, domain=None, range=Optional[str])

slots.dna_project_contact = Slot(uri=NMDC_SUB_SCHEMA.dna_project_contact, name="dna_project_contact", curie=NMDC_SUB_SCHEMA.curie('dna_project_contact'),
                   model_uri=NMDC_SUB_SCHEMA.dna_project_contact, domain=None, range=str)

slots.dna_samp_id = Slot(uri=NMDC_SUB_SCHEMA.dna_samp_id, name="dna_samp_id", curie=NMDC_SUB_SCHEMA.curie('dna_samp_id'),
                   model_uri=NMDC_SUB_SCHEMA.dna_samp_id, domain=None, range=str)

slots.dna_sample_format = Slot(uri=NMDC_SUB_SCHEMA.dna_sample_format, name="dna_sample_format", curie=NMDC_SUB_SCHEMA.curie('dna_sample_format'),
                   model_uri=NMDC_SUB_SCHEMA.dna_sample_format, domain=None, range=Union[str, "DnaSampleFormatEnum"])

slots.dna_sample_name = Slot(uri=NMDC_SUB_SCHEMA.dna_sample_name, name="dna_sample_name", curie=NMDC_SUB_SCHEMA.curie('dna_sample_name'),
                   model_uri=NMDC_SUB_SCHEMA.dna_sample_name, domain=None, range=str)

slots.dna_seq_project = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project, name="dna_seq_project", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project, domain=None, range=str)

slots.dna_seq_project_name = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project_name, name="dna_seq_project_name", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project_name'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project_name, domain=None, range=str)

slots.dna_seq_project_pi = Slot(uri=NMDC_SUB_SCHEMA.dna_seq_project_pi, name="dna_seq_project_pi", curie=NMDC_SUB_SCHEMA.curie('dna_seq_project_pi'),
                   model_uri=NMDC_SUB_SCHEMA.dna_seq_project_pi, domain=None, range=str)

slots.dna_volume = Slot(uri=NMDC_SUB_SCHEMA.dna_volume, name="dna_volume", curie=NMDC_SUB_SCHEMA.curie('dna_volume'),
                   model_uri=NMDC_SUB_SCHEMA.dna_volume, domain=None, range=str)

slots.dnase_rna = Slot(uri=NMDC_SUB_SCHEMA.dnase_rna, name="dnase_rna", curie=NMDC_SUB_SCHEMA.curie('dnase_rna'),
                   model_uri=NMDC_SUB_SCHEMA.dnase_rna, domain=None, range=Union[str, "DnaseRnaEnum"])

slots.emsl_data = Slot(uri=NMDC_SUB_SCHEMA.emsl_data, name="emsl_data", curie=NMDC_SUB_SCHEMA.curie('emsl_data'),
                   model_uri=NMDC_SUB_SCHEMA.emsl_data, domain=None, range=Optional[Union[Union[dict, EmslInterface], List[Union[dict, EmslInterface]]]])

slots.emsl_section = Slot(uri=NMDC_SUB_SCHEMA.emsl_section, name="emsl_section", curie=NMDC_SUB_SCHEMA.curie('emsl_section'),
                   model_uri=NMDC_SUB_SCHEMA.emsl_section, domain=None, range=Optional[str])

slots.emsl_store_temp = Slot(uri=NMDC_SUB_SCHEMA.emsl_store_temp, name="emsl_store_temp", curie=NMDC_SUB_SCHEMA.curie('emsl_store_temp'),
                   model_uri=NMDC_SUB_SCHEMA.emsl_store_temp, domain=None, range=str)

slots.env_package = Slot(uri=NMDC_SUB_SCHEMA.env_package, name="env_package", curie=NMDC_SUB_SCHEMA.curie('env_package'),
                   model_uri=NMDC_SUB_SCHEMA.env_package, domain=None, range=str)

slots.experimental_factor_other = Slot(uri=NMDC_SUB_SCHEMA.experimental_factor_other, name="experimental_factor_other", curie=NMDC_SUB_SCHEMA.curie('experimental_factor_other'),
                   model_uri=NMDC_SUB_SCHEMA.experimental_factor_other, domain=None, range=Optional[str])

slots.filter_method = Slot(uri=NMDC_SUB_SCHEMA.filter_method, name="filter_method", curie=NMDC_SUB_SCHEMA.curie('filter_method'),
                   model_uri=NMDC_SUB_SCHEMA.filter_method, domain=None, range=Optional[str])

slots.hcr_cores_data = Slot(uri=NMDC_SUB_SCHEMA.hcr_cores_data, name="hcr_cores_data", curie=NMDC_SUB_SCHEMA.curie('hcr_cores_data'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_cores_data, domain=None, range=Optional[Union[Union[dict, HcrCoresInterface], List[Union[dict, HcrCoresInterface]]]])

slots.hcr_fluids_swabs_data = Slot(uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_data, name="hcr_fluids_swabs_data", curie=NMDC_SUB_SCHEMA.curie('hcr_fluids_swabs_data'),
                   model_uri=NMDC_SUB_SCHEMA.hcr_fluids_swabs_data, domain=None, range=Optional[Union[Union[dict, HcrFluidsSwabsInterface], List[Union[dict, HcrFluidsSwabsInterface]]]])

slots.host_associated_data = Slot(uri=NMDC_SUB_SCHEMA.host_associated_data, name="host_associated_data", curie=NMDC_SUB_SCHEMA.curie('host_associated_data'),
                   model_uri=NMDC_SUB_SCHEMA.host_associated_data, domain=None, range=Optional[Union[Union[dict, HostAssociatedInterface], List[Union[dict, HostAssociatedInterface]]]])

slots.isotope_exposure = Slot(uri=NMDC_SUB_SCHEMA.isotope_exposure, name="isotope_exposure", curie=NMDC_SUB_SCHEMA.curie('isotope_exposure'),
                   model_uri=NMDC_SUB_SCHEMA.isotope_exposure, domain=None, range=Optional[str])

slots.jgi_metagenomics_section = Slot(uri=NMDC_SUB_SCHEMA.jgi_metagenomics_section, name="jgi_metagenomics_section", curie=NMDC_SUB_SCHEMA.curie('jgi_metagenomics_section'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_metagenomics_section, domain=None, range=Optional[str])

slots.jgi_metatranscriptomics_section = Slot(uri=NMDC_SUB_SCHEMA.jgi_metatranscriptomics_section, name="jgi_metatranscriptomics_section", curie=NMDC_SUB_SCHEMA.curie('jgi_metatranscriptomics_section'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_metatranscriptomics_section, domain=None, range=Optional[str])

slots.jgi_mg_data = Slot(uri=NMDC_SUB_SCHEMA.jgi_mg_data, name="jgi_mg_data", curie=NMDC_SUB_SCHEMA.curie('jgi_mg_data'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_mg_data, domain=None, range=Optional[Union[Union[dict, JgiMgInterface], List[Union[dict, JgiMgInterface]]]])

slots.jgi_mt_data = Slot(uri=NMDC_SUB_SCHEMA.jgi_mt_data, name="jgi_mt_data", curie=NMDC_SUB_SCHEMA.curie('jgi_mt_data'),
                   model_uri=NMDC_SUB_SCHEMA.jgi_mt_data, domain=None, range=Optional[Union[Union[dict, JgiMtInterface], List[Union[dict, JgiMtInterface]]]])

slots.micro_biomass_c_meth = Slot(uri=NMDC_SUB_SCHEMA.micro_biomass_c_meth, name="micro_biomass_c_meth", curie=NMDC_SUB_SCHEMA.curie('micro_biomass_c_meth'),
                   model_uri=NMDC_SUB_SCHEMA.micro_biomass_c_meth, domain=None, range=Optional[str])

slots.micro_biomass_n_meth = Slot(uri=NMDC_SUB_SCHEMA.micro_biomass_n_meth, name="micro_biomass_n_meth", curie=NMDC_SUB_SCHEMA.curie('micro_biomass_n_meth'),
                   model_uri=NMDC_SUB_SCHEMA.micro_biomass_n_meth, domain=None, range=Optional[str])

slots.microbial_biomass_c = Slot(uri=NMDC_SUB_SCHEMA.microbial_biomass_c, name="microbial_biomass_c", curie=NMDC_SUB_SCHEMA.curie('microbial_biomass_c'),
                   model_uri=NMDC_SUB_SCHEMA.microbial_biomass_c, domain=None, range=Optional[str])

slots.microbial_biomass_n = Slot(uri=NMDC_SUB_SCHEMA.microbial_biomass_n, name="microbial_biomass_n", curie=NMDC_SUB_SCHEMA.curie('microbial_biomass_n'),
                   model_uri=NMDC_SUB_SCHEMA.microbial_biomass_n, domain=None, range=Optional[str])

slots.misc_envs_data = Slot(uri=NMDC_SUB_SCHEMA.misc_envs_data, name="misc_envs_data", curie=NMDC_SUB_SCHEMA.curie('misc_envs_data'),
                   model_uri=NMDC_SUB_SCHEMA.misc_envs_data, domain=None, range=Optional[Union[Union[dict, MiscEnvsInterface], List[Union[dict, MiscEnvsInterface]]]])

slots.mixs_core_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_core_section, name="mixs_core_section", curie=NMDC_SUB_SCHEMA.curie('mixs_core_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_core_section, domain=None, range=Optional[str])

slots.mixs_inspired_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_inspired_section, name="mixs_inspired_section", curie=NMDC_SUB_SCHEMA.curie('mixs_inspired_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_inspired_section, domain=None, range=Optional[str])

slots.mixs_investigation_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_investigation_section, name="mixs_investigation_section", curie=NMDC_SUB_SCHEMA.curie('mixs_investigation_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_investigation_section, domain=None, range=Optional[str])

slots.mixs_modified_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_modified_section, name="mixs_modified_section", curie=NMDC_SUB_SCHEMA.curie('mixs_modified_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_modified_section, domain=None, range=Optional[str])

slots.mixs_nassf_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_nassf_section, name="mixs_nassf_section", curie=NMDC_SUB_SCHEMA.curie('mixs_nassf_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_nassf_section, domain=None, range=Optional[str])

slots.mixs_section = Slot(uri=NMDC_SUB_SCHEMA.mixs_section, name="mixs_section", curie=NMDC_SUB_SCHEMA.curie('mixs_section'),
                   model_uri=NMDC_SUB_SCHEMA.mixs_section, domain=None, range=Optional[str])

slots.non_microb_biomass = Slot(uri=NMDC_SUB_SCHEMA.non_microb_biomass, name="non_microb_biomass", curie=NMDC_SUB_SCHEMA.curie('non_microb_biomass'),
                   model_uri=NMDC_SUB_SCHEMA.non_microb_biomass, domain=None, range=Optional[str])

slots.non_microb_biomass_method = Slot(uri=NMDC_SUB_SCHEMA.non_microb_biomass_method, name="non_microb_biomass_method", curie=NMDC_SUB_SCHEMA.curie('non_microb_biomass_method'),
                   model_uri=NMDC_SUB_SCHEMA.non_microb_biomass_method, domain=None, range=Optional[str])

slots.org_nitro_method = Slot(uri=NMDC_SUB_SCHEMA.org_nitro_method, name="org_nitro_method", curie=NMDC_SUB_SCHEMA.curie('org_nitro_method'),
                   model_uri=NMDC_SUB_SCHEMA.org_nitro_method, domain=None, range=Optional[str])

slots.other_treatment = Slot(uri=NMDC_SUB_SCHEMA.other_treatment, name="other_treatment", curie=NMDC_SUB_SCHEMA.curie('other_treatment'),
                   model_uri=NMDC_SUB_SCHEMA.other_treatment, domain=None, range=Optional[str])

slots.plant_associated_data = Slot(uri=NMDC_SUB_SCHEMA.plant_associated_data, name="plant_associated_data", curie=NMDC_SUB_SCHEMA.curie('plant_associated_data'),
                   model_uri=NMDC_SUB_SCHEMA.plant_associated_data, domain=None, range=Optional[Union[Union[dict, PlantAssociatedInterface], List[Union[dict, PlantAssociatedInterface]]]])

slots.project_id = Slot(uri=NMDC_SUB_SCHEMA.project_id, name="project_id", curie=NMDC_SUB_SCHEMA.curie('project_id'),
                   model_uri=NMDC_SUB_SCHEMA.project_id, domain=None, range=str)

slots.proposal_dna = Slot(uri=NMDC_SUB_SCHEMA.proposal_dna, name="proposal_dna", curie=NMDC_SUB_SCHEMA.curie('proposal_dna'),
                   model_uri=NMDC_SUB_SCHEMA.proposal_dna, domain=None, range=str)

slots.proposal_rna = Slot(uri=NMDC_SUB_SCHEMA.proposal_rna, name="proposal_rna", curie=NMDC_SUB_SCHEMA.curie('proposal_rna'),
                   model_uri=NMDC_SUB_SCHEMA.proposal_rna, domain=None, range=str)

slots.replicate_number = Slot(uri=NMDC_SUB_SCHEMA.replicate_number, name="replicate_number", curie=NMDC_SUB_SCHEMA.curie('replicate_number'),
                   model_uri=NMDC_SUB_SCHEMA.replicate_number, domain=None, range=Optional[str])

slots.rna_absorb1 = Slot(uri=NMDC_SUB_SCHEMA.rna_absorb1, name="rna_absorb1", curie=NMDC_SUB_SCHEMA.curie('rna_absorb1'),
                   model_uri=NMDC_SUB_SCHEMA.rna_absorb1, domain=None, range=Optional[str])

slots.rna_absorb2 = Slot(uri=NMDC_SUB_SCHEMA.rna_absorb2, name="rna_absorb2", curie=NMDC_SUB_SCHEMA.curie('rna_absorb2'),
                   model_uri=NMDC_SUB_SCHEMA.rna_absorb2, domain=None, range=Optional[str])

slots.rna_collect_site = Slot(uri=NMDC_SUB_SCHEMA.rna_collect_site, name="rna_collect_site", curie=NMDC_SUB_SCHEMA.curie('rna_collect_site'),
                   model_uri=NMDC_SUB_SCHEMA.rna_collect_site, domain=None, range=str)

slots.rna_concentration = Slot(uri=NMDC_SUB_SCHEMA.rna_concentration, name="rna_concentration", curie=NMDC_SUB_SCHEMA.curie('rna_concentration'),
                   model_uri=NMDC_SUB_SCHEMA.rna_concentration, domain=None, range=str)

slots.rna_cont_type = Slot(uri=NMDC_SUB_SCHEMA.rna_cont_type, name="rna_cont_type", curie=NMDC_SUB_SCHEMA.curie('rna_cont_type'),
                   model_uri=NMDC_SUB_SCHEMA.rna_cont_type, domain=None, range=Union[str, "RnaContTypeEnum"])

slots.rna_cont_well = Slot(uri=NMDC_SUB_SCHEMA.rna_cont_well, name="rna_cont_well", curie=NMDC_SUB_SCHEMA.curie('rna_cont_well'),
                   model_uri=NMDC_SUB_SCHEMA.rna_cont_well, domain=None, range=str)

slots.rna_container_id = Slot(uri=NMDC_SUB_SCHEMA.rna_container_id, name="rna_container_id", curie=NMDC_SUB_SCHEMA.curie('rna_container_id'),
                   model_uri=NMDC_SUB_SCHEMA.rna_container_id, domain=None, range=str)

slots.rna_isolate_meth = Slot(uri=NMDC_SUB_SCHEMA.rna_isolate_meth, name="rna_isolate_meth", curie=NMDC_SUB_SCHEMA.curie('rna_isolate_meth'),
                   model_uri=NMDC_SUB_SCHEMA.rna_isolate_meth, domain=None, range=str)

slots.rna_organisms = Slot(uri=NMDC_SUB_SCHEMA.rna_organisms, name="rna_organisms", curie=NMDC_SUB_SCHEMA.curie('rna_organisms'),
                   model_uri=NMDC_SUB_SCHEMA.rna_organisms, domain=None, range=Optional[str])

slots.rna_project_contact = Slot(uri=NMDC_SUB_SCHEMA.rna_project_contact, name="rna_project_contact", curie=NMDC_SUB_SCHEMA.curie('rna_project_contact'),
                   model_uri=NMDC_SUB_SCHEMA.rna_project_contact, domain=None, range=str)

slots.rna_samp_id = Slot(uri=NMDC_SUB_SCHEMA.rna_samp_id, name="rna_samp_id", curie=NMDC_SUB_SCHEMA.curie('rna_samp_id'),
                   model_uri=NMDC_SUB_SCHEMA.rna_samp_id, domain=None, range=str)

slots.rna_sample_format = Slot(uri=NMDC_SUB_SCHEMA.rna_sample_format, name="rna_sample_format", curie=NMDC_SUB_SCHEMA.curie('rna_sample_format'),
                   model_uri=NMDC_SUB_SCHEMA.rna_sample_format, domain=None, range=Union[str, "RnaSampleFormatEnum"])

slots.rna_sample_name = Slot(uri=NMDC_SUB_SCHEMA.rna_sample_name, name="rna_sample_name", curie=NMDC_SUB_SCHEMA.curie('rna_sample_name'),
                   model_uri=NMDC_SUB_SCHEMA.rna_sample_name, domain=None, range=str)

slots.rna_seq_project = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project, name="rna_seq_project", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project, domain=None, range=str)

slots.rna_seq_project_name = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project_name, name="rna_seq_project_name", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project_name'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project_name, domain=None, range=str)

slots.rna_seq_project_pi = Slot(uri=NMDC_SUB_SCHEMA.rna_seq_project_pi, name="rna_seq_project_pi", curie=NMDC_SUB_SCHEMA.curie('rna_seq_project_pi'),
                   model_uri=NMDC_SUB_SCHEMA.rna_seq_project_pi, domain=None, range=str)

slots.rna_volume = Slot(uri=NMDC_SUB_SCHEMA.rna_volume, name="rna_volume", curie=NMDC_SUB_SCHEMA.curie('rna_volume'),
                   model_uri=NMDC_SUB_SCHEMA.rna_volume, domain=None, range=str)

slots.sample_id_section = Slot(uri=NMDC_SUB_SCHEMA.sample_id_section, name="sample_id_section", curie=NMDC_SUB_SCHEMA.curie('sample_id_section'),
                   model_uri=NMDC_SUB_SCHEMA.sample_id_section, domain=None, range=Optional[str])

slots.sample_link = Slot(uri=NMDC_SUB_SCHEMA.sample_link, name="sample_link", curie=NMDC_SUB_SCHEMA.curie('sample_link'),
                   model_uri=NMDC_SUB_SCHEMA.sample_link, domain=None, range=Optional[str])

slots.sample_shipped = Slot(uri=NMDC_SUB_SCHEMA.sample_shipped, name="sample_shipped", curie=NMDC_SUB_SCHEMA.curie('sample_shipped'),
                   model_uri=NMDC_SUB_SCHEMA.sample_shipped, domain=None, range=str)

slots.sample_type = Slot(uri=NMDC_SUB_SCHEMA.sample_type, name="sample_type", curie=NMDC_SUB_SCHEMA.curie('sample_type'),
                   model_uri=NMDC_SUB_SCHEMA.sample_type, domain=None, range=Union[str, "SampleTypeEnum"])

slots.sediment_data = Slot(uri=NMDC_SUB_SCHEMA.sediment_data, name="sediment_data", curie=NMDC_SUB_SCHEMA.curie('sediment_data'),
                   model_uri=NMDC_SUB_SCHEMA.sediment_data, domain=None, range=Optional[Union[Union[dict, SedimentInterface], List[Union[dict, SedimentInterface]]]])

slots.soil_data = Slot(uri=NMDC_SUB_SCHEMA.soil_data, name="soil_data", curie=NMDC_SUB_SCHEMA.curie('soil_data'),
                   model_uri=NMDC_SUB_SCHEMA.soil_data, domain=None, range=Optional[Union[Union[dict, SoilInterface], List[Union[dict, SoilInterface]]]])

slots.start_date_inc = Slot(uri=NMDC_SUB_SCHEMA.start_date_inc, name="start_date_inc", curie=NMDC_SUB_SCHEMA.curie('start_date_inc'),
                   model_uri=NMDC_SUB_SCHEMA.start_date_inc, domain=None, range=Optional[str])

slots.start_time_inc = Slot(uri=NMDC_SUB_SCHEMA.start_time_inc, name="start_time_inc", curie=NMDC_SUB_SCHEMA.curie('start_time_inc'),
                   model_uri=NMDC_SUB_SCHEMA.start_time_inc, domain=None, range=Optional[str])

slots.technical_reps = Slot(uri=NMDC_SUB_SCHEMA.technical_reps, name="technical_reps", curie=NMDC_SUB_SCHEMA.curie('technical_reps'),
                   model_uri=NMDC_SUB_SCHEMA.technical_reps, domain=None, range=Optional[str])

slots.type = Slot(uri=NMDC_SUB_SCHEMA.type, name="type", curie=NMDC_SUB_SCHEMA.curie('type'),
                   model_uri=NMDC_SUB_SCHEMA.type, domain=None, range=Optional[str])

slots.wastewater_sludge_data = Slot(uri=NMDC_SUB_SCHEMA.wastewater_sludge_data, name="wastewater_sludge_data", curie=NMDC_SUB_SCHEMA.curie('wastewater_sludge_data'),
                   model_uri=NMDC_SUB_SCHEMA.wastewater_sludge_data, domain=None, range=Optional[Union[Union[dict, WastewaterSludgeInterface], List[Union[dict, WastewaterSludgeInterface]]]])

slots.water_data = Slot(uri=NMDC_SUB_SCHEMA.water_data, name="water_data", curie=NMDC_SUB_SCHEMA.curie('water_data'),
                   model_uri=NMDC_SUB_SCHEMA.water_data, domain=None, range=Optional[Union[Union[dict, WaterInterface], List[Union[dict, WaterInterface]]]])

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

slots.air_temp = Slot(uri=MIXS['0000124'], name="air_temp", curie=MIXS.curie('0000124'),
                   model_uri=NMDC_SUB_SCHEMA.air_temp, domain=None, range=Optional[str])

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
                   model_uri=NMDC_SUB_SCHEMA.collection_date, domain=None, range=Optional[str])

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
                   model_uri=NMDC_SUB_SCHEMA.date_last_rain, domain=None, range=Optional[str])

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
                   model_uri=NMDC_SUB_SCHEMA.extreme_event, domain=None, range=Optional[str])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_SUB_SCHEMA.fao_class, domain=None, range=Optional[Union[str, "FaoClassEnum"]])

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC_SUB_SCHEMA.fertilizer_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.field, domain=None, range=Optional[str])

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC_SUB_SCHEMA.filter_type, domain=None, range=Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_SUB_SCHEMA.fire, domain=None, range=Optional[str])

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC_SUB_SCHEMA.fireplace_type, domain=None, range=Optional[str])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_SUB_SCHEMA.flooding, domain=None, range=Optional[str])

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
                   model_uri=NMDC_SUB_SCHEMA.iw_bt_date_well, domain=None, range=Optional[str])

slots.iwf = Slot(uri=MIXS['0000455'], name="iwf", curie=MIXS.curie('0000455'),
                   model_uri=NMDC_SUB_SCHEMA.iwf, domain=None, range=Optional[str])

slots.last_clean = Slot(uri=MIXS['0000814'], name="last_clean", curie=MIXS.curie('0000814'),
                   model_uri=NMDC_SUB_SCHEMA.last_clean, domain=None, range=Optional[str])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.lat_lon, domain=None, range=Optional[str])

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
                   model_uri=NMDC_SUB_SCHEMA.prod_start_date, domain=None, range=Optional[str])

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

slots.has_raw_value = Slot(uri=NMDC_SUB_SCHEMA.has_raw_value, name="has_raw_value", curie=NMDC_SUB_SCHEMA.curie('has_raw_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.was_generated_by = Slot(uri=NMDC_SUB_SCHEMA.was_generated_by, name="was_generated_by", curie=NMDC_SUB_SCHEMA.curie('was_generated_by'),
                   model_uri=NMDC_SUB_SCHEMA.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.investigation_field = Slot(uri=NMDC_SUB_SCHEMA.investigation_field, name="investigation field", curie=NMDC_SUB_SCHEMA.curie('investigation_field'),
                   model_uri=NMDC_SUB_SCHEMA.investigation_field, domain=None, range=Optional[str])

slots.started_at_time = Slot(uri=NMDC_SUB_SCHEMA.started_at_time, name="started_at_time", curie=NMDC_SUB_SCHEMA.curie('started_at_time'),
                   model_uri=NMDC_SUB_SCHEMA.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.startedAtTime])

slots.nucleic_acid_sequence_source_field = Slot(uri=NMDC_SUB_SCHEMA.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=NMDC_SUB_SCHEMA.curie('nucleic_acid_sequence_source_field'),
                   model_uri=NMDC_SUB_SCHEMA.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.name = Slot(uri=NMDC_SUB_SCHEMA.name, name="name", curie=NMDC_SUB_SCHEMA.curie('name'),
                   model_uri=NMDC_SUB_SCHEMA.name, domain=None, range=Optional[str])

slots.core_field = Slot(uri=NMDC_SUB_SCHEMA.core_field, name="core field", curie=NMDC_SUB_SCHEMA.curie('core_field'),
                   model_uri=NMDC_SUB_SCHEMA.core_field, domain=None, range=Optional[str])

slots.has_maximum_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_maximum_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.language = Slot(uri=NMDC_SUB_SCHEMA.language, name="language", curie=NMDC_SUB_SCHEMA.curie('language'),
                   model_uri=NMDC_SUB_SCHEMA.language, domain=None, range=Optional[str])

slots.ended_at_time = Slot(uri=NMDC_SUB_SCHEMA.ended_at_time, name="ended_at_time", curie=NMDC_SUB_SCHEMA.curie('ended_at_time'),
                   model_uri=NMDC_SUB_SCHEMA.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.endedAtTime])

slots.term = Slot(uri=NMDC_SUB_SCHEMA.term, name="term", curie=NMDC_SUB_SCHEMA.curie('term'),
                   model_uri=NMDC_SUB_SCHEMA.term, domain=NamedThing, range=Optional[Union[dict, OntologyClass]])

slots.alternative_identifiers = Slot(uri=NMDC_SUB_SCHEMA.alternative_identifiers, name="alternative_identifiers", curie=NMDC_SUB_SCHEMA.curie('alternative_identifiers'),
                   model_uri=NMDC_SUB_SCHEMA.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.has_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_numeric_value, name="has_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.acted_on_behalf_of = Slot(uri=NMDC_SUB_SCHEMA.acted_on_behalf_of, name="acted_on_behalf_of", curie=NMDC_SUB_SCHEMA.curie('acted_on_behalf_of'),
                   model_uri=NMDC_SUB_SCHEMA.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.has_minimum_numeric_value = Slot(uri=NMDC_SUB_SCHEMA.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=NMDC_SUB_SCHEMA.curie('has_minimum_numeric_value'),
                   model_uri=NMDC_SUB_SCHEMA.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.id = Slot(uri=NMDC_SUB_SCHEMA.id, name="id", curie=NMDC_SUB_SCHEMA.curie('id'),
                   model_uri=NMDC_SUB_SCHEMA.id, domain=None, range=URIRef)

slots.was_associated_with = Slot(uri=NMDC_SUB_SCHEMA.was_associated_with, name="was_associated_with", curie=NMDC_SUB_SCHEMA.curie('was_associated_with'),
                   model_uri=NMDC_SUB_SCHEMA.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.attribute = Slot(uri=NMDC_SUB_SCHEMA.attribute, name="attribute", curie=NMDC_SUB_SCHEMA.curie('attribute'),
                   model_uri=NMDC_SUB_SCHEMA.attribute, domain=None, range=Optional[str])

slots.was_informed_by = Slot(uri=NMDC_SUB_SCHEMA.was_informed_by, name="was_informed_by", curie=NMDC_SUB_SCHEMA.curie('was_informed_by'),
                   model_uri=NMDC_SUB_SCHEMA.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=NMDC_SUB_SCHEMA.longitude, domain=NamedThing, range=Optional[float], mappings = [SCHEMA.longitude])

slots.gold_path_field = Slot(uri=NMDC_SUB_SCHEMA.gold_path_field, name="gold_path_field", curie=NMDC_SUB_SCHEMA.curie('gold_path_field'),
                   model_uri=NMDC_SUB_SCHEMA.gold_path_field, domain=None, range=Optional[str])

slots.has_unit = Slot(uri=NMDC_SUB_SCHEMA.has_unit, name="has_unit", curie=NMDC_SUB_SCHEMA.curie('has_unit'),
                   model_uri=NMDC_SUB_SCHEMA.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=NMDC_SUB_SCHEMA.latitude, domain=NamedThing, range=Optional[float], mappings = [SCHEMA.latitude])

slots.used = Slot(uri=NMDC_SUB_SCHEMA.used, name="used", curie=NMDC_SUB_SCHEMA.curie('used'),
                   model_uri=NMDC_SUB_SCHEMA.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.environment_field = Slot(uri=NMDC_SUB_SCHEMA.environment_field, name="environment field", curie=NMDC_SUB_SCHEMA.curie('environment_field'),
                   model_uri=NMDC_SUB_SCHEMA.environment_field, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC_SUB_SCHEMA.description, domain=None, range=Optional[str])

slots.AirInterface_air_PM_concen = Slot(uri=MIXS['0000108'], name="AirInterface_air_PM_concen", curie=MIXS.curie('0000108'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_air_PM_concen, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_alt = Slot(uri=MIXS['0000094'], name="AirInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_alt, domain=AirInterface, range=Optional[str])

slots.AirInterface_barometric_press = Slot(uri=MIXS['0000096'], name="AirInterface_barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_barometric_press, domain=AirInterface, range=Optional[str])

slots.AirInterface_carb_dioxide = Slot(uri=MIXS['0000097'], name="AirInterface_carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_carb_dioxide, domain=AirInterface, range=Optional[str])

slots.AirInterface_carb_monoxide = Slot(uri=MIXS['0000098'], name="AirInterface_carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_carb_monoxide, domain=AirInterface, range=Optional[str])

slots.AirInterface_chem_administration = Slot(uri=MIXS['0000751'], name="AirInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_chem_administration, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_collection_date = Slot(uri=MIXS['0000011'], name="AirInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_collection_date, domain=AirInterface, range=str)

slots.AirInterface_depth = Slot(uri=MIXS['0000018'], name="AirInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_depth, domain=AirInterface, range=str)

slots.AirInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="AirInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ecosystem, domain=AirInterface, range=str)

slots.AirInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="AirInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ecosystem_category, domain=AirInterface, range=str)

slots.AirInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="AirInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ecosystem_subtype, domain=AirInterface, range=str)

slots.AirInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="AirInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ecosystem_type, domain=AirInterface, range=str)

slots.AirInterface_elev = Slot(uri=MIXS['0000093'], name="AirInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_elev, domain=AirInterface, range=float)

slots.AirInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="AirInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_env_broad_scale, domain=AirInterface, range=str)

slots.AirInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="AirInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_env_local_scale, domain=AirInterface, range=str)

slots.AirInterface_env_medium = Slot(uri=MIXS['0000014'], name="AirInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_env_medium, domain=AirInterface, range=str)

slots.AirInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="AirInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_experimental_factor, domain=AirInterface, range=Optional[str])

slots.AirInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="AirInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_geo_loc_name, domain=AirInterface, range=Optional[str])

slots.AirInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="AirInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_horizon_meth, domain=AirInterface, range=Optional[str])

slots.AirInterface_humidity = Slot(uri=MIXS['0000100'], name="AirInterface_humidity", curie=MIXS.curie('0000100'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_humidity, domain=AirInterface, range=Optional[str])

slots.AirInterface_lat_lon = Slot(uri=MIXS['0000009'], name="AirInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_lat_lon, domain=AirInterface, range=Optional[str])

slots.AirInterface_methane = Slot(uri=MIXS['0000101'], name="AirInterface_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_methane, domain=AirInterface, range=Optional[str])

slots.AirInterface_misc_param = Slot(uri=MIXS['0000752'], name="AirInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_misc_param, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_organism_count = Slot(uri=MIXS['0000103'], name="AirInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_organism_count, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="AirInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_oxy_stat_samp, domain=AirInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.AirInterface_oxygen = Slot(uri=MIXS['0000104'], name="AirInterface_oxygen", curie=MIXS.curie('0000104'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_oxygen, domain=AirInterface, range=Optional[str])

slots.AirInterface_perturbation = Slot(uri=MIXS['0000754'], name="AirInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_perturbation, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_pollutants = Slot(uri=MIXS['0000107'], name="AirInterface_pollutants", curie=MIXS.curie('0000107'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_pollutants, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="AirInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_rel_to_oxygen, domain=AirInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.AirInterface_salinity = Slot(uri=MIXS['0000183'], name="AirInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_salinity, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="AirInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_collec_device, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="AirInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_collec_method, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="AirInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_mat_process, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_size = Slot(uri=MIXS['0000001'], name="AirInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_size, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="AirInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_store_dur, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="AirInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_store_loc, domain=AirInterface, range=Optional[str])

slots.AirInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="AirInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_samp_store_temp, domain=AirInterface, range=str)

slots.AirInterface_size_frac = Slot(uri=MIXS['0000017'], name="AirInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_size_frac, domain=AirInterface, range=Optional[str])

slots.AirInterface_solar_irradiance = Slot(uri=MIXS['0000112'], name="AirInterface_solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_solar_irradiance, domain=AirInterface, range=Optional[str])

slots.AirInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="AirInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_specific_ecosystem, domain=AirInterface, range=str)

slots.AirInterface_temp = Slot(uri=MIXS['0000113'], name="AirInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_temp, domain=AirInterface, range=Optional[str])

slots.AirInterface_ventilation_rate = Slot(uri=MIXS['0000114'], name="AirInterface_ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ventilation_rate, domain=AirInterface, range=Optional[str])

slots.AirInterface_ventilation_type = Slot(uri=MIXS['0000756'], name="AirInterface_ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_ventilation_type, domain=AirInterface, range=Optional[str])

slots.AirInterface_volatile_org_comp = Slot(uri=MIXS['0000115'], name="AirInterface_volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_volatile_org_comp, domain=AirInterface, range=Optional[Union[str, List[str]]])

slots.AirInterface_wind_direction = Slot(uri=MIXS['0000757'], name="AirInterface_wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_wind_direction, domain=AirInterface, range=Optional[str])

slots.AirInterface_wind_speed = Slot(uri=MIXS['0000118'], name="AirInterface_wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=NMDC_SUB_SCHEMA.AirInterface_wind_speed, domain=AirInterface, range=Optional[str])

slots.BiofilmInterface_alkalinity = Slot(uri=MIXS['0000421'], name="BiofilmInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_alkalinity, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_alkyl_diethers = Slot(uri=MIXS['0000490'], name="BiofilmInterface_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_alkyl_diethers, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_alt = Slot(uri=MIXS['0000094'], name="BiofilmInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_alt, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_aminopept_act = Slot(uri=MIXS['0000172'], name="BiofilmInterface_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_aminopept_act, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_ammonium = Slot(uri=MIXS['0000427'], name="BiofilmInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ammonium, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="BiofilmInterface_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_bacteria_carb_prod, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_biomass = Slot(uri=MIXS['0000174'], name="BiofilmInterface_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_biomass, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_bishomohopanol = Slot(uri=MIXS['0000175'], name="BiofilmInterface_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_bishomohopanol, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_bromide = Slot(uri=MIXS['0000176'], name="BiofilmInterface_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_bromide, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_calcium = Slot(uri=MIXS['0000432'], name="BiofilmInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_calcium, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="BiofilmInterface_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_carb_nitro_ratio, domain=BiofilmInterface, range=Optional[float])

slots.BiofilmInterface_chem_administration = Slot(uri=MIXS['0000751'], name="BiofilmInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_chem_administration, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_chloride = Slot(uri=MIXS['0000429'], name="BiofilmInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_chloride, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_chlorophyll = Slot(uri=MIXS['0000177'], name="BiofilmInterface_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_chlorophyll, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_collection_date = Slot(uri=MIXS['0000011'], name="BiofilmInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_collection_date, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_depth = Slot(uri=MIXS['0000018'], name="BiofilmInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_depth, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_diether_lipids = Slot(uri=MIXS['0000178'], name="BiofilmInterface_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diether_lipids, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="BiofilmInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_carb_dioxide, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_diss_hydrogen = Slot(uri=MIXS['0000179'], name="BiofilmInterface_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_hydrogen, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="BiofilmInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_inorg_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_diss_org_carb = Slot(uri=MIXS['0000433'], name="BiofilmInterface_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_org_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_diss_org_nitro = Slot(uri=MIXS['0000162'], name="BiofilmInterface_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_org_nitro, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_diss_oxygen = Slot(uri=MIXS['0000119'], name="BiofilmInterface_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_diss_oxygen, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="BiofilmInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ecosystem, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="BiofilmInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ecosystem_category, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="BiofilmInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ecosystem_subtype, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="BiofilmInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ecosystem_type, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_elev = Slot(uri=MIXS['0000093'], name="BiofilmInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_elev, domain=BiofilmInterface, range=float)

slots.BiofilmInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="BiofilmInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_env_broad_scale, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="BiofilmInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_env_local_scale, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_env_medium = Slot(uri=MIXS['0000014'], name="BiofilmInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_env_medium, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="BiofilmInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_experimental_factor, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="BiofilmInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_geo_loc_name, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_glucosidase_act = Slot(uri=MIXS['0000137'], name="BiofilmInterface_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_glucosidase_act, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="BiofilmInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_horizon_meth, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_lat_lon = Slot(uri=MIXS['0000009'], name="BiofilmInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_lat_lon, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_magnesium = Slot(uri=MIXS['0000431'], name="BiofilmInterface_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_magnesium, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_mean_frict_vel = Slot(uri=MIXS['0000498'], name="BiofilmInterface_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_mean_frict_vel, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="BiofilmInterface_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_mean_peak_frict_vel, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_methane = Slot(uri=MIXS['0000101'], name="BiofilmInterface_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_methane, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_misc_param = Slot(uri=MIXS['0000752'], name="BiofilmInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_misc_param, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_n_alkanes = Slot(uri=MIXS['0000503'], name="BiofilmInterface_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_n_alkanes, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_nitrate = Slot(uri=MIXS['0000425'], name="BiofilmInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_nitrate, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_nitrite = Slot(uri=MIXS['0000426'], name="BiofilmInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_nitrite, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_nitro = Slot(uri=MIXS['0000504'], name="BiofilmInterface_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_nitro, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_org_carb = Slot(uri=MIXS['0000508'], name="BiofilmInterface_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_org_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_org_matter = Slot(uri=MIXS['0000204'], name="BiofilmInterface_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_org_matter, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_org_nitro = Slot(uri=MIXS['0000205'], name="BiofilmInterface_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_org_nitro, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_organism_count = Slot(uri=MIXS['0000103'], name="BiofilmInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_organism_count, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="BiofilmInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_oxy_stat_samp, domain=BiofilmInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.BiofilmInterface_part_org_carb = Slot(uri=MIXS['0000515'], name="BiofilmInterface_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_part_org_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_perturbation = Slot(uri=MIXS['0000754'], name="BiofilmInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_perturbation, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="BiofilmInterface_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_petroleum_hydrocarb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_ph = Slot(uri=MIXS['0001001'], name="BiofilmInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ph, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_ph_meth = Slot(uri=MIXS['0001106'], name="BiofilmInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_ph_meth, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_phaeopigments = Slot(uri=MIXS['0000180'], name="BiofilmInterface_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_phaeopigments, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_phosphate = Slot(uri=MIXS['0000505'], name="BiofilmInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_phosphate, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="BiofilmInterface_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_phosplipid_fatt_acid, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BiofilmInterface_potassium = Slot(uri=MIXS['0000430'], name="BiofilmInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_potassium, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_pressure = Slot(uri=MIXS['0000412'], name="BiofilmInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_pressure, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_redox_potential = Slot(uri=MIXS['0000182'], name="BiofilmInterface_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_redox_potential, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="BiofilmInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_rel_to_oxygen, domain=BiofilmInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.BiofilmInterface_salinity = Slot(uri=MIXS['0000183'], name="BiofilmInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_salinity, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="BiofilmInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_collec_device, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="BiofilmInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_collec_method, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="BiofilmInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_mat_process, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_size = Slot(uri=MIXS['0000001'], name="BiofilmInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_size, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="BiofilmInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_store_dur, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="BiofilmInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_store_loc, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="BiofilmInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_samp_store_temp, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_silicate = Slot(uri=MIXS['0000184'], name="BiofilmInterface_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_silicate, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_size_frac = Slot(uri=MIXS['0000017'], name="BiofilmInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_size_frac, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_sodium = Slot(uri=MIXS['0000428'], name="BiofilmInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_sodium, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="BiofilmInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_specific_ecosystem, domain=BiofilmInterface, range=str)

slots.BiofilmInterface_sulfate = Slot(uri=MIXS['0000423'], name="BiofilmInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_sulfate, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_sulfide = Slot(uri=MIXS['0000424'], name="BiofilmInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_sulfide, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_temp = Slot(uri=MIXS['0000113'], name="BiofilmInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_temp, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_tot_carb = Slot(uri=MIXS['0000525'], name="BiofilmInterface_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_tot_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_tot_nitro_content = Slot(uri=MIXS['0000530'], name="BiofilmInterface_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_tot_nitro_content, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_tot_org_carb = Slot(uri=MIXS['0000533'], name="BiofilmInterface_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_tot_org_carb, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_turbidity = Slot(uri=MIXS['0000191'], name="BiofilmInterface_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_turbidity, domain=BiofilmInterface, range=Optional[str])

slots.BiofilmInterface_water_content = Slot(uri=MIXS['0000185'], name="BiofilmInterface_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.BiofilmInterface_water_content, domain=BiofilmInterface, range=Optional[Union[str, List[str]]])

slots.BuiltEnvInterface_abs_air_humidity = Slot(uri=MIXS['0000122'], name="BuiltEnvInterface_abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_abs_air_humidity, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_address = Slot(uri=MIXS['0000218'], name="BuiltEnvInterface_address", curie=MIXS.curie('0000218'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_address, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_adj_room = Slot(uri=MIXS['0000219'], name="BuiltEnvInterface_adj_room", curie=MIXS.curie('0000219'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_adj_room, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_aero_struc = Slot(uri=MIXS['0000773'], name="BuiltEnvInterface_aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_aero_struc, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_air_temp = Slot(uri=MIXS['0000124'], name="BuiltEnvInterface_air_temp", curie=MIXS.curie('0000124'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_air_temp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_alt = Slot(uri=MIXS['0000094'], name="BuiltEnvInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_alt, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_amount_light = Slot(uri=MIXS['0000140'], name="BuiltEnvInterface_amount_light", curie=MIXS.curie('0000140'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_amount_light, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_arch_struc = Slot(uri=MIXS['0000774'], name="BuiltEnvInterface_arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_arch_struc, domain=BuiltEnvInterface, range=Optional[Union[str, "ArchStrucEnum"]])

slots.BuiltEnvInterface_avg_dew_point = Slot(uri=MIXS['0000141'], name="BuiltEnvInterface_avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_avg_dew_point, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_avg_occup = Slot(uri=MIXS['0000775'], name="BuiltEnvInterface_avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_avg_occup, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_avg_temp = Slot(uri=MIXS['0000142'], name="BuiltEnvInterface_avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_avg_temp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_bathroom_count = Slot(uri=MIXS['0000776'], name="BuiltEnvInterface_bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_bathroom_count, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_bedroom_count = Slot(uri=MIXS['0000777'], name="BuiltEnvInterface_bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_bedroom_count, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_build_docs = Slot(uri=MIXS['0000787'], name="BuiltEnvInterface_build_docs", curie=MIXS.curie('0000787'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_build_docs, domain=BuiltEnvInterface, range=Optional[Union[str, "BuildDocsEnum"]])

slots.BuiltEnvInterface_build_occup_type = Slot(uri=MIXS['0000761'], name="BuiltEnvInterface_build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_build_occup_type, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]])

slots.BuiltEnvInterface_building_setting = Slot(uri=MIXS['0000768'], name="BuiltEnvInterface_building_setting", curie=MIXS.curie('0000768'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_building_setting, domain=BuiltEnvInterface, range=Optional[Union[str, "BuildingSettingEnum"]])

slots.BuiltEnvInterface_built_struc_age = Slot(uri=MIXS['0000145'], name="BuiltEnvInterface_built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_built_struc_age, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_built_struc_set = Slot(uri=MIXS['0000778'], name="BuiltEnvInterface_built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_built_struc_set, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_built_struc_type = Slot(uri=MIXS['0000721'], name="BuiltEnvInterface_built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_built_struc_type, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_carb_dioxide = Slot(uri=MIXS['0000097'], name="BuiltEnvInterface_carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_carb_dioxide, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ceil_area = Slot(uri=MIXS['0000148'], name="BuiltEnvInterface_ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_area, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ceil_cond = Slot(uri=MIXS['0000779'], name="BuiltEnvInterface_ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "CeilCondEnum"]])

slots.BuiltEnvInterface_ceil_finish_mat = Slot(uri=MIXS['0000780'], name="BuiltEnvInterface_ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_finish_mat, domain=BuiltEnvInterface, range=Optional[Union[str, "CeilFinishMatEnum"]])

slots.BuiltEnvInterface_ceil_struc = Slot(uri=MIXS['0000782'], name="BuiltEnvInterface_ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_struc, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ceil_texture = Slot(uri=MIXS['0000783'], name="BuiltEnvInterface_ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_texture, domain=BuiltEnvInterface, range=Optional[Union[str, "CeilTextureEnum"]])

slots.BuiltEnvInterface_ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="BuiltEnvInterface_ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_thermal_mass, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ceil_type = Slot(uri=MIXS['0000784'], name="BuiltEnvInterface_ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_type, domain=BuiltEnvInterface, range=Optional[Union[str, "CeilTypeEnum"]])

slots.BuiltEnvInterface_ceil_water_mold = Slot(uri=MIXS['0000781'], name="BuiltEnvInterface_ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ceil_water_mold, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_collection_date = Slot(uri=MIXS['0000011'], name="BuiltEnvInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_collection_date, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_cool_syst_id = Slot(uri=MIXS['0000785'], name="BuiltEnvInterface_cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_cool_syst_id, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_date_last_rain = Slot(uri=MIXS['0000786'], name="BuiltEnvInterface_date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_date_last_rain, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_depth = Slot(uri=MIXS['0000018'], name="BuiltEnvInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_depth, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_dew_point = Slot(uri=MIXS['0000129'], name="BuiltEnvInterface_dew_point", curie=MIXS.curie('0000129'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_dew_point, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_door_comp_type = Slot(uri=MIXS['0000795'], name="BuiltEnvInterface_door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_comp_type, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorCompTypeEnum"]])

slots.BuiltEnvInterface_door_cond = Slot(uri=MIXS['0000788'], name="BuiltEnvInterface_door_cond", curie=MIXS.curie('0000788'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorCondEnum"]])

slots.BuiltEnvInterface_door_direct = Slot(uri=MIXS['0000789'], name="BuiltEnvInterface_door_direct", curie=MIXS.curie('0000789'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_direct, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorDirectEnum"]])

slots.BuiltEnvInterface_door_loc = Slot(uri=MIXS['0000790'], name="BuiltEnvInterface_door_loc", curie=MIXS.curie('0000790'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorLocEnum"]])

slots.BuiltEnvInterface_door_mat = Slot(uri=MIXS['0000791'], name="BuiltEnvInterface_door_mat", curie=MIXS.curie('0000791'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_mat, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorMatEnum"]])

slots.BuiltEnvInterface_door_move = Slot(uri=MIXS['0000792'], name="BuiltEnvInterface_door_move", curie=MIXS.curie('0000792'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_move, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorMoveEnum"]])

slots.BuiltEnvInterface_door_size = Slot(uri=MIXS['0000158'], name="BuiltEnvInterface_door_size", curie=MIXS.curie('0000158'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_size, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_door_type = Slot(uri=MIXS['0000794'], name="BuiltEnvInterface_door_type", curie=MIXS.curie('0000794'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_type, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorTypeEnum"]])

slots.BuiltEnvInterface_door_type_metal = Slot(uri=MIXS['0000796'], name="BuiltEnvInterface_door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_type_metal, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorTypeMetalEnum"]])

slots.BuiltEnvInterface_door_type_wood = Slot(uri=MIXS['0000797'], name="BuiltEnvInterface_door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_type_wood, domain=BuiltEnvInterface, range=Optional[Union[str, "DoorTypeWoodEnum"]])

slots.BuiltEnvInterface_door_water_mold = Slot(uri=MIXS['0000793'], name="BuiltEnvInterface_door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_door_water_mold, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_drawings = Slot(uri=MIXS['0000798'], name="BuiltEnvInterface_drawings", curie=MIXS.curie('0000798'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_drawings, domain=BuiltEnvInterface, range=Optional[Union[str, "DrawingsEnum"]])

slots.BuiltEnvInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="BuiltEnvInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ecosystem, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="BuiltEnvInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ecosystem_category, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="BuiltEnvInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ecosystem_subtype, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="BuiltEnvInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ecosystem_type, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_elev = Slot(uri=MIXS['0000093'], name="BuiltEnvInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_elev, domain=BuiltEnvInterface, range=float)

slots.BuiltEnvInterface_elevator = Slot(uri=MIXS['0000799'], name="BuiltEnvInterface_elevator", curie=MIXS.curie('0000799'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_elevator, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="BuiltEnvInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_env_broad_scale, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="BuiltEnvInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_env_local_scale, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_env_medium = Slot(uri=MIXS['0000014'], name="BuiltEnvInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_env_medium, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_escalator = Slot(uri=MIXS['0000800'], name="BuiltEnvInterface_escalator", curie=MIXS.curie('0000800'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_escalator, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_exp_duct = Slot(uri=MIXS['0000144'], name="BuiltEnvInterface_exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_exp_duct, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_exp_pipe = Slot(uri=MIXS['0000220'], name="BuiltEnvInterface_exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_exp_pipe, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="BuiltEnvInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_experimental_factor, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ext_door = Slot(uri=MIXS['0000170'], name="BuiltEnvInterface_ext_door", curie=MIXS.curie('0000170'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ext_door, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_ext_wall_orient = Slot(uri=MIXS['0000817'], name="BuiltEnvInterface_ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ext_wall_orient, domain=BuiltEnvInterface, range=Optional[Union[str, "ExtWallOrientEnum"]])

slots.BuiltEnvInterface_ext_window_orient = Slot(uri=MIXS['0000818'], name="BuiltEnvInterface_ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ext_window_orient, domain=BuiltEnvInterface, range=Optional[Union[str, "ExtWindowOrientEnum"]])

slots.BuiltEnvInterface_filter_type = Slot(uri=MIXS['0000765'], name="BuiltEnvInterface_filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_filter_type, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]])

slots.BuiltEnvInterface_fireplace_type = Slot(uri=MIXS['0000802'], name="BuiltEnvInterface_fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_fireplace_type, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_floor_age = Slot(uri=MIXS['0000164'], name="BuiltEnvInterface_floor_age", curie=MIXS.curie('0000164'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_age, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_floor_area = Slot(uri=MIXS['0000165'], name="BuiltEnvInterface_floor_area", curie=MIXS.curie('0000165'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_area, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_floor_cond = Slot(uri=MIXS['0000803'], name="BuiltEnvInterface_floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "FloorCondEnum"]])

slots.BuiltEnvInterface_floor_count = Slot(uri=MIXS['0000225'], name="BuiltEnvInterface_floor_count", curie=MIXS.curie('0000225'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_count, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_floor_finish_mat = Slot(uri=MIXS['0000804'], name="BuiltEnvInterface_floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_finish_mat, domain=BuiltEnvInterface, range=Optional[Union[str, "FloorFinishMatEnum"]])

slots.BuiltEnvInterface_floor_struc = Slot(uri=MIXS['0000806'], name="BuiltEnvInterface_floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_struc, domain=BuiltEnvInterface, range=Optional[Union[str, "FloorStrucEnum"]])

slots.BuiltEnvInterface_floor_thermal_mass = Slot(uri=MIXS['0000166'], name="BuiltEnvInterface_floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_thermal_mass, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_floor_water_mold = Slot(uri=MIXS['0000805'], name="BuiltEnvInterface_floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_floor_water_mold, domain=BuiltEnvInterface, range=Optional[Union[str, "FloorWaterMoldEnum"]])

slots.BuiltEnvInterface_freq_clean = Slot(uri=MIXS['0000226'], name="BuiltEnvInterface_freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_freq_clean, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_freq_cook = Slot(uri=MIXS['0000227'], name="BuiltEnvInterface_freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_freq_cook, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_furniture = Slot(uri=MIXS['0000807'], name="BuiltEnvInterface_furniture", curie=MIXS.curie('0000807'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_furniture, domain=BuiltEnvInterface, range=Optional[Union[str, "FurnitureEnum"]])

slots.BuiltEnvInterface_gender_restroom = Slot(uri=MIXS['0000808'], name="BuiltEnvInterface_gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_gender_restroom, domain=BuiltEnvInterface, range=Optional[Union[str, "GenderRestroomEnum"]])

slots.BuiltEnvInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="BuiltEnvInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_geo_loc_name, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_hall_count = Slot(uri=MIXS['0000228'], name="BuiltEnvInterface_hall_count", curie=MIXS.curie('0000228'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_hall_count, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_handidness = Slot(uri=MIXS['0000809'], name="BuiltEnvInterface_handidness", curie=MIXS.curie('0000809'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_handidness, domain=BuiltEnvInterface, range=Optional[Union[str, "HandidnessEnum"]])

slots.BuiltEnvInterface_heat_cool_type = Slot(uri=MIXS['0000766'], name="BuiltEnvInterface_heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_heat_cool_type, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]])

slots.BuiltEnvInterface_heat_deliv_loc = Slot(uri=MIXS['0000810'], name="BuiltEnvInterface_heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_heat_deliv_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "HeatDelivLocEnum"]])

slots.BuiltEnvInterface_heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="BuiltEnvInterface_heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_heat_sys_deliv_meth, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_heat_system_id = Slot(uri=MIXS['0000833'], name="BuiltEnvInterface_heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_heat_system_id, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_height_carper_fiber = Slot(uri=MIXS['0000167'], name="BuiltEnvInterface_height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_height_carper_fiber, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="BuiltEnvInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_horizon_meth, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_indoor_space = Slot(uri=MIXS['0000763'], name="BuiltEnvInterface_indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_indoor_space, domain=BuiltEnvInterface, range=Optional[Union[str, "IndoorSpaceEnum"]])

slots.BuiltEnvInterface_indoor_surf = Slot(uri=MIXS['0000764'], name="BuiltEnvInterface_indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_indoor_surf, domain=BuiltEnvInterface, range=Optional[Union[str, "IndoorSurfEnum"]])

slots.BuiltEnvInterface_inside_lux = Slot(uri=MIXS['0000168'], name="BuiltEnvInterface_inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_inside_lux, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_int_wall_cond = Slot(uri=MIXS['0000813'], name="BuiltEnvInterface_int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_int_wall_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "IntWallCondEnum"]])

slots.BuiltEnvInterface_last_clean = Slot(uri=MIXS['0000814'], name="BuiltEnvInterface_last_clean", curie=MIXS.curie('0000814'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_last_clean, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_lat_lon = Slot(uri=MIXS['0000009'], name="BuiltEnvInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_lat_lon, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_light_type = Slot(uri=MIXS['0000769'], name="BuiltEnvInterface_light_type", curie=MIXS.curie('0000769'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_light_type, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]])

slots.BuiltEnvInterface_max_occup = Slot(uri=MIXS['0000229'], name="BuiltEnvInterface_max_occup", curie=MIXS.curie('0000229'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_max_occup, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_mech_struc = Slot(uri=MIXS['0000815'], name="BuiltEnvInterface_mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_mech_struc, domain=BuiltEnvInterface, range=Optional[Union[str, "MechStrucEnum"]])

slots.BuiltEnvInterface_number_pets = Slot(uri=MIXS['0000231'], name="BuiltEnvInterface_number_pets", curie=MIXS.curie('0000231'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_number_pets, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_number_plants = Slot(uri=MIXS['0000230'], name="BuiltEnvInterface_number_plants", curie=MIXS.curie('0000230'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_number_plants, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_number_resident = Slot(uri=MIXS['0000232'], name="BuiltEnvInterface_number_resident", curie=MIXS.curie('0000232'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_number_resident, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_occup_density_samp = Slot(uri=MIXS['0000217'], name="BuiltEnvInterface_occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_occup_density_samp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_occup_document = Slot(uri=MIXS['0000816'], name="BuiltEnvInterface_occup_document", curie=MIXS.curie('0000816'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_occup_document, domain=BuiltEnvInterface, range=Optional[Union[str, "OccupDocumentEnum"]])

slots.BuiltEnvInterface_occup_samp = Slot(uri=MIXS['0000772'], name="BuiltEnvInterface_occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_occup_samp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_organism_count = Slot(uri=MIXS['0000103'], name="BuiltEnvInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_organism_count, domain=BuiltEnvInterface, range=Optional[Union[str, List[str]]])

slots.BuiltEnvInterface_pres_animal_insect = Slot(uri=MIXS['0000819'], name="BuiltEnvInterface_pres_animal_insect", curie=MIXS.curie('0000819'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_pres_animal_insect, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_quad_pos = Slot(uri=MIXS['0000820'], name="BuiltEnvInterface_quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_quad_pos, domain=BuiltEnvInterface, range=Optional[Union[str, "QuadPosEnum"]])

slots.BuiltEnvInterface_rel_air_humidity = Slot(uri=MIXS['0000121'], name="BuiltEnvInterface_rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_rel_air_humidity, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_rel_humidity_out = Slot(uri=MIXS['0000188'], name="BuiltEnvInterface_rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_rel_humidity_out, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_rel_samp_loc = Slot(uri=MIXS['0000821'], name="BuiltEnvInterface_rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_rel_samp_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "RelSampLocEnum"]])

slots.BuiltEnvInterface_room_air_exch_rate = Slot(uri=MIXS['0000169'], name="BuiltEnvInterface_room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_air_exch_rate, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_architec_elem = Slot(uri=MIXS['0000233'], name="BuiltEnvInterface_room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_architec_elem, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_condt = Slot(uri=MIXS['0000822'], name="BuiltEnvInterface_room_condt", curie=MIXS.curie('0000822'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_condt, domain=BuiltEnvInterface, range=Optional[Union[str, "RoomCondtEnum"]])

slots.BuiltEnvInterface_room_connected = Slot(uri=MIXS['0000826'], name="BuiltEnvInterface_room_connected", curie=MIXS.curie('0000826'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_connected, domain=BuiltEnvInterface, range=Optional[Union[str, "RoomConnectedEnum"]])

slots.BuiltEnvInterface_room_count = Slot(uri=MIXS['0000234'], name="BuiltEnvInterface_room_count", curie=MIXS.curie('0000234'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_count, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_dim = Slot(uri=MIXS['0000192'], name="BuiltEnvInterface_room_dim", curie=MIXS.curie('0000192'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_dim, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_door_dist = Slot(uri=MIXS['0000193'], name="BuiltEnvInterface_room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_door_dist, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_door_share = Slot(uri=MIXS['0000242'], name="BuiltEnvInterface_room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_door_share, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_hallway = Slot(uri=MIXS['0000238'], name="BuiltEnvInterface_room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_hallway, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_loc = Slot(uri=MIXS['0000823'], name="BuiltEnvInterface_room_loc", curie=MIXS.curie('0000823'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "RoomLocEnum"]])

slots.BuiltEnvInterface_room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="BuiltEnvInterface_room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_moist_dam_hist, domain=BuiltEnvInterface, range=Optional[int])

slots.BuiltEnvInterface_room_net_area = Slot(uri=MIXS['0000194'], name="BuiltEnvInterface_room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_net_area, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_occup = Slot(uri=MIXS['0000236'], name="BuiltEnvInterface_room_occup", curie=MIXS.curie('0000236'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_occup, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_samp_pos = Slot(uri=MIXS['0000824'], name="BuiltEnvInterface_room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_samp_pos, domain=BuiltEnvInterface, range=Optional[Union[str, "RoomSampPosEnum"]])

slots.BuiltEnvInterface_room_type = Slot(uri=MIXS['0000825'], name="BuiltEnvInterface_room_type", curie=MIXS.curie('0000825'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_type, domain=BuiltEnvInterface, range=Optional[Union[str, "RoomTypeEnum"]])

slots.BuiltEnvInterface_room_vol = Slot(uri=MIXS['0000195'], name="BuiltEnvInterface_room_vol", curie=MIXS.curie('0000195'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_vol, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_wall_share = Slot(uri=MIXS['0000243'], name="BuiltEnvInterface_room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_wall_share, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_room_window_count = Slot(uri=MIXS['0000237'], name="BuiltEnvInterface_room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_room_window_count, domain=BuiltEnvInterface, range=Optional[int])

slots.BuiltEnvInterface_samp_floor = Slot(uri=MIXS['0000828'], name="BuiltEnvInterface_samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_samp_floor, domain=BuiltEnvInterface, range=Optional[Union[str, "SampFloorEnum"]])

slots.BuiltEnvInterface_samp_room_id = Slot(uri=MIXS['0000244'], name="BuiltEnvInterface_samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_samp_room_id, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_samp_sort_meth = Slot(uri=MIXS['0000216'], name="BuiltEnvInterface_samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_samp_sort_meth, domain=BuiltEnvInterface, range=Optional[Union[str, List[str]]])

slots.BuiltEnvInterface_samp_time_out = Slot(uri=MIXS['0000196'], name="BuiltEnvInterface_samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_samp_time_out, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_samp_weather = Slot(uri=MIXS['0000827'], name="BuiltEnvInterface_samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_samp_weather, domain=BuiltEnvInterface, range=Optional[Union[str, "SampWeatherEnum"]])

slots.BuiltEnvInterface_season = Slot(uri=MIXS['0000829'], name="BuiltEnvInterface_season", curie=MIXS.curie('0000829'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_season, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_season_use = Slot(uri=MIXS['0000830'], name="BuiltEnvInterface_season_use", curie=MIXS.curie('0000830'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_season_use, domain=BuiltEnvInterface, range=Optional[Union[str, "SeasonUseEnum"]])

slots.BuiltEnvInterface_shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="BuiltEnvInterface_shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_shad_dev_water_mold, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_shading_device_cond = Slot(uri=MIXS['0000831'], name="BuiltEnvInterface_shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_shading_device_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "ShadingDeviceCondEnum"]])

slots.BuiltEnvInterface_shading_device_loc = Slot(uri=MIXS['0000832'], name="BuiltEnvInterface_shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_shading_device_loc, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_shading_device_mat = Slot(uri=MIXS['0000245'], name="BuiltEnvInterface_shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_shading_device_mat, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_shading_device_type = Slot(uri=MIXS['0000835'], name="BuiltEnvInterface_shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_shading_device_type, domain=BuiltEnvInterface, range=Optional[Union[str, "ShadingDeviceTypeEnum"]])

slots.BuiltEnvInterface_size_frac = Slot(uri=MIXS['0000017'], name="BuiltEnvInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_size_frac, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_space_typ_state = Slot(uri=MIXS['0000770'], name="BuiltEnvInterface_space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_space_typ_state, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_specific = Slot(uri=MIXS['0000836'], name="BuiltEnvInterface_specific", curie=MIXS.curie('0000836'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_specific, domain=BuiltEnvInterface, range=Optional[Union[str, "SpecificEnum"]])

slots.BuiltEnvInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="BuiltEnvInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_specific_ecosystem, domain=BuiltEnvInterface, range=str)

slots.BuiltEnvInterface_specific_humidity = Slot(uri=MIXS['0000214'], name="BuiltEnvInterface_specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_specific_humidity, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_substructure_type = Slot(uri=MIXS['0000767'], name="BuiltEnvInterface_substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_substructure_type, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]])

slots.BuiltEnvInterface_surf_air_cont = Slot(uri=MIXS['0000759'], name="BuiltEnvInterface_surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_air_cont, domain=BuiltEnvInterface, range=Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]])

slots.BuiltEnvInterface_surf_humidity = Slot(uri=MIXS['0000123'], name="BuiltEnvInterface_surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_humidity, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_surf_material = Slot(uri=MIXS['0000758'], name="BuiltEnvInterface_surf_material", curie=MIXS.curie('0000758'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_material, domain=BuiltEnvInterface, range=Optional[Union[str, "SurfMaterialEnum"]])

slots.BuiltEnvInterface_surf_moisture = Slot(uri=MIXS['0000128'], name="BuiltEnvInterface_surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_moisture, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_surf_moisture_ph = Slot(uri=MIXS['0000760'], name="BuiltEnvInterface_surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_moisture_ph, domain=BuiltEnvInterface, range=Optional[float])

slots.BuiltEnvInterface_surf_temp = Slot(uri=MIXS['0000125'], name="BuiltEnvInterface_surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_surf_temp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_temp = Slot(uri=MIXS['0000113'], name="BuiltEnvInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_temp, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_temp_out = Slot(uri=MIXS['0000197'], name="BuiltEnvInterface_temp_out", curie=MIXS.curie('0000197'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_temp_out, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_train_line = Slot(uri=MIXS['0000837'], name="BuiltEnvInterface_train_line", curie=MIXS.curie('0000837'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_train_line, domain=BuiltEnvInterface, range=Optional[Union[str, "TrainLineEnum"]])

slots.BuiltEnvInterface_train_stat_loc = Slot(uri=MIXS['0000838'], name="BuiltEnvInterface_train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_train_stat_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "TrainStatLocEnum"]])

slots.BuiltEnvInterface_train_stop_loc = Slot(uri=MIXS['0000839'], name="BuiltEnvInterface_train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_train_stop_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "TrainStopLocEnum"]])

slots.BuiltEnvInterface_typ_occup_density = Slot(uri=MIXS['0000771'], name="BuiltEnvInterface_typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_typ_occup_density, domain=BuiltEnvInterface, range=Optional[float])

slots.BuiltEnvInterface_ventilation_type = Slot(uri=MIXS['0000756'], name="BuiltEnvInterface_ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_ventilation_type, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_vis_media = Slot(uri=MIXS['0000840'], name="BuiltEnvInterface_vis_media", curie=MIXS.curie('0000840'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_vis_media, domain=BuiltEnvInterface, range=Optional[Union[str, "VisMediaEnum"]])

slots.BuiltEnvInterface_wall_area = Slot(uri=MIXS['0000198'], name="BuiltEnvInterface_wall_area", curie=MIXS.curie('0000198'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_area, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_wall_const_type = Slot(uri=MIXS['0000841'], name="BuiltEnvInterface_wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_const_type, domain=BuiltEnvInterface, range=Optional[Union[str, "WallConstTypeEnum"]])

slots.BuiltEnvInterface_wall_finish_mat = Slot(uri=MIXS['0000842'], name="BuiltEnvInterface_wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_finish_mat, domain=BuiltEnvInterface, range=Optional[Union[str, "WallFinishMatEnum"]])

slots.BuiltEnvInterface_wall_height = Slot(uri=MIXS['0000221'], name="BuiltEnvInterface_wall_height", curie=MIXS.curie('0000221'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_height, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_wall_loc = Slot(uri=MIXS['0000843'], name="BuiltEnvInterface_wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "WallLocEnum"]])

slots.BuiltEnvInterface_wall_surf_treatment = Slot(uri=MIXS['0000845'], name="BuiltEnvInterface_wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_surf_treatment, domain=BuiltEnvInterface, range=Optional[Union[str, "WallSurfTreatmentEnum"]])

slots.BuiltEnvInterface_wall_texture = Slot(uri=MIXS['0000846'], name="BuiltEnvInterface_wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_texture, domain=BuiltEnvInterface, range=Optional[Union[str, "WallTextureEnum"]])

slots.BuiltEnvInterface_wall_thermal_mass = Slot(uri=MIXS['0000222'], name="BuiltEnvInterface_wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_thermal_mass, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_wall_water_mold = Slot(uri=MIXS['0000844'], name="BuiltEnvInterface_wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_wall_water_mold, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_water_feat_size = Slot(uri=MIXS['0000223'], name="BuiltEnvInterface_water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_water_feat_size, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_water_feat_type = Slot(uri=MIXS['0000847'], name="BuiltEnvInterface_water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_water_feat_type, domain=BuiltEnvInterface, range=Optional[Union[str, "WaterFeatTypeEnum"]])

slots.BuiltEnvInterface_weekday = Slot(uri=MIXS['0000848'], name="BuiltEnvInterface_weekday", curie=MIXS.curie('0000848'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_weekday, domain=BuiltEnvInterface, range=Optional[Union[str, "WeekdayEnum"]])

slots.BuiltEnvInterface_window_cond = Slot(uri=MIXS['0000849'], name="BuiltEnvInterface_window_cond", curie=MIXS.curie('0000849'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_cond, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowCondEnum"]])

slots.BuiltEnvInterface_window_cover = Slot(uri=MIXS['0000850'], name="BuiltEnvInterface_window_cover", curie=MIXS.curie('0000850'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_cover, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowCoverEnum"]])

slots.BuiltEnvInterface_window_horiz_pos = Slot(uri=MIXS['0000851'], name="BuiltEnvInterface_window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_horiz_pos, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowHorizPosEnum"]])

slots.BuiltEnvInterface_window_loc = Slot(uri=MIXS['0000852'], name="BuiltEnvInterface_window_loc", curie=MIXS.curie('0000852'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_loc, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowLocEnum"]])

slots.BuiltEnvInterface_window_mat = Slot(uri=MIXS['0000853'], name="BuiltEnvInterface_window_mat", curie=MIXS.curie('0000853'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_mat, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowMatEnum"]])

slots.BuiltEnvInterface_window_open_freq = Slot(uri=MIXS['0000246'], name="BuiltEnvInterface_window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_open_freq, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_window_size = Slot(uri=MIXS['0000224'], name="BuiltEnvInterface_window_size", curie=MIXS.curie('0000224'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_size, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_window_status = Slot(uri=MIXS['0000855'], name="BuiltEnvInterface_window_status", curie=MIXS.curie('0000855'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_status, domain=BuiltEnvInterface, range=Optional[str])

slots.BuiltEnvInterface_window_type = Slot(uri=MIXS['0000856'], name="BuiltEnvInterface_window_type", curie=MIXS.curie('0000856'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_type, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowTypeEnum"]])

slots.BuiltEnvInterface_window_vert_pos = Slot(uri=MIXS['0000857'], name="BuiltEnvInterface_window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_vert_pos, domain=BuiltEnvInterface, range=Optional[Union[str, "WindowVertPosEnum"]])

slots.BuiltEnvInterface_window_water_mold = Slot(uri=MIXS['0000854'], name="BuiltEnvInterface_window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=NMDC_SUB_SCHEMA.BuiltEnvInterface_window_water_mold, domain=BuiltEnvInterface, range=Optional[str])

slots.HcrCoresInterface_additional_info = Slot(uri=MIXS['0000300'], name="HcrCoresInterface_additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_additional_info, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_alkalinity = Slot(uri=MIXS['0000421'], name="HcrCoresInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_alkalinity, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_alkalinity_method = Slot(uri=MIXS['0000298'], name="HcrCoresInterface_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_alkalinity_method, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_alt = Slot(uri=MIXS['0000094'], name="HcrCoresInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_alt, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_ammonium = Slot(uri=MIXS['0000427'], name="HcrCoresInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ammonium, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_api = Slot(uri=MIXS['0000157'], name="HcrCoresInterface_api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_api, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_aromatics_pc = Slot(uri=MIXS['0000133'], name="HcrCoresInterface_aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_aromatics_pc, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_asphaltenes_pc = Slot(uri=MIXS['0000135'], name="HcrCoresInterface_asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_asphaltenes_pc, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_basin = Slot(uri=MIXS['0000290'], name="HcrCoresInterface_basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_basin, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_benzene = Slot(uri=MIXS['0000153'], name="HcrCoresInterface_benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_benzene, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_calcium = Slot(uri=MIXS['0000432'], name="HcrCoresInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_calcium, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_chem_administration = Slot(uri=MIXS['0000751'], name="HcrCoresInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_chem_administration, domain=HcrCoresInterface, range=Optional[Union[str, List[str]]])

slots.HcrCoresInterface_chloride = Slot(uri=MIXS['0000429'], name="HcrCoresInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_chloride, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_collection_date = Slot(uri=MIXS['0000011'], name="HcrCoresInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_collection_date, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_density = Slot(uri=MIXS['0000435'], name="HcrCoresInterface_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_density, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_depos_env = Slot(uri=MIXS['0000992'], name="HcrCoresInterface_depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_depos_env, domain=HcrCoresInterface, range=Optional[Union[str, "DeposEnvEnum"]])

slots.HcrCoresInterface_depth = Slot(uri=MIXS['0000018'], name="HcrCoresInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_depth, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="HcrCoresInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_carb_dioxide, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="HcrCoresInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_inorg_carb, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="HcrCoresInterface_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_inorg_phosp, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_diss_iron = Slot(uri=MIXS['0000139'], name="HcrCoresInterface_diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_iron, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_diss_org_carb = Slot(uri=MIXS['0000433'], name="HcrCoresInterface_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_org_carb, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="HcrCoresInterface_diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_diss_oxygen_fluid, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="HcrCoresInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ecosystem, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="HcrCoresInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ecosystem_category, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="HcrCoresInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ecosystem_subtype, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="HcrCoresInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ecosystem_type, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_elev = Slot(uri=MIXS['0000093'], name="HcrCoresInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_elev, domain=HcrCoresInterface, range=float)

slots.HcrCoresInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="HcrCoresInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_env_broad_scale, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="HcrCoresInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_env_local_scale, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_env_medium = Slot(uri=MIXS['0000014'], name="HcrCoresInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_env_medium, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_ethylbenzene = Slot(uri=MIXS['0000155'], name="HcrCoresInterface_ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ethylbenzene, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="HcrCoresInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_experimental_factor, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_field = Slot(uri=MIXS['0000291'], name="HcrCoresInterface_field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_field, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="HcrCoresInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_geo_loc_name, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_hc_produced = Slot(uri=MIXS['0000989'], name="HcrCoresInterface_hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hc_produced, domain=HcrCoresInterface, range=Optional[Union[str, "HcProducedEnum"]])

slots.HcrCoresInterface_hcr = Slot(uri=MIXS['0000988'], name="HcrCoresInterface_hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hcr, domain=HcrCoresInterface, range=Optional[Union[str, "HcrEnum"]])

slots.HcrCoresInterface_hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="HcrCoresInterface_hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hcr_fw_salinity, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_hcr_geol_age = Slot(uri=MIXS['0000993'], name="HcrCoresInterface_hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hcr_geol_age, domain=HcrCoresInterface, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.HcrCoresInterface_hcr_pressure = Slot(uri=MIXS['0000395'], name="HcrCoresInterface_hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hcr_pressure, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_hcr_temp = Slot(uri=MIXS['0000393'], name="HcrCoresInterface_hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_hcr_temp, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="HcrCoresInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_horizon_meth, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_lat_lon = Slot(uri=MIXS['0000009'], name="HcrCoresInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_lat_lon, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_lithology = Slot(uri=MIXS['0000990'], name="HcrCoresInterface_lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_lithology, domain=HcrCoresInterface, range=Optional[Union[str, "LithologyEnum"]])

slots.HcrCoresInterface_magnesium = Slot(uri=MIXS['0000431'], name="HcrCoresInterface_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_magnesium, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_misc_param = Slot(uri=MIXS['0000752'], name="HcrCoresInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_misc_param, domain=HcrCoresInterface, range=Optional[Union[str, List[str]]])

slots.HcrCoresInterface_nitrate = Slot(uri=MIXS['0000425'], name="HcrCoresInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_nitrate, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_nitrite = Slot(uri=MIXS['0000426'], name="HcrCoresInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_nitrite, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="HcrCoresInterface_org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_org_count_qpcr_info, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_organism_count = Slot(uri=MIXS['0000103'], name="HcrCoresInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_organism_count, domain=HcrCoresInterface, range=Optional[Union[str, List[str]]])

slots.HcrCoresInterface_owc_tvdss = Slot(uri=MIXS['0000405'], name="HcrCoresInterface_owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_owc_tvdss, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="HcrCoresInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_oxy_stat_samp, domain=HcrCoresInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HcrCoresInterface_permeability = Slot(uri=MIXS['0000404'], name="HcrCoresInterface_permeability", curie=MIXS.curie('0000404'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_permeability, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_ph = Slot(uri=MIXS['0001001'], name="HcrCoresInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ph, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_ph_meth = Slot(uri=MIXS['0001106'], name="HcrCoresInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_ph_meth, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_porosity = Slot(uri=MIXS['0000211'], name="HcrCoresInterface_porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_porosity, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_potassium = Slot(uri=MIXS['0000430'], name="HcrCoresInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_potassium, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_pour_point = Slot(uri=MIXS['0000127'], name="HcrCoresInterface_pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_pour_point, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_pressure = Slot(uri=MIXS['0000412'], name="HcrCoresInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_pressure, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="HcrCoresInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_rel_to_oxygen, domain=HcrCoresInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HcrCoresInterface_reservoir = Slot(uri=MIXS['0000303'], name="HcrCoresInterface_reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_reservoir, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_resins_pc = Slot(uri=MIXS['0000134'], name="HcrCoresInterface_resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_resins_pc, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_salinity = Slot(uri=MIXS['0000183'], name="HcrCoresInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_salinity, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="HcrCoresInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_collec_device, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="HcrCoresInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_collec_method, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="HcrCoresInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_mat_process, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_md = Slot(uri=MIXS['0000413'], name="HcrCoresInterface_samp_md", curie=MIXS.curie('0000413'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_md, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_size = Slot(uri=MIXS['0000001'], name="HcrCoresInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_size, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="HcrCoresInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_store_dur, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="HcrCoresInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_store_loc, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="HcrCoresInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_store_temp, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_samp_subtype = Slot(uri=MIXS['0000999'], name="HcrCoresInterface_samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_subtype, domain=HcrCoresInterface, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.HcrCoresInterface_samp_transport_cond = Slot(uri=MIXS['0000410'], name="HcrCoresInterface_samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_transport_cond, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_tvdss = Slot(uri=MIXS['0000409'], name="HcrCoresInterface_samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_tvdss, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_type = Slot(uri=MIXS['0000998'], name="HcrCoresInterface_samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_type, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_samp_well_name = Slot(uri=MIXS['0000296'], name="HcrCoresInterface_samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_samp_well_name, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_saturates_pc = Slot(uri=MIXS['0000131'], name="HcrCoresInterface_saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_saturates_pc, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_size_frac = Slot(uri=MIXS['0000017'], name="HcrCoresInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_size_frac, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_sodium = Slot(uri=MIXS['0000428'], name="HcrCoresInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sodium, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="HcrCoresInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_specific_ecosystem, domain=HcrCoresInterface, range=str)

slots.HcrCoresInterface_sr_dep_env = Slot(uri=MIXS['0000996'], name="HcrCoresInterface_sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sr_dep_env, domain=HcrCoresInterface, range=Optional[Union[str, "SrDepEnvEnum"]])

slots.HcrCoresInterface_sr_geol_age = Slot(uri=MIXS['0000997'], name="HcrCoresInterface_sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sr_geol_age, domain=HcrCoresInterface, range=Optional[Union[str, "SrGeolAgeEnum"]])

slots.HcrCoresInterface_sr_kerog_type = Slot(uri=MIXS['0000994'], name="HcrCoresInterface_sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sr_kerog_type, domain=HcrCoresInterface, range=Optional[Union[str, "SrKerogTypeEnum"]])

slots.HcrCoresInterface_sr_lithology = Slot(uri=MIXS['0000995'], name="HcrCoresInterface_sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sr_lithology, domain=HcrCoresInterface, range=Optional[Union[str, "SrLithologyEnum"]])

slots.HcrCoresInterface_sulfate = Slot(uri=MIXS['0000423'], name="HcrCoresInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sulfate, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_sulfate_fw = Slot(uri=MIXS['0000407'], name="HcrCoresInterface_sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sulfate_fw, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_sulfide = Slot(uri=MIXS['0000424'], name="HcrCoresInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_sulfide, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_suspend_solids = Slot(uri=MIXS['0000150'], name="HcrCoresInterface_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_suspend_solids, domain=HcrCoresInterface, range=Optional[Union[str, List[str]]])

slots.HcrCoresInterface_tan = Slot(uri=MIXS['0000120'], name="HcrCoresInterface_tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tan, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_temp = Slot(uri=MIXS['0000113'], name="HcrCoresInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_temp, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_toluene = Slot(uri=MIXS['0000154'], name="HcrCoresInterface_toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_toluene, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tot_iron = Slot(uri=MIXS['0000105'], name="HcrCoresInterface_tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tot_iron, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tot_nitro = Slot(uri=MIXS['0000102'], name="HcrCoresInterface_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tot_nitro, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tot_phosp = Slot(uri=MIXS['0000117'], name="HcrCoresInterface_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tot_phosp, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tot_sulfur = Slot(uri=MIXS['0000419'], name="HcrCoresInterface_tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tot_sulfur, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="HcrCoresInterface_tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tvdss_of_hcr_press, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="HcrCoresInterface_tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_tvdss_of_hcr_temp, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_vfa = Slot(uri=MIXS['0000152'], name="HcrCoresInterface_vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_vfa, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_vfa_fw = Slot(uri=MIXS['0000408'], name="HcrCoresInterface_vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_vfa_fw, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_viscosity = Slot(uri=MIXS['0000126'], name="HcrCoresInterface_viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_viscosity, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_win = Slot(uri=MIXS['0000297'], name="HcrCoresInterface_win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_win, domain=HcrCoresInterface, range=Optional[str])

slots.HcrCoresInterface_xylene = Slot(uri=MIXS['0000156'], name="HcrCoresInterface_xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC_SUB_SCHEMA.HcrCoresInterface_xylene, domain=HcrCoresInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_add_recov_method = Slot(uri=MIXS['0001009'], name="HcrFluidsSwabsInterface_add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_add_recov_method, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_additional_info = Slot(uri=MIXS['0000300'], name="HcrFluidsSwabsInterface_additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_additional_info, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_alkalinity = Slot(uri=MIXS['0000421'], name="HcrFluidsSwabsInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_alkalinity, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_alkalinity_method = Slot(uri=MIXS['0000298'], name="HcrFluidsSwabsInterface_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_alkalinity_method, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_alt = Slot(uri=MIXS['0000094'], name="HcrFluidsSwabsInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_alt, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_ammonium = Slot(uri=MIXS['0000427'], name="HcrFluidsSwabsInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ammonium, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_api = Slot(uri=MIXS['0000157'], name="HcrFluidsSwabsInterface_api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_api, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_aromatics_pc = Slot(uri=MIXS['0000133'], name="HcrFluidsSwabsInterface_aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_aromatics_pc, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_asphaltenes_pc = Slot(uri=MIXS['0000135'], name="HcrFluidsSwabsInterface_asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_asphaltenes_pc, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_basin = Slot(uri=MIXS['0000290'], name="HcrFluidsSwabsInterface_basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_basin, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_benzene = Slot(uri=MIXS['0000153'], name="HcrFluidsSwabsInterface_benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_benzene, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_biocide = Slot(uri=MIXS['0001011'], name="HcrFluidsSwabsInterface_biocide", curie=MIXS.curie('0001011'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_biocide, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_biocide_admin_method = Slot(uri=MIXS['0000456'], name="HcrFluidsSwabsInterface_biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_biocide_admin_method, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_calcium = Slot(uri=MIXS['0000432'], name="HcrFluidsSwabsInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_calcium, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_chem_administration = Slot(uri=MIXS['0000751'], name="HcrFluidsSwabsInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_chem_administration, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, List[str]]])

slots.HcrFluidsSwabsInterface_chem_treat_method = Slot(uri=MIXS['0000457'], name="HcrFluidsSwabsInterface_chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_chem_treat_method, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_chem_treatment = Slot(uri=MIXS['0001012'], name="HcrFluidsSwabsInterface_chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_chem_treatment, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_chloride = Slot(uri=MIXS['0000429'], name="HcrFluidsSwabsInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_chloride, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_collection_date = Slot(uri=MIXS['0000011'], name="HcrFluidsSwabsInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_collection_date, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_density = Slot(uri=MIXS['0000435'], name="HcrFluidsSwabsInterface_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_density, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_depos_env = Slot(uri=MIXS['0000992'], name="HcrFluidsSwabsInterface_depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_depos_env, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "DeposEnvEnum"]])

slots.HcrFluidsSwabsInterface_depth = Slot(uri=MIXS['0000018'], name="HcrFluidsSwabsInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_depth, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="HcrFluidsSwabsInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_carb_dioxide, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="HcrFluidsSwabsInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_inorg_carb, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="HcrFluidsSwabsInterface_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_inorg_phosp, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_diss_iron = Slot(uri=MIXS['0000139'], name="HcrFluidsSwabsInterface_diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_iron, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_diss_org_carb = Slot(uri=MIXS['0000433'], name="HcrFluidsSwabsInterface_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_org_carb, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="HcrFluidsSwabsInterface_diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_diss_oxygen_fluid, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="HcrFluidsSwabsInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ecosystem, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="HcrFluidsSwabsInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ecosystem_category, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="HcrFluidsSwabsInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ecosystem_subtype, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="HcrFluidsSwabsInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ecosystem_type, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_elev = Slot(uri=MIXS['0000093'], name="HcrFluidsSwabsInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_elev, domain=HcrFluidsSwabsInterface, range=float)

slots.HcrFluidsSwabsInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="HcrFluidsSwabsInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_env_broad_scale, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="HcrFluidsSwabsInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_env_local_scale, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_env_medium = Slot(uri=MIXS['0000014'], name="HcrFluidsSwabsInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_env_medium, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_ethylbenzene = Slot(uri=MIXS['0000155'], name="HcrFluidsSwabsInterface_ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ethylbenzene, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="HcrFluidsSwabsInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_experimental_factor, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_field = Slot(uri=MIXS['0000291'], name="HcrFluidsSwabsInterface_field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_field, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="HcrFluidsSwabsInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_geo_loc_name, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_hc_produced = Slot(uri=MIXS['0000989'], name="HcrFluidsSwabsInterface_hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hc_produced, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "HcProducedEnum"]])

slots.HcrFluidsSwabsInterface_hcr = Slot(uri=MIXS['0000988'], name="HcrFluidsSwabsInterface_hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hcr, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "HcrEnum"]])

slots.HcrFluidsSwabsInterface_hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="HcrFluidsSwabsInterface_hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hcr_fw_salinity, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_hcr_geol_age = Slot(uri=MIXS['0000993'], name="HcrFluidsSwabsInterface_hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hcr_geol_age, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.HcrFluidsSwabsInterface_hcr_pressure = Slot(uri=MIXS['0000395'], name="HcrFluidsSwabsInterface_hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hcr_pressure, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_hcr_temp = Slot(uri=MIXS['0000393'], name="HcrFluidsSwabsInterface_hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_hcr_temp, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="HcrFluidsSwabsInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_horizon_meth, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_iw_bt_date_well = Slot(uri=MIXS['0001010'], name="HcrFluidsSwabsInterface_iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_iw_bt_date_well, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_iwf = Slot(uri=MIXS['0000455'], name="HcrFluidsSwabsInterface_iwf", curie=MIXS.curie('0000455'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_iwf, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_lat_lon = Slot(uri=MIXS['0000009'], name="HcrFluidsSwabsInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_lat_lon, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_lithology = Slot(uri=MIXS['0000990'], name="HcrFluidsSwabsInterface_lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_lithology, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "LithologyEnum"]])

slots.HcrFluidsSwabsInterface_magnesium = Slot(uri=MIXS['0000431'], name="HcrFluidsSwabsInterface_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_magnesium, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_misc_param = Slot(uri=MIXS['0000752'], name="HcrFluidsSwabsInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_misc_param, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, List[str]]])

slots.HcrFluidsSwabsInterface_nitrate = Slot(uri=MIXS['0000425'], name="HcrFluidsSwabsInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_nitrate, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_nitrite = Slot(uri=MIXS['0000426'], name="HcrFluidsSwabsInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_nitrite, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="HcrFluidsSwabsInterface_org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_org_count_qpcr_info, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_organism_count = Slot(uri=MIXS['0000103'], name="HcrFluidsSwabsInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_organism_count, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, List[str]]])

slots.HcrFluidsSwabsInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="HcrFluidsSwabsInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_oxy_stat_samp, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HcrFluidsSwabsInterface_ph = Slot(uri=MIXS['0001001'], name="HcrFluidsSwabsInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ph, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_ph_meth = Slot(uri=MIXS['0001106'], name="HcrFluidsSwabsInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_ph_meth, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_potassium = Slot(uri=MIXS['0000430'], name="HcrFluidsSwabsInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_potassium, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_pour_point = Slot(uri=MIXS['0000127'], name="HcrFluidsSwabsInterface_pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_pour_point, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_pressure = Slot(uri=MIXS['0000412'], name="HcrFluidsSwabsInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_pressure, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_prod_rate = Slot(uri=MIXS['0000452'], name="HcrFluidsSwabsInterface_prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_prod_rate, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_prod_start_date = Slot(uri=MIXS['0001008'], name="HcrFluidsSwabsInterface_prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_prod_start_date, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="HcrFluidsSwabsInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_rel_to_oxygen, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HcrFluidsSwabsInterface_reservoir = Slot(uri=MIXS['0000303'], name="HcrFluidsSwabsInterface_reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_reservoir, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_resins_pc = Slot(uri=MIXS['0000134'], name="HcrFluidsSwabsInterface_resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_resins_pc, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_salinity = Slot(uri=MIXS['0000183'], name="HcrFluidsSwabsInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_salinity, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="HcrFluidsSwabsInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_collec_device, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="HcrFluidsSwabsInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_collec_method, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_collect_point = Slot(uri=MIXS['0001015'], name="HcrFluidsSwabsInterface_samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_collect_point, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.HcrFluidsSwabsInterface_samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="HcrFluidsSwabsInterface_samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_loc_corr_rate, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="HcrFluidsSwabsInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_mat_process, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_preserv = Slot(uri=MIXS['0000463'], name="HcrFluidsSwabsInterface_samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_preserv, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_size = Slot(uri=MIXS['0000001'], name="HcrFluidsSwabsInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_size, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="HcrFluidsSwabsInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_store_dur, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="HcrFluidsSwabsInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_store_loc, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="HcrFluidsSwabsInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_store_temp, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_samp_subtype = Slot(uri=MIXS['0000999'], name="HcrFluidsSwabsInterface_samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_subtype, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.HcrFluidsSwabsInterface_samp_transport_cond = Slot(uri=MIXS['0000410'], name="HcrFluidsSwabsInterface_samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_transport_cond, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_type = Slot(uri=MIXS['0000998'], name="HcrFluidsSwabsInterface_samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_type, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_samp_well_name = Slot(uri=MIXS['0000296'], name="HcrFluidsSwabsInterface_samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_samp_well_name, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_saturates_pc = Slot(uri=MIXS['0000131'], name="HcrFluidsSwabsInterface_saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_saturates_pc, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_size_frac = Slot(uri=MIXS['0000017'], name="HcrFluidsSwabsInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_size_frac, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_sodium = Slot(uri=MIXS['0000428'], name="HcrFluidsSwabsInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_sodium, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="HcrFluidsSwabsInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_specific_ecosystem, domain=HcrFluidsSwabsInterface, range=str)

slots.HcrFluidsSwabsInterface_sulfate = Slot(uri=MIXS['0000423'], name="HcrFluidsSwabsInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_sulfate, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_sulfate_fw = Slot(uri=MIXS['0000407'], name="HcrFluidsSwabsInterface_sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_sulfate_fw, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_sulfide = Slot(uri=MIXS['0000424'], name="HcrFluidsSwabsInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_sulfide, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_suspend_solids = Slot(uri=MIXS['0000150'], name="HcrFluidsSwabsInterface_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_suspend_solids, domain=HcrFluidsSwabsInterface, range=Optional[Union[str, List[str]]])

slots.HcrFluidsSwabsInterface_tan = Slot(uri=MIXS['0000120'], name="HcrFluidsSwabsInterface_tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tan, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_temp = Slot(uri=MIXS['0000113'], name="HcrFluidsSwabsInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_temp, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_toluene = Slot(uri=MIXS['0000154'], name="HcrFluidsSwabsInterface_toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_toluene, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tot_iron = Slot(uri=MIXS['0000105'], name="HcrFluidsSwabsInterface_tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tot_iron, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tot_nitro = Slot(uri=MIXS['0000102'], name="HcrFluidsSwabsInterface_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tot_nitro, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tot_phosp = Slot(uri=MIXS['0000117'], name="HcrFluidsSwabsInterface_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tot_phosp, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tot_sulfur = Slot(uri=MIXS['0000419'], name="HcrFluidsSwabsInterface_tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tot_sulfur, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="HcrFluidsSwabsInterface_tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tvdss_of_hcr_press, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="HcrFluidsSwabsInterface_tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_tvdss_of_hcr_temp, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_vfa = Slot(uri=MIXS['0000152'], name="HcrFluidsSwabsInterface_vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_vfa, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_vfa_fw = Slot(uri=MIXS['0000408'], name="HcrFluidsSwabsInterface_vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_vfa_fw, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_viscosity = Slot(uri=MIXS['0000126'], name="HcrFluidsSwabsInterface_viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_viscosity, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_water_cut = Slot(uri=MIXS['0000454'], name="HcrFluidsSwabsInterface_water_cut", curie=MIXS.curie('0000454'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_water_cut, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_water_prod_rate = Slot(uri=MIXS['0000453'], name="HcrFluidsSwabsInterface_water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_water_prod_rate, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_win = Slot(uri=MIXS['0000297'], name="HcrFluidsSwabsInterface_win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_win, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HcrFluidsSwabsInterface_xylene = Slot(uri=MIXS['0000156'], name="HcrFluidsSwabsInterface_xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC_SUB_SCHEMA.HcrFluidsSwabsInterface_xylene, domain=HcrFluidsSwabsInterface, range=Optional[str])

slots.HostAssociatedInterface_alt = Slot(uri=MIXS['0000094'], name="HostAssociatedInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_alt, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_ances_data = Slot(uri=MIXS['0000247'], name="HostAssociatedInterface_ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_ances_data, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_biol_stat = Slot(uri=MIXS['0000858'], name="HostAssociatedInterface_biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_biol_stat, domain=HostAssociatedInterface, range=Optional[Union[str, "BiolStatEnum"]])

slots.HostAssociatedInterface_blood_press_diast = Slot(uri=MIXS['0000258'], name="HostAssociatedInterface_blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_blood_press_diast, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_blood_press_syst = Slot(uri=MIXS['0000259'], name="HostAssociatedInterface_blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_blood_press_syst, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_chem_administration = Slot(uri=MIXS['0000751'], name="HostAssociatedInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_chem_administration, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_collection_date = Slot(uri=MIXS['0000011'], name="HostAssociatedInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_collection_date, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_depth = Slot(uri=MIXS['0000018'], name="HostAssociatedInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_depth, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="HostAssociatedInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_ecosystem, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="HostAssociatedInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_ecosystem_category, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="HostAssociatedInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_ecosystem_subtype, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="HostAssociatedInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_ecosystem_type, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_elev = Slot(uri=MIXS['0000093'], name="HostAssociatedInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_elev, domain=HostAssociatedInterface, range=float)

slots.HostAssociatedInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="HostAssociatedInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_env_broad_scale, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="HostAssociatedInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_env_local_scale, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_env_medium = Slot(uri=MIXS['0000014'], name="HostAssociatedInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_env_medium, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="HostAssociatedInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_experimental_factor, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_genetic_mod = Slot(uri=MIXS['0000859'], name="HostAssociatedInterface_genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_genetic_mod, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="HostAssociatedInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_geo_loc_name, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_gravidity = Slot(uri=MIXS['0000875'], name="HostAssociatedInterface_gravidity", curie=MIXS.curie('0000875'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_gravidity, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="HostAssociatedInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_horizon_meth, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_age = Slot(uri=MIXS['0000255'], name="HostAssociatedInterface_host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_age, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_body_habitat = Slot(uri=MIXS['0000866'], name="HostAssociatedInterface_host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_body_habitat, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_body_product = Slot(uri=MIXS['0000888'], name="HostAssociatedInterface_host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_body_product, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_body_site = Slot(uri=MIXS['0000867'], name="HostAssociatedInterface_host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_body_site, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_body_temp = Slot(uri=MIXS['0000274'], name="HostAssociatedInterface_host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_body_temp, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_color = Slot(uri=MIXS['0000260'], name="HostAssociatedInterface_host_color", curie=MIXS.curie('0000260'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_color, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_common_name = Slot(uri=MIXS['0000248'], name="HostAssociatedInterface_host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_common_name, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_diet = Slot(uri=MIXS['0000869'], name="HostAssociatedInterface_host_diet", curie=MIXS.curie('0000869'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_diet, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_host_dry_mass = Slot(uri=MIXS['0000257'], name="HostAssociatedInterface_host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_dry_mass, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_family_relation = Slot(uri=MIXS['0000872'], name="HostAssociatedInterface_host_family_relation", curie=MIXS.curie('0000872'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_family_relation, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_host_genotype = Slot(uri=MIXS['0000365'], name="HostAssociatedInterface_host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_genotype, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_growth_cond = Slot(uri=MIXS['0000871'], name="HostAssociatedInterface_host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_growth_cond, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_height = Slot(uri=MIXS['0000264'], name="HostAssociatedInterface_host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_height, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_last_meal = Slot(uri=MIXS['0000870'], name="HostAssociatedInterface_host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_last_meal, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_host_length = Slot(uri=MIXS['0000256'], name="HostAssociatedInterface_host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_length, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_life_stage = Slot(uri=MIXS['0000251'], name="HostAssociatedInterface_host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_life_stage, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_phenotype = Slot(uri=MIXS['0000874'], name="HostAssociatedInterface_host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_phenotype, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_sex = Slot(uri=MIXS['0000811'], name="HostAssociatedInterface_host_sex", curie=MIXS.curie('0000811'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_sex, domain=HostAssociatedInterface, range=Optional[Union[str, "HostSexEnum"]])

slots.HostAssociatedInterface_host_shape = Slot(uri=MIXS['0000261'], name="HostAssociatedInterface_host_shape", curie=MIXS.curie('0000261'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_shape, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_subject_id = Slot(uri=MIXS['0000861'], name="HostAssociatedInterface_host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_subject_id, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="HostAssociatedInterface_host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_subspecf_genlin, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_host_substrate = Slot(uri=MIXS['0000252'], name="HostAssociatedInterface_host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_substrate, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_symbiont = Slot(uri=MIXS['0001298'], name="HostAssociatedInterface_host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_symbiont, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_host_taxid = Slot(uri=MIXS['0000250'], name="HostAssociatedInterface_host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_taxid, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_host_tot_mass = Slot(uri=MIXS['0000263'], name="HostAssociatedInterface_host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_host_tot_mass, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_lat_lon = Slot(uri=MIXS['0000009'], name="HostAssociatedInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_lat_lon, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_misc_param = Slot(uri=MIXS['0000752'], name="HostAssociatedInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_misc_param, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_organism_count = Slot(uri=MIXS['0000103'], name="HostAssociatedInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_organism_count, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="HostAssociatedInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_oxy_stat_samp, domain=HostAssociatedInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HostAssociatedInterface_perturbation = Slot(uri=MIXS['0000754'], name="HostAssociatedInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_perturbation, domain=HostAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.HostAssociatedInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="HostAssociatedInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_rel_to_oxygen, domain=HostAssociatedInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.HostAssociatedInterface_salinity = Slot(uri=MIXS['0000183'], name="HostAssociatedInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_salinity, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_capt_status = Slot(uri=MIXS['0000860'], name="HostAssociatedInterface_samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_capt_status, domain=HostAssociatedInterface, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.HostAssociatedInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="HostAssociatedInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_collec_device, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="HostAssociatedInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_collec_method, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_dis_stage = Slot(uri=MIXS['0000249'], name="HostAssociatedInterface_samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_dis_stage, domain=HostAssociatedInterface, range=Optional[Union[str, "SampDisStageEnum"]])

slots.HostAssociatedInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="HostAssociatedInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_mat_process, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_size = Slot(uri=MIXS['0000001'], name="HostAssociatedInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_size, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="HostAssociatedInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_store_dur, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="HostAssociatedInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_store_loc, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="HostAssociatedInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_samp_store_temp, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_size_frac = Slot(uri=MIXS['0000017'], name="HostAssociatedInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_size_frac, domain=HostAssociatedInterface, range=Optional[str])

slots.HostAssociatedInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="HostAssociatedInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_specific_ecosystem, domain=HostAssociatedInterface, range=str)

slots.HostAssociatedInterface_temp = Slot(uri=MIXS['0000113'], name="HostAssociatedInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.HostAssociatedInterface_temp, domain=HostAssociatedInterface, range=Optional[str])

slots.MiscEnvsInterface_alkalinity = Slot(uri=MIXS['0000421'], name="MiscEnvsInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_alkalinity, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_alt = Slot(uri=MIXS['0000094'], name="MiscEnvsInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_alt, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_ammonium = Slot(uri=MIXS['0000427'], name="MiscEnvsInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ammonium, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_biomass = Slot(uri=MIXS['0000174'], name="MiscEnvsInterface_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_biomass, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_bromide = Slot(uri=MIXS['0000176'], name="MiscEnvsInterface_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_bromide, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_calcium = Slot(uri=MIXS['0000432'], name="MiscEnvsInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_calcium, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_chem_administration = Slot(uri=MIXS['0000751'], name="MiscEnvsInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_chem_administration, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_chloride = Slot(uri=MIXS['0000429'], name="MiscEnvsInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_chloride, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_chlorophyll = Slot(uri=MIXS['0000177'], name="MiscEnvsInterface_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_chlorophyll, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_collection_date = Slot(uri=MIXS['0000011'], name="MiscEnvsInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_collection_date, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_density = Slot(uri=MIXS['0000435'], name="MiscEnvsInterface_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_density, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_depth = Slot(uri=MIXS['0000018'], name="MiscEnvsInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_depth, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_diether_lipids = Slot(uri=MIXS['0000178'], name="MiscEnvsInterface_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diether_lipids, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="MiscEnvsInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diss_carb_dioxide, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_diss_hydrogen = Slot(uri=MIXS['0000179'], name="MiscEnvsInterface_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diss_hydrogen, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="MiscEnvsInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diss_inorg_carb, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_diss_org_nitro = Slot(uri=MIXS['0000162'], name="MiscEnvsInterface_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diss_org_nitro, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_diss_oxygen = Slot(uri=MIXS['0000119'], name="MiscEnvsInterface_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_diss_oxygen, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="MiscEnvsInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ecosystem, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="MiscEnvsInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ecosystem_category, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="MiscEnvsInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ecosystem_subtype, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="MiscEnvsInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ecosystem_type, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_elev = Slot(uri=MIXS['0000093'], name="MiscEnvsInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_elev, domain=MiscEnvsInterface, range=float)

slots.MiscEnvsInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="MiscEnvsInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_env_broad_scale, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="MiscEnvsInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_env_local_scale, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_env_medium = Slot(uri=MIXS['0000014'], name="MiscEnvsInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_env_medium, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="MiscEnvsInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_experimental_factor, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="MiscEnvsInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_geo_loc_name, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="MiscEnvsInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_horizon_meth, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_lat_lon = Slot(uri=MIXS['0000009'], name="MiscEnvsInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_lat_lon, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_misc_param = Slot(uri=MIXS['0000752'], name="MiscEnvsInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_misc_param, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_nitrate = Slot(uri=MIXS['0000425'], name="MiscEnvsInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_nitrate, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_nitrite = Slot(uri=MIXS['0000426'], name="MiscEnvsInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_nitrite, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_nitro = Slot(uri=MIXS['0000504'], name="MiscEnvsInterface_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_nitro, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_org_carb = Slot(uri=MIXS['0000508'], name="MiscEnvsInterface_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_org_carb, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_org_matter = Slot(uri=MIXS['0000204'], name="MiscEnvsInterface_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_org_matter, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_org_nitro = Slot(uri=MIXS['0000205'], name="MiscEnvsInterface_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_org_nitro, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_organism_count = Slot(uri=MIXS['0000103'], name="MiscEnvsInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_organism_count, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="MiscEnvsInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_oxy_stat_samp, domain=MiscEnvsInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.MiscEnvsInterface_perturbation = Slot(uri=MIXS['0000754'], name="MiscEnvsInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_perturbation, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_ph = Slot(uri=MIXS['0001001'], name="MiscEnvsInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ph, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_ph_meth = Slot(uri=MIXS['0001106'], name="MiscEnvsInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_ph_meth, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_phosphate = Slot(uri=MIXS['0000505'], name="MiscEnvsInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_phosphate, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="MiscEnvsInterface_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_phosplipid_fatt_acid, domain=MiscEnvsInterface, range=Optional[Union[str, List[str]]])

slots.MiscEnvsInterface_potassium = Slot(uri=MIXS['0000430'], name="MiscEnvsInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_potassium, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_pressure = Slot(uri=MIXS['0000412'], name="MiscEnvsInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_pressure, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="MiscEnvsInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_rel_to_oxygen, domain=MiscEnvsInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.MiscEnvsInterface_salinity = Slot(uri=MIXS['0000183'], name="MiscEnvsInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_salinity, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="MiscEnvsInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_collec_device, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="MiscEnvsInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_collec_method, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="MiscEnvsInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_mat_process, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_size = Slot(uri=MIXS['0000001'], name="MiscEnvsInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_size, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="MiscEnvsInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_store_dur, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="MiscEnvsInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_store_loc, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="MiscEnvsInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_samp_store_temp, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_silicate = Slot(uri=MIXS['0000184'], name="MiscEnvsInterface_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_silicate, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_size_frac = Slot(uri=MIXS['0000017'], name="MiscEnvsInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_size_frac, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_sodium = Slot(uri=MIXS['0000428'], name="MiscEnvsInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_sodium, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="MiscEnvsInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_specific_ecosystem, domain=MiscEnvsInterface, range=str)

slots.MiscEnvsInterface_sulfate = Slot(uri=MIXS['0000423'], name="MiscEnvsInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_sulfate, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_sulfide = Slot(uri=MIXS['0000424'], name="MiscEnvsInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_sulfide, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_temp = Slot(uri=MIXS['0000113'], name="MiscEnvsInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_temp, domain=MiscEnvsInterface, range=Optional[str])

slots.MiscEnvsInterface_water_current = Slot(uri=MIXS['0000203'], name="MiscEnvsInterface_water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC_SUB_SCHEMA.MiscEnvsInterface_water_current, domain=MiscEnvsInterface, range=Optional[str])

slots.PlantAssociatedInterface_air_temp_regm = Slot(uri=MIXS['0000551'], name="PlantAssociatedInterface_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_air_temp_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_alt = Slot(uri=MIXS['0000094'], name="PlantAssociatedInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_alt, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_ances_data = Slot(uri=MIXS['0000247'], name="PlantAssociatedInterface_ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ances_data, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_antibiotic_regm = Slot(uri=MIXS['0000553'], name="PlantAssociatedInterface_antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_antibiotic_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_biol_stat = Slot(uri=MIXS['0000858'], name="PlantAssociatedInterface_biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_biol_stat, domain=PlantAssociatedInterface, range=Optional[Union[str, "BiolStatEnum"]])

slots.PlantAssociatedInterface_biotic_regm = Slot(uri=MIXS['0001038'], name="PlantAssociatedInterface_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_biotic_regm, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_chem_administration = Slot(uri=MIXS['0000751'], name="PlantAssociatedInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_chem_administration, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_chem_mutagen = Slot(uri=MIXS['0000555'], name="PlantAssociatedInterface_chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_chem_mutagen, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_climate_environment = Slot(uri=MIXS['0001040'], name="PlantAssociatedInterface_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_climate_environment, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_collection_date = Slot(uri=MIXS['0000011'], name="PlantAssociatedInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_collection_date, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_cult_root_med = Slot(uri=MIXS['0001041'], name="PlantAssociatedInterface_cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_cult_root_med, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_depth = Slot(uri=MIXS['0000018'], name="PlantAssociatedInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_depth, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="PlantAssociatedInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ecosystem, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="PlantAssociatedInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ecosystem_category, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="PlantAssociatedInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ecosystem_subtype, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="PlantAssociatedInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ecosystem_type, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_elev = Slot(uri=MIXS['0000093'], name="PlantAssociatedInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_elev, domain=PlantAssociatedInterface, range=float)

slots.PlantAssociatedInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="PlantAssociatedInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_env_broad_scale, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="PlantAssociatedInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_env_local_scale, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_env_medium = Slot(uri=MIXS['0000014'], name="PlantAssociatedInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_env_medium, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="PlantAssociatedInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_experimental_factor, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_fertilizer_regm = Slot(uri=MIXS['0000556'], name="PlantAssociatedInterface_fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_fertilizer_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_fungicide_regm = Slot(uri=MIXS['0000557'], name="PlantAssociatedInterface_fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_fungicide_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_gaseous_environment = Slot(uri=MIXS['0000558'], name="PlantAssociatedInterface_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_gaseous_environment, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_genetic_mod = Slot(uri=MIXS['0000859'], name="PlantAssociatedInterface_genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_genetic_mod, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="PlantAssociatedInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_geo_loc_name, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_gravity = Slot(uri=MIXS['0000559'], name="PlantAssociatedInterface_gravity", curie=MIXS.curie('0000559'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_gravity, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_growth_facil = Slot(uri=MIXS['0001043'], name="PlantAssociatedInterface_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_growth_facil, domain=PlantAssociatedInterface, range=Union[str, "GrowthFacilEnum"])

slots.PlantAssociatedInterface_growth_habit = Slot(uri=MIXS['0001044'], name="PlantAssociatedInterface_growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_growth_habit, domain=PlantAssociatedInterface, range=Optional[Union[str, "GrowthHabitEnum"]])

slots.PlantAssociatedInterface_growth_hormone_regm = Slot(uri=MIXS['0000560'], name="PlantAssociatedInterface_growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_growth_hormone_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_herbicide_regm = Slot(uri=MIXS['0000561'], name="PlantAssociatedInterface_herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_herbicide_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="PlantAssociatedInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_horizon_meth, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_age = Slot(uri=MIXS['0000255'], name="PlantAssociatedInterface_host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_age, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_common_name = Slot(uri=MIXS['0000248'], name="PlantAssociatedInterface_host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_common_name, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_dry_mass = Slot(uri=MIXS['0000257'], name="PlantAssociatedInterface_host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_dry_mass, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_genotype = Slot(uri=MIXS['0000365'], name="PlantAssociatedInterface_host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_genotype, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_height = Slot(uri=MIXS['0000264'], name="PlantAssociatedInterface_host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_height, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_length = Slot(uri=MIXS['0000256'], name="PlantAssociatedInterface_host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_length, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_life_stage = Slot(uri=MIXS['0000251'], name="PlantAssociatedInterface_host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_life_stage, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_phenotype = Slot(uri=MIXS['0000874'], name="PlantAssociatedInterface_host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_phenotype, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="PlantAssociatedInterface_host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_subspecf_genlin, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_host_symbiont = Slot(uri=MIXS['0001298'], name="PlantAssociatedInterface_host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_symbiont, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_host_taxid = Slot(uri=MIXS['0000250'], name="PlantAssociatedInterface_host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_taxid, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_tot_mass = Slot(uri=MIXS['0000263'], name="PlantAssociatedInterface_host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_tot_mass, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_host_wet_mass = Slot(uri=MIXS['0000567'], name="PlantAssociatedInterface_host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_host_wet_mass, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_humidity_regm = Slot(uri=MIXS['0000568'], name="PlantAssociatedInterface_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_humidity_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_lat_lon = Slot(uri=MIXS['0000009'], name="PlantAssociatedInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_lat_lon, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_light_regm = Slot(uri=MIXS['0000569'], name="PlantAssociatedInterface_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_light_regm, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_mechanical_damage = Slot(uri=MIXS['0001052'], name="PlantAssociatedInterface_mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_mechanical_damage, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="PlantAssociatedInterface_mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_mineral_nutr_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_misc_param = Slot(uri=MIXS['0000752'], name="PlantAssociatedInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_misc_param, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_non_min_nutr_regm = Slot(uri=MIXS['0000571'], name="PlantAssociatedInterface_non_min_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_non_min_nutr_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_organism_count = Slot(uri=MIXS['0000103'], name="PlantAssociatedInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_organism_count, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="PlantAssociatedInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_oxy_stat_samp, domain=PlantAssociatedInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.PlantAssociatedInterface_perturbation = Slot(uri=MIXS['0000754'], name="PlantAssociatedInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_perturbation, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_pesticide_regm = Slot(uri=MIXS['0000573'], name="PlantAssociatedInterface_pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_pesticide_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_ph_regm = Slot(uri=MIXS['0001056'], name="PlantAssociatedInterface_ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_ph_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_plant_growth_med = Slot(uri=MIXS['0001057'], name="PlantAssociatedInterface_plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_plant_growth_med, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_plant_product = Slot(uri=MIXS['0001058'], name="PlantAssociatedInterface_plant_product", curie=MIXS.curie('0001058'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_plant_product, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_plant_sex = Slot(uri=MIXS['0001059'], name="PlantAssociatedInterface_plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_plant_sex, domain=PlantAssociatedInterface, range=Optional[Union[str, "PlantSexEnum"]])

slots.PlantAssociatedInterface_plant_struc = Slot(uri=MIXS['0001060'], name="PlantAssociatedInterface_plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_plant_struc, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_radiation_regm = Slot(uri=MIXS['0000575'], name="PlantAssociatedInterface_radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_radiation_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_rainfall_regm = Slot(uri=MIXS['0000576'], name="PlantAssociatedInterface_rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_rainfall_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="PlantAssociatedInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_rel_to_oxygen, domain=PlantAssociatedInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.PlantAssociatedInterface_root_cond = Slot(uri=MIXS['0001061'], name="PlantAssociatedInterface_root_cond", curie=MIXS.curie('0001061'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_cond, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_carbon = Slot(uri=MIXS['0000577'], name="PlantAssociatedInterface_root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_carbon, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_macronutr = Slot(uri=MIXS['0000578'], name="PlantAssociatedInterface_root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_macronutr, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_micronutr = Slot(uri=MIXS['0000579'], name="PlantAssociatedInterface_root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_micronutr, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_ph = Slot(uri=MIXS['0001062'], name="PlantAssociatedInterface_root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_ph, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_regl = Slot(uri=MIXS['0000581'], name="PlantAssociatedInterface_root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_regl, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_solid = Slot(uri=MIXS['0001063'], name="PlantAssociatedInterface_root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_solid, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_root_med_suppl = Slot(uri=MIXS['0000580'], name="PlantAssociatedInterface_root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_root_med_suppl, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_salinity = Slot(uri=MIXS['0000183'], name="PlantAssociatedInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_salinity, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_salt_regm = Slot(uri=MIXS['0000582'], name="PlantAssociatedInterface_salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_salt_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_samp_capt_status = Slot(uri=MIXS['0000860'], name="PlantAssociatedInterface_samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_capt_status, domain=PlantAssociatedInterface, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.PlantAssociatedInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="PlantAssociatedInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_collec_device, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="PlantAssociatedInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_collec_method, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_dis_stage = Slot(uri=MIXS['0000249'], name="PlantAssociatedInterface_samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_dis_stage, domain=PlantAssociatedInterface, range=Optional[Union[str, "SampDisStageEnum"]])

slots.PlantAssociatedInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="PlantAssociatedInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_mat_process, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_size = Slot(uri=MIXS['0000001'], name="PlantAssociatedInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_size, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="PlantAssociatedInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_store_dur, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="PlantAssociatedInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_store_loc, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="PlantAssociatedInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_samp_store_temp, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_season_environment = Slot(uri=MIXS['0001068'], name="PlantAssociatedInterface_season_environment", curie=MIXS.curie('0001068'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_season_environment, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_size_frac = Slot(uri=MIXS['0000017'], name="PlantAssociatedInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_size_frac, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="PlantAssociatedInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_specific_ecosystem, domain=PlantAssociatedInterface, range=str)

slots.PlantAssociatedInterface_standing_water_regm = Slot(uri=MIXS['0001069'], name="PlantAssociatedInterface_standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_standing_water_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_temp = Slot(uri=MIXS['0000113'], name="PlantAssociatedInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_temp, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="PlantAssociatedInterface_tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_tiss_cult_growth_med, domain=PlantAssociatedInterface, range=Optional[str])

slots.PlantAssociatedInterface_water_temp_regm = Slot(uri=MIXS['0000590'], name="PlantAssociatedInterface_water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_water_temp_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.PlantAssociatedInterface_watering_regm = Slot(uri=MIXS['0000591'], name="PlantAssociatedInterface_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.PlantAssociatedInterface_watering_regm, domain=PlantAssociatedInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_alkalinity = Slot(uri=MIXS['0000421'], name="SedimentInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_alkalinity, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_alkyl_diethers = Slot(uri=MIXS['0000490'], name="SedimentInterface_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_alkyl_diethers, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_alt = Slot(uri=MIXS['0000094'], name="SedimentInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_alt, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_aminopept_act = Slot(uri=MIXS['0000172'], name="SedimentInterface_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_aminopept_act, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_ammonium = Slot(uri=MIXS['0000427'], name="SedimentInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ammonium, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="SedimentInterface_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_bacteria_carb_prod, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_biomass = Slot(uri=MIXS['0000174'], name="SedimentInterface_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_biomass, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_bishomohopanol = Slot(uri=MIXS['0000175'], name="SedimentInterface_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_bishomohopanol, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_bromide = Slot(uri=MIXS['0000176'], name="SedimentInterface_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_bromide, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_calcium = Slot(uri=MIXS['0000432'], name="SedimentInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_calcium, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="SedimentInterface_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_carb_nitro_ratio, domain=SedimentInterface, range=Optional[float])

slots.SedimentInterface_chem_administration = Slot(uri=MIXS['0000751'], name="SedimentInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_chem_administration, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_chloride = Slot(uri=MIXS['0000429'], name="SedimentInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_chloride, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_chlorophyll = Slot(uri=MIXS['0000177'], name="SedimentInterface_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_chlorophyll, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_collection_date = Slot(uri=MIXS['0000011'], name="SedimentInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_collection_date, domain=SedimentInterface, range=str)

slots.SedimentInterface_density = Slot(uri=MIXS['0000435'], name="SedimentInterface_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_density, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_depth = Slot(uri=MIXS['0000018'], name="SedimentInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_depth, domain=SedimentInterface, range=str)

slots.SedimentInterface_diether_lipids = Slot(uri=MIXS['0000178'], name="SedimentInterface_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diether_lipids, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="SedimentInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_carb_dioxide, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_diss_hydrogen = Slot(uri=MIXS['0000179'], name="SedimentInterface_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_hydrogen, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="SedimentInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_inorg_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_diss_org_carb = Slot(uri=MIXS['0000433'], name="SedimentInterface_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_org_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_diss_org_nitro = Slot(uri=MIXS['0000162'], name="SedimentInterface_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_org_nitro, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_diss_oxygen = Slot(uri=MIXS['0000119'], name="SedimentInterface_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_diss_oxygen, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="SedimentInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ecosystem, domain=SedimentInterface, range=str)

slots.SedimentInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="SedimentInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ecosystem_category, domain=SedimentInterface, range=str)

slots.SedimentInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="SedimentInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ecosystem_subtype, domain=SedimentInterface, range=str)

slots.SedimentInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="SedimentInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ecosystem_type, domain=SedimentInterface, range=str)

slots.SedimentInterface_elev = Slot(uri=MIXS['0000093'], name="SedimentInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_elev, domain=SedimentInterface, range=float)

slots.SedimentInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="SedimentInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_env_broad_scale, domain=SedimentInterface, range=str)

slots.SedimentInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="SedimentInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_env_local_scale, domain=SedimentInterface, range=str)

slots.SedimentInterface_env_medium = Slot(uri=MIXS['0000014'], name="SedimentInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_env_medium, domain=SedimentInterface, range=str)

slots.SedimentInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="SedimentInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_experimental_factor, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="SedimentInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_geo_loc_name, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_glucosidase_act = Slot(uri=MIXS['0000137'], name="SedimentInterface_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_glucosidase_act, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="SedimentInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_horizon_meth, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_lat_lon = Slot(uri=MIXS['0000009'], name="SedimentInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_lat_lon, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_magnesium = Slot(uri=MIXS['0000431'], name="SedimentInterface_magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_magnesium, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_mean_frict_vel = Slot(uri=MIXS['0000498'], name="SedimentInterface_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_mean_frict_vel, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="SedimentInterface_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_mean_peak_frict_vel, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_methane = Slot(uri=MIXS['0000101'], name="SedimentInterface_methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_methane, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_misc_param = Slot(uri=MIXS['0000752'], name="SedimentInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_misc_param, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_n_alkanes = Slot(uri=MIXS['0000503'], name="SedimentInterface_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_n_alkanes, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_nitrate = Slot(uri=MIXS['0000425'], name="SedimentInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_nitrate, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_nitrite = Slot(uri=MIXS['0000426'], name="SedimentInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_nitrite, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_nitro = Slot(uri=MIXS['0000504'], name="SedimentInterface_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_nitro, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_org_carb = Slot(uri=MIXS['0000508'], name="SedimentInterface_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_org_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_org_matter = Slot(uri=MIXS['0000204'], name="SedimentInterface_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_org_matter, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_org_nitro = Slot(uri=MIXS['0000205'], name="SedimentInterface_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_org_nitro, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_organism_count = Slot(uri=MIXS['0000103'], name="SedimentInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_organism_count, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="SedimentInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_oxy_stat_samp, domain=SedimentInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.SedimentInterface_part_org_carb = Slot(uri=MIXS['0000515'], name="SedimentInterface_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_part_org_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_particle_class = Slot(uri=MIXS['0000206'], name="SedimentInterface_particle_class", curie=MIXS.curie('0000206'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_particle_class, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_perturbation = Slot(uri=MIXS['0000754'], name="SedimentInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_perturbation, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="SedimentInterface_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_petroleum_hydrocarb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_ph = Slot(uri=MIXS['0001001'], name="SedimentInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ph, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_ph_meth = Slot(uri=MIXS['0001106'], name="SedimentInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_ph_meth, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_phaeopigments = Slot(uri=MIXS['0000180'], name="SedimentInterface_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_phaeopigments, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_phosphate = Slot(uri=MIXS['0000505'], name="SedimentInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_phosphate, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="SedimentInterface_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_phosplipid_fatt_acid, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SedimentInterface_porosity = Slot(uri=MIXS['0000211'], name="SedimentInterface_porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_porosity, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_potassium = Slot(uri=MIXS['0000430'], name="SedimentInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_potassium, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_pressure = Slot(uri=MIXS['0000412'], name="SedimentInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_pressure, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_redox_potential = Slot(uri=MIXS['0000182'], name="SedimentInterface_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_redox_potential, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="SedimentInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_rel_to_oxygen, domain=SedimentInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.SedimentInterface_salinity = Slot(uri=MIXS['0000183'], name="SedimentInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_salinity, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="SedimentInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_collec_device, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="SedimentInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_collec_method, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="SedimentInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_mat_process, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_size = Slot(uri=MIXS['0000001'], name="SedimentInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_size, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="SedimentInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_store_dur, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="SedimentInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_store_loc, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="SedimentInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_samp_store_temp, domain=SedimentInterface, range=str)

slots.SedimentInterface_sediment_type = Slot(uri=MIXS['0001078'], name="SedimentInterface_sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_sediment_type, domain=SedimentInterface, range=Optional[Union[str, "SedimentTypeEnum"]])

slots.SedimentInterface_silicate = Slot(uri=MIXS['0000184'], name="SedimentInterface_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_silicate, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_size_frac = Slot(uri=MIXS['0000017'], name="SedimentInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_size_frac, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_sodium = Slot(uri=MIXS['0000428'], name="SedimentInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_sodium, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="SedimentInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_specific_ecosystem, domain=SedimentInterface, range=str)

slots.SedimentInterface_sulfate = Slot(uri=MIXS['0000423'], name="SedimentInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_sulfate, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_sulfide = Slot(uri=MIXS['0000424'], name="SedimentInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_sulfide, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_temp = Slot(uri=MIXS['0000113'], name="SedimentInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_temp, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_tidal_stage = Slot(uri=MIXS['0000750'], name="SedimentInterface_tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_tidal_stage, domain=SedimentInterface, range=Optional[Union[str, "TidalStageEnum"]])

slots.SedimentInterface_tot_carb = Slot(uri=MIXS['0000525'], name="SedimentInterface_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_tot_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_tot_depth_water_col = Slot(uri=MIXS['0000634'], name="SedimentInterface_tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_tot_depth_water_col, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_tot_nitro_content = Slot(uri=MIXS['0000530'], name="SedimentInterface_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_tot_nitro_content, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_tot_org_carb = Slot(uri=MIXS['0000533'], name="SedimentInterface_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_tot_org_carb, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_turbidity = Slot(uri=MIXS['0000191'], name="SedimentInterface_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_turbidity, domain=SedimentInterface, range=Optional[str])

slots.SedimentInterface_water_content = Slot(uri=MIXS['0000185'], name="SedimentInterface_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.SedimentInterface_water_content, domain=SedimentInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_agrochem_addition = Slot(uri=MIXS['0000639'], name="SoilInterface_agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_agrochem_addition, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_air_temp_regm = Slot(uri=MIXS['0000551'], name="SoilInterface_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_air_temp_regm, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_al_sat = Slot(uri=MIXS['0000607'], name="SoilInterface_al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_al_sat, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_al_sat_meth = Slot(uri=MIXS['0000324'], name="SoilInterface_al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_al_sat_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_alt = Slot(uri=MIXS['0000094'], name="SoilInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_alt, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_ammonium_nitrogen = Slot(uri=NMDC_YAML['nmdc/ammonium_nitrogen'], name="SoilInterface_ammonium_nitrogen", curie=NMDC_YAML.curie('nmdc/ammonium_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ammonium_nitrogen, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_annual_precpt = Slot(uri=MIXS['0000644'], name="SoilInterface_annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_annual_precpt, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_annual_temp = Slot(uri=MIXS['0000642'], name="SoilInterface_annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_annual_temp, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_biotic_regm = Slot(uri=MIXS['0001038'], name="SoilInterface_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_biotic_regm, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_biotic_relationship = Slot(uri=MIXS['0000028'], name="SoilInterface_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_biotic_relationship, domain=SoilInterface, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.SoilInterface_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="SoilInterface_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_carb_nitro_ratio, domain=SoilInterface, range=Optional[float])

slots.SoilInterface_chem_administration = Slot(uri=MIXS['0000751'], name="SoilInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_chem_administration, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_climate_environment = Slot(uri=MIXS['0001040'], name="SoilInterface_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_climate_environment, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_collection_date = Slot(uri=MIXS['0000011'], name="SoilInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_collection_date, domain=SoilInterface, range=str)

slots.SoilInterface_crop_rotation = Slot(uri=MIXS['0000318'], name="SoilInterface_crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_crop_rotation, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_cur_land_use = Slot(uri=MIXS['0001080'], name="SoilInterface_cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_cur_land_use, domain=SoilInterface, range=Optional[Union[str, "CurLandUseEnum"]])

slots.SoilInterface_cur_vegetation = Slot(uri=MIXS['0000312'], name="SoilInterface_cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_cur_vegetation, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="SoilInterface_cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_cur_vegetation_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_depth = Slot(uri=MIXS['0000018'], name="SoilInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_depth, domain=SoilInterface, range=str)

slots.SoilInterface_drainage_class = Slot(uri=MIXS['0001085'], name="SoilInterface_drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_drainage_class, domain=SoilInterface, range=Optional[Union[str, "DrainageClassEnum"]])

slots.SoilInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="SoilInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ecosystem, domain=SoilInterface, range=str)

slots.SoilInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="SoilInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ecosystem_category, domain=SoilInterface, range=str)

slots.SoilInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="SoilInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ecosystem_subtype, domain=SoilInterface, range=str)

slots.SoilInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="SoilInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ecosystem_type, domain=SoilInterface, range=str)

slots.SoilInterface_elev = Slot(uri=MIXS['0000093'], name="SoilInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_elev, domain=SoilInterface, range=float)

slots.SoilInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="SoilInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_env_broad_scale, domain=SoilInterface, range=Union[str, "EnvBroadScaleSoilEnum"])

slots.SoilInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="SoilInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_env_local_scale, domain=SoilInterface, range=Union[str, "EnvLocalScaleSoilEnum"])

slots.SoilInterface_env_medium = Slot(uri=MIXS['0000014'], name="SoilInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_env_medium, domain=SoilInterface, range=Union[str, "EnvMediumSoilEnum"])

slots.SoilInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="SoilInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_experimental_factor, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_extreme_event = Slot(uri=MIXS['0000320'], name="SoilInterface_extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_extreme_event, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_fao_class = Slot(uri=MIXS['0001083'], name="SoilInterface_fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_fao_class, domain=SoilInterface, range=Optional[Union[str, "FaoClassEnum"]])

slots.SoilInterface_fire = Slot(uri=MIXS['0001086'], name="SoilInterface_fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_fire, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_flooding = Slot(uri=MIXS['0000319'], name="SoilInterface_flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_flooding, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_gaseous_environment = Slot(uri=MIXS['0000558'], name="SoilInterface_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_gaseous_environment, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="SoilInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_geo_loc_name, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_growth_facil = Slot(uri=MIXS['0001043'], name="SoilInterface_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_growth_facil, domain=SoilInterface, range=Union[str, "GrowthFacilEnum"])

slots.SoilInterface_heavy_metals = Slot(uri=MIXS['0000652'], name="SoilInterface_heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_heavy_metals, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_heavy_metals_meth = Slot(uri=MIXS['0000343'], name="SoilInterface_heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_heavy_metals_meth, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_humidity_regm = Slot(uri=MIXS['0000568'], name="SoilInterface_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_humidity_regm, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_lat_lon = Slot(uri=MIXS['0000009'], name="SoilInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_lat_lon, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_lbc_thirty = Slot(uri=NMDC_YAML['nmdc/lbc_thirty'], name="SoilInterface_lbc_thirty", curie=NMDC_YAML.curie('nmdc/lbc_thirty'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_lbc_thirty, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_lbceq = Slot(uri=NMDC_YAML['nmdc/lbceq'], name="SoilInterface_lbceq", curie=NMDC_YAML.curie('nmdc/lbceq'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_lbceq, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_light_regm = Slot(uri=MIXS['0000569'], name="SoilInterface_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_light_regm, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_link_class_info = Slot(uri=MIXS['0000329'], name="SoilInterface_link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_link_class_info, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_link_climate_info = Slot(uri=MIXS['0000328'], name="SoilInterface_link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_link_climate_info, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_local_class = Slot(uri=MIXS['0000330'], name="SoilInterface_local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_local_class, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_local_class_meth = Slot(uri=MIXS['0000331'], name="SoilInterface_local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_local_class_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_manganese = Slot(uri=NMDC_YAML['nmdc/manganese'], name="SoilInterface_manganese", curie=NMDC_YAML.curie('nmdc/manganese'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_manganese, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_micro_biomass_meth = Slot(uri=MIXS['0000339'], name="SoilInterface_micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_micro_biomass_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_microbial_biomass = Slot(uri=MIXS['0000650'], name="SoilInterface_microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_microbial_biomass, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_misc_param = Slot(uri=MIXS['0000752'], name="SoilInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_misc_param, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_nitrate_nitrogen = Slot(uri=NMDC_YAML['nmdc/nitrate_nitrogen'], name="SoilInterface_nitrate_nitrogen", curie=NMDC_YAML.curie('nmdc/nitrate_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_nitrate_nitrogen, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_nitrite_nitrogen = Slot(uri=NMDC_YAML['nmdc/nitrite_nitrogen'], name="SoilInterface_nitrite_nitrogen", curie=NMDC_YAML.curie('nmdc/nitrite_nitrogen'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_nitrite_nitrogen, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_org_matter = Slot(uri=MIXS['0000204'], name="SoilInterface_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_org_matter, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_org_nitro = Slot(uri=MIXS['0000205'], name="SoilInterface_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_org_nitro, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="SoilInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_oxy_stat_samp, domain=SoilInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.SoilInterface_ph = Slot(uri=MIXS['0001001'], name="SoilInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ph, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_ph_meth = Slot(uri=MIXS['0001106'], name="SoilInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_ph_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_phosphate = Slot(uri=MIXS['0000505'], name="SoilInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_phosphate, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_prev_land_use_meth = Slot(uri=MIXS['0000316'], name="SoilInterface_prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_prev_land_use_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_previous_land_use = Slot(uri=MIXS['0000315'], name="SoilInterface_previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_previous_land_use, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_profile_position = Slot(uri=MIXS['0001084'], name="SoilInterface_profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_profile_position, domain=SoilInterface, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.SoilInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="SoilInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_rel_to_oxygen, domain=SoilInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.SoilInterface_salinity = Slot(uri=MIXS['0000183'], name="SoilInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_salinity, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_salinity_meth = Slot(uri=MIXS['0000341'], name="SoilInterface_salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_salinity_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="SoilInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_samp_collec_device, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="SoilInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_samp_collec_method, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="SoilInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_samp_mat_process, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_samp_size = Slot(uri=MIXS['0000001'], name="SoilInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_samp_size, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="SoilInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_samp_store_temp, domain=SoilInterface, range=str)

slots.SoilInterface_season_precpt = Slot(uri=MIXS['0000645'], name="SoilInterface_season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_season_precpt, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_season_temp = Slot(uri=MIXS['0000643'], name="SoilInterface_season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_season_temp, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_sieving = Slot(uri=MIXS['0000322'], name="SoilInterface_sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_sieving, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_size_frac_low = Slot(uri=MIXS['0000735'], name="SoilInterface_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_size_frac_low, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_size_frac_up = Slot(uri=MIXS['0000736'], name="SoilInterface_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_size_frac_up, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_slope_aspect = Slot(uri=MIXS['0000647'], name="SoilInterface_slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_slope_aspect, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_slope_gradient = Slot(uri=MIXS['0000646'], name="SoilInterface_slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_slope_gradient, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_soil_horizon = Slot(uri=MIXS['0001082'], name="SoilInterface_soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_soil_horizon, domain=SoilInterface, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.SoilInterface_soil_text_measure = Slot(uri=MIXS['0000335'], name="SoilInterface_soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_soil_text_measure, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_soil_texture_meth = Slot(uri=MIXS['0000336'], name="SoilInterface_soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_soil_texture_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_soil_type = Slot(uri=MIXS['0000332'], name="SoilInterface_soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_soil_type, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_soil_type_meth = Slot(uri=MIXS['0000334'], name="SoilInterface_soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_soil_type_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="SoilInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_specific_ecosystem, domain=SoilInterface, range=str)

slots.SoilInterface_store_cond = Slot(uri=MIXS['0000327'], name="SoilInterface_store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_store_cond, domain=SoilInterface, range=Union[str, "StoreCondEnum"])

slots.SoilInterface_temp = Slot(uri=MIXS['0000113'], name="SoilInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_temp, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tillage = Slot(uri=MIXS['0001081'], name="SoilInterface_tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tillage, domain=SoilInterface, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.SoilInterface_tot_carb = Slot(uri=MIXS['0000525'], name="SoilInterface_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_carb, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="SoilInterface_tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_nitro_cont_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tot_nitro_content = Slot(uri=MIXS['0000530'], name="SoilInterface_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_nitro_content, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tot_org_c_meth = Slot(uri=MIXS['0000337'], name="SoilInterface_tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_org_c_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tot_org_carb = Slot(uri=MIXS['0000533'], name="SoilInterface_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_org_carb, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_tot_phosp = Slot(uri=MIXS['0000117'], name="SoilInterface_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_tot_phosp, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="SoilInterface_water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_water_cont_soil_meth, domain=SoilInterface, range=Optional[str])

slots.SoilInterface_water_content = Slot(uri=MIXS['0000185'], name="SoilInterface_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_water_content, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_watering_regm = Slot(uri=MIXS['0000591'], name="SoilInterface_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_watering_regm, domain=SoilInterface, range=Optional[Union[str, List[str]]])

slots.SoilInterface_zinc = Slot(uri=NMDC_YAML['nmdc/zinc'], name="SoilInterface_zinc", curie=NMDC_YAML.curie('nmdc/zinc'),
                   model_uri=NMDC_SUB_SCHEMA.SoilInterface_zinc, domain=SoilInterface, range=Optional[str])

slots.WastewaterSludgeInterface_alkalinity = Slot(uri=MIXS['0000421'], name="WastewaterSludgeInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_alkalinity, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_alt = Slot(uri=MIXS['0000094'], name="WastewaterSludgeInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_alt, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="WastewaterSludgeInterface_biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_biochem_oxygen_dem, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_chem_administration = Slot(uri=MIXS['0000751'], name="WastewaterSludgeInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_chem_administration, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="WastewaterSludgeInterface_chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_chem_oxygen_dem, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_collection_date = Slot(uri=MIXS['0000011'], name="WastewaterSludgeInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_collection_date, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_depth = Slot(uri=MIXS['0000018'], name="WastewaterSludgeInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_depth, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="WastewaterSludgeInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ecosystem, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="WastewaterSludgeInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ecosystem_category, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="WastewaterSludgeInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ecosystem_subtype, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="WastewaterSludgeInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ecosystem_type, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_efficiency_percent = Slot(uri=MIXS['0000657'], name="WastewaterSludgeInterface_efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_efficiency_percent, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_elev = Slot(uri=MIXS['0000093'], name="WastewaterSludgeInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_elev, domain=WastewaterSludgeInterface, range=float)

slots.WastewaterSludgeInterface_emulsions = Slot(uri=MIXS['0000660'], name="WastewaterSludgeInterface_emulsions", curie=MIXS.curie('0000660'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_emulsions, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="WastewaterSludgeInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_env_broad_scale, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="WastewaterSludgeInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_env_local_scale, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_env_medium = Slot(uri=MIXS['0000014'], name="WastewaterSludgeInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_env_medium, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="WastewaterSludgeInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_experimental_factor, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_gaseous_substances = Slot(uri=MIXS['0000661'], name="WastewaterSludgeInterface_gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_gaseous_substances, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="WastewaterSludgeInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_geo_loc_name, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="WastewaterSludgeInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_horizon_meth, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_indust_eff_percent = Slot(uri=MIXS['0000662'], name="WastewaterSludgeInterface_indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_indust_eff_percent, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_inorg_particles = Slot(uri=MIXS['0000664'], name="WastewaterSludgeInterface_inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_inorg_particles, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_lat_lon = Slot(uri=MIXS['0000009'], name="WastewaterSludgeInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_lat_lon, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_misc_param = Slot(uri=MIXS['0000752'], name="WastewaterSludgeInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_misc_param, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_nitrate = Slot(uri=MIXS['0000425'], name="WastewaterSludgeInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_nitrate, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_org_particles = Slot(uri=MIXS['0000665'], name="WastewaterSludgeInterface_org_particles", curie=MIXS.curie('0000665'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_org_particles, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_organism_count = Slot(uri=MIXS['0000103'], name="WastewaterSludgeInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_organism_count, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="WastewaterSludgeInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_oxy_stat_samp, domain=WastewaterSludgeInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.WastewaterSludgeInterface_perturbation = Slot(uri=MIXS['0000754'], name="WastewaterSludgeInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_perturbation, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_ph = Slot(uri=MIXS['0001001'], name="WastewaterSludgeInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ph, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_ph_meth = Slot(uri=MIXS['0001106'], name="WastewaterSludgeInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_ph_meth, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_phosphate = Slot(uri=MIXS['0000505'], name="WastewaterSludgeInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_phosphate, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_pre_treatment = Slot(uri=MIXS['0000348'], name="WastewaterSludgeInterface_pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_pre_treatment, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_primary_treatment = Slot(uri=MIXS['0000349'], name="WastewaterSludgeInterface_primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_primary_treatment, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_reactor_type = Slot(uri=MIXS['0000350'], name="WastewaterSludgeInterface_reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_reactor_type, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="WastewaterSludgeInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_rel_to_oxygen, domain=WastewaterSludgeInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.WastewaterSludgeInterface_salinity = Slot(uri=MIXS['0000183'], name="WastewaterSludgeInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_salinity, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="WastewaterSludgeInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_collec_device, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="WastewaterSludgeInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_collec_method, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="WastewaterSludgeInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_mat_process, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_size = Slot(uri=MIXS['0000001'], name="WastewaterSludgeInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_size, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="WastewaterSludgeInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_store_dur, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="WastewaterSludgeInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_store_loc, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="WastewaterSludgeInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_samp_store_temp, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_secondary_treatment = Slot(uri=MIXS['0000351'], name="WastewaterSludgeInterface_secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_secondary_treatment, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_sewage_type = Slot(uri=MIXS['0000215'], name="WastewaterSludgeInterface_sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_sewage_type, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_size_frac = Slot(uri=MIXS['0000017'], name="WastewaterSludgeInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_size_frac, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_sludge_retent_time = Slot(uri=MIXS['0000669'], name="WastewaterSludgeInterface_sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_sludge_retent_time, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_sodium = Slot(uri=MIXS['0000428'], name="WastewaterSludgeInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_sodium, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="WastewaterSludgeInterface_soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_soluble_inorg_mat, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_soluble_org_mat = Slot(uri=MIXS['0000673'], name="WastewaterSludgeInterface_soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_soluble_org_mat, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="WastewaterSludgeInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_specific_ecosystem, domain=WastewaterSludgeInterface, range=str)

slots.WastewaterSludgeInterface_suspend_solids = Slot(uri=MIXS['0000150'], name="WastewaterSludgeInterface_suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_suspend_solids, domain=WastewaterSludgeInterface, range=Optional[Union[str, List[str]]])

slots.WastewaterSludgeInterface_temp = Slot(uri=MIXS['0000113'], name="WastewaterSludgeInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_temp, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_tertiary_treatment = Slot(uri=MIXS['0000352'], name="WastewaterSludgeInterface_tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_tertiary_treatment, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_tot_nitro = Slot(uri=MIXS['0000102'], name="WastewaterSludgeInterface_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_tot_nitro, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_tot_phosphate = Slot(uri=MIXS['0000689'], name="WastewaterSludgeInterface_tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_tot_phosphate, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WastewaterSludgeInterface_wastewater_type = Slot(uri=MIXS['0000353'], name="WastewaterSludgeInterface_wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=NMDC_SUB_SCHEMA.WastewaterSludgeInterface_wastewater_type, domain=WastewaterSludgeInterface, range=Optional[str])

slots.WaterInterface_alkalinity = Slot(uri=MIXS['0000421'], name="WaterInterface_alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_alkalinity, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_alkalinity_method = Slot(uri=MIXS['0000298'], name="WaterInterface_alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_alkalinity_method, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_alkyl_diethers = Slot(uri=MIXS['0000490'], name="WaterInterface_alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_alkyl_diethers, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_alt = Slot(uri=MIXS['0000094'], name="WaterInterface_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_alt, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_aminopept_act = Slot(uri=MIXS['0000172'], name="WaterInterface_aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_aminopept_act, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_ammonium = Slot(uri=MIXS['0000427'], name="WaterInterface_ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ammonium, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_atmospheric_data = Slot(uri=MIXS['0001097'], name="WaterInterface_atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_atmospheric_data, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_bac_prod = Slot(uri=MIXS['0000683'], name="WaterInterface_bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_bac_prod, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_bac_resp = Slot(uri=MIXS['0000684'], name="WaterInterface_bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_bac_resp, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="WaterInterface_bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_bacteria_carb_prod, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_biomass = Slot(uri=MIXS['0000174'], name="WaterInterface_biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_biomass, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_bishomohopanol = Slot(uri=MIXS['0000175'], name="WaterInterface_bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_bishomohopanol, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_bromide = Slot(uri=MIXS['0000176'], name="WaterInterface_bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_bromide, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_calcium = Slot(uri=MIXS['0000432'], name="WaterInterface_calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_calcium, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="WaterInterface_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_carb_nitro_ratio, domain=WaterInterface, range=Optional[float])

slots.WaterInterface_chem_administration = Slot(uri=MIXS['0000751'], name="WaterInterface_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_chem_administration, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_chloride = Slot(uri=MIXS['0000429'], name="WaterInterface_chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_chloride, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_chlorophyll = Slot(uri=MIXS['0000177'], name="WaterInterface_chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_chlorophyll, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_collection_date = Slot(uri=MIXS['0000011'], name="WaterInterface_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_collection_date, domain=WaterInterface, range=str)

slots.WaterInterface_conduc = Slot(uri=MIXS['0000692'], name="WaterInterface_conduc", curie=MIXS.curie('0000692'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_conduc, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_density = Slot(uri=MIXS['0000435'], name="WaterInterface_density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_density, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_depth = Slot(uri=MIXS['0000018'], name="WaterInterface_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_depth, domain=WaterInterface, range=str)

slots.WaterInterface_diether_lipids = Slot(uri=MIXS['0000178'], name="WaterInterface_diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diether_lipids, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="WaterInterface_diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_carb_dioxide, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_hydrogen = Slot(uri=MIXS['0000179'], name="WaterInterface_diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_hydrogen, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_inorg_carb = Slot(uri=MIXS['0000434'], name="WaterInterface_diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_inorg_carb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="WaterInterface_diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_inorg_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="WaterInterface_diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_inorg_phosp, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_org_carb = Slot(uri=MIXS['0000433'], name="WaterInterface_diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_org_carb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_org_nitro = Slot(uri=MIXS['0000162'], name="WaterInterface_diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_org_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_diss_oxygen = Slot(uri=MIXS['0000119'], name="WaterInterface_diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_diss_oxygen, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_down_par = Slot(uri=MIXS['0000703'], name="WaterInterface_down_par", curie=MIXS.curie('0000703'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_down_par, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_ecosystem = Slot(uri=NMDC_YAML['nmdc/ecosystem'], name="WaterInterface_ecosystem", curie=NMDC_YAML.curie('nmdc/ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ecosystem, domain=WaterInterface, range=str)

slots.WaterInterface_ecosystem_category = Slot(uri=NMDC_YAML['nmdc/ecosystem_category'], name="WaterInterface_ecosystem_category", curie=NMDC_YAML.curie('nmdc/ecosystem_category'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ecosystem_category, domain=WaterInterface, range=str)

slots.WaterInterface_ecosystem_subtype = Slot(uri=NMDC_YAML['nmdc/ecosystem_subtype'], name="WaterInterface_ecosystem_subtype", curie=NMDC_YAML.curie('nmdc/ecosystem_subtype'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ecosystem_subtype, domain=WaterInterface, range=str)

slots.WaterInterface_ecosystem_type = Slot(uri=NMDC_YAML['nmdc/ecosystem_type'], name="WaterInterface_ecosystem_type", curie=NMDC_YAML.curie('nmdc/ecosystem_type'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ecosystem_type, domain=WaterInterface, range=str)

slots.WaterInterface_elev = Slot(uri=MIXS['0000093'], name="WaterInterface_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_elev, domain=WaterInterface, range=float)

slots.WaterInterface_env_broad_scale = Slot(uri=MIXS['0000012'], name="WaterInterface_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_env_broad_scale, domain=WaterInterface, range=str)

slots.WaterInterface_env_local_scale = Slot(uri=MIXS['0000013'], name="WaterInterface_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_env_local_scale, domain=WaterInterface, range=str)

slots.WaterInterface_env_medium = Slot(uri=MIXS['0000014'], name="WaterInterface_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_env_medium, domain=WaterInterface, range=str)

slots.WaterInterface_experimental_factor = Slot(uri=MIXS['0000008'], name="WaterInterface_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_experimental_factor, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_fluor = Slot(uri=MIXS['0000704'], name="WaterInterface_fluor", curie=MIXS.curie('0000704'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_fluor, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_geo_loc_name = Slot(uri=MIXS['0000010'], name="WaterInterface_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_geo_loc_name, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_glucosidase_act = Slot(uri=MIXS['0000137'], name="WaterInterface_glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_glucosidase_act, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_horizon_meth = Slot(uri=MIXS['0000321'], name="WaterInterface_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_horizon_meth, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_lat_lon = Slot(uri=MIXS['0000009'], name="WaterInterface_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_lat_lon, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_light_intensity = Slot(uri=MIXS['0000706'], name="WaterInterface_light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_light_intensity, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_mean_frict_vel = Slot(uri=MIXS['0000498'], name="WaterInterface_mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_mean_frict_vel, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="WaterInterface_mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_mean_peak_frict_vel, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_misc_param = Slot(uri=MIXS['0000752'], name="WaterInterface_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_misc_param, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_n_alkanes = Slot(uri=MIXS['0000503'], name="WaterInterface_n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_n_alkanes, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_nitrate = Slot(uri=MIXS['0000425'], name="WaterInterface_nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_nitrate, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_nitrite = Slot(uri=MIXS['0000426'], name="WaterInterface_nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_nitrite, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_nitro = Slot(uri=MIXS['0000504'], name="WaterInterface_nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_org_carb = Slot(uri=MIXS['0000508'], name="WaterInterface_org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_org_carb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_org_matter = Slot(uri=MIXS['0000204'], name="WaterInterface_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_org_matter, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_org_nitro = Slot(uri=MIXS['0000205'], name="WaterInterface_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_org_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_organism_count = Slot(uri=MIXS['0000103'], name="WaterInterface_organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_organism_count, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="WaterInterface_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_oxy_stat_samp, domain=WaterInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.WaterInterface_part_org_carb = Slot(uri=MIXS['0000515'], name="WaterInterface_part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_part_org_carb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_part_org_nitro = Slot(uri=MIXS['0000719'], name="WaterInterface_part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_part_org_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_perturbation = Slot(uri=MIXS['0000754'], name="WaterInterface_perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_perturbation, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="WaterInterface_petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_petroleum_hydrocarb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_ph = Slot(uri=MIXS['0001001'], name="WaterInterface_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ph, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_ph_meth = Slot(uri=MIXS['0001106'], name="WaterInterface_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_ph_meth, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_phaeopigments = Slot(uri=MIXS['0000180'], name="WaterInterface_phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_phaeopigments, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_phosphate = Slot(uri=MIXS['0000505'], name="WaterInterface_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_phosphate, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="WaterInterface_phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_phosplipid_fatt_acid, domain=WaterInterface, range=Optional[Union[str, List[str]]])

slots.WaterInterface_photon_flux = Slot(uri=MIXS['0000725'], name="WaterInterface_photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_photon_flux, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_potassium = Slot(uri=MIXS['0000430'], name="WaterInterface_potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_potassium, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_pressure = Slot(uri=MIXS['0000412'], name="WaterInterface_pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_pressure, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_primary_prod = Slot(uri=MIXS['0000728'], name="WaterInterface_primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_primary_prod, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_redox_potential = Slot(uri=MIXS['0000182'], name="WaterInterface_redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_redox_potential, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="WaterInterface_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_rel_to_oxygen, domain=WaterInterface, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.WaterInterface_salinity = Slot(uri=MIXS['0000183'], name="WaterInterface_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_salinity, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_collec_device = Slot(uri=MIXS['0000002'], name="WaterInterface_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_collec_device, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_collec_method = Slot(uri=MIXS['0001225'], name="WaterInterface_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_collec_method, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_mat_process = Slot(uri=MIXS['0000016'], name="WaterInterface_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_mat_process, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_size = Slot(uri=MIXS['0000001'], name="WaterInterface_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_size, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_store_dur = Slot(uri=MIXS['0000116'], name="WaterInterface_samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_store_dur, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_store_loc = Slot(uri=MIXS['0000755'], name="WaterInterface_samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_store_loc, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_samp_store_temp = Slot(uri=MIXS['0000110'], name="WaterInterface_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_samp_store_temp, domain=WaterInterface, range=str)

slots.WaterInterface_silicate = Slot(uri=MIXS['0000184'], name="WaterInterface_silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_silicate, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_size_frac = Slot(uri=MIXS['0000017'], name="WaterInterface_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_size_frac, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_size_frac_low = Slot(uri=MIXS['0000735'], name="WaterInterface_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_size_frac_low, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_size_frac_up = Slot(uri=MIXS['0000736'], name="WaterInterface_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_size_frac_up, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_sodium = Slot(uri=MIXS['0000428'], name="WaterInterface_sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_sodium, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_soluble_react_phosp = Slot(uri=MIXS['0000738'], name="WaterInterface_soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_soluble_react_phosp, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_specific_ecosystem = Slot(uri=NMDC_YAML['nmdc/specific_ecosystem'], name="WaterInterface_specific_ecosystem", curie=NMDC_YAML.curie('nmdc/specific_ecosystem'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_specific_ecosystem, domain=WaterInterface, range=str)

slots.WaterInterface_sulfate = Slot(uri=MIXS['0000423'], name="WaterInterface_sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_sulfate, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_sulfide = Slot(uri=MIXS['0000424'], name="WaterInterface_sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_sulfide, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_suspend_part_matter = Slot(uri=MIXS['0000741'], name="WaterInterface_suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_suspend_part_matter, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_temp = Slot(uri=MIXS['0000113'], name="WaterInterface_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_temp, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_tidal_stage = Slot(uri=MIXS['0000750'], name="WaterInterface_tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tidal_stage, domain=WaterInterface, range=Optional[Union[str, "TidalStageEnum"]])

slots.WaterInterface_tot_depth_water_col = Slot(uri=MIXS['0000634'], name="WaterInterface_tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tot_depth_water_col, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_tot_diss_nitro = Slot(uri=MIXS['0000744'], name="WaterInterface_tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tot_diss_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="WaterInterface_tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tot_inorg_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_tot_nitro = Slot(uri=MIXS['0000102'], name="WaterInterface_tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tot_nitro, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_tot_part_carb = Slot(uri=MIXS['0000747'], name="WaterInterface_tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_tot_part_carb, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_turbidity = Slot(uri=MIXS['0000191'], name="WaterInterface_turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_turbidity, domain=WaterInterface, range=Optional[str])

slots.WaterInterface_water_current = Slot(uri=MIXS['0000203'], name="WaterInterface_water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC_SUB_SCHEMA.WaterInterface_water_current, domain=WaterInterface, range=Optional[str])

slots.DhMultiviewCommonColumns_source_mat_id = Slot(uri=MIXS['0000026'], name="DhMultiviewCommonColumns_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC_SUB_SCHEMA.DhMultiviewCommonColumns_source_mat_id, domain=DhMultiviewCommonColumns, range=Union[str, DhMultiviewCommonColumnsSourceMatId])

slots.DhMultiviewCommonColumns_samp_name = Slot(uri=MIXS['0001107'], name="DhMultiviewCommonColumns_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC_SUB_SCHEMA.DhMultiviewCommonColumns_samp_name, domain=DhMultiviewCommonColumns, range=Optional[str])

slots.AttributeValue_type = Slot(uri=NMDC_SUB_SCHEMA.type, name="AttributeValue_type", curie=NMDC_SUB_SCHEMA.curie('type'),
                   model_uri=NMDC_SUB_SCHEMA.AttributeValue_type, domain=AttributeValue, range=Optional[str])

slots.Activity_id = Slot(uri=NMDC_SUB_SCHEMA.id, name="Activity_id", curie=NMDC_SUB_SCHEMA.curie('id'),
                   model_uri=NMDC_SUB_SCHEMA.Activity_id, domain=Activity, range=Union[str, ActivityId])