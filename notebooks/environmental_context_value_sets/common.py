from operator import index

from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A, PART_OF
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
import requests
import pprint

from typing import Dict, Any
import csv

from sklearn.feature_extraction.text import CountVectorizer  # from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from scipy.sparse import hstack

import re

import os

import duckdb
import sqlite3

import gzip
import shutil

from urllib.parse import urlparse




# todo is filling memory with things like this a good idea? for understandability? or performance?
# todo they should be aggregated somewhere, as specified by the config.yaml
# todo or should we going straight to data frames? in which case a dlist of dicts might be preferable
def get_curie_descendants_label_dict(curie, predicates, adapter):
    curie_label_dict = {}
    for descendant in adapter.descendants(curie, predicates=predicates):
        curie_label_dict[descendant] = adapter.label(descendant)
    return curie_label_dict


def curie_descendants_label_dict_to_lod(curie_label_dict):
    return [{'curie': k, 'label': v} for k, v in curie_label_dict.items()]


def curie_descendants_label_lod_to_df(curie_label_lod):
    return pd.DataFrame(curie_label_lod)


def get_schemaview_from_source(source):
    return SchemaView(source)


# def get_schema_from_schemaview(schemaview):
#     return schemaview.schema

def parse_hierarchically_underscored_strings(hierarchically_underscored_string_list):
    result = []
    for item in hierarchically_underscored_string_list:
        # Remove leading underscores for label, split on '[' to separate curie
        label, curie = item.lstrip('_').split(' [')
        # Remove the trailing ']' from curie
        curie = curie.rstrip(']')
        # Append dictionary with label and curie
        result.append({'label': label.strip(), 'curie': curie.strip()})
    return result


def dedupe_underscoreless_pvs(underscoreless_pvs):
    # Dictionary to store CURIE as key and list of unique labels as values
    curie_to_labels = {}

    for item in underscoreless_pvs:
        curie = item['curie']
        label = item['label']

        # Initialize the list if curie is not yet a key
        if curie not in curie_to_labels:
            curie_to_labels[curie] = []

        # Add label if it is not already in the list for this curie
        if label not in curie_to_labels[curie]:
            curie_to_labels[curie].append(label)
    return curie_to_labels


def validate_curie_label_list_dict(curie_label_dict, adapter, print_flag=False):
    problem_curies = []
    valid_curies = []
    for curie, labels in curie_label_dict.items():
        true_label = adapter.label(curie)
        if true_label not in labels:
            problem_curies.append(curie)
            if print_flag:
                print(f"Error: {curie} has true label {true_label} which doesn't appear in {labels}")
        else:
            valid_curies.append({"curie": curie, "label": true_label})
    return {"problems": problem_curies, "valids": valid_curies}


# todo could pre-determine the collection sizes
# todo could report elapsed time

def get_docs_from_nmdc_collection(base_url, collection_name, max_page_size=1000, stop_after=None):
    """
    Fetch all documents from a paginated API. Defaults to fetching a large number of documents per page.
    Optionally stop after a specified number of documents.

    Parameters:
    - base_url: The base URL of the API endpoint (e.g., 'https://api.microbiomedata.org/nmdcschema/').
    - collection_name: The name of the collection to fetch (e.g., 'biosample_set').
    - max_page_size: The maximum number of items to retrieve per page (default 1000).
    - stop_after: Optional parameter to stop fetching after a certain number of documents (default None).

    Returns:
    - A list of documents fetched from the API.
    """
    documents = []
    page_token = None
    total_documents = 0
    page_count = 0

    # Construct the full URL with the collection name
    url = f"{base_url}{collection_name}"

    while True:
        page_count += 1
        # Prepare the query parameters
        params = {
            'collection_name': collection_name,
            'max_page_size': max_page_size,  # Set large max_page_size to reduce pagination
        }

        if page_token:
            params['page_token'] = page_token  # Add the page token for pagination

        # Send the request to the API
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            break

        data = response.json()

        # Add the current page of documents to the list
        num_documents_on_page = len(data['resources'])
        documents.extend(data['resources'])
        total_documents += num_documents_on_page

        # Status reporting
        print(f"Fetched page {page_count} with {num_documents_on_page} documents. Total fetched: {total_documents}")

        # If stop_after is provided, stop fetching after reaching the specified number of documents
        if stop_after and total_documents >= stop_after:
            documents = documents[:stop_after]  # Trim to the required number
            print(f"Reached stop_after limit of {stop_after} documents.")
            break

        # Check if there is a next page
        page_token = data.get('next_page_token')
        if not page_token:
            print("All documents fetched.")
            break  # Exit the loop if no more pages are available

    return documents


