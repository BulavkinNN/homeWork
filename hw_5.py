from collections import deque

def get_fib(n):
    '''

    :param n:int
    :return: nuber Fibodachi
    '''
    fib_list = deque([-1, 2], maxlen=2)
    for i in (range(0, n+1)):
        fib_list.appendleft(sum(fib_list))
        yield sum(fib_list)

def get_evenfib(n):
    '''

    :param n:
    :return: Even nuber Fibodachi
    '''
    fib_list = deque([-1, 2], maxlen=2)
    for i in (range(0, n+1)):
        fib_list.appendleft(sum(fib_list))
        result = sum(fib_list)
        if result % 2 != 0:
            continue
        yield result

for i in get_fib(77):
    print (i)