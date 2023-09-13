#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ Returns a set of common elements in two sets
        Args:
            set_1: first set
            set_2: second set

        Returns:
            returns a set of common elements in two sets
    """
    set_1 = list(set(set_1))
    set_2 = list(set(set_2))

    common = []
    for idx1 in range(len(set_1)):
        for idx2 in range(len(set_2)):
            if set_1[idx1] == set_2[idx2]:
                common.append(set_1[idx1])
    return common
