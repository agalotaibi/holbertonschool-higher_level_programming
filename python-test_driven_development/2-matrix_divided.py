#!/usr/bin/python3
"""
This module defines the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers/floats.
        div (int/float): divisor.

    Returns:
        list of lists: new matrix with divided values.

    Raises:
        TypeError: if input is invalid.
        ZeroDivisionError: if div is 0.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
