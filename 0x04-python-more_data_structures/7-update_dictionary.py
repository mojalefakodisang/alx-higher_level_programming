#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ Updates a dictionary
        Args:
            a_dictionary: input dictionary
            key: key to be searched
            value: value of the key

        Returns:
            returns an updated dictionary
    """
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value

    return a_dictionary
