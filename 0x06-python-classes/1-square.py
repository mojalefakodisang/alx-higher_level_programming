#!/usr/bin/python3
"""Square module with a Square class containing a private attribute """


class Square:
    """Class with a private attribute size

        Args:
            size: private attribute size

        Attributes;
            size: a private attribute
    """
    def __init__(self, size):
        """ Initializing function

        Args:
            size: private attribute size

        Return:
            no return value
        """
        self.__size = size
