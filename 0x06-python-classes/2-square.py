#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a squre"""

    def __init__(self, size=0):
        """ Function that initialize class Square

            Args:
                size (int): size attribute
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size nust be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
