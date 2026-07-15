#!/usr/bin/env python3
"""Performs a convolution on images using multiple kernels."""

import numpy as np
from math import ceil, floor


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple kernels.

    Args:
        images: numpy.ndarray of shape (m, h, w, c)
        kernels: numpy.ndarray of shape (kh, kw, c, nc)
        padding: 'same', 'valid', or tuple (ph, pw)
        stride: tuple (sh, sw)

    Returns:
        numpy.ndarray containing the convolved images.
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if kc != c:
        raise ValueError("kernels and images must have the same number of channels")

    if padding == 'same':
        ph = ceil(((h - 1) * sh + kh - h) / 2)
        pw = ceil(((w - 1) * sw + kw - w) / 2)
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant'
    )

    oh = floor((h + 2 * ph - kh) / sh) + 1
    ow = floor((w + 2 * pw - kw) / sw) + 1

    output = np.zeros((m, oh, ow, nc))

    for i in range(oh):
        for j in range(ow):
            current = padded[
                :,
                i * sh:i * sh + kh,
                j * sw:j * sw + kw,
                :
            ]
            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    current * kernels[:, :, :, k],
                    axis=(1, 2, 3)
                )

    return output
