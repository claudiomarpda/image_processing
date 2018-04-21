"""
Thresholding on Y with a median m.
    Case 1: m from user input
    Case 2: m from mean of Y values
"""

import cv2 as cv
import color
import util


THRESHOLDING_FACTOR = 127

name = "skate.jpg"
original = util.read_image(name)

# Mean from user input
black_white_user = color.thresholding_user(original, THRESHOLDING_FACTOR)
cv.imshow('Thresholding User Input', black_white_user)
util.write_image("thres-user-" + name, black_white_user)

# Mean calculated from Y component
black_white_mean = color.thresholding_mean(original)
cv.imshow('Thresholding Mean', black_white_mean)
util.write_image("thres-mean-" + name, black_white_mean)

cv.waitKey(0)
cv.destroyAllWindows()
