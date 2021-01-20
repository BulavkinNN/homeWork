import time


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        return stop_timer - start_timer

    return inner


def get_list(list_exc, output):
    return list_exc, output


def coint(count):
    count_copy = count
    while (count_copy):
        pass
        count_copy -= 1;


coint
