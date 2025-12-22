#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age

        Args:
            first_name: Student's first name
            last_name: Student's last name
            age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs: List of attribute names to retrieve (optional)
                   If None, retrieves all attributes

        Returns:
            Dictionary containing specified or all instance attributes
        """
        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        
        Args:
            json: Dictionary with attribute names as keys and values
        """
        for key, value in json.items():
            setattr(self, key, value)
