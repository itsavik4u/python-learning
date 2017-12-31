import unittest
from calc import Calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        c = Calc()
        # cover the edge cases
        self.assertEqual(c.add(36, 4), 40)
        self.assertEqual(c.add(-1, 1), 0)
        self.assertEqual(c.add(-2, -4), -6)
        self.assertEqual(c.add(-36, 4), -32)

    def test_div(self):
        c = Calc()
        # cover the edge cases
        self.assertEqual(c.div(36, 4), 9)
        self.assertEqual(c.div(-1, 1), -1)
        self.assertEqual(c.div(-1, -1), 1)
        self.assertEqual(c.div(5, 2), 2)

        # checking / raising the exception
        # self.assertRaises(ValueError, c.div, 10, 0)
        # alternate: using context manager
        with self.assertRaises(ValueError):
            # call the function normally
            c.div(10, 0)


if __name__ == '__main__':
    unittest.main()
