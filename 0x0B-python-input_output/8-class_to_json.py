#!/usr/bin/python3
"""The class_to_json module"""


def class_to_json(obj):
    """Returns the dict description with simple data struct for JSON"""
    return obj.__dict__
