import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 10), 5)     # 10 / 2
        self.assertEqual(divide(5, 20), 4)     # 20 / 5
        self.assertAlmostEqual(divide(2, 5), 2.5)  # 5 / 2
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 10), 1.0)
        self.assertAlmostEqual(logarithm(4, 16), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # base 1 invalid
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)  # argument must be positive

    def test_hypotenuse(self):  # 3 assertions
        # assuming calculator has: def hypotenuse(a, b): return math.hypot(a, b)
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):  # 3 assertions
        # assuming calculator has: def square_root(x): return math.sqrt(x)
        with self.assertRaises(ValueError):
            square_root(-9)

        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(16), 4.0)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
