# RGB to Negative

import cv2 as cv
import color
import util

name = "skate.jpg"
original = util.read_image(name)

negative = color.rgb_to_negative(original)
cv.imshow('Negative', negative)
util.write_image("neg-" + name, negative)

cv.waitKey(0)
cv.destroyAllWindows()
