#!/usr/bin/python3
def no_c(my_string):
    """Removes c in a string with nothing
        my_string: input string

        Return: Returns a string without c in a string
    """
    new_string = ""
    for char in my_string:
        if char == "c" or char == "C":
            char = ""
        new_string += char
    return new_string
