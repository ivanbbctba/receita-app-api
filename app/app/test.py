"""
Sample test file
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Sample test class
    """

    def test_add_numbers(self):
        """
        Sample test method
        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Sample test method
        """
        res = calc.subtract(5, 6)
        self.assertEqual(res, -1)
