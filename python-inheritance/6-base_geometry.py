#!/usr/bin/python3
"""
This module contains the BaseGeometry class based on 5-base_geometry.py.
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
