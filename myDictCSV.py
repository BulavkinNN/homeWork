import myDict
import csv


class MyDictCSV(object):#myDict.MyDict

    def __init__(self):
        # self.file_csv = self.get_random_name() + ".csv"
        self.file_csv = "11111111111111.csv"

    def write_csv(self, key, value=''):
        with open(self.file_csv, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow(key+";"+ value)


    def read_csv(self):
        with open(self.file_csv, 'r', newline='', encoding="utf-8") as csvfile:  # newline /n
            reader = csv.reader(csvfile, delimiter=' ')
            return [row for row in reader]  # watch in reader



c= MyDictCSV()
c.write_csv("12","15")
c.write_csv("13","16")
print(c.read_csv())