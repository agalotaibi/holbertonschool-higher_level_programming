#!/usr/bin/python3
"""
Module that create an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: name of the file to read from.

    Returns:
        Python object loaded from JSON file.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
