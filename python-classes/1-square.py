#!/usr/bin/python3
"""
This module defines a class Square based on 0-square.py.
It adds a private instance attribute 'size'.
"""


class Square:
    """
    This class defines a square by a private instance attribute 'size'.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type verification yet).
        """
        self.__size = size
