#!/usr/bin/python3
"""Module for write files"""


def write_file(filename="", text=""):
    """write a UTF-8 text file and
    returns the number of characters written.

    Args:
        filename: path to the file to open & write (default: "").
        text: to be written in the filename.

    Return:
        the number of charecters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
