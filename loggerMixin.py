import sys
import time


class LoggerMixin:

    def log(self, comment, *args, **kwargs):
        """how to access the  parent's function scope"""
        caller = sys._getframe(1).f_code.co_name
        print(f"{time.asctime()}  Start function {caller}, {comment}-{args}-{kwargs}")
