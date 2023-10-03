#!/usr/bin/python3
"""
The ``text_indentation`` module
Has 'text_indentation' function
"""


def text_indentation(text):
    """Checks for special characters then prints a newline."""
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    flag = 0
    for x in text:
        if flag == 0:
            if x == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if x == "." or x == "?" or x == ":":
                print(x)
                print()
                flag = 0
            else:
                print(x, end="")
