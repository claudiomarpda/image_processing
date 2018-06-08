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
    :return: 1d vector with new signals
    """

    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    # Through cosines
    for k in range(n):
        _sum = 0
        # Through all signals
        for i in range(n):
            _sum += ck(k) * signals[i] * math.cos(2 * math.pi * freq(n, k) * i + theta(n, k))

        _sum *= math.sqrt(2.0 / n)
        new_signals[k] = _sum

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
        _sum *= math.sqrt(2.0 / n)
        new_signals[i] = _sum

    return new_signals


def transform_2d(signals, inverse=False):
    """
    Bi dimensional DCT
    :param inverse: true for IDCT
    :param signals: 2d vector with all signals
    :return: 2d vector with new signals
    """

    rows = signals.shape[0]
    new_signals = np.zeros_like(signals).astype(float)

    for r in range(rows):
        if inverse:
            new_signals[r] = i_transform_1d(signals[r, :])
        else:
            new_signals[r] = transform_1d(signals[r, :])

    return new_signals
