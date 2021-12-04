import logging
from typing import Any

from prance import ResolvingParser  # type: ignore


def retrieve_swagger_doc(swagger_file: str) -> Any:
    logging.info(
        "Loading swagger documentation from %s",
        swagger_file,
    )
    return ResolvingParser(url=swagger_file)
