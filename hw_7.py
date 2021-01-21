from ste import ste, tools


#response = ste.STE.list(list_exc=[Exception])
#print(response)


response = ste.STE.test([ZeroDivisionError], count=900000)
print(response)

def se():
    try:
        print("Hello")
        print("world!")
    except SyntaxError:
        pass

#se()

