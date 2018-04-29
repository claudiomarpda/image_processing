"""
Convolutions with Edge Detection Filters
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

_offset = 1

# Original
name = "monkey.jpg"
_img = util.read_image(name)
cv.imshow("Original", _img)

# Gray
img_gray = color.rgb_to_gray(_img)
cv.imshow("Gray", img_gray)
util.write_image("gray-" + name, img_gray)

# Convolution Kernel b1
util.do_convolution_show_and_write(_img, kernel_b1, "conv-b1-" + name, _offset)
# Convolution Gray Kernel b1
util.do_convolution_show_and_write(img_gray, kernel_b1, "conv-b1-gray-" + name, _offset)

# b2
util.do_convolution_show_and_write(_img, kernel_b2, "conv-b2-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_b2, "conv-b2-gray-" + name, _offset)

# b3
util.do_convolution_show_and_write(_img, kernel_b3, "conv-b3-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_b3, "conv-b3-gray-" + name, _offset)

# b4
util.do_convolution_show_and_write(_img, kernel_b4, "conv-b4-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_b4, "conv-b4-gray-" + name, _offset)

cv.waitKey(0)
cv.destroyAllWindows()
