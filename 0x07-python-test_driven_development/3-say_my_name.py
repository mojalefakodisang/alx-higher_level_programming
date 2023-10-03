#!/usr/bin/python3
"""
'say_my_name' module
It takes in first_name and last_name and prints them
"""


def say_my_name(first_name, last_name=""):
    """Prints name and last name"""
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
