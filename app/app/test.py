from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    """add to number"""
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_number(self):
        self.assertEqual(subtract(10, 5), 5)
