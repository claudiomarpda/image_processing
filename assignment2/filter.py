import numpy as np
import util


def convolution(img, kernel, offset):
    output = np.zeros_like(img)

    # image width and height
    iw = output.shape[1]
    ih = output.shape[0]

    # kernel width and height
    kw = np.shape(kernel)[1]
    kh = np.shape(kernel)[0]

    print(kernel)
    print(np.shape(kernel))

    global sum

    # Kernel edges
    # We gonna use filters like
    #   3x3 (One central point plus 1 point around):
    #       3 // 2 = 1

    kw_edge = kw // 2
    kh_edge = kh // 2

    # Iterate the matrix
    # Rows
    for ir in range(0, ih, offset):
        for ic in range(0, iw, offset):
            # Sum is the RGB value that starts with 0 for every pixel
            # sum = [0, 0, 0]
            sum = np.zeros(3)

            # Go through the kernel
            for kr in range(kh):
                for kc in range(kw):

                    # Pixel
                    # py is row
                    py = ir - kh_edge + kr
                    # px is column
                    px = ic - kw_edge + kc

                    # Check invalid indexes of the image, the edges
                    if (py < 0 or py >= ih) or (px < 0 or px >= iw):
                        continue

                    # Apply kernel on every pixel
                    #   RGB * kernel
                    #   [b, g, r] * kernel[kr, kc]
                    #   Example:
                    #       [101, 102, 103] * 1
                    sum += img[py, px] * kernel[kr, kc]

            output[ir, ic] = sum

    output = util.check_img_pixels_bounds(output)
    return output


def convolution2(img, kernel):
    output = np.zeros_like(img)

    # Image width and height
    iw = output.shape[1]
    ih = output.shape[0]

    # Kernel height
    kh = np.shape(kernel)[0]

    # Considering a kernel NxN
    # We gonna use 3x3
    #   3x3 (One central point plus 1 point around):
    #       3 // 2 = 1
    #       Integer division
    kernel_edge = kh // 2

    for c in range(kernel_edge, iw - kernel_edge):
        for r in range(kernel_edge, ih - kernel_edge):
            img_kernel = img[
                         r - kernel_edge:r + kernel_edge + 1,
                         c - kernel_edge:c + kernel_edge + 1]

            # apply filter on the kernel
            output[r, c, 2] = np.sum(img_kernel[:, :, 2] * kernel)  # R
            output[r, c, 1] = np.sum(img_kernel[:, :, 1] * kernel)  # G
            output[r, c, 0] = np.sum(img_kernel[:, :, 0] * kernel)  # B

    output = util.check_img_pixels_bounds(output)

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

    # Force real number to ensure right math results, although all the parameters are integers
    # If r_max was left as an integer, the math would lose precision and return a wrong value
    r_max = float(r_max)

    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1))


def histogram_expansion(img, l):
    """
    Calculate gray scale values according to lightness intensity

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
                pixel[i] = util.check_8bytes_bounds(pixel[i])

            output[r, c, :] = pixel

    return output
