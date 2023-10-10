#!/usr/bin/python3
"""The append write module"""


def append_write(filename="", text=""):
    """Appends text on an existing file

        Args:
            filename: file path
            text: text to be appended
    """
    char_count = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        for i in text:
            char_count += 1
        f.write(text)

    return char_count
