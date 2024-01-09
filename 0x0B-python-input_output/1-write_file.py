#!/usr/bin/python3
"""Module containing write_file method"""


def write_file(filename="", text=""):
    """Method that write text into a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): content to be written on the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
