import logging
from typing import Any, Dict, Optional

import requests
from requests import Response

from fuzzy_swagger.fuzz_generator import type_mapper_func


def create_request(
    server: str,
    base_path: str,
    http_method: str,
    path: str,
    path_params: list,
    query_params: list,
    form_data_params: list,
    body_json: Optional[Any],
) -> None:
    url = server + base_path
    for path_param in path_params:
        path_param_type = path_param["type"]
        fuzz_func = type_mapper_func(path_param_type)
        fuzzed_value = fuzz_func(path_param)

        path = path.replace("{" + path_param["name"] + "}", str(fuzzed_value))

    full_path = url + path

    payload = {}
    for query_param in query_params:
        query_param_type = query_param["type"]
        fuzz_func = type_mapper_func(query_param_type)
        fuzzed_value = fuzz_func(query_param)
        payload[query_param["name"]] = fuzzed_value

    for form_data_param in form_data_params:
        form_data_param_type = form_data_param["type"]
        fuzz_func = type_mapper_func(form_data_param_type)
        fuzzed_value = fuzz_func(form_data_param)
        payload[form_data_param["name"]] = fuzzed_value

    content_type = "application/json"

    if form_data_params and any(f["type"] == "file" for f in form_data_params):
        content_type = "multipart/form-data;boundary=----FuzzBoundary"
    elif form_data_params:
        content_type = "application/x-www-form-urlencoded"

    if http_method == "get":
        headers: Dict[str, str] = {}
        get_response: Response = requests.get(
            full_path, headers=headers, params=payload
        )
        process_response(http_method, url, path, get_response)
    elif http_method == "post":
        headers = {"Content-Type": content_type}
        post_response: Response = requests.post(
            full_path, headers=headers, params=payload, json=body_json
        )
        process_response(http_method, url, path, post_response)

    logging.debug("------------------")


def process_response(http_method: str, url: str, path: str, r: Any) -> None:
    if r.status_code > 399:
        logging.info("Sending %s request to %s%s", http_method.upper(), url, path)
        logging.debug(r.content)
