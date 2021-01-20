from ste import ste


response = ste.STE.list(list_exc=[BaseException])
print(response)


response = ste.STE.test(count=1000)
print(response)

def se():
    try:
        print("Hello")
        print("world!")
    except SyntaxError:
        pass

se()

