import pprint
import pandas as pd
from linkml_runtime import SchemaView
from rdflib import Graph, URIRef, RDFS
import re
import os
import click
from typing import List, Dict, Set, Optional

# Constants
ROOT_SUBSET = URIRef("http://purl.obolibrary.org/obo/ENVO_03605010")
NMDC_SUB_SCHEMA_DOCS_BASE = "https://microbiomedata.github.io/submission-schema/"

PREFIX_MAP = {
    "http://purl.obolibrary.org/obo/ENVO_": "ENVO:"
}


def extract_brackets(strings: List[str]) -> List[Optional[str]]:
    """
    Extract content within square brackets from each string in the list.

    This function is used to extract CURIEs from permissible values in the submission schema.

    Args:
        strings (List[str]): List of strings potentially containing bracketed content.

    Returns:
        List[Optional[str]]: Extracted content or None if no brackets are found.
    """
    pattern = re.compile(r'\[(.*?)\]')
    return [match.group(1) if (match := pattern.search(s)) else None for s in strings]


def get_recursive_subproperties(graph: Graph, property_uri: URIRef) -> Set[URIRef]:
    """
    Recursively retrieve all subproperties of a given property in the RDF graph.

    This identifies all EnvO classes that are part of a specific subset hierarchy.

    Args:
        graph (Graph): RDF graph representing the EnvO ontology.
        property_uri (URIRef): URI of the root subset to explore.

    Returns:
        Set[URIRef]: All discovered subproperties.
    """
    subproperties = set()
    to_explore = [property_uri]
    while to_explore:
        current = to_explore.pop()
        for s in graph.subjects(predicate=RDFS.subPropertyOf, object=current):
            if s not in subproperties:
                subproperties.add(s)
                to_explore.append(s)
    return subproperties


