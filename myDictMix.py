import myDict
import loggerMixin


class MyDictMix(myDict.MyDict, loggerMixin.LoggerMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.log("Message from function mixin", vars())
