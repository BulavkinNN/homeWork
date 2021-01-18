class LoggerMixin(object):

    @staticmethod
    def log(comment):
        """how to access the  parent's function scope"""
        print(globals() , comment)
