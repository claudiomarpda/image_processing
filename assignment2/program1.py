import cv2 as cv
import numpy as np

import color
import filter
import util

c = 1
d = 1

# Sharpness filter
kernel1 = np.array([
    [0, -c, 0],
    [-c, (4 * c) + d, -c],
    [0, -c, 0]
])

# Sharpness filter
kernel2 = np.array([
    [-c, -c, -c],
    [-c, (8 * c) + d, -c],
    [-c, -c, -c]
])

# Edge detection filter
kernel3 = [
    [- 1 / 8, - 1 / 8, - 1 / 8],
    [- 1 / 8, 1, - 1 / 8],
    [- 1 / 8, - 1 / 8, - 1 / 8]
]

offset = 1

# Original
name = "monkey.jpg"
img = util.read_image(name)
cv.imshow("Original", img)

# Gray
img_gray = color.rgb_to_gray(img)
cv.imshow("Gray", img_gray)
util.write_image("gray-" + name, img_gray)

# Convolution Kernel 1
output1 = filter.convolution(img, kernel1, offset)
cv.imshow("My Convolution", output1)
util.write_image("c1-my-" + name, output1)


# Gray + Convolution Kernel 1
output1 = filter.convolution(img_gray, kernel1, offset)
cv.imshow("My Convolution Gray", output1)
util.write_image("c1-my-gray-" + name, output1)

cv.waitKey(0)
cv.destroyAllWindows()
