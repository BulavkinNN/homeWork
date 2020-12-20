import unittest
import myDict


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.myDict = myDict.MyDict([('15', 'fifteen'), ('16', 'sixteen'), ('1','one')])
        self.myDict2 = myDict.MyDict([('15_new', 'fifteen_new'), ('16_new', 'sixteen_new'), ('1_new', 'one_new')])
        self.myDict3 = myDict.MyDict.fromkeys([1, 2, 3, 4, 5], "numbers")

    def tearDown(self):
        pass

    def test_clear(self):
        self.assertEqual(self.myDict.clear(), None)
        self.assertEqual(len(self.myDict), 0)

    def test_fromkeys(self):
        self.assertEqual(len(self.myDict3), 5)


    def test_update(self):
        self.assertEqual(self.myDict.update(self.myDict2), None)
        self.assertEqual(len(self.myDict), 6)

    def test_key(self):
        self.assertEqual(self.myDict['15'], 'fifteen')
        self.assertEqual(self.myDict.get("new", "Unknown user"), "Unknown user")

    def test_pop(self):
        self.assertEqual(self.myDict.pop("15"), 'fifteen')
        self.assertEqual(len(self.myDict), 2)
        self.assertIn(self.myDict.popitem(), ('one', 'sixteen')) #'one' or 'sixteen' , order is different


    def test_del(self):
        self.assertEqual(self.myDict.__delitem__('15'), None)
        self.assertEqual(len(self.myDict), 2)

    def test_str(self):
        self.assertEqual(self.myDict.pop("15"), 'fifteen')
        self.assertEqual(self.myDict.pop("16"), 'sixteen')
        self.assertEqual(self.myDict.__str__(), "['1 : one']") # stay only one element, because the order is different

    def test_get(self):
        self.assertEqual(self.myDict.get('16'), 'sixteen')

    def test_copy(self):
        self.assertCountEqual(self.myDict, self.myDict.copy()) # a(elements)  = b (elements)
        self.assertEqual(self.myDict, self.myDict.copy())  # a != b (elements)

    def test_type(self):
        self.assertIsInstance(self.myDict, myDict.MyDict)  #isinstance(a, b)

    def test_in(self):
        self.assertIn('16', self.myDict)  # a in b
        self.assertIn('1', self.myDict)  # a in b
        self.assertIn('1', self.myDict.keys()) # a in b
        self.assertIn(('1', 'one'), self.myDict.items())  # a in b
        self.assertIn('one', self.myDict.values())  # a in b

    def test_iter(self):
        self.assertIn(next(self.myDict), ['16','15','1'])  # a in b
        self.assertIn(next(self.myDict), ['16','15','1'])  # a in b
        self.assertIn(next(self.myDict), ['16','15','1'])  # a in b
        self.assertRaises(StopIteration, next(self.myDict), )  # a end


if __name__ == '__main__':
    unittest.main()
