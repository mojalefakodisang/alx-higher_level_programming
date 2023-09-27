#!/usr/bin/python3
"""Module with a clss Square """


class Square:
    """ Clase that takes in a size and returns its area"""

    def __init__(self, size=0):
        """Method that initializes Square class

            Args:
                size: size attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that return square of a size

            Return: returns the square of size
        """
        return self.__size ** 2
