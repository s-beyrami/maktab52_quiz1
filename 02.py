import jdatetime

class TimestamOpen:
    def __init__(self, filename, mode: "a"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.opentime = jdatetime.datetime.now()
        self.f = open(self.filename, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closetime = jdatetime.datetime.now()
        self.f.write(f'\n open time : {self.opentime} \n close time : {self.closetime} ')

        return True


with TimestamOpen("text.txt", "x") as new_file:
    new_file()
