import unittest
import test_myDict
import myDictMix

class MyTestCase(test_myDict.MyTestCase):


    def setUp(self):
        self.myDict = myDictMix.MyDictMix([('15', 'fifteen'), ('16', 'sixteen'), ('1','one')])
        self.myDict2 = myDictMix.MyDictMix([('15_new', 'fifteen_new'), ('16_new', 'sixteen_new'), ('1_new', 'one_new')])
        self.myDict3 = myDictMix.MyDictMix.fromkeys([1, 2, 3, 4, 5], "numbers")

if __name__ == '__main__':
    unittest.main()
