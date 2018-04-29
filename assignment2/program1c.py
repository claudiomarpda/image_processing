"""
Convolutions with Emboss Filters
"""

import cv2 as cv
import numpy as np

import color
import util

kernel_c1 = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, -1]
])

kernel_c2 = np.array([
    [0, 0, -1],
    [0, 1, 0],
    [0, 0, 0]
])

kernel_c3 = np.array([
    [0, 0, 2],
    [0, -1, 0],
    [-1, 0, 0]
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

# Convolution Kernel c1
util.do_convolution_show_and_write(_img, kernel_c1, "conv-c1-" + name, _offset)
# Convolution Gray Kernel c1
util.do_convolution_show_and_write(img_gray, kernel_c1, "conv-c1-gray-" + name, _offset)

# 2
util.do_convolution_show_and_write(_img, kernel_c2, "conv-c2-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_c2, "conv-c2-gray-" + name, _offset)

# 3
util.do_convolution_show_and_write(_img, kernel_c3, "conv-c3-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_c3, "conv-c3-gray-" + name, _offset)


cv.waitKey(0)
cv.destroyAllWindows()
