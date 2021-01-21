from ste import ste, tools


#response = ste.STE.list(list_exc=[Exception])
#print(response)

print ("raice")
response = ste.STE.test([ZeroDivisionError, AttributeError, NameError, LookupError], manual_raise=True, count=1000000)
for item in response:
    print(item)
print("make exception in functions")
response = ste.STE.test(["ZeroDivisionError", "AttributeError", "NameError", "LookupError","1"], manual_raise=False, count=1000000)
for item in response:
    print(item)

def se():
    try:
        print("Hello")
        print("world!")
    except SyntaxError:
        pass

#se()

