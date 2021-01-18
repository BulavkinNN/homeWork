import myDict
import loggerMixin


class MyDictMix(myDict.MyDict, loggerMixin.LoggerMixin):


    def __init__(self, *args, **kwargs):
        self.name_workdir = self.get_random_name() + "/"
        self.make_workdir()
        self.keysset = set()
        for item in args:
            for key, value in item:
                self.add(key, value)
        self.copy_keys = []
        self.pos_iter = 0
        self.log("Message from function mixin", vars())
