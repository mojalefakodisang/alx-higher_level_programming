#!/usr/bin/python3
"""Module containing text_indentation method"""


def text_indentation(text):
    """Method that indentate input text

    Args:
        text (str): Text to be indented

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    mod_text = ""
    i = 0
    printed_indend = 0
    text = text.strip()
    for i in range(len(text)):
        if (text[i] in [".", "?", ":"]):
            printed_indend = 1
            print(text[i], end="\n\n")
        elif printed_indend == 1  and text[i] == " ":
            i += 1
        else:
            printed_indend = 0
            print(text[i], end="")
