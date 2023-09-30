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
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in position):
            raise TypeError("position must be a tuple of 3 positive integers")
        
        self.__size = size
        self.__position = position

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
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Method that return square of a size

            Return: returns the square of size
        """
        return self.__size ** 2

    def my_print(self):
        """Method that replaces a square of a number with #"""
        if self.__size == 0:
            print()
            return

        for lin in range(self.__position[1]):
            print()
        for col in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
