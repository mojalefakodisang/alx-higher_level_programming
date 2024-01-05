#!/usr/bin/python3
"""Module containing the add_integers method"""


def add_integer(a, b=98):
    """Method that adds two integers

    Args:
        a (int or float): First integer
        b (int or float): Second integer. Defaults to 98.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
