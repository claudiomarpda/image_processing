import numpy as np


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
