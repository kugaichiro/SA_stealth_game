import csv
import os

import write_data

class LoadData(object):

    def __init__(self):
        self.current_dir = None
        self.parent_dir = None
        write_data.WriteData().get_directory()

        self.system_file_path = os.path.join(str(self.parent_dir), "system-data")
        self.option_file_path = None
        self.file_name = None
        self.field_name = None
        self.resource = None
        self.file = None
        self.options = None

    def load_option(self, file="option.csv"):
        self.file = file
        with open(self.file, 'r', encoding="utf8", newline="") as csvfile:
            self.options = csv.DictReader(csvfile)
            for row in self.options:
                print(row['option'], row['is_on'])


LoadData().load_option()
