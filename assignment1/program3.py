# RGB to Negative

import cv2 as cv
import color
import util

name = "skate.jpg"
original = util.read_image(name)

negative = color.negative(original)
cv.imshow('RGB Negative', negative)
util.write_image("rgb-neg-" + name, negative)

yiq = color.yiq_to_rgb(original)
yiq_negative = color.negative(yiq)
cv.imshow('YIQ Negative', yiq_negative)
util.write_image("yiq-neg-" + name, yiq_negative)

cv.waitKey(0)
cv.destroyAllWindows()
