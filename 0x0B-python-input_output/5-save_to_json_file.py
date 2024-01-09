#!/usr/bin/python3
"""Module containing save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file

    Args:
        my_obj (any): any Python data structure
        filename (str, any): name of the file
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
