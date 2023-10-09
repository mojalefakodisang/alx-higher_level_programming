#!/usr/bin/python3
"""The '8-rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class"""

    def __init__(self, width, height):
        """Initiates class Rectangle

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Implemets area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Super method for printing"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
