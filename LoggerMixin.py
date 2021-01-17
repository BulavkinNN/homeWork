class LoggerMixin:

    @staticmethod
    def log(comment):
        print(vars(), comment)
