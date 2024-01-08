#!/usr/bin/python3
"""Module containing class BaseGeometry"""
BaseGeometry = __import__('6-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry class"""

    def __init__(self, width, height):
        """Method that initiates Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

