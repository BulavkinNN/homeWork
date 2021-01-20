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

@timer
def make_count(count, name_exc):
    count_copy = count
    while count_copy:
        try:
            raise name_exc
        except name_exc:
            pass
        count_copy -= 1



