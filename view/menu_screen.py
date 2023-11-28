import pygame
import sys
from pygame.locals import *

from prototype.operation.operation_User import Operation
import parts


class MenuScreen(object):

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction_key = None
        pygame.init()
        self.direction = {}
        self.buttons = []
        self.buttons_position = []
        self.buttons_length = []
        self.title = None
        self.title_position = None
        self.screen = None
        self.font_title = None
        self.font_button = None
        self.menu_op = Operation(0, 0)

    def expand_screen(self, caption_title):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        pygame.display.set_caption(caption_title)

    def setup_menu_screen(self, title="Stealth Game", title_size=None, button_size=None, **buttons_name):
        self.menu_op.square_y = 0
        self.menu_op.screen_address = None
        self.direction = {}
        self.buttons = []
        self.buttons_position = []
        self.buttons_length = []

        self.font_title = pygame.font.Font("PixelMplus12-Regular.ttf", self.screen_height // 6)
        self.font_button = pygame.font.Font("PixelMplus12-Regular.ttf", self.screen_height // 15)

        self.title = self.font_title.render(title, True, (255, 0, 0))
        self.title_position = self.title.get_rect(center=(self.screen_width // 2, self.screen_height // 3))
        for position, button in enumerate(buttons_name.keys()):
            self.direction[button] = buttons_name[button]
            self.buttons.append(self.font_button.render(button, True, (255, 255, 255)))
            self.buttons_position.append(
                self.buttons[position].get_rect(center=(self.screen_width // 2,
                                                        self.screen_height // 2 + (
                                                                self.screen_height // 15) * position)))
            self.buttons_length.append(self.font_button.size(button + "  ")[0])
        self.direction_key = list(self.direction.keys())

    def draw_menu_screen(self):
        self.setup_menu_screen("Stealth Game", start=1, load=2, option=3, exit="exit")
        while self.menu_op.is_running:
            self.screen.fill((0, 0, 0))

            self.screen.blit(self.title, self.title_position)
            for button, button_position in zip(self.buttons, self.buttons_position):
                self.screen.blit(button, button_position)
            parts.cursor_triangle(self.screen, self.screen_width // 2 - self.buttons_length[self.menu_op.square_y] / 2,
                                  (self.screen_height // 15) * self.menu_op.square_y + self.screen_height // 2,
                                  self.screen_height // 30)

            pygame.display.update()
            self.menu_op.menu_operation(len(self.buttons))
            self.change_menu_screen()

    def change_menu_screen(self):
        try:
            if self.direction[self.direction_key[self.menu_op.screen_address]] == 0:
                self.setup_menu_screen("Stealth Game", start=1, load=2, option=3, exit="exit")

            if self.direction[self.direction_key[self.menu_op.screen_address]] == 1:
                self.setup_menu_screen("難易度は?", Original=11, Easy=12, ホームに戻る=0)
                pygame.init()

            if self.direction[self.direction_key[self.menu_op.screen_address]] == 2:
                self.setup_menu_screen("ロード画面", セーブデータ1=21, セーブデータ2=22, セーブデータ3=23,
                                       ホームに戻る=0)

            if self.direction[self.direction_key[self.menu_op.screen_address]] == 3:
                self.setup_menu_screen("オプション", スクリーン設定=31, ホームに戻る=0)

            if self.direction[self.direction_key[self.menu_op.screen_address]] == "exit":
                pygame.quit()
                sys.exit()

            if self.direction[self.direction_key[self.menu_op.screen_address]] == 11:
                pass

        except TypeError:
            pass


class SubMenuPopUp(MenuScreen):

    def __init__(self, screen_width, screen_height):
        self.popup_width = screen_width // 2
        self.popup_height = screen_height // 2
        super().__init__(self.popup_width, self.popup_height)

    def setup_sub_menu(self, title, **buttons_name):
        super().setup_menu_screen(title, 30, 20, **buttons_name)

    def draw_sub_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.popup_width, self.popup_height,
                                                  self.popup_width, self.screen_height))
        


pygame.init()
pygame.display.set_mode()
