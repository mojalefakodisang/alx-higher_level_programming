#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix in row and columns
        matrix: input matrix

        Return: No return values
    """
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
