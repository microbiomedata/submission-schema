import csv
import math
import os
import pprint
import string

import dotenv
import pandas as pd
import requests
import yaml

dotenv_path = "../../../local/.env"
dotenv.load_dotenv(dotenv_path)
google_maps_key_val = os.environ.get('GOOGLE_MAPS_API_KEY')


def get_elevation_from_google_maps_api(lat, lon, google_maps_key_val, geocoding_base_url):
    params = {
        "locations": f"{lat},{lon}",  # process multiple locations?
        "key": google_maps_key_val,
    }
    elev = requests.get(url=geocoding_base_url, params=params)
    print(elev.json())


def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Radius of the Earth in kilometers
    radius = 6371.0  # Earth's radius in kilometers

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = radius * c

    return distance


def read_yaml_file(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data


def read_tsv_file(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        rows = []
        for row in reader:
            rows.append(row)
    return rows


def dump_dict_to_tsv(tsv_file, lod_to_dump, fieldnames):
    with open(tsv_file, 'w', encoding='utf-8') as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in lod_to_dump:
            writer.writerow(row)


def load_lines_from_file(file_path):
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            lines.append(line)
    return lines


def replace_punctuation(text):
    punctuation = string.punctuation
    for char in punctuation:
        text = text.replace(char, ' ')
    return text


def replace_multiple_whitespace(text):
    return " ".join(text.split())


def normalize_address(raw_address):
    temp = raw_address.lower()
    temp = replace_punctuation(temp)
    temp = replace_multiple_whitespace(temp)
    temp = temp.strip()
    return temp


def convert_escaped_hex_to_utf8(escaped_hex_string):
    bytes_object = escaped_hex_string.encode('unicode_escape')
    utf8_string = bytes_object.decode('utf-8')
    return utf8_string


def get_unique_dict_vals(the_dict):
    the_set = set()
    for k, v in the_dict.items():
        the_set.add(v)
    return the_set


def get_biosamples_from_mongo_via_api(nmdc_runtime_api_address="https://api.microbiomedata.org/nmdcschema/",
                                      mongo_max_biosamples=1000,
                                      mongo_biosample_geospatial_data_tsv='mongo_biosample_geospatial_data.tsv'):
    mongo_biosample_stats = requests.get(f"{nmdc_runtime_api_address}collection_stats").json()
    mongo_biosample_stats_dict = {}
    for i in mongo_biosample_stats:
        mongo_biosample_stats_dict[i['ns']] = i['storageStats']

    mongo_biosample_stats = mongo_biosample_stats_dict["nmdc.biosample_set"]

    pprint.pprint(mongo_biosample_stats)

    params = {
        "max_page_size": mongo_max_biosamples,
    }

    next_page_token = None

    mongo_biosamples_dict = {}

    while True:
        if next_page_token:
            params['page_token'] = next_page_token
        mongo_biosamples_response = requests.get(
            url=f"{nmdc_runtime_api_address}biosample_set",
            params=params,
        ).json()
        for biosample in mongo_biosamples_response['resources']:
            mongo_biosamples_dict[biosample['id']] = biosample
        if "next_page_token" in mongo_biosamples_response:
            next_page_token = mongo_biosamples_response["next_page_token"]
            print(f"next_page_token: {next_page_token}")
        else:
            break

    print(len(mongo_biosamples_dict))

    mongo_biosamples_geospatial_data = []
    for k, v in mongo_biosamples_dict.items():
        temp = {}
        temp['id'] = v['id']
        temp['geo_loc_name'] = v['geo_loc_name']['has_raw_value']
        temp['geo_loc_name_normalized'] = normalize_address(v['geo_loc_name']['has_raw_value'])
        temp['latitude'] = v['lat_lon']['latitude']
        temp['latitude_decimal_len'] = len(str(v['lat_lon']['latitude']).split('.')[1])  # todo trim off trailing zeros
        temp['longitude'] = v['lat_lon']['longitude']
        temp['longitude_decimal_len'] = len(str(v['lat_lon']['longitude']).split('.')[1])
        if 'elev' in v:
            temp['elev'] = v['elev']
        else:
            the_keys = list(v.keys())
            the_keys.sort()
            # print(the_keys)
        mongo_biosamples_geospatial_data.append(temp)

    fieldnames = ['id',
                  'elev',
                  'geo_loc_name',
                  'geo_loc_name_normalized',
                  'latitude',
                  "latitude_decimal_len",
                  'longitude',
                  'longitude_decimal_len',
                  ]

    with open(mongo_biosample_geospatial_data_tsv, 'w', encoding='utf-8') as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in mongo_biosamples_geospatial_data:
            writer.writerow(row)


def get_biosample_geospatial_data_from_portal(
        ret_max,
        desired_fields,
        dotenv_path="../../../local/.env",
        portal_submitted_biosample_data_tsv='portal_submitted_biosample_data.tsv',
        base_url="https://data.microbiomedata.org/api/metadata_submission",
):
    dotenv.load_dotenv(dotenv_path)
    data_microbiomedata_org_session_cookie = os.environ.get('DATA_MICROBIOMEDATA_ORG_SESSION_COOKIE')

    params = {
        "limit": ret_max,
        "offset": 0,
    }

    cookies = {'session': data_microbiomedata_org_session_cookie}

    authors = {}
    submissions = {}
    portal_submitted_biosamples = []
    # portal_submitted_biosample_fields = set()
    while True:
        portal_submissions_response = requests.get(url=base_url,
                                                   params=params,
                                                   cookies=cookies,
                                                   )
        portal_submissions_response = portal_submissions_response.json()
        if "results" in portal_submissions_response and portal_submissions_response["results"]:
            for result in portal_submissions_response["results"]:
                authors[result['author']['id']] = result['author']
                submissions[result['id']] = {
                    'author': result['author']['id'],
                    'author_orcid': result['author']['orcid'],
                    'packageName': result['metadata_submission']['packageName'],
                    # "package": result['package'],
                }
                next_key = f"{result['metadata_submission']['packageName']}_data"
                if "sampleData" in result[
                    'metadata_submission'] and next_key in \
                        result['metadata_submission']['sampleData']:
                    biosamples = result['metadata_submission']['sampleData'][next_key]
                    for biosample in biosamples:
                        temp_portal_submitted_geospatial_data = {}
                        for desired_field in desired_fields:
                            if desired_field in biosample:
                                if desired_field == 'elev' or desired_field == 'lat_lon':
                                    parts = biosample[desired_field].split(' ')
                                    if len(parts) == 2:
                                        temp_portal_submitted_geospatial_data[f"{desired_field}_0"] = parts[0]
                                        temp_portal_submitted_geospatial_data[f"{desired_field}_1"] = parts[1]
                                    else:
                                        print(
                                            f"{desired_field} of {biosample[desired_field]} has {len(parts)} part(s) in {result['id']}")
                                elif desired_field == 'geo_loc_name':
                                    temp_portal_submitted_geospatial_data[desired_field] = biosample[desired_field]
                                    temp_portal_submitted_geospatial_data[
                                        'geo_loc_name_normalized'] = normalize_address(
                                        biosample[desired_field])
                                else:
                                    temp_portal_submitted_geospatial_data[desired_field] = biosample[desired_field]
                        temp_portal_submitted_geospatial_data['submission_id'] = result['id']
                        if result['id'] in submissions and 'author' in submissions[result['id']]:
                            author_id = submissions[result['id']]['author']
                            if author_id in authors:
                                if "name" in authors[author_id]:
                                    temp_portal_submitted_geospatial_data['author_name'] = authors[author_id]['name']
                            else:
                                print(f"author not found for submission {result['id']}")
                        portal_submitted_biosamples.append(temp_portal_submitted_geospatial_data)

                else:
                    print(f"sampleData is NOT available for submission {result['id']}")
            params['offset'] += ret_max
            print(f"params['offset']: {params['offset']}")
        else:
            break

    # pprint.pprint(authors)
    # pprint.pprint(submissions)

    useful_fields = desired_fields.copy()
    useful_fields.remove('elev')
    useful_fields.remove('lat_lon')
    useful_fields.append("elev_0")
    useful_fields.append("elev_1")
    useful_fields.append("lat_lon_0")
    useful_fields.append("lat_lon_1")
    useful_fields.append("geo_loc_name_normalized")
    useful_fields.sort()

    portal_submitted_biosample_fields = ['submission_id', 'author_name'] + useful_fields

    with open(portal_submitted_biosample_data_tsv, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=portal_submitted_biosample_fields, delimiter='\t')

        writer.writeheader()

        for row in portal_submitted_biosamples:
            writer.writerow(row)


def normalize_and_geocode_mongo_geo_loc_names(mongo_biosample_geospatial_data_tsv,
                                              portal_biosample_geospatial_data_tsv,
                                              geocoding_base_url,
                                              desired_format,
                                              output_yaml,
                                              # dotenv_path="../../../local/.env"
                                              ):
    # dotenv.load_dotenv(dotenv_path)
    # google_maps_key_val = os.environ.get('GOOGLE_MAPS_API_KEY')

    # normalized_addresses = {}
    unique_normalized_geo_loc_names = set()
    with open(mongo_biosample_geospatial_data_tsv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')

        for row in reader:
            if 'geo_loc_name' in row:
                unique_normalized_geo_loc_names.add(row['geo_loc_name_normalized'])
                # glv = row['geo_loc_name_normalized']
                # glv_norm = normalize_address(glv)
                # normalized_addresses[glv] = glv_norm
            else:
                print(f"no geo_loc_name for {row['id']}")

    with open(portal_biosample_geospatial_data_tsv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')

        for row in reader:
            if 'geo_loc_name' in row:
                unique_normalized_geo_loc_names.add(row['geo_loc_name_normalized'])
                # glv = row['geo_loc_name_normalized']
                # glv_norm = normalize_address(glv)
                # normalized_addresses[glv] = glv_norm
            else:
                print(f"no geo_loc_name for {row['id']}")

    # unique_normalized_geo_loc_names = list(get_unique_dict_vals(normalized_addresses))
    unique_normalized_geo_loc_names = list(unique_normalized_geo_loc_names)
    unique_normalized_geo_loc_names.sort()
    print(len(unique_normalized_geo_loc_names))  # 264

    url_with_format = f"{geocoding_base_url}{desired_format}"

    geocoded = {}
    for address_val in unique_normalized_geo_loc_names:
        if address_val:
            print(address_val)
            params = {
                "address": address_val,
                "key": google_maps_key_val,
            }
            response = requests.get(url=url_with_format, params=params)
            result = response.json()
            geocoded[address_val] = result

    with open(output_yaml, 'w') as yamlfile:
        yaml.dump(geocoded, yamlfile, default_flow_style=False)


def make_geolocation_table_with_diags(input_yaml):
    geolocation_dict = read_yaml_file(input_yaml)
    rows = []
    for k, v in geolocation_dict.items():
        if "results" in v:
            for i in v['results']:
                location = i['geometry']['location']
                temp_dict = {
                    'normalized_address': k,
                    "lat": location['lat'],
                    'lon': location['lng'],
                }
                if "formatted_address" in i:
                    temp_dict['formatted_address'] = i['formatted_address']
                if "bounds" in i['geometry']:
                    bounds = i['geometry']['bounds']
                    pprint.pprint(bounds)
                    ne_bound = bounds['northeast']
                    sw_bound = bounds['southwest']
                    dist = haversine(ne_bound['lat'], ne_bound['lng'], sw_bound['lat'], sw_bound['lng'])
                    temp_dict['ne_lat'] = ne_bound['lat']
                    temp_dict['ne_lon'] = ne_bound['lng']
                    temp_dict['sw_lat'] = sw_bound['lat']
                    temp_dict['sw_lon'] = sw_bound['lng']
                    temp_dict['distance_between_corners'] = dist
                rows.append(temp_dict)
    pprint.pprint(rows)
    fieldnames = [
        'normalized_address',
        'formatted_address',
        'lat',
        'lon',
        'distance_between_corners',
        'ne_lat',
        'ne_lon',
        'sw_lat',
        'sw_lon',
    ]
    dump_dict_to_tsv("geocoding_table.tsv", rows, fieldnames)


def mongodb_lat_lon_diff(mongodb_biosample_geospatial_data_tsv, geocoding_table_tsv):  # todo output_tsv
    mongodb_frame = pd.read_csv(mongodb_biosample_geospatial_data_tsv, sep='\t')
    geocoding_rows = pd.read_csv(geocoding_table_tsv, sep='\t')
    merged = pd.merge(mongodb_frame, geocoding_rows, how='left', left_on='geo_loc_name_normalized',
                      right_on='normalized_address')
    merged_lod = merged.to_dict('records')
    for i in merged_lod:
        i['lat_lon_diff'] = haversine(i['latitude'], i['longitude'], i['lat'], i['lon'])
    merged_frame = pd.DataFrame(merged_lod)
    merged_frame.to_csv("mongodb_lat_lon_diff.tsv", sep='\t')


# "MAIN" BELOW


# get_biosample_geospatial_data_from_portal(
#     ret_max=100,
#     desired_fields=[
#         'collection_date',
#         'elev',
#         'env_package',
#         'geo_loc_name',
#         'lat_lon',
#         'samp_name',
#         'source_mat_id',
#     ],
# )
#
# mongo_biosample_geospatial_data_tsv_fp = 'mongo_biosample_geospatial_data.tsv'
#
# get_biosamples_from_mongo_via_api(mongo_biosample_geospatial_data_tsv=mongo_biosample_geospatial_data_tsv_fp)
#
# normalize_and_geocode_mongo_geo_loc_names(geocoding_base_url="https://maps.googleapis.com/maps/api/geocode/",
#                                           desired_format="json",
#                                           mongo_biosample_geospatial_data_tsv=mongo_biosample_geospatial_data_tsv_fp,
#                                           portal_biosample_geospatial_data_tsv='portal_submitted_biosample_data.tsv',
#                                           output_yaml='geocoded_normalized_geo_loc_names.yaml'
#                                           )

# make_geolocation_table_with_diags('geocoded_normalized_geo_loc_names.yaml')

# get_elevation_from_google_maps_api(lat=38.889248, lon=-77.050636, google_maps_key_val=google_maps_key_val,
#                                    geocoding_base_url="https://maps.googleapis.com/maps/api/elevation/json")

mongodb_lat_lon_diff("mongo_biosample_geospatial_data.tsv", "geocoding_table.tsv")
