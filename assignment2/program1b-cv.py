"""
Convolutions with Edge Detection Filters using OpenCV 2 Library
"""

import cv2 as cv
import numpy as np

import color
import util

kernel_b1 = np.array([
    [- 1 / 8, - 1 / 8, - 1 / 8],
    [- 1 / 8, 1, - 1 / 8],
    [- 1 / 8, - 1 / 8, - 1 / 8]
])

kernel_b2 = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

kernel_b3 = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

kernel_b4 = np.array([
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
])

# Original
name = "monkey.jpg"
_img = util.read_image(name)
cv.imshow("Original", _img)

# Gray
img_gray = color.rgb_to_gray(_img)
cv.imshow("Gray", img_gray)

# Convolution Kernel b1
util.cv_do_convolution_show_and_write(_img, kernel_b1, "cv-conv-b1-" + name)
# Convolution Gray Kernel b1
util.cv_do_convolution_show_and_write(img_gray, kernel_b1, "cv-conv-b1-gray-" + name)

# b2
util.cv_do_convolution_show_and_write(_img, kernel_b2, "cv-conv-b2-" + name)
util.cv_do_convolution_show_and_write(img_gray, kernel_b2, "cv-conv-b2-gray-" + name)

# b3
util.cv_do_convolution_show_and_write(_img, kernel_b3, "cv-conv-b3-" + name)
util.cv_do_convolution_show_and_write(img_gray, kernel_b3, "cv-conv-b3-gray-" + name)

# b4
util.cv_do_convolution_show_and_write(_img, kernel_b4, "cv-conv-b4-" + name)
util.cv_do_convolution_show_and_write(img_gray, kernel_b4, "cv-conv-b4-gray-" + name)
