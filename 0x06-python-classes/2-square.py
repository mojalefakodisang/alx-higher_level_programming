#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a squre"""

    def __init__(self, size=0):
        """ Function that initialize class Square

            Args:
                size (int): size attribute
        """
        if not isinstance(size, int):
            raise TypeError("size nust be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
