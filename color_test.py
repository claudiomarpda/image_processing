import unittest
import color


class TestColor(unittest.TestCase):
    def test_rgb_to_yiq_should_succeed1(self):
        y, i, q = color.calculate_rgb_to_yiq(25, 25, 25)
        print(y, i, q)
        self.assertTrue(y == 25 and i == 0 and q == 0)

    def test_rgb_to_yiq_should_succeed2(self):
        y, i, q = color.calculate_rgb_to_yiq(200, 200, 200)
        print(y, i, q)
        self.assertTrue(y == 200 and i == 0 and q == 0)

    def test_rgb_to_yiq_should_succeed3(self):
        y, i, q = color.calculate_rgb_to_yiq(100, 0, 0)
        print(y, i, q)
        self.assertTrue(29 <= y <= 30 and 59 <= i <= 60 and 21 <= q <= 22)


if __name__ == '__main__':
    unittest.main()
