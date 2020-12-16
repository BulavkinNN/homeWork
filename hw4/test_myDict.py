import unittest
import myDict

c = myDict()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(c, False)


if __name__ == '__main__':
    unittest.main()
