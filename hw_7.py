from ste import ste, tools

print("*************************")
print("raice")
response = ste.STE.test([ZeroDivisionError, AttributeError, NameError, LookupError], manual_raise=True, count=1000000,
                        output="list")
for item in response:
    print(item)

print("*************************")
print("make exception in functions")
response = ste.STE.test(["ZeroDivisionError", "AttributeError", "NameError", "LookupError"], manual_raise=False,
                        count=1000000, output="list")
for item in response:
    print(item)


def se():
    try:
        print("Hello")
        print("world!")
    except SyntaxError:
        pass


# se()
#////////////////////////////////////////////////// traceback

import sys
import traceback


def recur_err(n):
    global count_recursion
    if n == 1:
        return "error"
    count_recursion += 1
    print("Recur №", count_recursion)
    return n + recur_err(n - 1)


count_recursion = 0
# Set max recursion (1000 default)
sys.setrecursionlimit(50002)

#print(sys.tracebacklimit(2000))

try:
    print(recur_err(40000))
except Exception as e:
    traceback.print_exc()
    
    print("Exception ==",e)
    print("limit recurs= ", sys.getrecursionlimit())
    print("Last recur №", count_recursion)

finally:
    traceback_obj = sys.exc_info()[2]
    traceback.print_tb(traceback_obj)
