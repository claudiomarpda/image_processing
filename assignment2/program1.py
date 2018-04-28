import cv2 as cv
import numpy as np

import color
import filter
import util

name = "monkey.jpg"
img = util.read_image(name)
cv.imshow("Original", img)

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

# Edge detection
kernel3 = [
    [- 1 / 8, - 1 / 8, - 1 / 8],
    [- 1 / 8, 1, - 1 / 8],
    [- 1 / 8, - 1 / 8, - 1 / 8]
]

# My convolution
output1 = filter.convolution(img, kernel1, 1)
cv.imshow("My Convolution", output1)
util.write_image("c1-my-" + name, output1)
#
# CV convolution
output1 = cv.filter2D(src=img, kernel=kernel1, ddepth=-1)
cv.imshow('OpenCV Convolution', output1)
util.write_image("c1-cv-" + name, output1)
#
# My gray scale + convolution
img_gray = color.rgb_to_gray(img)
output1 = filter.convolution(img_gray, kernel1, 1)
cv.imshow("My Convolution Gray", output1)
util.write_image("c1-my-gray-" + name, output1)
#
# CV gray scale + convolution
output1 = cv.filter2D(src=img_gray, kernel=kernel1, ddepth=-1)
cv.imshow('OpenCV Convolution Gray', output1)
util.write_image("c1-cv-gray-" + name, output1)
#
cv.waitKey(0)
cv.destroyAllWindows()
