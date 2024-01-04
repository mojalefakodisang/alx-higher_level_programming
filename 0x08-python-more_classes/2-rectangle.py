#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Magic method that initializes a new rectangle

        Args:
            width (int, optional): Width of a rectangle. Defaults to 0.
            height (int, optional): Height of a rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that gets width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Method that gets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter
