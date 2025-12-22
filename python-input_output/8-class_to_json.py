#!/usr/bin/python3
"""Module that contains class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object
    
    Args:
        obj: An instance of a Class
        
    Returns:
        Dictionary with all serializable attributes of obj
    """
    return obj.__dict__