def get_name_or_rawval(env_scale: Dict[str, Any]) -> str:
    """Safely extract label from environmental scale data."""
    if env_scale:
        term = env_scale.get('term')
        if term:
            return term.get('name', term.get('has_raw_value', ''))
    return ''


def tsv_to_dict_of_dicts(tsv_file, outer_key_column):
    """
    Reads a TSV file into a dictionary of dictionaries.

    :param tsv_file: Path to the TSV file.
    :param outer_key_column: The column name or index to be used as the key for the outer dictionary.
    :return: A dictionary of dictionaries, with outer keys being the values from the specified column.
    """
    with open(tsv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')

        result = {}

        for row in reader:
            outer_key = row[outer_key_column]
            result[outer_key] = {key: value for key, value in row.items() if key != outer_key_column}

    return result


# todo only gets authoritative labels from the passed adapter, which is presumably EnvO only
# todo would benefit from caching of labels

def biosamples_lod_context_extractor(biosamples_lod, adapter, env_pacakge_overrides=None):
    new_lod = []
    for biosample in biosamples_lod:
        insdc_identifiers = biosample.get('insdc_biosample_identifiers', [])

        env_broad_scale_label = get_name_or_rawval(biosample.get('env_broad_scale'))
        env_local_scale_label = get_name_or_rawval(biosample.get('env_local_scale'))
        env_medium_label = get_name_or_rawval(biosample.get('env_medium'))

        # Extracting optional scalar env_package.has_raw_value
        env_package_has_raw_value = biosample.get('env_package', {}).get('has_raw_value', '')

        # Extracting required multivalued part_of
        associated_studies = '|'.join(biosample.get('associated_studies', []))  # Assuming part_of is a list of strings

        row: Dict[str, str] = {
            'id': biosample['id'],
            'insdc_biosample_identifiers': '|'.join(insdc_identifiers) if insdc_identifiers else '',

            'env_broad_scale_id': biosample['env_broad_scale']['term']['id'],
            'env_broad_scale_mongo_label': env_broad_scale_label,
            'env_broad_scale_auth_label': adapter.label(biosample['env_broad_scale']['term']['id']),

            'env_local_scale_id': biosample['env_local_scale']['term']['id'],
            'env_local_scale_mongo_label': env_local_scale_label,
            'env_local_scale_auth_label': adapter.label(biosample['env_local_scale']['term']['id']),

            'env_medium_id': biosample['env_medium']['term']['id'],
            'env_medium_mongo_label': env_medium_label,
            'env_medium_auth_label': adapter.label(biosample['env_medium']['term']['id']),

            'env_package_has_raw_value': env_package_has_raw_value,
            'normalized_env_package': 'soil' if env_package_has_raw_value == 'ENVO:00001998' else env_package_has_raw_value.lower(),
            # todo abstract this though label search, or at least providing a lookup structure

            'associated_studies': associated_studies
        }

        if env_pacakge_overrides and biosample['id'] in env_pacakge_overrides:
            print(
                f"Overriding env_package for biosample {biosample['id']} from {row['normalized_env_package']} to {env_pacakge_overrides[biosample['id']]['mam_inferred_env_package']}")
            row['normalized_env_package'] = env_pacakge_overrides[biosample['id']]['mam_inferred_env_package']

        new_lod.append(row)
    return new_lod


def get_hierarchy_terms(curie: str, adapter) -> dict:
    """
    Extract ancestor and descendant terms from the ontology for a given CURIE,
    using caching to improve performance and filtering by 'is_a' relationships.

    Args:
        curie (str): CURIE identifier for the ontology term.
        adapter: Ontology adapter.

    Returns:
        dict: Dictionary containing lists of ancestor and descendant terms.
    """
    if curie in ancestor_cache:
        ancestors = ancestor_cache[curie]
    else:
        try:
            ancestors = list(adapter.ancestors(curie, predicates=[IS_A]))
            ancestor_cache[curie] = [adapter.label(ancestor) for ancestor in ancestors if ancestor]
        except Exception as e:
            print(f"Error retrieving ancestors for {curie}: {e}")
            ancestor_cache[curie] = []

    if curie in descendant_cache:
        descendants = descendant_cache[curie]
    else:
        try:
            descendants = list(adapter.descendants(curie, predicates=[IS_A]))
            descendant_cache[curie] = [adapter.label(descendant) for descendant in descendants if descendant]
        except Exception as e:
            print(f"Error retrieving descendants for {curie}: {e}")
            descendant_cache[curie] = []

    return {
        'ancestors': ancestor_cache[curie],
        'descendants': descendant_cache[curie],
    }


def vectorize_terms(df, column):
    """
    Vectorize the ancestor or descendant terms for a given column.

    Args:
        df (pd.DataFrame): The input dataframe.
        column (str): The column name to vectorize.

    Returns:
        sparse matrix: The vectorized term matrix.
    """
    vectorizer = CountVectorizer()
    return vectorizer.fit_transform(
        df[column].apply(lambda x: ' '.join([str(term) for term in x if term is not None]) if x is not None else '')
    )


def predict_from_normalized_env_packages(df_raw, adapter):
    # Apply the function to the relevant columns

    df = df_raw.copy()
    for column in ['env_broad_scale_id', 'env_local_scale_id', 'env_medium_id']:
        df[f'{column}_ancestors'] = df[column].apply(lambda x: get_hierarchy_terms(x, adapter)['ancestors'])
        df[f'{column}_descendants'] = df[column].apply(lambda x: get_hierarchy_terms(x, adapter)['descendants'])

    # Vectorize each set of terms separately
    broad_scale_ancestors = vectorize_terms(df, 'env_broad_scale_id_ancestors')
    broad_scale_descendants = vectorize_terms(df, 'env_broad_scale_id_descendants')

    local_scale_ancestors = vectorize_terms(df, 'env_local_scale_id_ancestors')
    local_scale_descendants = vectorize_terms(df, 'env_local_scale_id_descendants')

    medium_ancestors = vectorize_terms(df, 'env_medium_id_ancestors')
    medium_descendants = vectorize_terms(df, 'env_medium_id_descendants')

    # Combine all feature matrices
    X = hstack([
        broad_scale_ancestors,
        broad_scale_descendants,
        local_scale_ancestors,
        local_scale_descendants,
        medium_ancestors,
        medium_descendants
    ])

    # Filter the DataFrame to only include non-null rows for the target column
    df_filtered = df[df['normalized_env_package'].notnull() & (df['normalized_env_package'] != "")]

    # Extract the target variable
    y = df_filtered['normalized_env_package']

    # Ensure X corresponds to the filtered rows
    X_filtered = X[df_filtered.index]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_filtered, y, test_size=0.3, random_state=42)

    # Train a Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    print(classification_report(y_test, y_pred))

    # # Predict the normalized_env_package for all rows
    # df['predicted_normalized_env_package'] = clf.predict(X)

    # # If you want to add confidence scores for each class
    # class_probabilities = clf.predict_proba(X)
    # 
    # # Get the class labels from the model
    # class_labels = clf.classes_
    # 
    # # Add a column for each class with the corresponding confidence score
    # for i, class_label in enumerate(class_labels):
    #     df[f'confidence_{class_label}'] = class_probabilities[:, i]
    # 
    # return df

    return clf.predict(X)


def parse_curie_label(text, approved_prefixes=['ENVO']):
    # Case-insensitive pattern for matching approved prefixes followed by an ID
    pattern = r'\b(?:' + '|'.join(approved_prefixes) + r')\s*[:_]\s*(\d+)\b'
    curie_match = re.search(pattern, text, re.IGNORECASE)

    if curie_match:
        curie = f"{approved_prefixes[0].upper()}:{curie_match.group(1)}"  # standardize prefix to 'ENVO:ID'
        label = re.sub(pattern, "", text).strip("[]() ")
        # replace any colons in the label with a whitespace
        return pd.Series([label, curie])
    else:
        label = re.sub(r':', ' ', text)
        return pd.Series([label, None])  # No CURIE found, return original label and None for CURIE


def get_longest_annotation_curie(text, adapter):
    annotations = adapter.annotate_text(text)
    if not annotations:  # Check if annotations list is empty
        return None
    try:
        longest_annotation = max(annotations, key=lambda x: x.subject_end - x.subject_start)
        return longest_annotation.object_id
    except ValueError:
        return None  # Return None if there's an unexpected issue with finding the max
