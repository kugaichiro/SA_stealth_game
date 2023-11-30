import csv
import os
from distutils.util import strtobool


from prototype.model import write_data

class LoadData(object):

    def __init__(self):
        self.current_dir = None
        self.parent_dir = None
        self.get_directory()

        self.system_file_path = os.path.join(str(self.parent_dir), "system-data")
        self.option_file_path = None
        self.menu_data_dir_path = os.path.join(self.system_file_path, "menudata")
        self.file_name = None
        self.field_name = None
        self.options = {}

        self.is_full_screen = True

        self.menu_title = None
        self.menu_buttons = None

    def get_directory(self):
        # ファイルのある階層のディレクトリパスを取得
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 1つ上の階層のディレクトリパスを取得
        self.parent_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))

    def load_option(self, file="option.csv"):
        self.option_file_path = os.path.join(self.system_file_path, file)
        if os.path.exists(self.option_file_path):
            with open(self.option_file_path, 'r', encoding="utf8", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.options[row[0]] = row[1]
                self.is_full_screen = strtobool(self.options['FULL SCREEN'])

    def load_menu_data_file(self, menu_num: str):
        self.menu_data_file_path = os.path.join(self.menu_data_dir_path, "menu"+menu_num+".csv")

        if os.path.exists(self.menu_data_file_path):

            with open(self.menu_data_file_path, 'r', encoding="utf8", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                resource = {}
                for row in csv_reader:
                    if row[0] == "title":
                        self.menu_title = row[1]
                    else:
                        resource[row[0]] = row[1]

                self.menu_buttons = resource.copy()


                


