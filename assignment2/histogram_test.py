import unittest
import numpy as np
import filter


class TestHistogram(unittest.TestCase):

    def test_histogram_expansion_formula_should_succeed(self):
        """
        Testing expansion formula
        """

        # This configuration assures the output matrix is the same as the input using the expansion formula
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

        for r in range(h):
            for c in range(w):
                self.assertEqual(a[r, c], output[r, c])

    def test_histogram_equalization_formula_should_succeed(self):
        """
        Testing equalization formula
        """

        # Configuration
        a = np.array([[0, 1, 1], [2, 4, 4], [2, 1, 0]])
        # Distribution result
        b = np.array([1, 2, 3, 3, 4])
        _l = 5
        # End of config

        # Image width and height
        h = a.shape[0]
        w = a.shape[1]

        # Histogram
        histogram = np.zeros([5]).astype(int)

        # Rows
        for r in range(h):
            # Columns
            for c in range(w):
                v = a[r, c]
                # Counts occurrence of values
                histogram[v] += 1

        # Accumulator
        acc = 0
        distribution = np.zeros([_l])

        for l in range(_l):
            acc += histogram[l]
            print('args ' + str(_l) + ', ' + str(h) + ', ' + str(w) + ', ' + str(acc))
            distribution[l] = filter.calc_equalization(_l, float(h), float(w), acc).astype(int)

        print('original')
        print(a)
        print('histogram count ' + str(histogram))
        print('distribution ' + str(distribution))

        for i in range(l):
            self.assertEqual(distribution[i], b[i])

