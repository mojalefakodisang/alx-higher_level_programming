#!/usr/bin/python3
"""Module containing the print_square method"""


def print_square(size):
    """Method that prints a square with a "#" character

    Args:
        size (int): Length or size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")

    for i in range(size):
        print("#" * size)
