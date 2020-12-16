import random
from datetime import datetime
import os


class MyDict(object):

    def __init__(self, *args, **kwargs):
        self.name_workdir = self.get_random_name() + "/"
        self.make_workdir()
        self.keysset = set()

    def get_random_name(self):
        return self.get_datenow() + '__' + str(random.randrange(10000, 99999))

    def get_datenow(self):
        dn = datetime.now()
        return f"{dn.day}_{dn.month}_{dn.year}__{dn.hour}_{dn.second}_{dn.microsecond}"

    def make_workdir(self):
        if os.path.exists(self.name_workdir):
            raise Exception("Bingo!")
        os.mkdir(self.name_workdir)

    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        for key in self.keysset.copy():
            self.del_keyvalue(key)

    def copy(self):
        """ D.copy() -> a shallow copy of D """
        """ Make init copy keyset and file from old to new dir"""
        obj = MyDict()
        for key, value in self.items():
            obj.add(key, value)
        return obj

    @staticmethod  # known case
    def fromkeys(*args, **kwargs):  # real signature unknown
        """ Create a new dictionary with keys from iterable and values set to value. """
        pass

    def get(self, *args, **kwargs):
        """ Return the value for key if key is in the dictionary, else default. """
        if args[0] and args[0] in self.keysset:
            return self.read_value(str(args[0]))
        else:
            return args[1] or None  # args[1] or

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        return ((key, self.get(key)) for key in self.keysset)

    def keys(self):
        return (keys for keys in self.keys)

    def pop(self, k, d=None):  # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        if self.get(k, d):
            d = self.get(k)
            self.del_keyvalue(k)
            return d
        raise KeyError('Not found key')

    def popitem(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return a (key, value) pair as a 2-tuple.
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        pass

    def setdefault(self, *args, **kwargs):  # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        Return the value for key if key is in the dictionary, else default.
        """
        if args[0] in self.keysset:
            return self.get(args[0])
        self.add(args[0], args[1]) if len(args) == 2 else self.add(args[0])



    def update(self, E=None, **F):  # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def __len__(self):
        return len(self.keysset)

    def values(self):
        """ D.values() -> return iterable obj for all values """
        return (self.get(key) for key in self.keysset)

    def __del__(self):
        self.clear()
        if os.path.exists(self.name_workdir):
            print('By!')
            os.rmdir(self.name_workdir)

    def del_keyvalue(self, key):
        self.keysset.remove(key)
        os.remove(self.name_workdir + str(key))

    def add(self, key, value=""):
        with open(self.name_workdir + str(key), "w") as file:
            file.write(value)
            self.keysset.add(key)

    def read_value(self, key):
        with open(self.name_workdir + str(key), "r") as file:
            return file.read()


c = MyDict()
print(c.name_workdir)
c.add("15", "sdsdsdsd")
print(c.get("15"))
c.add("16", "sdsdsdsd1")
print(c.get("15"))
c.add("17", "sdsdsdsd2")

print(len(c))
d = c.copy()

for key, value in d.items():
    print(key, value)
print(id(c))
print(id(d))
d.setdefault("18")
for key, value in d.items():
    print(key, value)
