"""
Basic Operations on Images
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
"""

import numpy as np
import cv2 as cv


def check_8bytes_bounds(x):
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

    y = check_8bytes_bounds(y)
    i = check_8bytes_bounds(i)
    q = check_8bytes_bounds(q)

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

    r = check_8bytes_bounds(r)
    g = check_8bytes_bounds(g)
    b = check_8bytes_bounds(b)

    return r, g, b


def yiq_to_rgb(image):
    # Get YIQ components from the image
    q, i, y = cv.split(image)

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


def red_band(image):
    output = np.copy(image)
    output[:, :, 1] = 0
    output[:, :, 0] = 0
    return output


def green_band(image):
    output = np.copy(image)
    output[:, :, 2] = 0
    output[:, :, 0] = 0
    return output


def blue_band(image):
    output = np.copy(image)
    output[:, :, 2] = 0
    output[:, :, 1] = 0
    return output


def monochromatic_red(image):
    output = np.copy(image)
    r = output[:, :, 2]
    output[:, :, 1] = r
    output[:, :, 0] = r
    return output


def monochromatic_green(image):
    output = np.copy(image)
    g = output[:, :, 0]
    output[:, :, 2] = g
    output[:, :, 0] = g
    return output


def monochromatic_blue(image):
    output = np.copy(image)
    b = output[:, :, 0]
    output[:, :, 2] = b
    output[:, :, 1] = b
    return output


def calculate_rgb_to_gray(r, g, b):
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return check_8bytes_bounds(gray)


def rgb_to_gray(image):
    # Get RGB components from the image
    b, g, r = cv.split(image)

    gray = np.empty_like(image)

    width = image.shape[0]
    height = image.shape[1]

    for w in range(width):
        for h in range(height):
            gray_unit = calculate_rgb_to_gray(r[w][h], g[w][h], b[w][h])
            gray[w][h][2] = gray_unit
            gray[w][h][1] = gray_unit
            gray[w][h][0] = gray_unit

    return gray


def negative(image):
    neg = np.empty_like(image)

    neg[:, :, 2] = 255 - image[:, :, 2]
    neg[:, :, 1] = 255 - image[:, :, 1]
    neg[:, :, 0] = 255 - image[:, :, 0]

    return neg


def calculate_add_bright(r, g, b, factor):
    r += factor
    g += factor
    b += factor

    r = check_8bytes_bounds(r)
    g = check_8bytes_bounds(g)
    b = check_8bytes_bounds(b)

    return r, g, b


def calculate_mult_bright(r, g, b, factor):
    r *= factor
    g *= factor
    b *= factor

    r = check_8bytes_bounds(r)
    g = check_8bytes_bounds(g)
    b = check_8bytes_bounds(b)

    return r, g, b


def modify_brightness(image, factor, calculate):
    bright = np.copy(image)
    # Get RGB components from the image
    b, g, r = cv.split(bright)

    width = image.shape[0]
    height = image.shape[1]

    # Add additive brightness to every R, G and B component
    for w in range(width):
        for h in range(height):
            # The new brightness according to function argument "calculate"
            r[w][h], g[w][h], b[w][h] = calculate(r[w][h], g[w][h], b[w][h], factor)

            bright[w][h][2] = r[w][h]
            bright[w][h][1] = g[w][h]
            bright[w][h][0] = b[w][h]

    return bright


def additive_brightness(image, factor):
    return modify_brightness(image, factor, calculate_add_bright)


def multiplicative_brightness(image, factor):
    return modify_brightness(image, factor, calculate_mult_bright)


def calculate_threshold(y, mean):
    if y > mean:
        # White pixel
        return 255
    # Black pixel
    return 0


def thresholding(image, mean, y):
    # Copy image matrix
    black_white = np.copy(image)

    width = y.shape[0]
    height = y.shape[1]

    # Iterate the whole image
    for w in range(width):
        for h in range(height):
            y[w][h] = calculate_threshold(y[w][h], mean)

    # Update the output image with thresholding values
    black_white[:, :, 2] = y
    black_white[:, :, 1] = y
    black_white[:, :, 0] = y

    return black_white


def thresholding_user(image, mean):
    # Get YIQ
    yiq = rgb_to_yiq(image)
    # Get Y component
    y = yiq[:, :, 2]
    return thresholding(image, mean, y)


def thresholding_mean(image):
    # Get YIQ
    yiq = rgb_to_yiq(image)
    # Get Y component
    y = yiq[:, :, 2]
    mean = np.mean(y)
    return thresholding(image, mean, y)
