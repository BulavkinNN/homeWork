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
    except (OverflowError, MemoryError):
        break
    result_table[buffer] = check_time
    print(f"buf= {buffer}, check_time= {check_time:,}")
    check_time_prev = check_time
    buffer_list.append(buffer_list[-1] * 2)  # Make list [0,2,4,8,16,32 and ....

# print result
for k, v in result_table.items():
    if v == min(result_table.values()):
        print(f"Optimal buffering = {k:,}, time = {v:,}")
    if v == max(result_table.values()):
        print(f"Non-optimal buffering = {k:,}, time = {v:,}")

# draw result
v_max = max(result_table.values())
scale = (50/v_max)
sort_key = sorted(result_table.keys())
print(f"\nBuffering      {(' '*50):<50} Time, ns\n")
for key in sort_key:
    print(f"{key:<13,} {('*'*int(result_table[key]*scale)):<50} {result_table[key]:,}")


# /////////////////////////////////////////
print("Read EXIF data from jpq file")
file_name = "hw_8_source/fisherman.jpg"
file_name = "hw_8_source/1.jpg"
marker_mapping = {
    b'\xFF\xd8': "Start of Image",
    b'\xff\xe0': "Application Default Header",
    b'\xff\xdb': "Quantization Table",
    b'\xff\xc0': "Start of Frame",
    b'\xff\xc4': "Define Huffman Table",
    b'\xff\xda': "Start of Scan",
    b'\xff\xd9': "End of Image"
}

def ord_(dta):
    if isinstance(dta, str):
        return ord(dta)
    return dta


def _find_jpeg_exif(file):
    file.seek(2)
    marker = file.read(2)


    if marker == b'\xff\xe0':
        print("Default header")
        lenth_data = int.from_bytes(file.read(2),'big')

        if lenth_data==16:
            print("All norm!")
        print(f"Identifier={file.read(4).decode()}{int.from_bytes(file.read(1),'big')}")
        print(f"version= {int.from_bytes(file.read(1),'big')}.{int.from_bytes(file.read(1),'big')}")
        print(f"units= {int.from_bytes(file.read(1), 'big')}")
        print(f"density= {int.from_bytes(file.read(2),'big')}x{int.from_bytes(file.read(2),'big')}")
        print(f"trumbnail= {int.from_bytes(file.read(1), 'big')}x{int.from_bytes(file.read(1), 'big')}")

with open(file_name, "rb") as file:
    data = file.read(2)
    print (data)
    if data[0:2] == b'\xFF\xD8':
        # it's a JPEG file
        #try:
        _find_jpeg_exif(file)
        #except Exception as e:
            #print("Except", e)

