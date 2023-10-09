#!/usr/bin/python3
"""The '10-square' module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square which inherited attributes of Rectangle"""

    def __init__(self, size):
        """Initiates class Square

            Args:
                size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
