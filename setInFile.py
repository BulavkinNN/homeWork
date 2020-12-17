class SetInFile(object):

    def __init__(self, work_dir="", file_name="setinfile.sif"):
        self.work_dir = work_dir
        self.file_name = file_name

    def get_all(self):
        """

        :return:
        """
        print(type(self.reader()))
        return self.reader()

    def add(self, *args):
        for item in args:
            if item in self.get_all:
                print(type(self.get_all))
                self.writer(item)

    def clear(self):
        self.writer("", access="w")

    def writer(self, *args, access="a"):
        with open(self.work_dir + self.file_name, access) as file:
            for item in args:
                file.write(item)

    def reader(self, *args):
        with open(self.work_dir + self.file_name, "r") as file:
            all_data = file.readlines()
            print(type(all_data))
            if len(args) == 0:
                return all_data
            if type(args) == int and args[0] < len(all_data):
                return all_data[args[0]]
            return None

    def __iter__(self):
        return (item for item in self.get_all())


s = SetInFile()
s.add("15")
print(s.reader())
s.clear()
print(s.reader())