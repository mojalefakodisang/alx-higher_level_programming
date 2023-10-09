#!/usr/bin/python3
"""The '5-base_geometry.py' module"""


class BaseGeometry:
    """The BaseGeometry class"""

    def area(self):
        """Area of BaseGeometry class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer

            Args:
                name (str): name of the parameter
                value (int): The parameter to validate
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if not (value > 0):
            raise ValueError("{} must be greater than 0".format(name))
