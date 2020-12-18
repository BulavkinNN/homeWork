import myDict
import csv
import os


class MyDictCSV(myDict.MyDict):

    def __init__(self):
        self.file_csv = self.get_random_name() + ".csv"
        self._write_csv(key="") #make empty file


# make the coin in file write and write or skip
    def _write_csv(self, key, value=''):
        with open(self.file_csv, 'a', newline='',  encoding="utf-8") as csvfile:
            if key: # if not key, make new file in __init__
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow((key, value))


    def _read_csv(self):
        with open(self.file_csv, 'r', newline='', encoding="utf-8") as csvfile:  # newline /n
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            return [row for row in reader]  # watch in reader

    def add(self, key, value=""):
        if key not in self.keys(): # New key
            self._write_csv(key, value)
         #if update???

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        return ((item[0], item[1]) for item in self._read_csv())

    def values(self):
        """ D.values() -> return iterable obj for all values """
        return (value for keys, value in self.items())

    def keys(self):
        return (keys for keys, value in self.items())

    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        self._write_csv(key="")

    def __del__(self):
        os.remove(self.file_csv)


    def __len__(self):
        return len(self._read_csv())




c= MyDictCSV()
c.add("12","Andrey")
c.add("13","Dmitriy")
print(c._read_csv())
print(len(c))
for key in c.keys():
    print(key)
for value in c.values():
    print(value)
for key,value in c.items():
    print(key, value)

e = c.copy()
print(e)