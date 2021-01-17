class LoggerMixin(object):

    @staticmethod
    def log(comment):
        print(vars(), comment)
