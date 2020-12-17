import unittest



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dict = dict([('15', 'fifteen'), ('16', 'sixteen'), ('1', 'one')])
        self.dict2 = dict([('15_new', 'fifteen_new'), ('16_new', 'sixteen_new'), ('1_new', 'one_new')])

    def tearDown(self):
        pass

    def test_clear(self):
        self.assertEqual(self.dict.clear(), None)
        self.assertEqual(len(self.dict), 0)

    def test_update(self):
        self.assertEqual(self.dict.update(self.dict2), None)
        self.assertEqual(len(self.dict), 6)

    def test_key(self):
        self.assertEqual(self.dict['15'], 'fifteen')
        self.assertEqual(self.dict.get("new", "Unknown user"), "Unknown user")
        self.assertEqual(self.dict.pop("15"), 'fifteen')

    def test_get(self):
        self.assertEqual(self.dict.get('16'), 'sixteen')

    def test_copy(self):
        self.assertCountEqual(self.dict, self.dict.copy()) # a(elements)  = b (elements)
        self.assertNotEqual(self.dict, self.dict.copy())  # a != b

    def test_type(self):
        self.assertIsInstance(self.dict, dict)  #isinstance(a, b)

    def test_in(self):
        self.assertIn('16', self.dict)  # a in b
        self.assertIn('1', self.dict)  # a in b
        self.assertIn('1', self.dict.keys())  # a in b
        self.assertIn(('1','one'), self.dict.items())  # a in b
        self.assertIn('one', self.dict.values())  # a in b


if __name__ == '__main__':
    unittest.main()
