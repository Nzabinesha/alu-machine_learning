#!/usr/bin/env python3
"""Module that calculates the shape of a matrix."""


def matrix_shape(matrix):
    """Calculate the shape of a matrix.

    Args:
        matrix: a nested list representing the matrix.

    Returns:
        A list of integers representing the shape of the matrix.
    """
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
