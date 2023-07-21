# test_calculator.py
import unittest
from calculator import add_numbers

class TestCalculator(unittest.TestCase):

    def test_add_numbers_positive(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-5, -7)
        self.assertEqual(result, -12)

    def test_add_numbers_mixed(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
