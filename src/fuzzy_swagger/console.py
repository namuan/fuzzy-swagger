import logging

import fire  # type: ignore

from fuzzy_swagger.orchestra import play

logging.basicConfig(
    handlers=[
        logging.StreamHandler(),
    ],
    format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logging.captureWarnings(capture=True)


def main(swagger: str, server: str) -> None:
    logging.info(
        "Checking %s and running tests against %s",
        swagger,
        server,
    )
    play(swagger, server)


def cli() -> None:
    fire.Fire(main)


if __name__ == "__main__":
    cli()
