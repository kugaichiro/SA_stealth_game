import csv
import os

import load_data

class WriteData(object):

    def __init__(self):
        self.current_dir = None
        self.parent_dir = None
        self.get_directory()

        self.system_file_path = os.path.join(str(self.parent_dir), "system-data")
        self.option_file_path = None
        self.file_name = None
        self.field_name = None
        self.resource = None

    def get_directory(self):
        # ファイルのある階層のディレクトリパスを取得
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 1つ上の階層のディレクトリパスを取得
        self.parent_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))

    def change_option(self, file="option.csv", **change):
        self.option_file_path = os.path.join(self.system_file_path, file)
        with open(self.option_file_path, 'w', encoding="utf8", newline="") as csvfile:
            fieldnames = ['option', 'is_on']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerow({'option': 'FULL SCREEN', 'is_on': 'True'})

    def write_file(self, file_name: str, field_name: list, **resource):
        self.file_name = file_name
        self.resource = resource
        with open(self.file_name, 'w', encoding="utf8", newline="") as csvfile:
            self.field_name = field_name
            writer = csv.DictWriter(csvfile, self.field_name)
            writer.writeheader()
            for key, value in self.resource.items():
                writer.writerow({self.field_name[0]: key, self.field_name[1]: value})


w = WriteData()
w.change_option()