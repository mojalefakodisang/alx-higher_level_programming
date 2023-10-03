#!/usr/bin/python3
""" Module that adds two integers from INT_MIN to INT_MAX"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers
        Args:
            a: first integer
            b: second integer, set to 98 at default
        Return:
            returns the sum of the two integers a and b
    """
    Sum = 0
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if (not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)):
        raise TypeError("b must be an integer")

    Sum = a + b
    return Sum
