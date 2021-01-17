class LoggerMixin(object):

    @staticmethod
    def log(comment):
        print(globals() , comment)
