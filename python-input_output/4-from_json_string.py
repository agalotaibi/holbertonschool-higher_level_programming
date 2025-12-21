#!/usr/bin/python3
"""Module that converts JSON string to Python object"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) 
    represented by a JSON string.

    Args:
        my_str: JSON string to convert

    Returns:
        Python object (list, dict, etc.)
    """

    return json.load(my_str)
