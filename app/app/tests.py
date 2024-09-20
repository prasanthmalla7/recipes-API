from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    def test_add(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub(self):
        res = calc.sub(10, 7)

        self.assertEqual(res, 3)
