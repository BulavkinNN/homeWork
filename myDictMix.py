import myDict
import loggerMixin


class MyDictMix(myDict.MyDict, loggerMixin.LoggerMixin):
    pass
