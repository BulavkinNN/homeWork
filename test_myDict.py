import unittest
import myDict


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.myDict = myDict.MyDict([('15', 'fifteen'), ('16', 'sixteen'), ('1','one')])#(['15', 'fifteen'], ['16', 'sixteen'], ['1', 'one'])
        self.myDict2 = myDict.MyDict([('15_new', 'fifteen_new'), ('16_new', 'sixteen_new'), ('1_new', 'one_new')])
    def tearDown(self):
        self.myDict.__del__()

    def test_clear(self):
        self.assertEqual(self.myDict.clear(), None)
        self.assertEqual(len(self.myDict), 0)

    def test_update(self):
        self.assertEqual(self.myDict.update(self.myDict2), None)
        self.assertEqual(len(self.myDict), 6)

    def test_key(self):
        self.assertEqual(self.myDict['15'], 'fifteen')
        self.assertEqual(self.myDict.get("new", "Unknown user"), "Unknown user")
        self.assertEqual(self.myDict.pop("15"), 'fifteen')


    def test_get(self):
        self.assertEqual(self.myDict.get('16'), 'sixteen')

    def test_copy(self):
        self.assertCountEqual(self.myDict, self.myDict.copy()) # a(elements)  = b (elements)
        self.assertNotEqual(self.myDict, self.myDict.copy())  # a != b (elements)

    def test_type(self):
        self.assertIsInstance(self.myDict, myDict.MyDict)  #isinstance(a, b)

    def test_in(self):
        self.assertIn('16', self.myDict)  # a in b
        self.assertIn('1', self.myDict)  # a in b
        self.assertIn('1', self.myDict.keys()) # a in b
        self.assertIn(('1', 'one'), self.myDict.items())  # a in b
        self.assertIn('one', self.myDict.values())  # a in b

if __name__ == '__main__':
    unittest.main()
