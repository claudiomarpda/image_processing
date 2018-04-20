"""

"""

import cv2 as cv

import filter
import util

KERNEL = 3

name = "lenna-noise.png"
original = util.read_image(name)
cv.imshow('Original', original)

# Average
average = filter.average(original, KERNEL)
cv.imshow('Average Filter', average)
util.write_image("average-filter-" + name, average)

# Median
median = filter.median(original, KERNEL)
cv.imshow('Median Filter', median)
util.write_image("median-filter-" + name, median)

cv.waitKey(0)
cv.destroyAllWindows()
