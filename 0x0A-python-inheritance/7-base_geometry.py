#!/usr/bin/python3
"""Module that contains class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method that defines area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a value of a geometry"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
