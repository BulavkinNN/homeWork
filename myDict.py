import random
from datetime import datetime
import os


class MyDict(dict):

    def log(self):
        pass

    
    def timer(func):
        import time

        def decor_fun(*args, **kwargs):
            print(func)
            t = time.perf_counter_ns()
            result = func(*args, **kwargs)

            print(func.__name__, time.perf_counter_ns() - t)
            return result

        return decor_fun


    def __init__(self, *args, **kwargs):
        self.name_workdir = self.get_random_name() + "/"
        self.make_workdir()
        self.keysset = set()
        for item in args:
            for key, value in item:
                self.add(key, value)
        self.copy_keys = []
        self.pos_iter = 0

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
        obj = self.__class__()  # make obj self class
        for key, value in self.items():
            obj.add(key, value)
        return obj

    @classmethod  # known case
    def fromkeys(cls, keys_iterable, value=None):  # real signature unknown
        """ Create a new dictionary with keys from iterable and values set to value. """
        obj = cls()  # make obj self class
        for key in keys_iterable:
            obj[key] = value
        return obj

    def get(self, *args, **kwargs):
        """ Return the value for key if key is in the dictionary, else default. """
        if len(args) > 0 and args[0] in self.keysset:
            return self.read_value(str(args[0]))
        elif len(args) == 2:
            return args[1]
        return None  # Хотел вот так args[1] or None !!!!!!!!!!!

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        return ((key, self.get(key)) for key in self.keysset)

    def keys(self):
        return (keys for keys, _ in self.items())

    def pop(self, key, d=None):  # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        if self.get(key, d):
            d = self.get(key)
            self.__delitem__(key)
            return d
        raise KeyError('Not found key')

    def popitem(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return a (key, value) pair as a 2-tuple.
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        if len(self) == 0:
            raise KeyError("My_dict is empty")
        return self.pop(list(self.keys())[self.__len__() - 1])  # find last in list key and self.pop

    def setdefault(self, *args, **kwargs):  # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        Return the value for key if key is in the dictionary, else default.
        """
        if args[0] in self.keysset:
            return self.get(args[0])
        self.add(args[0], args[1]) if len(args) == 2 else self.add(args[0])

    @timer
    @log
    def update(self, *args):  # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        for item in args:
            for key, value in item.items():
                self.add(key, value)

    def __len__(self):
        return len(self.keysset)

    def values_(self):
        """ D.values() -> return iterable obj for all values """
        return (self.get(key) for key in self.keysset)

    def values(self):
        """ D.values() -> return iterable obj for all values """
        return (value for _, value in self.items())

    def __del__(self):
        self.clear()
        if os.path.exists(self.name_workdir):
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

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, args):
        return self.get(args)

    def __call__(self, *args, **kwargs):
        # make calleble!!!
        return self.__str__()

    def __iter__(self):
        return (key for key in self.keys())

    def __copy__(self):
        self.copy()

    def __str__(self):
        return str(["{} : {}".format(key, value) for key, value in self.items()])

    def __contains__(self, key):  # real signature unknown
        """ True if the dictionary has the specified key, else False. """
        return key in self.keys()

    def __delitem__(self, key):  # real signature unknown
        """ Delete self[key]. """
        self.del_keyvalue(key)

    def __next__(self):
        if len(self.copy_keys) == self.pos_iter == 0:
            self.copy_keys = list(self.keys())
        if self.__len__() == 0 or len(self.copy_keys) == 0 and self.pos_iter > 0:
            self.pos_iter = 0
            raise StopIteration("Key was end out")
        #     if self.copy_keys not in list(self.keys()):
        #        raise StopIteration("The keys was updates")
        self.pos_iter += 1
        return self.copy_keys.pop()
