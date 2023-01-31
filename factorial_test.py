"""
- developers need to write unit tests
- solid test suite makes developer confident to make big changes in the project
- `python factorial_test.py`

"""


import unittest

from factorial import fact, div


class TestFactorial(unittest.TestCase):

    def normal(self):
        pass

    def test_fact_5(self):
        """test case for `fact()` function"""

        result = fact(5)
        self.assertEqual(result, 120)

    def test_div_by_natural(self):
        """test case for `div()` function"""

        result = div(10)
        self.assertEqual(result, 1.0)

    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == "__main__":
    unittest.main()
