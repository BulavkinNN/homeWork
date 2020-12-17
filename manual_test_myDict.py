import myDict

test_obg = myDict.MyDict(['1', 'one'], ["15", "fifteen"], ['16', 'sixteen'])
print(f">>id(test_obg)  {id(test_obg)}")
print(f">>type(test_obg)  {type(test_obg)}")
print(f'>>for key, value in test_obg.items()  {[(key,value) for key,value in test_obg.items()]}')
print(f">>test_obg['1']  {test_obg['1']}")
print(f'>>for key, value in test_obg.items()  {[(key,value) for key,value in test_obg.items()]}')
print(f'>>test_obg.add("17", "seventeen")  {test_obg.add("17", "seventeen")}')
print(f'>>for key, value in test_obg.items()  {[(key,value) for key,value in test_obg.items()]}')
print(f'>>test_obg.pop("1")  {test_obg.pop("1")}')
print(f'>>for key, value in test_obg.items()  {[(key,value) for key,value in test_obg.items()]}')
print(f'>>len(test_obg) {len(test_obg)}')
print('>>(test_obg.update({"1":"new_one"})', test_obg.update({"1" : "new_one"}))
print(f'>>for key, value in test_obg.items()  {[(key,value) for key,value in test_obg.items()]}')
for key in test_obg:
    print(key)