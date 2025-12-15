#!/usr/bin/python3
"""
This module have a method that check if the object is instance class
or is an instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    method check if the object is exactly
    an instance of class or class that inherited from.

    Args:
        obj: the object ot be check
        a_class the class to check aganist

    Retrun:
        True: if the object is instance of class
        or calss inherited from.
        False: if it not instance of class
        or calss inherited from.
    """
    return isinstance(obj, a_class)
