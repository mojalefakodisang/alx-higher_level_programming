#!/usr/bin/python3
""" The 'is_same_class' module"""


def is_same_class(obj, a_class):
    """Checks if obj is part of a_class"""
    if type(obj) == a_class:
        return True
    return False
