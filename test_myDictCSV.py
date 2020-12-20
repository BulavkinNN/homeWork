import unittest
import myDictCSV
import test_myDict


class MyTestCase(test_myDict.MyTestCase):

    def setUp(self):
        self.myDict = myDictCSV.MyDictCSV([('15', 'fifteen'), ('16', 'sixteen'), ('1','one')])
        self.myDict2 = myDictCSV.MyDictCSV([('15_new', 'fifteen_new'), ('16_new', 'sixteen_new'), ('1_new', 'one_new')])
        self.myDict3 = myDictCSV.MyDictCSV.fromkeys([1, 2, 3, 4, 5], "numbers")

if __name__ == '__main__':
    unittest.main()
