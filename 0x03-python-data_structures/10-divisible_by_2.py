#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Checks if the contents of a list are divisible by 2
        my_list: input list

        Return: returns a list of bool that checks integers are divisible by 2
    """
    list_result = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result
