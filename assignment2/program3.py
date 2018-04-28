import cv2 as cv
import color
import util
import filter

name = 'monkey.jpg'
img = util.read_image(name)
lightness = 350

img_gray = color.rgb_to_gray(img)
cv.imshow('RGB to Gray (r=g=b)', img_gray)
util.write_image("gray-" + name, img_gray)

img_expansion = filter.histogram_expansion(img_gray, lightness)
cv.imshow('Histogram Expansion L=' + str(lightness), img_expansion)
util.write_image('hist-exp-l' + str(lightness) + '-' + name, img_expansion)

cv.waitKey(0)
cv.destroyAllWindows()
