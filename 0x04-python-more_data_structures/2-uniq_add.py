#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Adds only unique elements in a list
        Args:
            my_list: input list

        Returns:
            returns sum of unique elements in a list
    """
    uniq_list = list(set(my_list))
    sum = 0

    for contents in uniq_list:
        sum += contents

    return sum
