import time
import logging.config
logging.config.fileConfig(fname='hw_8_source/file.conf',disable_existing_loggers=False)#



# import exifread
# logging.basicConfig(level=logging.INFO, filename="root.log", filemode="r")
#logging.basicConfig(level=logging.INFO)


def timer(func):
    def inner(*arg, **kwargs):
        start_timer = time.perf_counter_ns()
        func(*arg, **kwargs)
        stop_timer = time.perf_counter_ns()
        # logging.debug(f'function {func.__name__}  work {stop_timer - start_timer} ns')

        return stop_timer - start_timer  # ns

    return inner

logging.FileHandler
@timer
def read_from_file(file):
    file.read()


def test_buffering(file_name="e:\Mult.avi"):
    buffer_list = [0, 2]
    result_table = dict()

    logger.info('Start reading big file')
    while True:
        buffer = buffer_list.pop(0)

        try:
            with open(file_name, mode='rb', buffering=buffer) as file:
                check_time = read_from_file(file)  #
        except (OverflowError, MemoryError) as e:
            logger.error(f'Error when read file {e}', exc_info=False)
            break
        result_table[buffer] = check_time
        logger.debug(f"buf= {buffer}, check_time= {check_time:,}")
        buffer_list.append(buffer_list[-1] * 2)  # Make list [0,2,4,8,16,32 and ....
    return result_table


def print_result(result_table):
    # print result
    logger.info('Print optimal/non-optimal result')
    for k, v in result_table.items():
        if v == min(result_table.values()):
            print(f"Optimal buffering = {k:,}, time = {v:,} ns")
        if v == max(result_table.values()):
            print(f"Non-optimal buffering = {k:,}, time = {v:,} ns")
    return result_table


def draw_result(result_table):
    # draw result
    logger.info('Draw result')
    v_max = max(result_table.values())
    scale = (v_max / 50)
    sort_key = sorted(result_table.keys())
    print(f"{('-' * 75)}")
    print(f"\nBuffering                 *= {scale: .3} ns{(' ' * 25):<25} Time, ns\n")
    print(f"{('-' * 75)}")
    for key in sort_key:
        print(f"{key:<13,} {('*' * int(result_table[key] / scale)):<50} {result_table[key]:,}")
    print(f"{('-' * 75)}")


# /////////////////////////////////////////
def _find_jpeg_exif(file):
    file.seek(2)
    marker = file.read(2)

    if marker == b'\xff\xe0':
        logger.debug("Default header")
        length_data = int.from_bytes(file.read(2), 'big')

        if length_data == 16:
            logger.info("Length after Default header == 16")
        logger.debug(f"Identifier={file.read(4).decode()}{int.from_bytes(file.read(1), 'big')}")
        logger.debug(f"version= {int.from_bytes(file.read(1), 'big')}.{int.from_bytes(file.read(1), 'big')}")
        logger.debug(f"units= {int.from_bytes(file.read(1), 'big')}")
        logger.debug(f"density= {int.from_bytes(file.read(2), 'big')}x{int.from_bytes(file.read(2), 'big')}")
        logger.debug(f"trumbnail= {int.from_bytes(file.read(1), 'big')}x{int.from_bytes(file.read(1), 'big')}")


def read_exif(file_name="hw_8_source/1.jpg"):
    logger.info("Read EXIF data from jpq file")
    # file_name = "hw_8_source/fisherman.jpg"
    # file_name = "hw_8_source/1.jpg"
    #marker in jpg not use!!!
    marker_mapping = {
        b'\xFF\xd8': "Start of Image",
        b'\xff\xe0': "Application Default Header",
        b'\xff\xdb': "Quantization Table",
        b'\xff\xc0': "Start of Frame",
        b'\xff\xc4': "Define Huffman Table",
        b'\xff\xda': "Start of Scan",
        b'\xff\xd9': "End of Image"
    }

    with open(file_name, "rb") as file:
        data = file.read(2)
        logger.debug(f"data (first 2 bytes) {data}" )
        if data[0:2] == b'\xFF\xD8':
            logger.info("It`s jpeg file")
            try:
                _find_jpeg_exif(file)
            except Exception as e:
                logger.error(f'Error reading exif from jpeg {e}', exc_info=True)


# /////////////////////////////////////////
def test_logging():
    logger.warning("Try  logging.exception() not in try: except")
    logger.exception("Try  logging.exception() not in try: except")

logger = logging.getLogger("sampleLogger")
# /////////////////////////////////////////
draw_result(print_result(test_buffering("e:\Mult.avi")))
read_exif(file_name="hw_8_source/1.jpg")
test_logging()
