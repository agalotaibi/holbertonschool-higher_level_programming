#!/usr/bin/python3
"""Module for reading files"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to stdout

    Args:
        filename: path to the file to read (default: "")
    """

    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    print(read_file, end="")
