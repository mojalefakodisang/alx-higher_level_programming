#!/usr/bin/python3
"""Module containing a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives a dictionary representation"""
        flag = 0
        all = vars(self)
        if type(attrs) is not list:
            flag = 1
        else:
            for el in attrs:
                if type(el) is not str:
                    flag = 1

        if flag == 1:
            return all
        else:
            return dict((key, all[key]) for key in attrs if key in all)

    def reload_from_json(self, json):
        """Replaces all attributes of student instance"""
        for key, value in json.items():
            setattr(self, key, value)
