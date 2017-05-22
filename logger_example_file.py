import logging
from logger import setup_logger
setup_logger()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

logger.setLevel(logging.DEBUG)  # sets the logging level for this script


def add_two_strings(string_one, string_two):
    """
    Concatenates two strings
    :param string_one
    :param string_two
    :return: concatenation of two strings
    """
    logger.debug("string one: {0}".format(string_one))
    logger.debug("string two: {0}".format(string_two))

    logger.debug("let's check we have two strings...")
    if isinstance(string_one, str) or isinstance(string_two, str):
        logger.debug("Great! Both '{0}' and '{1}' are strings".format(string_one, string_two))
    else:
        logger.error("We can't create a new phrase because we have a number!")
        return None

    return_value = string_one + " " + string_two
    logger.info("return value of add_two_strings: '{0}'".format(return_value))
    return return_value

add_two_strings("yo", "hi")






















#

#

#
