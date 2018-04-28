import unittest
import numpy as np
import filter


class TestHistogram(unittest.TestCase):

    def test_histogram_expansion_formula_should_succeed(self):
        """
        Testing expansion formula
        """

        # This configuration assures the output matrix is the same as the input
        # For expansion formula
        a = np.array([[0, 1, 1], [2, 4, 4], [2, 1, 0]])
        _min = a.min()
        _max = a.max()
        _l = 5
        # End of config

        # Image width and height
        w = a.shape[1]
        h = a.shape[0]

        output = np.zeros_like(a)

        for r in range(h):
            for c in range(w):
                output[r, c] = filter.calc_expansion(a[r, c], _min, _max, _l)

        print('Input matrix')
        print(a)
        print('Output matrix')
        print(output)
        np.alltrue(a == output)
