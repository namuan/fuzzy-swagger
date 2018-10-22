from prance import ResolvingParser
from fuzzy_swagger.logger import *


def retrieve_swagger_doc(swagger_file):
    debug("Loading swagger documentation from %s" % (swagger_file))
    return ResolvingParser(url=swagger_file)
