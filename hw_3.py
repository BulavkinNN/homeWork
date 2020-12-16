def getmax_int():
    """
    Get max int
    :return: int
    """
    pass


def getmin_int():
    """
    Get  min int
    :return:result
    """
    pass


def max_float(a):
    """
    Get result max float +1
    :return:result
    """
    if type(a) in (int, float) and a > 0:
        import sys
        max_f = sys.float_info.max
        return max_f + a
    raise TypeError('Need  int, float >0')


def min_float(a):
    """
    Get result min float -1
    :return:result
    """
    if type(a) in (int, float) and a < 0:
        import sys
        min_f = sys.float_info.min
        return min_f + a
    raise TypeError('Need  int, float < 0')


def max_str(count=90000000):
    """
    Make max string
    :return:int with len of string
    """
    try:
        while (1):
            my_str = "1" * count
            #print(my_str)
            del my_str
            count += 1
    except (OverflowError, MemoryError):
        return count


def append_max_list():
    """
    Append list with 1 item in other lists
    :return: int How many list in list
    """
    import random
    import sys
    my_list = []
    try:
        while (1):
            # print(coint)
            my_list.append(random.uniform(sys.float_info.min, sys.float_info.max))
    except (OverflowError, MemoryError):
        return len(my_list)


def max_list():
    """
    Get max items in list
    :return: int How many items in list
    """
    coint = 0
    my_list = [1]
    try:
        while (1):
            #print(coint)
            my_list = [my_list[:]]
            coint += 1
    except (OverflowError, MemoryError):
        return coint


def explore_int_division(a, b):
    """
    Input: 2 int
    Errors: TypeError, Zero_division
    :return: int
    """
    if type(a) == type(b) == int:
        return a // b
    raise TypeError('Need only int')


def exp_int(a, b):
    """
    exponentiation a in b
    Input: 2 int
    Errors: TypeError
    :return: int
    """
    if type(a) == type(b) == int and a != 0:
        return a ** b
    raise TypeError('Need only int and a not 0')


def remainder_div_int(a, b):
    """
    remainder of division a in b
    Input: 2 int not 0
    Errors: TypeError
    :return: int
    """
    if type(a) == type(b) == int and 0 not in (a, b):
        return a % b
    raise TypeError('Need only int and a or b not 0')


def sum_range_int(a, b):
    """
    sum positive int in range from a to b
    Input: 2 int not 0
    Errors: TypeError
    :return: int
    """
    if type(a) == type(b) == int and a < b:
        return sum([item for item in range(a, b) if item > 0])
    raise TypeError('Need only int and a not > b')


def sum_abs_int(*args):
    """
    abs sum with only int
    Input: int can other type
    :return: int
    """
    # Как сгенерировать ошибку при других типах, в вписанном списке?
    return sum([abs(a) for a in args if type(a) == int])


def explore_float():
    """
    5 action with dict
    :return:
    """
    pass


def explore_complex():
    """
    5 action with dict
    :return:
    """
    pass


def con_str(a, b):
    """
    Concatenation str a+b
    :return:str
    """
    if type(a) == type(b) == str:
        return a + b
    raise TypeError('Need only str')


def ispalindrome_str(a):
    """
    Check is a palindrome
    :return:bool True or False
    """
    if type(a) == str:
        return a == a[::-1]
    raise TypeError('Need only str')


def howmany_char(string, char):
    """
    How many times a character appears in a string
    :return:int
    """
    if type(string) == type(char) == str:
        return string.count(char)
    raise TypeError('Need only 2 str')


def sumdigits_number(number):
    """
    sum of digits in a number. Make with methods str.
    :return:bool True or False
    """
    if type(number) == int:
        return sum([int(item) for item in str(number)])
    raise TypeError('Need only int')


def upin_str(a, step):
    """
    Up char in str with in step
    :return:str
    """
    if type(a) != str or type(step) != int or step < 1:
        raise TypeError('Need only str')
    counter = 0
    new_str = ""
    for item in a:
        if counter % step == 0:
            new_str += item.upper()
        else:
            new_str += item
        counter += 1
    return new_str


def value_bool(value):
    """
    Input
    :return: bool
    """
    return bool(value)

def and_bool(value1, value2):
    """
    Logical + (and)
    :return: bool
    """
    return bool(value1) and bool(value2)

def or_bool(value1, value2):
    """
    Logical or
    :return: bool
    """
    return bool(value1) or bool(value2)

def not_bool(value1):
    """
    Logical or
    :return: bool
    """
    return not bool(value1)

def notand_bool(value1, value2):
    """
    Invert or
    :return: bool
    """
    return not (bool(value1) and bool(value2))

def make_list(*args):
    """
    5 action with list
    :return: list
    """
    return list(args)


def makerange_list(int_start, int_end):
    """
    Make list from range
    :return: list
    """
    if type(int_start) == type(int_end) == int and int_start < int_end:
        return list(range(int_start, int_end))
    raise TypeError('Need  2 int(a,b), and  a < b')


def compare_list(list_a, list_b):
    """
    Make  list with item in list_a, but not in   list_b
    :return: list
    """
    if type(list_a) != list or type(list_b) != list:
        raise TypeError('Need only 2 list')
    return [item for item in list_a if item not in list_b]


def extend_list(list_a, list_b):
    """
    Make  list with item in list_a, but not in   list_b
    :return: list
    """
    if type(list_a)!= list or type(list_b) != list:
        raise TypeError('Need only 2 list')
    list_a.extend(list_b)
    return list_a


def palindrome_list(list_a):
    """
    Check is list palindrome
    :return: bool
    """
    if type(list_a) != list:
        raise TypeError('Need only  list')
    list_b = list_a.copy()
    list_a.reverse()
    return list_a == list_b


def make_dict(my_list):
    """
    from list make dict
    :return: dict
    """
    if type(my_list) != list:
        raise TypeError('Need list')
    return dict.fromkeys(my_list)



def update_dict(dict_a, dict_b):
    """
    Make dict_a + dict_b
    :return:dict
    """
    if type(dict_a) != dict or type(dict_b) != dict:
        raise TypeError('Need only 2 dict')
    dict_a.update(dict_b)
    return dict_a


def maxvalue_dict(dict_a):
    """
    Find max value
    :return:dict
    """
    if type(dict_a) != dict:
        raise TypeError('Need only dict')
    result = {}
    max_values = max(dict_a.values())
    for key, value in dict_a.items():
        if value == max_values:
            result[key] = value
    return result


def make_set(*args):
    """
    5 action with dict
    :return:
    """
    return set(args)


def inter_set(set_a, set_b):
    """
    Intersection 2 set

    :return: set
    """
    if type(set_a)!= set or type(set_b) != set:
        raise TypeError('Need only 2 set')
    return set_a & set_b


def notinter_set(set_a, set_b):
    """
    Intersection 2 set

    :return: set
    """
    if type(set_a)!= set or type(set_b) != set:
        raise TypeError('Need only 2 set')
    inter_set = set_a & set_b
    set_a.update(set_b)
    return set([item for item in set_a if item not in inter_set])


def unique_set(*args):
    """
    check if all numbers in sequence are unique

    :return: bool
    """
    if type(args) != tuple:
        raise TypeError('Need only tuple')
    return len(args) == len(set(args))


def uniquein_set(set_a, set_b):
    """
    return  set, elements included in A or B, but not both of them

    :return: set
    """
    if type(set_a)!= set or type(set_b) != set:
        raise TypeError('Need only 2 set')
    return set_a ^ set_b
