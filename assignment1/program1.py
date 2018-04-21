# RGB-YIQ-RGB conversion

import cv2 as cv
import color
import util

# An image is a matrix with the dimensions [w][h][3]. 3 for R, G and B

name = "32bits.png"
original = util.read_image(name)

# RGB to YIQ
yiq = color.rgb_to_yiq(original)
cv.imshow('YIQ', yiq)
util.write_image("yiq-" + name, yiq)

# YIQ to RGB
rgb = color.yiq_to_rgb(yiq)
cv.imshow('RGB', rgb)
util.write_image("rgb-" + name, rgb)

cv.waitKey(0)
cv.destroyAllWindows()
