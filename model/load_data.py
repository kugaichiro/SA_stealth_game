import csv


class LoadData(object):

    def __init__(self, file="option.csv"):
        self.file = file
        self.options = None

    def load_option(self):
        with open(self.file, encoding="utf8", newline="") as file:
            self.options = csv.reader(file)
            for option in self.options:
                print(option)


LoadOption().load_option()