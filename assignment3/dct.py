import math
import numpy as np


def ck(k):
    """
    :param k: cosine index
    """
    return math.sqrt(0.5) if k == 0 else 1


def freq(n, k):
    """
    :param n: number of signals
    :param k: cosine index
    """
    return k / (2.0 * n)


def theta(n, k):
    """
    :param n: number of signals
    :param k: cosine index
    """
    return (k * math.pi) / (2.0 * n)


def transform_1d(signals):
    """
    One dimensional DCT
    :param signals: 1d vector with all signals
    :param coef: number of significant coefficients to be preserved. 0 to preserve all of them.
    :return: 1d vector with new signals
    """

    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    # Through cosines
    for k in range(n):
        _sum = 0
        # Through all signals
        for i in range(n):
            _sum += signals[i] * math.cos(2 * math.pi * freq(n, k) * i + theta(n, k))

        new_signals[k] = math.sqrt(2.0 / n) * ck(k) * _sum

    return new_signals


def i_transform_1d(signals):
    """
    One dimensional IDCT
    :param signals: 1d vector with all signals
    :return: 1d vector with new signals
    """
    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    # Through all signals
    for i in range(n):
        _sum = 0
        # Through cosines
        for k in range(n):
            _sum += ck(k) * signals[k] * math.cos(2 * math.pi * freq(n, k) * i + theta(n, k))

        new_signals[i] = math.sqrt(2.0 / n) * _sum

    return new_signals


def i_transform_2d(signals):
    """
    Bidimensional IDCT
    :param signals: 2d vector with all signals
    :return: 2d vector with new signals
    """

    height = signals.shape[0]
    width = signals.shape[1]
    new_signals_1 = np.zeros_like(signals).astype(float)
    new_signals_2 = np.zeros_like(signals).astype(float)

    # Apply IDCT on all rows
    for h in range(height):
        new_signals_1[h, :] = i_transform_1d(signals[h, :])
    # Apply IDCT on all columns of the previous result
    for w in range(width):
        new_signals_2[:, w] = i_transform_1d(new_signals_1[:, w])

    return new_signals_2


def transform_2d(signals, coef=0):
    """
     Bidimensional DCT
     :param signals: 2d vector with all signals
     :param coef: number of significant coefficients to be preserved. 0 to preserve all of them.
     :return: 2d vector with new signals
     """

    height = signals.shape[0]
    width = signals.shape[1]
    new_signals_1 = np.zeros_like(signals).astype(float)
    new_signals_2 = np.zeros_like(signals).astype(float)

    # Apply DCT on all rows
    for h in range(height):
        new_signals_1[h, :] = transform_1d(signals[h, :])
    # Apply DCT on all columns of the previous result
    for w in range(width):
        new_signals_2[:, w] = transform_1d(new_signals_1[:, w])

    if coef > 0:
        # Flat the 2D array in 1D
        new_signals_3 = np.sort(np.array(new_signals_2).ravel())
        # Sort the 1D array in decreasing order
        new_signals_3 = new_signals_3[::-1]

        for i in range(coef - 1, width * height):
            new_signals_3[i] = 0

        # Go back from 1D to 2D
        new_signals_3 = np.reshape(new_signals_3, (-1, height))

        for w in range(width):
            for h in range(height):
                for c in range(coef):
                    if new_signals_2[h, w] == new_signals_3[c]:
                        continue
                    else:
                        new_signals_2[h, w] = 0

    return new_signals_2
