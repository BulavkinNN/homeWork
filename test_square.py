import unittest
import square


class MyTestCase(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square.get_square(4), 16)
        self.assertEqual(square.get_square(-4), 16)
        self.assertEqual(square.get_square(1), 1)
        self.assertEqual(square.get_square(25.5), 650.25)
        self.assertEqual(square.get_square(3+4j), (-7+24j))

    def test_value(self):
        self.assertRaises(ValueError, square.get_square, 0)
        self.assertRaises(ValueError, square.get_square, (0+3j))
        self.assertRaises(ValueError, square.get_square, (3 + 0j))

    def test_types(self):
        self.assertRaises(TypeError, square.get_square, "1234")
        self.assertRaises(TypeError, square.get_square, True)
        self.assertRaises(TypeError, square.get_square, [1])


if __name__ == '__main__':
    unittest.main()
