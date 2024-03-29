#!/usr/bin/python3

"""Defines a json-object function."""
import json


def from_json_string(my_str):
    """Returns python object from JSON string."""
    return json.loads(my_str)
