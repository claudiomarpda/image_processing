"""
Basic Operations on Images
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
"""

import numpy as np
import cv2 as cv


def calculate_rgb_to_yiq(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    return np.trunc(y), np.trunc(i), np.trunc(q)


def rgb_to_yiq(image):
    # TODO: Handle R, G and B limits during conversion

    # Get RGB components from the image
    b, g, r = cv.split(image)

    # Create an empty matrix with the dimension of the input image
    yiq_img = np.empty_like(image)

    # Calculate YIQ for the whole matrix
    y, i, q = calculate_rgb_to_yiq(r, g, b)

    # Set YIQ in the output image
    # R, G and B, respectively
    yiq_img[:, :, 2] = y
    yiq_img[:, :, 1] = i
    yiq_img[:, :, 0] = q

    return yiq_img


def calculate_yiq_to_rgb(y, i, q):
    r = y + 0.956 * i + 0.621 * q
    g = y - 0.272 * i - 0.647 * q
    b = y - 1.106 * i + 1.703 * q
    return np.trunc(r), np.trunc(g), np.trunc(b)


def yiq_to_rgb(image):
    # TODO: Handle R, G and B limits during conversion

    # Get YIQ components from the image
    q, i, y = cv.split(image)

    # Create an empty matrix with the dimension of the input image
    rgb_img = np.empty_like(image)

    # Calculate YIQ for the whole matrix
    r, g, b = calculate_rgb_to_yiq(y, i, q)

    # Set RGB in the output image
    rgb_img[:, :, 2] = r
    rgb_img[:, :, 1] = g
    rgb_img[:, :, 0] = b

    return rgb_img
