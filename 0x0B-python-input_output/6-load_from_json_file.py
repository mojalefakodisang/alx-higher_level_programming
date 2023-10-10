#!/usr/bin/python3
"""The load from json file module"""


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    import json

    with open(filename) as f:
        return json.load(f)
