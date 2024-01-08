#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
