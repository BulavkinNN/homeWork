class MakeExc:
    """ Class make errors in our functions"""

    @staticmethod
    def make_zerodivisionerror():
        1 / 0

    @staticmethod
    def make_syntaxerror():  # not work
        # i = 1.test
        pass

    @staticmethod
    def make_attributeerror():
        "".test

    @staticmethod
    def make_nameerror():
        print_

    @staticmethod
    def make_lookuperror():
        "123"[5]
