#!/usr/bin/env python3
"""Module that performs matrix multiplication."""


def mat_mul(mat1, mat2):
    """Perform matrix multiplication.

    Args:
        mat1: a 2D list of ints/floats.
        mat2: a 2D list of ints/floats.

    Returns:
        A new 2D list that is the matrix product of mat1 and mat2,
        or None if the two matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for row in mat1:
        new_row = []
        for col in zip(*mat2):
            new_row.append(sum(a * b for a, b in zip(row, col)))
        result.append(new_row)
    return result
