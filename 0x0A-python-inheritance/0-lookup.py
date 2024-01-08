#!/usr/bin/python3
"""Module containing a lookup method"""


def lookup(obj):
    """Look up method

    Arg:
        obj: any object to be looked at

    Returns:
        returns all available attributes
    """
    return dir(obj)
