#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """Divides the elements of the matrix with a divisor

    Args:
        matrix (list of lists): List of list with integers/floats
        div (int, float): Divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        list: returns a new list with divided matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0 or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    len_row = len(matrix)
    len_col = len(matrix[0])

    for i in range(len_row):
        if not isinstance(matrix[i], list) or len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(matrix[i]) != len_col:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len_col):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
