import random
from datetime import datetime
import os

class MyDict(dict):

    def __init__(self):
        self.name_dir = self.get_date() + self.get_random_name()
        self.make_dir()

    def get_random_name(self):
        return str(random.randrange(10000, 99999))

    def get_date(self):
        dn = datetime.now()
        return f"{dn.day}_{dn.month}_{dn.year}__{dn.hour}_{dn.second}_{dn.microsecond}_"

    def make_dir(self):
        os.mkdir(self.name_dir)

    def __del__(self):
        os.rmdir(self.name_dir)



c = MyDict()
print(c.name_dir)
d = input()
