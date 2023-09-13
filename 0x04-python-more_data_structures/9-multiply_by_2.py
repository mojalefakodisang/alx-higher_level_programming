#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ Multiplies values of the dictionary by 2
        Args:
            a_dictionary: input dictionary

        Returns:
            returns a new dictionary
    """
    for keys in a_dictionary:
        a_dictionary[keys] *= 2
    return a_dictionary
