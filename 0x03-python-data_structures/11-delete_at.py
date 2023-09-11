#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes an element at a specific index
        my_list: input list
        idx: index at which to delete element, 0 at default

        Return: returns a list with deleted element on success
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
        return my_list
