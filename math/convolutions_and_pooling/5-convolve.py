#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple
kernels.
"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Performs a convolution on images using multiple kernels.

    Args:
        images: numpy.ndarray of shape (m, h, w, c) containing
            multiple images.
            m is the number of images.
            h is the height in pixels of the images.
            w is the width in pixels of the images.
            c is the number of channels in the image.
        kernels: numpy.ndarray of shape (kh, kw, c, nc) containing
            the kernels for the convolution.
            kh is the height of a kernel.
            kw is the width of a kernel.
            nc is the number of kernels.
        padding: either a tuple of (ph, pw), 'same', or 'valid'.
            if 'same', performs a same convolution.
            if 'valid', performs a valid convolution.
            if a tuple:
                ph is the padding for the height of the image.
                pw is the padding for the width of the image.
        stride: tuple of (sh, sw).
            sh is the stride for the height of the image.
            sw is the stride for the width of the image.

    Returns:
        numpy.ndarray containing the convolved images.
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        if kh % 2 == 0:
            ph = ((h - 1) * sh + kh - h) // 2 + 1
        else:
            ph = ((h - 1) * sh + kh - h) // 2
        if kw % 2 == 0:
            pw = ((w - 1) * sw + kw - w) // 2 + 1
        else:
            pw = ((w - 1) * sw + kw - w) // 2
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant',
        constant_values=0
    )

    output_h = ((h + (2 * ph) - kh) // sh) + 1
    output_w = ((w + (2 * pw) - kw) // sw) + 1

    convolved = np.zeros((m, output_h, output_w, nc))

    for i in range(output_h):
        for j in range(output_w):
            y = i * sh
            x = j * sw
            image_slice = padded[:, y:y + kh, x:x + kw, :]
            convolved[:, i, j, :] = np.tensordot(
                image_slice, kernels, axes=([1, 2, 3], [0, 1, 2])
            )

    return convolved
