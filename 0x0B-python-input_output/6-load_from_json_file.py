#!/usr/bin/python3
"""Module containing load_from_json_file method"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename (str, json): name of the JSON file
    """
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)
