#!/usr/bin/python3
"""
This module have a method that check if the object is instance class.
"""


def is_same_class(obj, a_class):
    """
    method returns True if the object is 
    exactly an instance of class; otherwise False

    Args:
        obj: the object ot be check
        a_class the class to check aganist

    Retrun:
        True: if the object is instance of class
        False: if it not instance of class
    """
    return type(obj) is a_class
