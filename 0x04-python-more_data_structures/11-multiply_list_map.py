#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ Returns a list will all values multiplied by number."""
    return list(map(lambda x: x * number, my_list))
