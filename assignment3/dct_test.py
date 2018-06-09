import unittest
import numpy as np
import dct


class TestDCT(unittest.TestCase):

    def test_dct1d_should_succeed(self):
        signals = [3, -4, 2, 1]
        print('\nOriginal signals')
        print(signals)
        new_signals = dct.transform_1d(signals)
        print('Transform')
        print(new_signals)
        print('-------')

        i_signals = dct.i_transform_1d(new_signals)
        print('Inverse transform')
        print(signals)
        print('=======')
        for r in range(len(signals)):
            self.assertEqual(signals[r], round(i_signals[r], 2))

    def test_dct2d_should_succeed(self):
        signals = np.array([[3, -4, 2, 1], [3, -4, 2, 1]])
        print('\nOriginal signals')
        print(signals)
        new_signals = dct.transform_2d(signals)
        print('Transform')
        print(new_signals)
        print('-------')

        i_signals = dct.i_transform_2d(new_signals)
        print('Inverse transform')
        print(signals)
        print('=======')

        for r in range(signals.shape[0]):
            for c in range(signals.shape[1]):
                self.assertEqual(signals[r, c], round(i_signals[r, c], 2))
