import csv
import os

try: 
    from prototype.model.load_data import LoadData
except ModuleNotFoundError:
    from model.load_data import LoadData


class WriteData(object):

    def __init__(self):
        self.current_dir = None
        self.parent_dir = None
        self.get_directory()

        self.system_file_path = os.path.join(self.parent_dir, "system-data")
        self.savedata_dir_path = os.path.join(self.system_file_path, "savedata")
        self.option_file_path = None
        self.file_name = None
        self.field_name = None
        self.resource = None
        self.load = LoadData()

    def get_directory(self):
        # ファイルのある階層のディレクトリパスを取得
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 1つ上の階層のディレクトリパスを取得
        self.parent_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))

    def change_option(self, file="option.csv", *change):
        self.option_file_path = os.path.join(self.system_file_path, file)
        self.load.load_option()
        if os.path.exists(self.option_file_path):
            with open(self.option_file_path, 'w', encoding="utf8", newline="") as csvfile:
                fieldnames = ['option', 'is_on']
                writer = csv.DictWriter(csvfile, fieldnames)
                writer.writeheader()
                del self.load.options["option"]
                for key, value in self.load.options.items():
                    if key in change:
                        writer.writerow({fieldnames[0]: key, fieldnames[1]: not value})
                    else:
                        writer.writerow({fieldnames[0]: key, fieldnames[1]: value})
        else:
            raise FileNotFoundError

    def save_data(self, file_name: str, last_map_address: int, last_position: list, **resource):
        savedata_file_path = os.path.join(self.savedata_dir_path, file_name)
        with open(savedata_file_path, 'w', encoding="utf8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([last_map_address])
            writer.writerow(last_position)
            for item, num in resource.items():
                writer.writerow([item, num])
                
    def keep_command(self, **commands):
        command_file_path = os.path.join(self.system_file_path, "command.csv")
        self.load.get_command()
        with open(command_file_path, 'a', encoding="utf8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for command, value in commands.items():
                writer.writerow([command, value])
                
    def clear_command(self):
        command_file_path = os.path.join(self.system_file_path, "command.csv")
        with open(command_file_path, 'w', encoding="utf8", newline="") as csvfile:
            pass
                
