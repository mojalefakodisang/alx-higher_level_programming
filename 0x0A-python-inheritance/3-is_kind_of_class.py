#!/usr/bin/python3
""" The '3-is_kind_of_class.py' module"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
