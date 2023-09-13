#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a sorted dictionary keys
        Args:
            a_dictionary: input dictionary

        Returns:
            no return value returned
    """
    key_list = []
    for keys, values in a_dictionary.keys():
        key_list.append(keys)

    for keys in sorted(key_list):
        values = a_dictionary[keys]
        print("{}: {}".format(keys, values))
