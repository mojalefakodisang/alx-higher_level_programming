#!/usr/bin/python3
"""The save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
