from typing import Any, Dict, List, Union

from fuzzy_swagger.fuzz_generator import fuzz_array, fuzz_object


def json_from_schema(body_type: str, body_schema: Dict) -> Union[List[Any], Any]:
    if body_type == "array":
        return fuzz_array(body_schema)
    elif body_type == "object":
        return fuzz_object(body_schema["properties"])

    raise ValueError(f"Unknown body type: {body_type}")
