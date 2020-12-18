import myDict
import csv
import os


class MyDictCSV(myDict.MyDict):

    def __init__(self):
        self.file_csv = self.get_random_name() + ".csv"
        self.clear()  # make empty file

    def _write_allcsv(self, list_items):
        self.clear() # write all in empty file
        for key, value in list_items:
            self._write_csv(key, value)

    def _write_csv(self, key="", value='', mode_write='a'):
        with open(self.file_csv, mode_write, newline='', encoding="utf-8") as csvfile:
            if key:  # if not key, make new file in __init__
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow((key, value))

    def _read_csv(self):
        with open(self.file_csv, 'r', newline='', encoding="utf-8") as csvfile:  # newline /n
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            return [row for row in reader]  # watch in reader

    def add(self, key, value=""):
        if key not in self.keys():  # New key
            self._write_csv(key, value)
        else:
            new_edit_dict = self._read_csv()[:] #make copy dict
            new_edit_dict[self._get_indexkey(key)] = [key, value] #find index [key, value] and rewrite new value
            self._write_allcsv(new_edit_dict) #all new dict write in file

    def _get_indexkey(self, key):
        """
        :param key:
        :return: int  index in items
        """
        return self._read_csv().index([key, self.get(key=key)])

    def get(self, d=None, key=None):
        """ Return the value for key if key is in the dictionary, else default(d) or d=None. """
        if key and key in self.keys():
            for (k, v) in self.items():
                if k == key:
                    d = v
        return d

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        return ((item[0], item[1]) for item in self._read_csv())

    def values(self):
        """ D.values() -> return iterable obj for all values """
        return (value for _, value in self.items())

    def keys(self):
        return (keys for keys, _ in self.items())

    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        self._write_csv(mode_write="w")

    def __del__(self):
        os.remove(self.file_csv)

    def __len__(self):
        return len(self._read_csv())


c = MyDictCSV()
c.add("12", "Andrey")
c.add("13", "Dmitriy")
c.add("14", "Dmitriy14")
c.add("15", "Dmitriy15")

c.add("13", "Dmitriy_n")
for key, value in c.items():
    print(key, value)

print(len(c))