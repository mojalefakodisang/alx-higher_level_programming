#!/usr/bin/python3
""" The read file module"""


def read_file(filename=""):
    """Reads contents of a file

        Args:
            filename: path to the file to be read
    """
    with open(filename, mode="r") as f:
        for line in f:
            print(line, end="")
