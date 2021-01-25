import time


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        return stop_timer - start_timer  # ns

    return inner


@timer
def read_from_file(file,size):
    file.read(size)

progress =1
check_time =[0,1]
check_time_prev =1e10
buffer_list = [0, 2]

while check_time[-2] > check_time[-1]:
    buffer = buffer_list.pop(0)
    print('buf=', buffer)
    for i in range(0,5):
        with open("e:\Mult.mkv", mode='rb', buffering=buffer) as file:
            check_time += read_from_file(file, size =1000000)#
    check_time.append(check_time /  5)
    progress = check_time_prev - check_time
    check_time_prev = check_time
    print("prog=",progress)
    buffer_list.append(pow(buffer_list[-1],2)) #Make list [0,2,4,8,16,32 and ....