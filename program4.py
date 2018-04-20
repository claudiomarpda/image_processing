"""
Additive brightness control.
Resulting pixel value = original pixel value + c, c integer).
Watch out for R, G and B bounds!
"""

import cv2 as cv
import color
import util


BRIGHTNESS_FACTOR = 100

name = "skate.jpg"
original = util.read_image(name)

bright = color.additive_brightness(original, BRIGHTNESS_FACTOR)
cv.imshow('Additive Brightness', bright)
util.write_image("rgb-add-bright-" + name, bright)

yiq = color.rgb_to_yiq(original)
bright = color.additive_brightness(yiq, BRIGHTNESS_FACTOR)
cv.imshow('Additive Brightness', bright)
util.write_image("yiq-add-bright-" + name, bright)

cv.waitKey(0)
cv.destroyAllWindows()
