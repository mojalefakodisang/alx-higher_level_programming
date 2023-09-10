#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces element at a certain index within a list
        my_list: input list
        idx: index at which you are to replace with element
        element: element to be added

        Return: returns a new list with replaced elements
    """
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list
