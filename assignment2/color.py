import numpy as np
import cv2 as cv
import util


def calculate_rgb_to_gray(r, g, b):
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return util.check_8bytes_bounds(gray)


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
