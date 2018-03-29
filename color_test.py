import unittest
import color


class TestColor(unittest.TestCase):
    # RGB to YIQ

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

    # YIQ to RGB

    def test_yiq_to_rgb_should_succeed1(self):
        r, g, b = color.calculate_yiq_to_rgb(25, 0, 0)
        print(r, g, b)
        self.assertTrue(r == 25 and g == 25 and b == 25)

    def test_yiq_to_rgb_should_succeed2(self):
        r, g, b = color.calculate_yiq_to_rgb(200, 0, 0)
        print(r, g, b)
        self.assertTrue(r == 200 and g == 200 and b == 200)

    def test_yiq_to_rgb_should_succeed3(self):
        r, g, b = color.calculate_yiq_to_rgb(29.9, 59.6, 21.1)
        print(r, g, b)
        self.assertTrue(99 <= r <= 100 and 0 <= g <= 1 and 0 <= b <= 1)


if __name__ == '__main__':
    unittest.main()
