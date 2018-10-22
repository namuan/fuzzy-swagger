from fuzzy_swagger.body_to_json import json_from_schema
from fuzzy_swagger.logger import *
from fuzzy_swagger.request_factory import create_request
from fuzzy_swagger.swagger_doc import retrieve_swagger_doc


def play(swagger_doc, server):
    swagger_spec = retrieve_swagger_doc(swagger_doc)
    base_path = swagger_spec.specification["basePath"]
    swagger_paths = swagger_spec.specification['paths']
    for path, path_specs in swagger_paths.items():
        for http_method, http_method_specs in path_specs.items():
            debug("Checking path: %s, http method: %s" % (path, http_method))
            body_schema = next(
                (schema['schema'] for schema in http_method_specs['parameters'] if schema['in'] == 'body'), None)
            query_params = [schema for schema in http_method_specs['parameters'] if schema['in'] == 'query']
            path_params = [schema for schema in http_method_specs['parameters'] if schema['in'] == 'path']
            form_data_params = [schema for schema in http_method_specs['parameters'] if schema['in'] == 'formData']

            body_json = None
            if body_schema:
                body_json = json_from_schema(body_schema['type'], body_schema)

            create_request(
                server,
                base_path,
                http_method,
                path,
                path_params,
                query_params,
                form_data_params,
                body_json
            )
