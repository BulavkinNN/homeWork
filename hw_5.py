from collections import deque

def get_fib(n):
    '''

    :param n:int
    :return: nuber Fibodachi
    '''
    fib_list = deque([1, -1], maxlen=2)
    for i in (range(0, n+1)):
        result = sum(fib_list)
        yield result
        fib_list.appendleft(result)


def get_evenfib(n):
    '''

    :param n:
    :return: Even nuber Fibodachi
    '''
    fib_list = deque([1, -1], maxlen=2)
    for i in (range(0, n+1)):
        result = sum(fib_list)
        if result % 2 != 0:
            continue
        yield result
        fib_list.appendleft(sum(fib_list))

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
        fib_list.appendleft(sum(fib_list))
        if result % 2 != 0:
            continue
        yield result


for i in get_even3fib(21):
    print (i)