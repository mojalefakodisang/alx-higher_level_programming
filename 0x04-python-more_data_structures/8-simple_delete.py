#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ Deletes a key within a dictionary
        Args:
            a_dictionary: input dictionary
            key: key to be deleted

        Returns:
            returns a dictionary without deleted key
    """
    if key not in a_dictionary:
        return a_dictionary
    else:
        for i in a_dictionary:
            if i == key:
                del a_dictionary[i]
                break
        return a_dictionary
