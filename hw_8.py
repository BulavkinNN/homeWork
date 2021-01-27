import time
import logging

# import exifread
logging.basicConfig(level=logging.INFO)


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        #logging.debug(f'function {func.__name__}  work {stop_timer - start_timer} ns')

        return stop_timer - start_timer  # ns

    return inner


@timer
def read_from_file(file):
    file.read()


buffer_list = [0, 2]
result_table = dict()

logging.info('Start reading big file')
while True:
    buffer = buffer_list.pop(0)

    try:
        with open("e:\Mult.avi", mode='rb', buffering=buffer) as file:
            check_time = read_from_file(file)  #
    except (OverflowError, MemoryError) as e:
        logging.error(f'Error when read file {e}')
        break
    result_table[buffer] = check_time
    logging.debug(f"buf= {buffer}, check_time= {check_time:,}")
    buffer_list.append(buffer_list[-1] * 2)  # Make list [0,2,4,8,16,32 and ....

# print result
logging.info('Print optimal/non-optimal result')
for k, v in result_table.items():
    if v == min(result_table.values()):
        print(f"Optimal buffering = {k:,}, time = {v:,} ns")
    if v == max(result_table.values()):
        print(f"Non-optimal buffering = {k:,}, time = {v:,} ns")

# draw result
logging.info('Draw result')
v_max = max(result_table.values())
scale = (50 / v_max)
sort_key = sorted(result_table.keys())
print(f"\nBuffering      *={int(scale)} ns{(' ' * 40):<50} Time, ns\n")
for key in sort_key:
    print(f"{key:<13,} {('*' * int(result_table[key] * scale)):<50} {result_table[key]:,}")

# /////////////////////////////////////////
logging.info("Read EXIF data from jpq file")
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
        logging.debug("Default header")
        length_data = int.from_bytes(file.read(2), 'big')

        if length_data == 16:
            logging.info("Length after Default header == 16")
        logging.debug(f"Identifier={file.read(4).decode()}{int.from_bytes(file.read(1), 'big')}")
        logging.debug(f"version= {int.from_bytes(file.read(1), 'big')}.{int.from_bytes(file.read(1), 'big')}")
        logging.debug(f"units= {int.from_bytes(file.read(1), 'big')}")
        logging.debug(f"density= {int.from_bytes(file.read(2), 'big')}x{int.from_bytes(file.read(2), 'big')}")
        logging.debug(f"trumbnail= {int.from_bytes(file.read(1), 'big')}x{int.from_bytes(file.read(1), 'big')}")


with open(file_name, "rb") as file:
    data = file.read(2)
    logging.debug("data (first 2 bytes)", data)
    if data[0:2] == b'\xFF\xD8':
        logging.info("It`s jpeg file")
        try:
            _find_jpeg_exif(file)
        except Exception as e:
            logging.error(f'Error reading exif from jpeg {e}')
