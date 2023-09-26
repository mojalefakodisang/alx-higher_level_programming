#!/usr/bin/python3
def safe_print_integer(value):
    """ Prints an integer

        Args:
            value: input integer

        Return:
            True: value has been correctly printed
            False: returns false otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
