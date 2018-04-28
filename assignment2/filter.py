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

                    # Apply filter on every pixel
                    #   RGB * filter
                    #   [b, g, r] * filter[kr, kc]
                    #   Example:
                    #       [101, 102, 103] * 1
                    sum += img[py, px] * kernel[kr, kc]

            output[ir, ic] = sum

    output = util.check_matrix_bounds(output)
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

    output = util.check_matrix_bounds(output)

    return output
