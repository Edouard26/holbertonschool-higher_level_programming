#!/usr/bin/python3
"""
    file for function class_to_json
"""


def class_to_json(obj):
    """
    Returns a dictionary description suitable for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """

    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
