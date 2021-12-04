import logging

import fire  # type: ignore

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
        "Checking {swagger} and running tests against {server}",
        extra={"swagger": swagger, "server": server},
    )


def cli() -> None:
    fire.Fire(main)


if __name__ == "__main__":
    cli()
