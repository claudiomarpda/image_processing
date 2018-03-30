# Monochrome images in individual R, G, and B

import cv2 as cv
import color
import util

name = "skate.jpg"
original = util.read_image(name)

red = color.mono_red(original)
cv.imshow('Mono Red', red)
util.write_image("red-" + name, red)

green = color.mono_green(original)
cv.imshow('Mono Green', green)
util.write_image("green-" + name, green)

blue = color.mono_blue(original)
cv.imshow('Mono Blue', blue)
util.write_image("blue-" + name, blue)

gray = color.rgb_to_gray(original)
cv.imshow('Gray', gray)
util.write_image("gray-" + name, gray)


cv.waitKey(0)
cv.destroyAllWindows()
