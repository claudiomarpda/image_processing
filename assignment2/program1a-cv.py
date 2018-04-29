"""
Convolution with Sharpness Filters using OpenCV 2 Library
"""

import cv2 as cv
import numpy as np

import color
import util

c = 1
d = 1

# Sharpness filters

kernel1 = np.array([
    [0, -c, 0],
    [-c, (4 * c) + d, -c],
    [0, -c, 0]
])

kernel2 = np.array([
    [-c, -c, -c],
    [-c, (8 * c) + d, -c],
    [-c, -c, -c]
])

name = "monkey.jpg"
img = util.read_image(name)
cv.imshow("Original", img)

# Gray
img_gray = color.rgb_to_gray(img)
cv.imshow("Gray", img_gray)

# Convolution Kernel a1
util.cv_do_convolution_show_and_write(img, kernel1, "cv-conv-a1-" + name)
# Convolution Gray Kernel a1
util.cv_do_convolution_show_and_write(img_gray, kernel1, "cv-conv-a1-gray-" + name)

# a1
util.cv_do_convolution_show_and_write(img, kernel2, "cv-conv-a2-" + name)
util.cv_do_convolution_show_and_write(img_gray, kernel2, "cv-conv-a2-gray-" + name)

cv.waitKey(0)
cv.destroyAllWindows()
