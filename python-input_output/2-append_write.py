#!/usr/bin/python3
"""Module for appended text to files"""


def append_write(filename="", text=""):
    """append a UTF-8 text file and
    returns the number of characters appended.

    Args:
        filename: path to the file to open & appended (default: "").
        text: to be appended in the filename.

    Return:
        the number of characters appended
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
