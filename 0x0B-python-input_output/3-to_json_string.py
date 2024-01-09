#!/usr/bin/python3
"""Module containing the to_json_string method"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj (_type_): _description_
    """
    return json.dumps(my_obj)
