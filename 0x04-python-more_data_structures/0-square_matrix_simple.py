#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Squares the indecies of the matrix
        Args:
            matrix: nested list

        Returns:
            returns a nested list with squared of every index in the list
    """
    sq_matrix = []
    for idx in range(len(matrix)):
        sq_matrix.append(list(map(lambda x: x ** 2, matrix[idx])))
    return sq_matrix
