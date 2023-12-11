import pygame
from pygame.locals import *
import sys

try:
    from prototype.operation.operation_user import Operation
    from prototype.model.load_data import LoadData
    from prototype.model.write_data import WriteData
except ModuleNotFoundError:
    from ..operation.operation_user import Operation
    from ..model.load_data import LoadData
    from ..model.write_data import WriteData

import parts


class GameScreen(object):

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()
        self.screen = None
        self.game_op = Operation(0, 0)
        self.load_data = LoadData()
        self.load_data.load_map_tip()
        self.game_popup = None
        self.item_list = []

    def expand_game_screen(self, caption_title="Stealth Game"):
        self.load_data.load_option("option.csv")
        if self.load_data.options["FULL SCREEN"]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(caption_title)
        self.game_popup = SubGamePupUp(self.screen, self.screen_width, self.screen_height)

    def setup_game_screen(self, save_data_num=1):
        self.load_data.load_charactor("guardman")
        self.item_list = []

    def draw_game_screen(self):
        self.setup_game_screen()
        while self.game_op.is_running:
            self.screen.fill((255, 255, 255))
            self.draw_map(self.game_op.map_address)
            self.screen.blit(self.load_data.charactor["guardman"][self.game_op.charactor_direction],
                             [self.game_op.x, self.game_op.y])
            pygame.display.update()
            self.game_op.game_operation(self.screen_width, self.screen_height,
                                        self.load_data.map_info, True)
            if self.game_op.is_expand_popup:
                self.game_popup.setup_sub_menu("Pause", ゲームを再開="return", ゲームをセーブ=1,
                                               ゲームをロード=2, メインメニュー="mainmenu")
                self.game_popup.draw_sub_menu()
                self.game_op.is_running = not self.game_popup.is_return_menu
                self.game_op.is_expand_popup = False

    def draw_map(self, map_address):
        self.load_data.load_map_file(map_address)
        for row in range(12):
            for column in range(15):
                print(int(self.load_data.map_info[row][2*column:2*(column+1)]))
                self.screen.blit(self.load_data.maptips[int(self.load_data.map_info[row][2*column:2*(column+1)])],
                                 (column*50, row*50))


"""G = GameScreen(800, 600)
G.expand_game_screen("S")
G.draw_game_screen()"""


class SubGamePupUp(object):

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.popup_width = screen_width // 2
        self.popup_height = screen_height // 1.5
        self.title = None
        self.title_position = None
        self.font_title = None
        self.font_button = None
        self.popup_op = Operation(0, 0)
        self.direction = {}
        self.buttons = []
        self.buttons_position = []
        self.buttons_length = []
        self.direction_key = None
        self.load_popup = LoadData()
        self.write = WriteData()
        self.is_running = True
        self.is_game_start = False
        self.is_return_menu = False

    def setup_sub_menu(self, title="Pause", **buttons_name):
        # buttons_nameは２つまで!!!
        if len(buttons_name) > 4:
            raise ExceedError("buttons_nameは4個まで")
        self.popup_op.square_x = 0
        self.popup_op.screen_address = None
        self.direction = {}
        self.buttons = []
        self.buttons_position = []
        self.buttons_length = []
        self.direction_key = None
        self.is_running = True

        self.font_title = pygame.font.Font("PixelMplus12-Regular.ttf", int(self.popup_height // 15))
        self.font_button = pygame.font.Font("PixelMplus12-Regular.ttf", int(self.popup_height // 15))

        self.title = self.font_title.render(title, True, (255, 255, 255))
        self.title_position = self.title.get_rect(center=(self.screen_width // 2, self.screen_height // 3))
        for position, button in enumerate(buttons_name.keys()):
            self.direction[button] = buttons_name[button]
            self.buttons.append(self.font_button.render(button, True, (255, 255, 255)))
            self.buttons_position.append(self.buttons[position].get_rect(
                center=(self.screen_width // 2, self.screen_height // 2 + (self.screen_height // 15) * position)))
            self.buttons_length.append(self.font_button.size(button + "   ")[0])

        self.direction_key = list(self.direction.keys())

    def draw_sub_menu(self):
        while self.is_running:
            parts.popup_rect(self.screen, self.screen_width // 2, self.screen_height // 2, self.popup_width,
                             self.popup_height)
            self.screen.blit(self.title, self.title_position)
            for button, button_position in zip(self.buttons, self.buttons_position):
                self.screen.blit(button, button_position)
            parts.cursor_triangle(self.screen, self.screen_width // 2 - self.buttons_length[self.popup_op.square_y] / 2,
                                  (self.screen_height // 15) * self.popup_op.square_y + self.screen_height // 2,
                                  self.screen_height // 30)

            pygame.display.update()

            self.popup_op.game_popup_operation(True)
            self.reflection_command()

    def reflection_command(self):
        command = None
        try:
            command = self.direction[self.direction_key[self.popup_op.command]]
            self.popup_op.command = None
        except TypeError:
            pass

        try:
            if command == "return":
                self.is_running = False

            if command == "mainmenu":
                self.is_return_menu = True
                self.is_running = False

            if command == "save":
                pass

            if command == "31":
                self.load_popup.load_option()
                self.write.change_option("option.csv", "FULL SCREEN")
                self.load_popup.load_option()
                if self.load_popup.options["FULL SCREEN"]:
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
                else:
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                self.running = False

        except FileNotFoundError:
            pass
        self.popup_op.command = None


class ExceedError(Exception):
    pass
