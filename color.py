"""
Basic Operations on Images
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
"""

import numpy as np
import cv2 as cv


def calculate_rgb_to_yiq(r, g, b):
    # TODO: Handle R, G and B limits during conversion

    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    return np.trunc(y), np.trunc(i), np.trunc(q)


def rgb_to_yiq(image):
    # Get RGB components from the image
    b, g, r = cv.split(image)

    # Create an empty matrix with the dimension of the input image
    out = np.empty_like(image)

    # Calculate YIQ for the whole matrix
    y, i, q = calculate_rgb_to_yiq(r, g, b)

    # Set YIQ in the output image
    # R, G and B, respectively
    out[:, :, 2] = y
    out[:, :, 1] = i
    out[:, :, 0] = q

    return out
