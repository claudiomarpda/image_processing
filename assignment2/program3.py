"""
Histogram Expansion and Equalization
Conversions:

gray to expansion
gray to equalization
gray to expansion to equalization
gray to equalization to expansion

"""

import cv2 as cv
import color
import util
import filter

name = 'monkey.jpg'
img = util.read_image(name)
lightness = 350

# RGB to Gray
img_gray = color.rgb_to_gray(img)
cv.imshow('RGB to Gray (r=g=b)', img_gray)
util.write_image("gray-" + name, img_gray)

# Gray to Expansion
img_expansion = filter.histogram_expansion(img_gray, lightness)
cv.imshow('Histogram Expansion L=' + str(lightness), img_expansion)
util.write_image('hist-exp-l' + str(lightness) + '-' + name, img_expansion)

# Expansion to Equalization
img_equalization = filter.histogram_equalization(img_expansion)
cv.imshow('Histogram Expansion L=' + str(lightness) + ' + Equalization', img_equalization)
util.write_image('hist-exp-l' + str(lightness) + '-eq-' + name, img_equalization)

# Gray to Equalization
img_equalization = filter.histogram_equalization(img_gray)
cv.imshow('Histogram Equalization', img_equalization)
util.write_image('hist-eq-' + name, img_equalization)

# Equalization to Expansion
img_expansion = filter.histogram_expansion(img_equalization, lightness)
cv.imshow('Histogram Equalization + Expansion L=' + str(lightness), img_expansion)
util.write_image('hist-eq-exp-l' + str(lightness) + '-' + name, img_expansion)

cv.waitKey(0)
cv.destroyAllWindows()
