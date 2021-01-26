import time
import exifread

def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        return stop_timer - start_timer  # ns

    return inner


@timer
def read_from_file(file):
    file.read()


progress = 1
check_time = 0
check_time_prev = 0
buffer_list = [0, 2]
result_table = dict()

while True:
    buffer = buffer_list.pop(0)

    try:
        with open("e:\Mult.avi", mode='rb', buffering=buffer) as file:
            check_time = read_from_file(file)  #
    except OverflowError:
        break
    result_table[buffer] = check_time
    print(f"buf= {buffer}, check_time= {check_time:,}")
    check_time_prev = check_time
    buffer_list.append(buffer_list[-1] * 2)  # Make list [0,2,4,8,16,32 and ....

# print result
for k,v in result_table.items():
    if v == min(result_table.values()):
        print(f"Optimal buffering = {k:,}, time = {v:,}")
    if v == max(result_table.values()):
        print(f"Non-optimal buffering = {k:,}, time = {v:,}")

# /////////////////////////////////////////
print("Read EXIF data from jpq file")
