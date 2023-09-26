#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of list, only integers

        Args:
            my_list: input list
            x: elelments

        Return:
            returns the real number of integers
    """
    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            length += 1
        except (ValueError, TypeError):
            pass
    print()
    return length
