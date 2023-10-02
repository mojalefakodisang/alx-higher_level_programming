#!/usr/bin/python3
""" Module that has a class rectangle"""


class Rectangle:
    """ Class Rectangle"""

    def __init__(self, width=0, height=0):
        """ Method that initializes attributes"""
        self.width = width
        self.height = height

    def __del__(self):
        """ Prints message if instance is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """ Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle

            Args:
                value: value to be set as width
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle

            Args:
                value: value to be set as height
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Gets area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Gets perimeter of the rectangle"""
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """ Prints the rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))

        return string

    def __repr__(self):
        """ Representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
