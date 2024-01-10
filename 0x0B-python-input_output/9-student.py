#!/usr/bin/python3
"""Module containing a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation"""
        return vars(self)
