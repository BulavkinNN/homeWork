import time
import makeExc


def format_output(func):
    def inner(*arg, **kwargs):
        result = func(*arg, **kwargs)
        return f"Exception {arg[1]} was raises {arg[0]} at {result} ns ({result / 1e9}s) 1={result / arg[0]} ns"

    return inner


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        return stop_timer - start_timer  # ns

    return inner


@format_output
@timer
def make_count(count, name_exc, manual_raise):
    count_copy = count
    if manual_raise:
        while count_copy:
            try:
                raise name_exc  # type('ZeroDivisionError', (), {}) make object
            except name_exc:
                count_copy -= 1
    else:
        func = select_method(name_exc)
        if not func:
            return None
        while count_copy:
            try:
                func()
            except Exception:  # need Exception in input!
                count_copy -= 1


def select_method(name_exc):
    """ Check method in class make_exc"""
    new_method = "make_" + name_exc
    if new_method in dir(makeExc.MakeExc):
        return getattr(makeExc.MakeExc, new_method, )
    raise TypeError("Internal error, can`t find method in class make_exc")



