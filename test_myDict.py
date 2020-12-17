import unittest
import myDict


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.myDict = myDict.MyDict(['15', 'fifteen'], ['16', 'sixteen'], ['1', 'one'])

    def tearDown(self):
        self.myDict.__del__()

    def test_key(self):
        self.assertEqual(self.myDict['15'], 'fifteen')

    def test_get(self):
        self.assertEqual(self.myDict.get('16'), 'sixteen')

    def test_copy(self):
        self.assertCountEqual(self.myDict, self.myDict.copy()) # a(elements)  = b (elements)
        self.assertNotEqual(self.myDict, self.myDict.copy())  # a != b (elements)

    def test_type(self):
        self.assertIsInstance(self.myDict, myDict.MyDict)  #isinstance(a, b)

    def test_type(self):
        self.assertIn('16', self.myDict)  # a is b
        self.assertIn('1', self.myDict)  # a is b

if __name__ == '__main__':
    unittest.main()