def load_ontology(file_path: str) -> Graph:
    """
    Load an OWL ontology into an RDF graph.

    Args:
        file_path (str): Path to the ontology file.

    Returns:
        Graph: RDF graph of the ontology.

    Raises:
        FileNotFoundError: If the ontology file does not exist.
        ValueError: If the ontology file cannot be parsed.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Ontology file not found: {file_path}")
    graph = Graph()
    try:
        graph.parse(file_path, format="xml")
    except Exception as e:
        raise ValueError(f"Failed to parse ontology file {file_path}: {e}")
    return graph


def iri_to_curie(iri: URIRef) -> Optional[str]:
    """
    Convert an IRI to a CURIE using the defined prefix mapping.

    Args:
        iri (URIRef): IRI to convert.

    Returns:
        Optional[str]: CURIE representation if the prefix matches, else None.
    """
    iri_str = str(iri)
    for uri_prefix, curie_prefix in PREFIX_MAP.items():
        if iri_str.startswith(uri_prefix):
            return iri_str.replace(uri_prefix, curie_prefix)
    return None


def curie_to_iri(curie: str) -> Optional[URIRef]:
    """
    Convert a CURIE to its corresponding IRI.

    Args:
        curie (str): CURIE string to convert.

    Returns:
        Optional[URIRef]: Converted IRI, or None if the CURIE prefix is unknown.
    """
    for uri_prefix, curie_prefix in PREFIX_MAP.items():
        if curie.startswith(curie_prefix):
            return URIRef(curie.replace(curie_prefix, uri_prefix))
    return None


def get_rdfs_label(graph: Graph, iri: URIRef) -> Optional[str]:
    """
    Retrieve the rdfs:label for a given IRI.

    Args:
        graph (Graph): RDF graph to search.
        iri (URIRef): IRI of the entity.

    Returns:
        Optional[str]: Label if found, else None.
    """
    labels = list(graph.objects(subject=iri, predicate=RDFS.label))
    return str(labels[0]) if labels else None


def create_see_also_dict(graph: Graph, properties: Set[URIRef]) -> Dict[str, List[str]]:
    """
    Map subset CURIEs to their associated seeAlso documentation links.

    Args:
        graph (Graph): RDF graph of EnvO ontology.
        properties (Set[URIRef]): Set of subset URIs.

    Returns:
        Dict[str, List[str]]: Mapping of subset CURIEs to seeAlso links.
    """
    see_also_dict = {}
    for prop in properties:
        see_alsos = [str(link).replace(NMDC_SUB_SCHEMA_DOCS_BASE, "").rstrip('/')
                     for link in graph.objects(subject=prop, predicate=RDFS.seeAlso)
                     if str(link).startswith(NMDC_SUB_SCHEMA_DOCS_BASE)]
        if see_alsos:
            curie = iri_to_curie(prop)
            if curie:
                see_also_dict[curie] = see_alsos
    return see_also_dict


@click.command()
@click.option('--envo-owl-path', type=click.Path(exists=True), default='../../../envo.owl',
              help='Path to the ENVO OWL file.')
@click.option('--schema-path', type=click.Path(exists=True),
              default='../../../src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml',
              help='Path to the NMDC submission schema YAML file.')
@click.option('--output-file', type=click.Path(), default='../nmdc_env_context_subset_membership.tsv',
              help='Path to save the output TSV file.')
def main(envo_owl_path: str, schema_path: str, output_file: str):
    """
    Generate a TSV ROBOT template asserting in-subset relationships between EnvO classes and NMDC-defined subsets.

    This script cross-references EnvO ontology subsets with NMDC enumeration documentation
    to identify and record valid in-subset relationships.
    """
    schema_view = SchemaView(schema_path)
    ontology_graph = load_ontology(envo_owl_path)
    subproperties = get_recursive_subproperties(ontology_graph, ROOT_SUBSET)
    subproperties.add(ROOT_SUBSET)

    see_alsos_dict = create_see_also_dict(ontology_graph, subproperties)

    df = pd.DataFrame([{'ID': 'ID', 'label for convenience': '',
                        'subset': 'AI http://www.geneontology.org/formats/oboInOwl#inSubset'}])

    for subset, classes in see_alsos_dict.items():
        for sem_class in classes:
            ed = schema_view.get_enum(sem_class)
            if ed and hasattr(ed, 'permissible_values'):
                for pv in filter(None, extract_brackets(ed.permissible_values)):
                    iri = curie_to_iri(pv)
                    label = get_rdfs_label(ontology_graph, iri) if iri else None
                    if label:
                        df.loc[len(df)] = [pv, label, subset]
                    else:
                        print(f"[ERROR] Missing label for {pv}")

    df.to_csv(output_file, sep='\t', index=False)
    print(f"TSV file saved to '{output_file}'")


if __name__ == "__main__":
    main()

# from oaklib import get_adapter
# from oaklib.datamodels.vocabulary import IS_A
#
# # assumes there's an envo.db in the oaklib cache (~/.data/oaklib) that already has the subset annotation properties defined
# #   and see_also annotated with URLs for enumeration documentation pages from the submission schema
# #   like https://microbiomedata.github.io/submission-schema/EnvBroadScaleSoilEnum/
# #   building the envo.owl file locally is recommended
# #   the database can be then generated with the sem-sql project with this command
# #   semsql make envo.db
#
# # envo_adapter_string = "sqlite:obo:envo"
# envo_adapter_string = "sqlite:../../../envo.owl"
#
# root_property = "ENVO:03605010"
#
# output_file = '../nmdc_env_context_subset_membership.tsv'
#
#
# def get_all_subproperties(adapter, root_property):
#     """
#     Recursively fetch all subproperties of the root_property.
#     """
#     collected = set()
#     to_process = [root_property]
#
#     while to_process:
#         current = to_process.pop()
#         subproperties = adapter.relationships(objects=[current], predicates=['rdfs:subPropertyOf'])
#         for subproperty, _, _ in subproperties:
#             if subproperty not in collected:
#                 collected.add(subproperty)
#                 to_process.append(subproperty)
#     return collected
#
#
# envo_adapter = get_adapter(envo_adapter_string) # a SqlImplementation
#
# subs = get_all_subproperties(envo_adapter, root_property)
# pprint.pprint(subs)
#
# for subp in subs:
#     print(subp)
#     emm = envo_adapter.entity_metadata_map(subp)
#     pprint.pprint(emm)
