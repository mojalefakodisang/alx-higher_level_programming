#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a sorted dictionary keys
        Args:
            a_dictionary: input dictionary

        Returns:
            no return value returned
    """
    for keys in sorted(a_dictionary):
        print("{:s}: {}".format(keys, a_dictionary[keys]))
