#!/usr/bin/python3
"""
This module defines a class Square based on 1-square.py.
It adds a private instance attribute 'size'.
"""

class Square:
    """
    This class defines a square by a private instance attribute 'size'.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        
        Args:
        size (int): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
