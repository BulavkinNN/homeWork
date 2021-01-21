from ste import ste, tools

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
