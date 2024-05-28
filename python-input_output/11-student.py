#!/usr/bin/python3
"""
File class for Student
"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a student instance.
        If attrs is a list of strings, only those attributes are included in the dictionary.
        Otherwise, all attributes are included.
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)

