#!/usr/bin/python3

"""Defines a string-to-JSON function."""


def to_json_string(my_obj):
    import json
    """
    Converts an object to a JSON string.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
