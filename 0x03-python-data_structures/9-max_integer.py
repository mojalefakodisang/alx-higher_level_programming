#!/usr/bin/python3
def max_integer(my_list=[]):
    """Sorts the list and returns the max integer of list
        my_list: input list

        Return: max value of the list
    """
    if not my_list:
        return None
    else:
        i = len(my_list) - 1
        while i > 1:
            j = 0
            while j < i:
                # checks if the integers are greater then swich
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp

                j += 1
            i -= 1
            return my_list[j]
