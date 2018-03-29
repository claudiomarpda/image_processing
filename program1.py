# RGB-YIQ-RGB conversion

import cv2 as cv
import color
import util


img_name = "skate.jpg"
original_img = util.read_image(img_name)

# RGB-YIQ
processed_img = color.rgb_to_yiq(original_img)
cv.imshow(img_name + ' - YIQ', processed_img)
util.write_image("yiq-" + img_name, processed_img)

# YIQ-RGB
# TODO: YIQ-RGB conversion

cv.waitKey(0)
cv.destroyAllWindows()

