#!/usr/bin/python3
def multiple_returns(sentence):
    """ Multiple returns 
        Args:
            sentence: input string

        Returns:
            length: length of the sentence else 0
            first_letter: first of the sentence else None
    """
    if sentence == "":
        length = 0
        first_letter = "None"
    else:
        length = len(sentence)
        first_letter = sentence[0]
    return (length, first_letter)
