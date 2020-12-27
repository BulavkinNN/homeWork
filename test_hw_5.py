import unittest
import hw_5
import math


class MyTestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(list(hw_5.get_fib(5)), [0, 1, 1, 2, 3, 5])

    def test_valuefib(self):
        self.assertRaises(ValueError, list, hw_5.get_fib('s'))
        self.assertRaises(ValueError, list, hw_5.get_fib(0))

    def test_evenfib(self):
        self.assertEqual(list(hw_5.get_evenfib(5)), [0, 2])

    def test_valueevenfib(self):
        self.assertRaises(ValueError, list, hw_5.get_evenfib('s'))
        self.assertRaises(ValueError, list, hw_5.get_evenfib(0))

    def test_n_evenfib(self):
        self.assertEqual(list(hw_5.get_n_evenfib(5)), [0, 2, 8, 34, 144])

    def test_valuen_evenfib(self):
        self.assertRaises(ValueError, list, hw_5.get_n_evenfib('s'))
        self.assertRaises(ValueError, list, hw_5.get_n_evenfib(0))

    def test_3fib(self):
        self.assertEqual(list(hw_5.get_3fib(5)), [0, 0, 1, 1, 2])

    def test_value3fib(self):
        self.assertRaises(ValueError, list, hw_5.get_3fib('s'))
        self.assertRaises(ValueError, list, hw_5.get_3fib(0))

    def test_even3fib(self):
        self.assertEqual(list(hw_5.get_even3fib(5)), [0, 0, 2])

    def test_valueeven3fib(self):
        self.assertRaises(ValueError, list, hw_5.get_even3fib('s'))
        self.assertRaises(ValueError, list, hw_5.get_even3fib(0))

    def test_n_even3fib(self):
        self.assertEqual(list(hw_5.get_n_even3fib(5)), [0, 0, 2, 4, 24])

    def test_valuen_even3fib(self):
        with self.assertRaises(ValueError):
            list(hw_5.get_n_even3fib('s'))
        with self.assertRaises(ValueError):
            list(hw_5.get_n_even3fib(0))

    def test_pi(self):
        self.assertEqual(list(hw_5.gen_pi(9)), [3, '.', 1, 4, 1, 5, 9, 2, 6, 5, 3])  # list with n digit of pi
        self.assertEqual(float(hw_5.get_pi(15)), math.pi)  # 15 digit of pi == math.pi

    def test_valuen_pi(self):
        self.assertRaises(ValueError, hw_5.get_pi, 's')
        self.assertRaises(ValueError, hw_5.get_pi, 0)
        self.assertRaises(ValueError, hw_5.get_pi, -1)


if __name__ == '__main__':
    unittest.main()
