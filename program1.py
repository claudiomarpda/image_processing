# RGB-YIQ-RGB conversion

import cv2 as cv
import color
import util


# TODO: Fix conversions. YIQ to RGB doesn't show the original image.

img_name = "skate.jpg"
original_img = util.read_image(img_name)

# RGB-YIQ
yiq_img = color.rgb_to_yiq(original_img)
cv.imshow(img_name + ' - YIQ', yiq_img)
util.write_image("yiq-" + img_name, yiq_img)

# YIQ-RGB
rgb_img = color.yiq_to_rgb(yiq_img)
cv.imshow(img_name + ' - RGB', rgb_img)
util.write_image("rgb-" + img_name, rgb_img)

cv.waitKey(0)
cv.destroyAllWindows()

