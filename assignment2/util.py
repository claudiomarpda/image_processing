import cv2 as cv

IMG_PATH = 'img/'


def read_image(name):
    return cv.imread(IMG_PATH + name)


def write_image(name, image):
    cv.imwrite(IMG_PATH + name, image)


def check_8bits_bounds(x):
    if x > 255:
        return 255
    elif x < 0:
        return 0

    return x


def check_img_pixels_bounds(matrix):
    # Image width and height
    w = matrix.shape[1]
    h = matrix.shape[0]

    # If no characters is printed, there is no rgb out of bounds (0, 255)

    # Rows
    for r in range(h):
        # Columns
        for c in range(w):
            # RGB
            for i in range(3):
                # Prints for visual illustration
                if matrix[r, c, i] < 0:
                    matrix[r, c, i] = 0
                    print('<')
                if matrix[r, c, i] > 255:
                    print('>')
                    matrix[r, c, i] = 255

                # Check bounds
                matrix[r, c, i] = check_8bits_bounds(matrix[r, c, i])

    return matrix
