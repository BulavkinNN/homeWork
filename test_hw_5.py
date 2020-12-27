import unittest
import hw_5
import math

class MyTestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(list(hw_5.get_fib(5)), [0, 1, 1, 2, 3, 5])

    def test_evenfib(self):
        self.assertEqual(list(hw_5.get_evenfib(5)), [0, 2])

    def test_3fib(self):
        self.assertEqual(list(hw_5.get_3fib(5)), [0, 0, 1, 1, 2])

    def test_even3fib(self):
        self.assertEqual(list(hw_5.get_even3fib(5)), [0, 0, 2])

    def test_pi(self):
        self.assertEqual(list(hw_5.gen_pi(9)), [3, '.', 1, 4, 1, 5, 9, 2, 6, 5, 3])
        self.assertEqual(float(hw_5.get_pi(15)), math.pi)


if __name__ == '__main__':
    unittest.main()
