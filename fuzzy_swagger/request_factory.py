import requests

from .fuzz_generator import *
from .logger import *


def create_request(server, base_path, http_method, path, path_params, query_params, form_data_params, body_json):
    url = server + base_path
    for path_param in path_params:
        path_param_type = path_param['type']
        fuzz_func = type_mapping.get(path_param_type)
        fuzzed_value = fuzz_func(path_param)

        path = path.replace("{" + path_param['name'] + "}", str(fuzzed_value))

    full_path = url + path

    payload = {}
    for query_param in query_params:
        query_param_type = query_param['type']
        fuzz_func = type_mapping.get(query_param_type)
        fuzzed_value = fuzz_func(query_param)
        payload[query_param['name']] = fuzzed_value

    for form_data_param in form_data_params:
        form_data_param_type = form_data_param['type']
        fuzz_func = type_mapping.get(form_data_param_type)
        fuzzed_value = fuzz_func(form_data_param)
        payload[form_data_param['name']] = fuzzed_value

    content_type = 'application/json'

    if form_data_params and any(f['type'] == 'file' for f in form_data_params):
        content_type = 'multipart/form-data;boundary=----FuzzBoundary'
    elif form_data_params:
        content_type = 'application/x-www-form-urlencoded'

    if http_method == 'get':
        headers = {}
        r = requests.get(full_path, headers=headers, params=payload)
        process_response(http_method, url, path, r)
    elif http_method == 'post':
        headers = {'Content-Type': content_type}
        r = requests.post(full_path, headers=headers, params=payload, json=body_json)
        process_response(http_method, url, path, r)

    debug("------------------")


def process_response(http_method, url, path, r):
    if r.status_code > 399:
        info("Sending %s request to %s%s" % (http_method.upper(), url, path))
        info(r.content)
