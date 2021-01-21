import time
import make_exc


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


def get_list(list_exc, output):
    return list_exc, output


@format_output
@timer
def make_count(count, name_exc):
    count_copy = count
    func = select_method(class_to_str(name_exc))
    if not func:
        while count_copy:
            try:
                raise name_exc
            except name_exc:
                pass
            count_copy -= 1
    else:
        while count_copy:
            try:
                func()
            except name_exc:
                pass
            count_copy -= 1


def select_method(name_exc):
    new_method = "make_" + name_exc
    print(new_method)
    if new_method in dir(make_exc.MakeExc):
        return getattr(make_exc.MakeExc, new_method, )
    return None


def class_to_str(name_exc):
    str = str(name_exc).split(" << ")[0]
