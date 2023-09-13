#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Returns a set of all elements present in one set
        Args:
            set_1: first set
            set_2: second set

        Returns:
            returns all elements present in one set
    """
    diff = set_1.symmetric_difference(set_2)
    return diff
