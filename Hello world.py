import sys
import traceback


def make_except():
    raise ValueError


def say_hello():
    """First Home Work"""
    try:
        make_except()
    except ValueError:
        print(sys.gettrace())
        #print(len(sys.exc_info()))
        #say_hello()



try:
    say_hello()
finally:
    print(traceback.extract_stack())