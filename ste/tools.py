import time

def format_output(func):
    def inner(*arg, **kwargs):
        result = func(*arg, **kwargs)
        return f"Exception {arg[1]} was raises {arg[0]} at {result} ns ({result/1e9}s) 1={result/arg[0]} ns"

    return inner

def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        return stop_timer - start_timer  # ns

    return inner


def get_list(list_exc, output):
    return list_exc, output




@format_output
@timer
def make_count(count, name_exc):
    count_copy = count
    while count_copy:
        try:
            raise name_exc
        except name_exc:
            pass
        count_copy -= 1

