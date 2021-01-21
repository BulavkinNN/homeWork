class MakeExc:

    @staticmethod
    def make_ZeroDivisionError():
        1 / 0

    @staticmethod
    def make_SyntaxError():  # not work
        # i = 1.test
        pass

    @staticmethod
    def make_AttributeError():
        "".test

    @staticmethod
    def make_NameError():
        print_

    @staticmethod
    def make_LookupError():
        "123"[5]
