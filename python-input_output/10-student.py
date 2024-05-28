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
    Initializes  dictionnary representation of student instance
    """
    json_dict = {}
    if attrs is None:
        json_dict = self.__dict__.copy
    else:
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

            return json_dict
