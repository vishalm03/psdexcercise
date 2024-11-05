import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp


class TestScientificCalculator(unittest.TestCase):
    # sin
    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1, places=5)
    
    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1, places=5)
    
    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0, places=5)
    
    def test_sin_invalid_input(self):
        with self.assertRaises(TypeError):
            sin("hello")
    
    # cos
    def test_cos_positive(self):
        self.assertAlmostEqual(cos(90), 0, places=5)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(-90), 0, places=5)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos(0), 1, places=5)

    def test_cos_invalid_input(self):
        with self.assertRaises(TypeError):
            cos("hello")
    
    # tan
    def test_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1, places=5)

    def test_tan_negative(self):
        self.assertAlmostEqual(tan(-45), -1, places=5)

    def test_tan_zero(self):
        self.assertAlmostEqual(tan(0), 0, places=5)

    def test_tan_invalid_input(self):
        with self.assertRaises(TypeError):
            tan("hello")
    
    # sqrt
    def test_sqrt_positive(self):
        self.assertAlmostEqual(sqrt(16), 4, places=5)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(sqrt(0), 0, places=5)

    def test_sqrt_invalid_input(self):
        with self.assertRaises(TypeError):
            sqrt("hello")

    def test_sqrt_negative_input(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
    
    # log
    def test_log_positive(self):
        self.assertAlmostEqual(log(10), math.log(10), places=5)

    def test_log_one(self):
        self.assertAlmostEqual(log(1), 0, places=5)

    def test_log_invalid_input(self):
        with self.assertRaises(TypeError):
            log("hello")

    def test_log_negative_input(self):
        with self.assertRaises(ValueError):
            log(-1)
    
    # exp
    def test_exp_positive(self):
        self.assertAlmostEqual(exp(1), math.exp(1), places=5)

    def test_exp_zero(self):
        self.assertAlmostEqual(exp(0), 1, places=5)

    def test_exp_invalid_input(self):
        with self.assertRaises(TypeError):
            exp("hello")


if __name__ == '__main__':
    unittest.main()
