#!/usr/bin/python3
"""The '1-my_list.py' module"""


class MyList(list):
    """The 'MyList' class"""

    def print_sorted(self):
        """Prints a sorted list of MyList class"""
        print(sorted(self))
