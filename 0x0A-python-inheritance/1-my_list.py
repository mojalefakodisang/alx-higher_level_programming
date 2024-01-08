#!/usr/bin/python3
"""Module that contains class MyList"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Print sorted list - pulic method"""
        print(sorted(i for i in self))
