#!/usr/bin/python3
"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """Function defined"""
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
