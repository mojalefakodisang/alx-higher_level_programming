#!/usr/bin/python3
"""Module that contains append_write method"""


def append_write(filename="", text=""):
    """Method that appends text into a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as file:
        no_chars = file.write(text)

        return no_chars
