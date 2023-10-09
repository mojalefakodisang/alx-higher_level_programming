#!/usr/bin/python3
""" The '4-inherits_from.py' module"""


def inherits_from(obj, a_class):
    """Checks if obj is inherited from a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
