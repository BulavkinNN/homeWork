import unittest
import hw_3


class MyTestCase(unittest.TestCase):

    def test_getmax_int(self):

        self.assertEqual(hw_3.getmax_int(), None)

    def test_getmin_int(self):

        self.assertEqual(hw_3.getmin_int(), None)

    def test_max_float(self):
        self.assertEqual(hw_3.max_float(0.1), 1.7976931348623157e+308)

    def test_min_float(self):
        self.assertEqual(hw_3.min_float(-0.01), -0.01)

    def test_max_str(self):

        self.assertEqual(hw_3.max_str(), None)

    def test_append_max_list(self):

        self.assertEqual(hw_3.append_max_list(), None)

    def test_max_list(self):

        self.assertEqual(hw_3.max_list(), None)

    def test_int1(self):
        self.assertEqual(hw_3.explore_int_division(10, 3), 3)

    def test_intvalue1(self):
        self.assertRaises(TypeError, hw_3.explore_int_division, "12", 1)

    def test_int2(self):
        self.assertEqual(hw_3.exp_int(8, 2), 64)

    def test_intvalue2(self):
        self.assertRaises(TypeError, hw_3.exp_int, "12", 1)

    def test_int3self(self):
        self.assertEqual(hw_3.remainder_div_int(10, 3), 1)

    def test_intvalue3(self):
        self.assertRaises(TypeError, hw_3.remainder_div_int, "12", 1)

    def test_int4(self):
        self.assertEqual(hw_3.sum_range_int(1, 6), 15)

    def test_intvalue4(self):
        self.assertRaises(TypeError, hw_3.sum_range_int, 1, -1)

    def test_int5(self):
        self.assertEqual(hw_3.sum_abs_int(1, 2, 3, 4, 5), 15)

    def test_explore_float1(self):
        self.assertEqual(hw_3.add_float(0.01, 0.02), 0.03)

    def test_explore_float2(self):
        self.assertEqual(hw_3.sub_float(0.01, 0.02), -0.01)

    def test_explore_float3(self):
        self.assertEqual(hw_3.mul_float(0.01, 0.02), 0.0002)

    def test_explore_float4(self):
        self.assertEqual(hw_3.div_float(0.02, 0.01), 2)

    def test_explore_complex1(self):
        self.assertEqual(hw_3.add_complex((1+1j), (2+2j)), (3+3j))

    def test_explore_complex2(self):
        self.assertEqual(hw_3.sub_complex((1+1j), (2+2j)), (-1-1j))

    def test_explore_complex3(self):
        self.assertEqual(hw_3.mul_complex((1+1j), (2+2j)), 4j)

    def test_explore_complex4(self):
        self.assertEqual(hw_3.div_complex((2+2j), (1+1j)), 2)

    def test_str1(self):
        self.assertEqual(hw_3.con_str("Hello ", "world!"), "Hello world!")

    def test_strvalue1(self):
        self.assertRaises(TypeError, hw_3.con_str, {1, 2, 3}, 1)

    def test_str2(self):
        self.assertEqual(hw_3.ispalindrome_str("abcdcba"), True)

    def test_strvalue2(self):
        self.assertRaises(TypeError, hw_3.ispalindrome_str, {1, 2, 3})

    def test_str3(self):
        self.assertEqual(hw_3.howmany_char("Hello", "l"), 2)

    def test_strvalue3(self):
        self.assertRaises(TypeError, hw_3.howmany_char, 123, "2")

    def test_str4(self):
        self.assertEqual(hw_3.sumdigits_number(12), 3)

    def test_strvalue4(self):
        self.assertRaises(TypeError, hw_3.sumdigits_number, '12')

    def test_str5(self):
        self.assertEqual(hw_3.upin_str("abcdefg", 2), "AbCdEfG")

    def test_strvalue5(self):
        self.assertRaises(TypeError, hw_3.upin_str, "1234", "2")

    def test_bool1(self):
        self.assertEqual(hw_3.value_bool(1), True)

    def test_bool2(self):
        self.assertEqual(hw_3.and_bool(1, 0), False)

    def test_bool3(self):
        self.assertEqual(hw_3.or_bool(1, 0), True)

    def test_bool4(self):
        self.assertEqual(hw_3.not_bool(False), True)

    def test_bool5(self):
        self.assertEqual(hw_3.notand_bool(0, 0), True)
        self.assertEqual(hw_3.notand_bool(0, 1), True)
        self.assertEqual(hw_3.notand_bool(1, 1), False)
        self.assertEqual(hw_3.notand_bool(1, 0), True)
        self.assertEqual(hw_3.notand_bool(True, 0), True)

    def test_list1(self):
        self.assertEqual(hw_3.make_list(1, 2, 3, 4, 5), [1, 2, 3, 4, 5])

    def test_list2(self):
        self.assertEqual(hw_3.makerange_list(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_listvalue2(self):
        self.assertRaises(TypeError, hw_3.makerange_list, (1, -1))

    def test_list3(self):
        self.assertEqual(hw_3.compare_list([1, 2, 3, 4, 5], [3, 4, 5]), [1, 2])

    def test_listvalue3(self):
        self.assertRaises(TypeError, hw_3.compare_list, (1, 2, 3), (4, 5, 6))

    def test_list4(self):
        self.assertEqual(hw_3.extend_list([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_listvalue4(self):
        self.assertRaises(TypeError, hw_3.extend_list, (1, 2, 3), (4, 5))

    def test_list5(self):
        self.assertEqual(hw_3.palindrome_list([1, 2, 3, 2, 1]), True)

    def test_listvalue5(self):
        self.assertRaises(TypeError, hw_3.palindrome_list, (1, 2, 3))

    def test_dict1(self):
        self.assertEqual(hw_3.make_dict([1, 2, 3, 4, 5]), {1: None, 2: None, 3: None, 4: None, 5: None})

    def test_dictvalue1(self):
        self.assertRaises(TypeError, hw_3.make_dict, (1, 2, 3))

    def test_dict2(self):
        self.assertEqual(hw_3.update_dict({'a': 1, 'b': 2}, {'c': 3, "d": 4}), {'a': 1, 'b': 2, 'c': 3, "d": 4})

    def test_dictvalue2(self):
        self.assertRaises(TypeError, hw_3.maxvalue_dict, [1, 2, 3], [3, 5])

    def test_dict3(self):
        self.assertEqual(hw_3.maxvalue_dict({'a': 1, 'b': 2, 'c': 3, "d": 4, 'e': 5}), {"e": 5})

    def test_dictvalue3(self):
        self.assertRaises(TypeError, hw_3.maxvalue_dict, [1, 2, 3])

    def test_set1(self):
        self.assertEqual(hw_3.make_set(1, 2, 3, 4, 5), {1, 2, 3, 4, 5})

    def test_setvalue1(self):
        self.assertRaises(TypeError, hw_3.make_set, [1, 2, 3])

    def test_set2(self):
        self.assertEqual(hw_3.inter_set({1, 2, 3}, {2, 3, 4, 5}), {2, 3})

    def test_setvalue2(self):
        self.assertRaises(TypeError, hw_3.inter_set, [1, 2, 3], [2, 3, 4])

    def test_set3(self):
        self.assertEqual(hw_3.notinter_set({1, 2, 3}, {2, 3, 4, 5}), {1, 4, 5})

    def test_setvalue3(self):
        self.assertRaises(TypeError, hw_3.notinter_set, [1, 2, 3], [2, 3, 4])

    def test_set4(self):
        self.assertEqual(hw_3.unique_set(1, 2, 3), True)

    def test_setvalue4(self):
        self.assertRaises(TypeError, hw_3.unique_set, [1, 2, 3])

    def test_set5(self):
        self.assertEqual(hw_3.uniquein_set({1, 2, 3}, {2, 3, 4, 5}), {1, 4, 5})

    def test_setvalue5(self):
        self.assertRaises(TypeError, hw_3.uniquein_set, [1, 2, 3], [2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
