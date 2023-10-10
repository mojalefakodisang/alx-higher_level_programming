#!/usr/bin/python3
"""The from_json_string module"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    import json

    return json.loads(my_str)
