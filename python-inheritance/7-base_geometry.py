#!/usr/bin/python3
"""
This module contains the BaseGeometry class based on 6-base_geometry.py.
"""


class BaseGeometry:
    """
    A class that serves as a base for geometry-related classes.
    """
    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: Always raises with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name: The name of the parameter (always a string)
            value: The value to be validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
