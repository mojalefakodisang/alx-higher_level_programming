#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Magic method that initializes a new rectangle

        Args:
            width (int, optional): Width of a rectangle. Defaults to 0.
            height (int, optional): Height of a rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Representation of a rectangle"""
        rec = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            rec += "#" * self.__width + "\n"
            if (i == self.__height - 1):
                rec += "#" * self.__width

        return rec

    def __repr__(self):
        """Representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Detects when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
