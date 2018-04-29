import numpy as np
import util

_8BITS = 256


def convolution(img, kernel, offset):
    output = np.zeros_like(img)

    # Flip the kernel up to down and left to right
    kernel = np.flipud(np.fliplr(kernel))

    # image width and height
    iw = output.shape[1]
    ih = output.shape[0]

    # kernel width and height
    kw = np.shape(kernel)[1]
    kh = np.shape(kernel)[0]

    # Kernel edges
    # We gonna use filters like
    #   3x3 (One central point plus 1 point around):
    #       3 // 2 = 1
    kw_edge = kw // 2
    kh_edge = kh // 2

    global _sum

    # Rows
    for ir in range(0, ih, offset):
        for ic in range(0, iw, offset):
            # Sum is the RGB value that starts with 0 for every pixel
            # sum = [0, 0, 0]
            _sum = np.zeros(3)

            # Go through the kernel
            for kr in range(kh):
                # Pixel row
                py = ir - kh_edge + kr
                # Check invalid indexes of the image, the kernel edges
                if py < 0 or py >= ih:
                    continue

                for kc in range(kw):
                    # Pixel column
                    px = ic - kw_edge + kc
                    # Check invalid indexes of the image, the kernel edges
                    if px < 0 or px >= iw:
                        continue

                    # Apply kernel on every pixel
                    r = img[py, px, 2] * kernel[kr, kc]
                    g = img[py, px, 1] * kernel[kr, kc]
                    b = img[py, px, 0] * kernel[kr, kc]

                    _sum[2] += r
                    _sum[1] += g
                    _sum[0] += b

            _sum[2] = util.check_8bits_bounds(_sum[2])
            _sum[1] = util.check_8bits_bounds(_sum[1])
            _sum[0] = util.check_8bits_bounds(_sum[0])

            output[ir, ic, 2] = _sum[2]
            output[ir, ic, 1] = _sum[1]
            output[ir, ic, 0] = _sum[0]

    return output


def calc_expansion(r, r_min, r_max, l):
    """
    Formula for Histogram Expansion

    :param r: Gray scalar value of the image
    :param r_min: Minimum gray value of the image
    :param r_max: Maximum gray value of the image
    :param l: Lightness intensity
    :return: New gray scalar value
    """

    # Force real number to ensure right math results, although all the arguments are integers
    # If r_max was left as an integer, the math would lose precision and return a wrong value
    r_max = float(r_max)

    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1))


def histogram_expansion(img, l):
    """
    Histogram Expansion is a point technique that takes in count
    each gray scale value individually.
    Calculate gray scale values according to lightness intensity.

    :param img: Gray scale image with R = B = G
    :param l: Lightness intensity
    :return: A new image
    """

    output = np.zeros_like(img)

    # Image width and height
    iw = img.shape[1]
    ih = img.shape[0]

    # Assuming R = G = B
    # Get the value of only one channel
    _max = img[:, :, 0].max()
    _min = img[:, :, 0].min()

    # Rows
    for r in range(ih):
        # Columns
        for c in range(iw):

            # Pixel [R, G, B]
            pixel = np.zeros(3)

            for i in range(3):
                # Assuming R = G = B
                # Get the value of one channel (0 = blue)
                pixel[i] = calc_expansion(img[r, c, 0], _min, _max, l)
                pixel[i] = util.check_8bits_bounds(pixel[i])

            output[r, c, :] = pixel

    return output


def calc_equalization(l, h, w, acc):
    """
    Formula for Histogram Equalization

    :param l: The number of bits available for the image
    :param h: Image height
    :param w: Image width
    :param acc: The accumulated value (gray scale) of histogram occurrence
    :return: Equalized value in gray scale
    """

    h = float(h)
    w = float(w)

    return np.round(
        (((l - 1) / (h * w)) * acc)
    )


def histogram_equalization(img):
    """
    Histogram Equalization can produce a richer image visually.
    It aims to produce a image with uniform gray scale values.
    It is a local technique that takes in count the occurrence of
    all image's pixels with the same gray scale vale.

    Uses a 8 bits distribution (256 values, 0 to 255).

    :param img: Gray scale image with R = B = G
    :return: New image with equalized values in gray scale
    """

    output = np.zeros_like(img)

    # Image width and height
    ih = img.shape[0]
    iw = img.shape[1]

    # Histogram
    histogram = np.zeros([_8BITS]).astype(int)

    # Counting occurrence of values
    # Rows
    for r in range(ih):
        # Columns
        for c in range(iw):
            # Assuming R = G = B
            # Get gray value (0 to 255)
            gray_value = img[r, c, 0]  # 0 = blue

            histogram[gray_value] += 1

    # Accumulator
    acc = 0
    distribution = np.zeros([_8BITS]).astype(int)

    # Getting new distribution with equalization
    for l in range(_8BITS):
        acc += histogram[l]
        distribution[l] = calc_equalization(_8BITS, ih, iw, acc)
        distribution[l] = util.check_8bits_bounds(distribution[l])

    # Updating image with equalized values
    for r in range(ih):
        for c in range(iw):
            gray_value = img[r, c, 0]
            output[r, c, :] = distribution[gray_value]

    return output
