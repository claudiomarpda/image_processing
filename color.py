"""
Basic Operations on Images
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
"""

import numpy as np
import cv2 as cv


def check_8bytes_bound(x):
    x = np.rint(x)

    if x > 255:
        return 255
    elif x < 0:
        return 0

    return x


def calculate_rgb_to_yiq(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b

    y = check_8bytes_bound(y)
    i = check_8bytes_bound(i)
    q = check_8bytes_bound(q)

    return y, i, q


def rgb_to_yiq(image):
    # Get RGB components from the image
    b, g, r = cv.split(image)

    # Create an empty matrix with the dimension of the input image
    yiq = np.empty_like(image)

    width = image.shape[0]
    height = image.shape[1]

    # Calculate YIQ from the input image, pixel by pixel

    for w in range(width):
        for h in range(height):
            y, i, q = calculate_rgb_to_yiq(r[w][h], g[w][h], b[w][h])
            yiq[w][h][2] = y
            yiq[w][h][1] = i
            yiq[w][h][0] = q

    return yiq


def calculate_yiq_to_rgb(y, i, q):
    r = y + 0.956 * i + 0.621 * q
    g = y - 0.272 * i - 0.647 * q
    b = y - 1.106 * i + 1.703 * q

    r = check_8bytes_bound(r)
    g = check_8bytes_bound(g)
    b = check_8bytes_bound(b)

    return r, g, b


def yiq_to_rgb(image):
    # Get YIQ components from the image
    q, i, y = cv.split(image)

    # Create an empty matrix with the dimension of the input image
    rgb = np.empty_like(image)

    width = image.shape[0]
    height = image.shape[1]

    # Calculate RGB from the input image, pixel by pixel

    for w in range(width):
        for h in range(height):
            r, g, b = calculate_yiq_to_rgb(y[w][h], i[w][h], q[w][h])

            rgb[w][h][2] = r
            rgb[w][h][1] = g
            rgb[w][h][0] = b

    return rgb


def mono_red(image):
    mono = np.copy(image)
    mono[:, :, 1] = 0
    mono[:, :, 0] = 0
    return mono


def mono_green(image):
    mono = np.copy(image)
    mono[:, :, 2] = 0
    mono[:, :, 0] = 0
    return mono


def mono_blue(image):
    mono = np.copy(image)
    mono[:, :, 2] = 0
    mono[:, :, 1] = 0
    return mono
