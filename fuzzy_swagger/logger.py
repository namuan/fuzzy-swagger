import logging


def set_verbose_logging():
    logging.basicConfig(level=logging.DEBUG)


def debug(message):
    logging.debug(message)


def info(message):
    logging.info(message)
