#!/usr/bin/python3
"""
This module is all about returner list
of available attributes & methods of an object
"""


def lookup(obj):
    """return list of available attributes & methods of an object"""
    return dir(obj)
