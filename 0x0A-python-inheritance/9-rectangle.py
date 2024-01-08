#!/usr/bin/python3
"""Module containing class BaseGeometry"""
BaseGeometry = __import__('8-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Method that initiates Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String magic method of Rectangle class"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
