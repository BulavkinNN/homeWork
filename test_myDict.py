import unittest
import myDict

c = myDict()


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.myDict = myDict()

    def tearDown(self):
        self.myDict.__del__()

    def test_something(self):
        self.assertEqual(c, False)


if __name__ == '__main__':
    unittest.main()
