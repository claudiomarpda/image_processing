import cv2 as cv

PATH = "img/"


def read_image(name):
    return cv.imread(PATH + name)


def write_image(name, image):
    cv.imwrite(PATH + name, image)
