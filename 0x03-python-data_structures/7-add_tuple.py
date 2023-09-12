#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ Adds two tuples
        Args:
            tuple_a: first tuple
            tuple_b: second tuple

        Returns:
            returns the sum of the two tuples at success
    """
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) < 2:
        for i in range(2 - len(list_a)):
            list_a.append(0)

    if len(list_b) < 2:
        for i in range(2 - len(list_b)):
            list_b.append(0)

    a = list_a[0] + list_b[0]
    b = list_a[1] + list_b[1]

    results = (a, b)
    return results
