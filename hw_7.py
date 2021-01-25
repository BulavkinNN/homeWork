from ste import ste


def print_list(inp_list: iter):
    for item in inp_list:
        print(item)


print("\n*************************  raice  ****************")
list_exc_to_test = [ZeroDivisionError, AttributeError, NameError, LookupError]
response = ste.STE.test(list_exc_to_test, manual_raise=True, count=1000000, output="list")
print_list(response)

print("\n*************************  make exception in functions ***********")
response = ste.STE.test(list_exc_to_test, manual_raise=False, count=1000000, output="list")
print_list(response)

print("\n*************************  try import with SyntaxError ***********")


def se():
    try:
        import ste.syntax_error
    except SyntaxError:
        print("\n ... catch SyntaxError, when import  'syntax_error.py'")


se()

print("\n********************************** traceback ****************")
import sys
import traceback


def recur_err(n):
    global count_recursion
    if n == 1:
        return "error"
    count_recursion += 1
    #print("Recur №", count_recursion)
    # Code for long stack trace shot: return n + recur_err(n - 1)
    if n % 2 == 0:
        return n + recur_err(n - 1)
    return n + recur_err(n - 1 + 1 - 1)


count_recursion = 0
# Set max recursion (1000 default)
sys.setrecursionlimit(50000)



try:
    print(recur_err(20000))
except Exception as e:
    with open("analise_tb.log", "w") as file:
        traceback.print_exc(file=file)
    with open("analise_tb.log", "r") as file:
        contents = file.readlines()
        print(f"Traceback = {len(contents)} lines!")
    print("Exception =", e)
    print("limit recurs =", sys.getrecursionlimit())
    print("Last level of recurs =", count_recursion)

finally:
    traceback_obj = sys.exc_info()[2] # if don`t catch
    traceback.print_tb(traceback_obj)
