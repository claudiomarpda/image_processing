"""
    Edge detection filters Sobel and Laplace
"""

import cv2 as cv
import filter
import util
import color

name = "skate.jpg"
# name = "lenna.png"
original = util.read_image(name)
# cv.imshow('Original', original)

# Sobel X
# sobel_x = cv.Sobel(original, cv.CV_64F, 1, 0, 3)
sobel_x = filter.sobel_x(original)
cv.imshow('Sobel X', sobel_x)
util.write_image("sobelx-filter-" + name, sobel_x)

# Sobel Y
# sobel_y = cv.Sobel(original, cv.CV_64F, 0, 1, 3)
sobel_y = filter.sobel_y(original)
cv.imshow('Sobel Y', sobel_y)
util.write_image("sobely-filter-" + name, sobel_y)

# Sobel XY
# sobel_xy = cv.Sobel(original, cv.CV_64F, 1, 1, 3)
sobel_xy = filter.sobel_xy(original)
cv.imshow('Sobel XY', sobel_xy)
util.write_image("sobelxy-filter-" + name, sobel_xy)

# Laplace
# laplace = cv.Laplacian(original, cv.CV_64F)
laplace = filter.laplace(original)
cv.imshow('Laplace', laplace)
util.write_image("laplace-filter-" + name, laplace)

cv.waitKey(0)
cv.destroyAllWindows()
