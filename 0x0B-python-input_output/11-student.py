#!/usr/bin/python3
"""The student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives a dictionary representation of Students"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""
        for k, v in json.items():
            if k == "first_name":
                self.first_name = v
            elif k == "last_name":
                self.last_name = v
            elif k == "age":
                self.age = v
