#!/usr/bin/python3
"""Module: class to json"""


def class_to_json(obj):
    """Converts an object to a dictionary representation
    for JSON serialization."""
    dict_result = {}
    for name, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dict_result[name] = value
    return dict_result
