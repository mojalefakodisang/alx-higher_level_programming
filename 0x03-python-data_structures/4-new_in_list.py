#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element at a specific index
        my_list: input list
        idx: index at which you are replacing element
        element: element you going to replace

        Return: returns original list else a replaced list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
