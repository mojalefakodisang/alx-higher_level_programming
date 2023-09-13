#!/usr/bin/python3
def number_keys(a_dictionary):
    """ Returns the number of keys in a dictionary
        Args:
            a_dictionary: input dictionary

        Returns:
            returns a number of keys in a dictionary
    """
    keys = 0
    for i in a_dictionary.keys():
        keys += 1

    return keys
