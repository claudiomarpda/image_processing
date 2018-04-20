import numpy as np

KERNEL_DIM = 3


def filter_frame(image, kernel, filter_func):
    output = np.empty_like(image)

    width = output.shape[0]
    height = output.shape[1]

    # Iterate the matrix

    # Rows
    for w in range(width):
        # Kernel's rows
        row_start = w - (kernel + 1)
        row_end = w + (kernel - 1)

        # Check invalid index
        if row_start < 0:
            row_start = w
        if row_end > width:
            row_end = width

        # Columns
        for h in range(height):
            # Kernel's columns
            column_start = h - (kernel + 1)
            column_end = h + (kernel - 1)

            # Check invalid index
            if column_start < 0:
                column_start = 0
            if column_end > height:
                column_end = height

            # Calculate R, G and B according to filter function type
            output[w, h, 2] = filter_func(image[row_start: row_end, column_start: column_end, 2]).astype(int)  # R
            output[w, h, 1] = filter_func(image[row_start: row_end, column_start: column_end, 1]).astype(int)  # G
            output[w, h, 0] = filter_func(image[row_start: row_end, column_start: column_end, 0]).astype(int)  # B

    return output


def average(image, kernel):
    return filter_frame(image, kernel, np.mean)


def median(image, kernel):
    return filter_frame(image, kernel, np.median)


def kernel_area(image, operation_func):
    output = np.empty_like(image)

    width = output.shape[1]
    height = output.shape[0]

    # Iterate the matrix

    # Rows
    for r in range(KERNEL_DIM, height - KERNEL_DIM):

        # Columns
        for c in range(KERNEL_DIM, width - KERNEL_DIM):
            # Calculate R, G and B according to operation function
            output[r, c, 2] = np.mean(operation_func(image[r: r + KERNEL_DIM, c: c + KERNEL_DIM, 2])).astype(int)  # R
            output[r, c, 1] = np.mean(operation_func(image[r: r + KERNEL_DIM, c: c + KERNEL_DIM, 1])).astype(int)  # G
            output[r, c, 0] = np.mean(operation_func(image[r: r + KERNEL_DIM, c: c + KERNEL_DIM, 0])).astype(int)  # B

    return output


def calculate_sobel_x(image):
    x_kernel = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    return image * x_kernel


def calculate_sobel_y(image):
    y_kernel = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    return image * y_kernel


def sobel_x(image):
    return kernel_area(image, calculate_sobel_x)


def sobel_y(image):
    return kernel_area(image, calculate_sobel_y)


def sobel_xy(image):
    return (kernel_area(image, calculate_sobel_x) +
           kernel_area(image, calculate_sobel_y)) / 2


def sobel_xy2(image):
    m = np.empty_like(image)
    mx = kernel_area(image, calculate_sobel_x)
    my = kernel_area(image, calculate_sobel_y)

    # r = np.empty_like(m[:, 0, 2])

    r = np.sqrt(np.square(mx[:, :, 2]) + np.square(my[:, :, 2]))
    g = np.sqrt(np.square(mx[:, :, 1]) + np.square(my[:, :, 1]))
    b = np.sqrt(np.square(mx[:, :, 0]) + np.square(my[:, :, 0]))

    m[:, :, 2] = r
    m[:, :, 1] = g
    m[:, :, 0] = b

    return m


def calculate_laplace(image):
    kernel = [0, 1, 0], [1, -4, 1], [0, 1, 0]
    return image * kernel


def laplace(image):
    return kernel_area(image, calculate_laplace)


def calculate_custom_filter1(image):
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    return image * kernel


def calculate_custom_filter2(image):
    kernel = [[0, 0, 0], [0, 1, 0], [0, 0, -1]]
    return image * kernel


def custom_filter1(image):
    return kernel_area(image, calculate_custom_filter1)


def custom_filter2(image):
    return kernel_area(image, calculate_custom_filter2)
