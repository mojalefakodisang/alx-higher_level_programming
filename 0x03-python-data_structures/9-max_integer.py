#!/usr/bin/python3
def max_integer(my_list=[]):
    """Sorts the list and returns the max integer of list
        my_list: input list

        Return: max value of the list
    """
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
