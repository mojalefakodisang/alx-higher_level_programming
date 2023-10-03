#!/usr/bin/python3
"""
This is the 2-matrix_divided module
It has matrix_divided function
"""


def matrix_divided(matrix, div):
    """Matrix elements divided by div."""
    new_matrix = []
    row_len = []
    row_count = 0
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list)):
        raise TypeError(msg)
    for row in matrix:
        if (not isinstance(row, list)):
            raise TypeError(msg)
        row_len.append(len(row))
        for col in row:
            if (not isinstance(col, int) and
                    not isinstance(col, float)):
                raise TypeError(msg)
        row_count += 1

    if len(set(row_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, int) or isinstance(div, float):
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))

    return new_matrix
