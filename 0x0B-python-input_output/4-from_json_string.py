#!/usrbin/python3
"""Module containing from_json_string method"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string

    Args:
        my_str (_type_): JSON string
    """
    return json.loads(my_str)
