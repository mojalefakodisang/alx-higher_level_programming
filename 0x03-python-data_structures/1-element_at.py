#!/usr/bin/python3
def element_at(my_list, idx):
    """Returns element of my_list at index idx
        my_list: Input list
        idx: index

        Return: returns element at index idx
    """
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None
    element = my_list[idx]
    return element
