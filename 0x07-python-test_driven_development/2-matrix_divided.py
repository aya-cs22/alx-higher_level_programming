#!/usr/bin/python3
"""Module for add a+b method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    Returns:
        list: List of lists representing divided matrix.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("All elements of the matrix must be " +
                                "integers or floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        divided_matrix.append(new_row)

    return divided_matrix
