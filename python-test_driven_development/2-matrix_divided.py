#!/usr/bin/python3
"""
Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    new_matrix = []
    row_length = 0

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(msg_type)

        if i == 0:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError(msg_size)

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
