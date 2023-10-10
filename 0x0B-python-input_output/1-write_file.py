#!/usr/bin/python3
"""The write file module"""


def write_file(filename="", text=""):
    """Writes text into a file object

        Args:
            filename: file path
            text: text to be written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        char_count = 0
        for i in text:
            char_count += 1
        f.write(text)

        return char_count
