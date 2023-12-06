import csv
import os
from distutils.util import strtobool
import pygame
from pygame.locals import *

NumOfMapTip = 3


class LoadData(object):

    def __init__(self):
        self.current_dir = None
        self.parent_dir = None
        self.get_directory()

        self.system_dir_path = os.path.join(str(self.parent_dir), "system-data")
        self.option_dir_path = self.system_dir_path
        self.menu_data_dir_path = os.path.join(self.system_dir_path, "menudata")
        self.stage_data_dir_path = os.path.join(self.system_dir_path, "stagedata")
        self.picture_data_dir_path = os.path.join(self.system_dir_path, "picture")
        self.option_file_path = None
        self.menu_data_file_path = None
        self.popup_data_file_path = None
        self.stage_data_file_path = None
        self.file_name = None
        self.field_name = None
        self.options = {}

        self.is_full_screen = True

        self.menu_title = None
        self.menu_buttons = None

        self.popup_text = None
        self.popup_buttons = None

        self.map_info = []

        self.maptips = []

        self.charactor = {}

    def get_directory(self):
        # ファイルのある階層のディレクトリパスを取得
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 1つ上の階層のディレクトリパスを取得
        self.parent_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))

    def load_option(self, file="option.csv"):
        self.option_file_path = os.path.join(self.system_dir_path, file)
        if os.path.exists(self.option_file_path):
            with open(self.option_file_path, 'r', encoding="utf8", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.options[row[0]] = row[1]
                for key, value in self.options.items():
                    if key == "option":
                        continue
                    self.options[key] = strtobool(value)

    def load_menu_data_file(self, menu_num: str):
        self.menu_data_file_path = os.path.join(self.menu_data_dir_path, "menu" + menu_num + ".csv")

        self.menu_title = None
        self.menu_buttons = None
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

        else:
            raise FileNotFoundError

    def load_popup_menu_file(self, popup_menu_num: str):
        self.popup_data_file_path = os.path.join(self.menu_data_dir_path, "popup" + popup_menu_num + ".csv")

        self.popup_text = None
        self.popup_buttons = None
        if os.path.exists(self.popup_data_file_path):

            with open(self.popup_data_file_path, 'r', encoding="utf8", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                resource = {}
                for row in csv_reader:
                    if row[0] == "text":
                        self.popup_text = row[1]
                    else:
                        resource[row[0]] = row[1]

                self.popup_buttons = resource.copy()
        else:
            raise FileNotFoundError

    def load_map_file(self, map_num):
        self.stage_data_file_path = os.path.join(self.stage_data_dir_path, "stage" + str(map_num) + ".txt")
        with open(self.stage_data_file_path, 'r', encoding="utf8", newline="") as file:
            file_info = file.readlines()
        for row in range(12):
            self.map_info.append(file_info[row][:17])

    def load_map_tip(self):

        for map_tip_num in range(NumOfMapTip):
            maptip_file_path = os.path.join(self.picture_data_dir_path, "maptip" + str(map_tip_num) + ".jpg")
            self.maptips.append(pygame.image.load(maptip_file_path))

    def load_charactor(self, name: str):
        self.charactor[name] = []

        charactor_dir_path = os.path.join(self.picture_data_dir_path, "charactor")
        for direction in range(4):
            charactor_file_path = os.path.join(charactor_dir_path, name + str(direction) + ".jpg")
            if os.path.exists(charactor_file_path):
                charactor = pygame.image.load(charactor_file_path).convert()
                color_transparent = charactor.get_at((0, 0))
                charactor.set_colorkey(color_transparent, RLEACCEL)
                self.charactor[name].append(charactor)
            else:
                raise FileNotFoundError

