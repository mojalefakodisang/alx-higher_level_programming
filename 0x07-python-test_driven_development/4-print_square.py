#!/usr/bin/python3
"""
The 'print_square' module
Uses print_square function to print squares
"""


def print_square(size):
    """Prints a square with a character"""
    if size == 0:
        return
    if isinstance(size, str):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
