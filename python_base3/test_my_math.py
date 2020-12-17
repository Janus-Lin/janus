"""
janus.test_my_math
~~~~~~~~~~~~~~~~~~

功能: 测试用例

版权所有 © 2020
"""
import unittest
from python_base3.data import my_math


class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')

    def test_floats(self):

        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')


if __name__ == '__main__':
    unittest.main()
