import myDict
import csv
import os


class MyDictCSV(myDict.MyDict):#

    def __init__(self):
        self.file_csv = self.get_random_name() + ".csv"


    def _write_csv(self, key, value=''):
        with open(self.file_csv, 'w', newline='',  encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow((key, value))


    def _read_csv(self):
        with open(self.file_csv, 'r', newline='', encoding="utf-8") as csvfile:  # newline /n
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            return [row for row in reader]  # watch in reader

    def __del__(self):
        os.remove(self.file_csv)

    def __len__(self):
        return len(self._read_csv())




c= MyDictCSV()
c._write_csv("12","Andrey")
c._write_csv("13","Dmitriy")
print(c._read_csv())
print(len(c))
