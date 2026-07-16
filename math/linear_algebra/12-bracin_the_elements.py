#!/usr/bin/env python3
"""Module that performs element-wise operations on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication,
    and division.

    Args:
        mat1: array-like input that can be interpreted as a
            numpy.ndarray.
        mat2: array-like input that can be interpreted as a
            numpy.ndarray.

    Returns:
        A tuple containing the element-wise sum, difference,
        product, and quotient, respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
