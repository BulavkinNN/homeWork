from decimal import Decimal
import decimal

from collections import deque


def get_fib(n: int) -> int:
    '''
    Calculates n numbers Fibonacci
    :param n:int >0
    :return: int number Fibonacci by generator
    '''
    if type(n) !=int or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1], maxlen=2)  # All time only 2 items
    for i in (range(0, n + 1)):  # i count
        result = sum(fib_list)
        yield result
        fib_list.appendleft(result)


def get_evenfib(n: int) -> int:
    '''
    Calculates n numbers Fibonacci, and return only even
    :param n: int > 0
    :return: Even number Fibonacci by generator
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1], maxlen=2)  # All time only 2 items
    for i in (range(0, n + 1)):
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            yield result


def get_n_evenfib(n: int) -> int:
    '''
    Calculates n even numbers Fibonacci
    :param n: int > 0 How many need numbers
    :return: Even number Fibonacci by generator
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1], maxlen=2)
    while n > 0:  # n count every cycle -1
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            n -= 1
            yield result


def get_3fib(n: int) -> int:
    '''
    Calculates n numbers 3bonacci
    :param n:int > 0
    :return: number 3bonacci by generator
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1, 0], maxlen=3)  # All time only 3 items
    for i in (range(0, n)):
        yield sum(fib_list)
        fib_list.appendleft(sum(fib_list))


def get_even3fib(n: int) -> int:
    '''
    Calculates n numbers 3bonacci return even numbers
    :param n: int > 0
    :return: Even number 3bonacciby generator
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1, 0], maxlen=3)  # All time only 3 items
    for i in (range(0, n)):
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            yield result


def get_n_even3fib(n: int) -> int:
    '''
    Calculates n even numbers 3bonacci
    :param n:  int > 0
    :return: N Even number 3bonacci by generator
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    fib_list = deque([1, -1, 0], maxlen=3)
    while n > 0:
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            n -= 1
            yield result


def get_pi(n: int) -> Decimal:
    '''
    Calculates n numbers pi
    :param n: int > 0
    :return: Decimal pi
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only int > 0")
    with decimal.localcontext(decimal.Context(prec=n + 1)):  # digit number
        pi = 0
        for k in range(0, n):
            i1 = Decimal(4) / (8 * k + 1)
            i2 = Decimal(2) / (8 * k + 4)
            i3 = Decimal(1) / (8 * k + 5)
            i4 = Decimal(1) / (8 * k + 6)
            pi += pow(Decimal(16), -k) * (i1 - i2 - i3 - i4)
    return pi


def gen_pi(number: int) -> int or str:
    '''
    Generator for n numbers pi
    :param number: int > 0
    :return: int, str (".") numbers pi
    '''
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only int > 0")
    pi = str(get_pi(number))
    for i in pi:  # or pi[2:] skip error with int(.)
        yield int(i) if i.isdigit() else "."
