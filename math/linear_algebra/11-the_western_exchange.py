#!/usr/bin/env python3
"""Module that transposes a numpy.ndarray."""


def np_transpose(matrix):
    """Transpose a numpy.ndarray.

    Args:
        matrix: array-like input that can be interpreted as a
            numpy.ndarray.

    Returns:
        A new numpy.ndarray that is the transpose of matrix.
    """
    return matrix.transpose()
