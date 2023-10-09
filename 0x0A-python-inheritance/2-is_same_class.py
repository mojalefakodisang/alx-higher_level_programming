#!/usr/bin/python3
""" The 'is_same_class' module"""


def is_same_class(obj, a_class):
    """Checks if obj is part of a_class"""
    if (not isinstance(obj, a_class)):
        return False
    return True
