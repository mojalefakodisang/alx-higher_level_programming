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
    while(i in range(len(text))):
        if (text[i] in [".", "?", ":"]):
            mod_text += text[i] + "\n\n"
            i += 2
        mod_text += text[i]
        i += 1

    print(mod_text)
