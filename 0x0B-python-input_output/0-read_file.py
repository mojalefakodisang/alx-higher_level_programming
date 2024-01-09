#!/usr/bin/python3
"""Module that contains a read_file method"""


def read_file(filename=""):
    """Reads and prints contents of a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
