# Monochromatic and colored images in individual R, G, and B

import cv2 as cv
import color
import util

name = "skate.jpg"
original = util.read_image(name)

# Processing

red_band = color.red_band(original)
green_band = color.green_band(original)
blue_band = color.blue_band(original)

mono_red = color.monochromatic_red(original)
mono_green = color.monochromatic_green(original)
mono_blue = color.monochromatic_blue(original)

gray = color.rgb_to_gray(original)

# Save

util.write_image("red-" + name, red_band)
util.write_image("green-" + name, green_band)
util.write_image("blue-" + name, blue_band)
util.write_image("mono-red-" + name, mono_red)
util.write_image("mono-green-" + name, mono_green)
util.write_image("mono-blue-" + name, mono_blue)
util.write_image("gray-" + name, gray)

# Show

cv.imshow('Red', red_band)
cv.imshow('Green', green_band)
cv.imshow('Blue', blue_band)

cv.imshow('Monochromatic Red', mono_red)
cv.imshow('Monochromatic Green', mono_green)
cv.imshow('Monochromatic Blue', mono_blue)

cv.imshow('Gray', gray)


cv.waitKey(0)
cv.destroyAllWindows()
