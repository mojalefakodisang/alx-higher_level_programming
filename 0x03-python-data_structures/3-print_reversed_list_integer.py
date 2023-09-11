#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints our list in reverse
        my_list: input list

        Return: No values returned
    """
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
