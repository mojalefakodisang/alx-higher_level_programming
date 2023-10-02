#!/usr/bin/python3
""" Module that has a class rectangle"""


class Rectangle:
    """ Class Rectangle"""

    def __init__(self, width=0, height=0):
        """ Method that initializes attributes"""
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if (not isinstance(height, int)):
            raise TypeError("height must be integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

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
        if (value < 0):
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
