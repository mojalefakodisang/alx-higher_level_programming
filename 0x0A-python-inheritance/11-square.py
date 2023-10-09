#!/usr/bin/python3
"""The '11-square' module"""
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

    def area(self):
        """Calculates area of square"""
        return self.__size ** 2

    def __str__(self):
        """super method"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
