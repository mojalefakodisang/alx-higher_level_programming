#!/usr/bin/python3
"""The student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation of Students"""
        return self.__dict__
