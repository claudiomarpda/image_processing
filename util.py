import cv2 as cv
from numpy import rint

PATH = "img/"


def read_image(name):
    return cv.imread(PATH + name)


def write_image(name, image):
    cv.imwrite(PATH + name, image)


def check_8bytes_bounds(x):
    x = rint(x)
    if x > 255:
        return 255
    elif x < 0:
        return 0

    return x
