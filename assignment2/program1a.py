"""
Convolutions with Sharpness Filters
"""

import cv2 as cv
import numpy as np

import color
import util

c = 1
d = 1

kernel_a1 = np.array([
    [0, -c, 0],
    [-c, (4 * c) + d, -c],
    [0, -c, 0]
])

kernel_a2 = np.array([
    [-c, -c, -c],
    [-c, (8 * c) + d, -c],
    [-c, -c, -c]
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

# Convolution Kernel a1
util.do_convolution_show_and_write(_img, kernel_a1, "conv-a1-" + name, _offset)
# Convolution Gray Kernel a1
util.do_convolution_show_and_write(img_gray, kernel_a1, "conv-a1-gray-" + name, _offset)

# a2
util.do_convolution_show_and_write(_img, kernel_a2, "conv-a2-" + name, _offset)
util.do_convolution_show_and_write(img_gray, kernel_a2, "conv-a2-gray-" + name, _offset)

cv.waitKey(0)
cv.destroyAllWindows()
