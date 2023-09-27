#!/usr/bin/python3
"""Module with a clss Square """


class Square:
    """ Clase that takes in a size and returns its area"""

    def __init__(self, size=0, position=(0, 0)):
        """Method that initializes Square class

            Args:
                size: size attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Method that return square of a size

            Return: returns the square of size
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method that gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Method that gets position of spaces before # """
        return self.__position

    @position.setter
    def position(self, value):
        """Method that sets position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that replaces a square of a number with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
