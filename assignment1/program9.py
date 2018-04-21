"""
    Custom filters
"""

import cv2 as cv
import filter
import util
import color

name = "skate.jpg"
# name = "32bits.png"
original = util.read_image(name)
cv.imshow('Original', original)

# Custom 1
custom1 = filter.custom_filter1(original)
cv.imshow('Custom 1', custom1)
util.write_image("custom1-filter-" + name, custom1)

# Custom 2
custom2 = filter.custom_filter2(original)
cv.imshow('Custom 2', custom2)
util.write_image("custom2-filter-" + name, custom2)

cv.waitKey(0)
cv.destroyAllWindows()
