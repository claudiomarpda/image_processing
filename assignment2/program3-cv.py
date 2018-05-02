import cv2 as cv

import util

# Equalization with OpenCV
img_cv = cv.imread('img/tree.jpg', 0)
cv_eq = cv.equalizeHist(img_cv)
cv.imshow('cv-eq-tree.jpg', cv_eq)
util.write_image('cv-eq-tree.jpg', cv_eq)

cv.waitKey(0)
cv.destroyAllWindows()