import cv2 as cv

IMG_PATH = 'img/'


def read_image(name):
    return cv.imread(IMG_PATH + name)


def write_image(name, image):
    cv.imwrite(IMG_PATH + name, image)
