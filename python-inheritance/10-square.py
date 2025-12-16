#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size: positive intger
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        return the area of rectanglr
        """
        return self.__size * self.__size
