from decimal import Decimal
import decimal

from collections import deque


def get_fib(n):
    '''

    :param n:int
    :return: nuber Fibodachi
    '''
    fib_list = deque([1, -1], maxlen=2)
    for i in (range(0, n + 1)):
        result = sum(fib_list)
        yield result
        fib_list.appendleft(result)


def get_evenfib(n):
    '''

    :param n:
    :return: Even number Fibodachi
    '''
    fib_list = deque([1, -1], maxlen=2)
    for i in (range(0, n + 1)):
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            yield result



def get_3fib(n):
    '''

    :param n:int
    :return: nuber 3Fibodachi
    '''
    fib_list = deque([1, -1, 0], maxlen=3)
    for i in (range(0, n)):
        yield sum(fib_list)
        fib_list.appendleft(sum(fib_list))


def get_even3fib(n):
    '''

    :param n:
    :return: Even nuber 3Fibodachi
    '''
    fib_list = deque([1, -1, 0], maxlen=3)
    for i in (range(0, n)):
        result = sum(fib_list)
        fib_list.appendleft(result)
        if result % 2 == 0:
            yield result



def get_pi(n):
    with decimal.localcontext(decimal.Context(prec=n + 1)):  # digit number
        pi = 0
        for k in range(0, n):
            i1 = Decimal(4) / (8 * k + 1)
            i2 = Decimal(2) / (8 * k + 4)
            i3 = Decimal(1) / (8 * k + 5)
            i4 = Decimal(1) / (8 * k + 6)
            pi += pow(Decimal(16), -k) * (i1 - i2 - i3 - i4)
    return pi


def gen_pi(number):
    pi = str(get_pi(number))
    for i in pi:  # or pi[2:] skip error with int(.)
        yield int(i) if i.isdigit() else "."
