import time


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        print(stop_timer - start_timer)
        return stop_timer - start_timer

    return inner