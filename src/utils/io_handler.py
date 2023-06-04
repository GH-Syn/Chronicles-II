"""
About
-----
`io.py` contains io related utility units.
"""

import argparse
from glob import glob
import json
import os
import sys

import loguru


def get_parser():
    """
    Get parser from argparse library
    """

    parser = argparse.ArgumentParser(
        prog="Chronicles II",
        description="CLI for Chronicles II",
        add_help=True,
        allow_abbrev=True,
    )

    return parser


def get_display_size_from_config(config='config.json'):
    """
    Get display size from configuration.

    Default location: config.json

    :param config: Configuration file - defaults to `config.json`
    :raises FileNotFoundError: If `config.json` is not in `os.getcwd()`
    :return: Returns tuple value containing width and height.
    """

    if config in glob.glob(os.path.join(os.getcwd())):
        file_config = json.load(open(config, 'r'))
        return file_config['size']

    raise FileNotFoundError("Cannot locate configuration file.")

def set_logging_level(level = "DEBUG"):
    """
    Replace and set the logging level.

    Default logging level is debug.

    :param level: Logging level - default is debug
    :raises ValueError: If `level` is not valid
    """

    levels = [
            "DEBUG",
            "NOSET",
            "INFO",
            "CRITICAL",
            "ERROR",
            "WARNING",
            ]
    if level not in levels:
        raise ValueError(f"Level must be one of the following: {[i for i in levels]}]")

    loguru.logger.remove()
    loguru.logger.add(sys.stderr, level=level)

