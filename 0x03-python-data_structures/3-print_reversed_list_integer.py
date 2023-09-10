#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints our list in reverse
        my_list: input list

        Return: No values returned
    """
    length = len(my_list)
    i = -1
    while i >= -length:
        print("{:d}".format(my_list[i]))
        i -= 1
