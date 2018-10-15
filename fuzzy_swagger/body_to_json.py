from .fuzz_generator import *


def json_from_schema(body_type, body_schema):
    if body_type == 'array':
        return fuzz_array(body_schema)
    elif body_type == 'object':
        return fuzz_object(body_schema['properties'])
