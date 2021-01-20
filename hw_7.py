from ste import ste


response = ste.STE.list(list_exc=[BaseException])
print(response)


response = ste.STE.test()
print(response)
