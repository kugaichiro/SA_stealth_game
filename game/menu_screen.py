import pygame
import sys
from pygame.locals import *

try:
    from prototype.operation.operation_user import Operation
    from prototype.model.load_data import LoadData
    from prototype.model.write_data import WriteData
    import parts
except ModuleNotFoundError:
    from operation.operation_user import Operation
    from model.load_data import LoadData
    from model.write_data import WriteData
    from game import parts


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
        self.load_data = LoadData()
        self.game_info = {}
        self.sub_menu = None
        self.is_game_start = False

    def expand_screen(self, caption_title):
        self.load_data.load_option("option.csv")
        if self.load_data.options["FULL SCREEN"]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.sub_menu = SubMenuPopUp(self.screen, self.screen_width, self.screen_height)
        pygame.display.set_caption(caption_title)

    def setup_menu_screen(self, title="Stealth Game", title_size=None, button_size=None, **buttons_name):
        self.menu_op.square_y = 0
        self.menu_op.screen_address = None
        self.direction = {}
        self.buttons = []
        self.buttons_position = []
        self.buttons_length = []

        self.font_title = pygame.font.Font("system-data/PixelMplus12-Regular.ttf", self.screen_height // 6)
        self.font_button = pygame.font.Font("system-data/PixelMplus12-Regular.ttf", self.screen_height // 15)

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
        self.load_data.load_menu_data_file("0")
        self.setup_menu_screen(self.load_data.menu_title, **self.load_data.menu_buttons)
        while self.menu_op.is_running:
            self.screen.fill((0, 0, 0))

            self.screen.blit(self.title, self.title_position)
            for button, button_position in zip(self.buttons, self.buttons_position):
                self.screen.blit(button, button_position)
            parts.cursor_triangle(self.screen, self.screen_width // 2 - self.buttons_length[self.menu_op.square_y] / 2,
                                  (self.screen_height // 15) * self.menu_op.square_y + self.screen_height // 2,
                                  self.screen_height // 30)

            pygame.display.update()
            self.menu_op.menu_operation(len(self.buttons), True)

            self.change_menu_screen()

    def change_menu_screen(self):
        command = None
        try:
            command = self.direction[self.direction_key[self.menu_op.command]]
            self.menu_op.command = None
        except TypeError:
            pass

        try:
            if command == "exit":
                pygame.quit()
                sys.exit()
            self.load_data.load_menu_data_file(str(command))
            self.setup_menu_screen(self.load_data.menu_title, **self.load_data.menu_buttons)

        except FileNotFoundError:
            try:
                self.load_data.load_popup_menu_file(str(command))
                self.sub_menu.setup_sub_menu(self.load_data.popup_text, **self.load_data.popup_buttons)
                self.sub_menu.draw_sub_menu()
                self.menu_op.is_running = not self.sub_menu.is_game_start
            except FileNotFoundError:
                pass


class SubMenuPopUp(object):

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.popup_width = screen_width // 2
        self.popup_height = screen_height // 2
        self.text = None
        self.text_position = None
        self.font_text = None
        self.font_button = None
        self.bold_font_button = None
        self.popup_op = Operation(0, 0)
        self.direction = {}
        self.buttons = []
        self.bold_font_buttons = []
        self.buttons_position = []
        self.buttons_length = []
        self.direction_key = None
        self.load_popup = LoadData()
        self.write = WriteData()
        self.is_running = True
        self.is_game_start = False

    def setup_sub_menu(self, text, **buttons_name):
        # buttons_nameは２つまで!!!
        if len(buttons_name) > 2:
            raise ExceedError("buttons_nameは２個まで")
        self.popup_op.square_x = 0
        self.popup_op.screen_address = None
        self.direction = {}
        self.buttons = []
        self.bold_font_buttons = []
        self.buttons_position = []
        self.buttons_length = []
        self.direction_key = None
        self.is_running = True

        self.font_text = pygame.font.Font("system-data/PixelMplus12-Regular.ttf", self.popup_height // 15)
        self.font_button = pygame.font.Font("system-data/PixelMplus12-Regular.ttf", self.popup_height // 15)
        self.bold_font_button = pygame.font.Font("system-data/PixelMplus12-Bold.ttf", self.popup_height // 15)

        self.text = self.font_text.render(text, True, (255, 255, 255))
        self.text_position = self.text.get_rect(center=(self.screen_width // 2, self.screen_height // 3))
        for position, button in enumerate(buttons_name.keys()):
            self.direction[button] = buttons_name[button]
            self.buttons.append(self.font_button.render(button, True, (125, 125, 125)))
            self.bold_font_buttons.append(self.bold_font_button.render(button, True, (255, 255, 255)))
            self.buttons_position.append(self.buttons[position].get_rect(
                center=(self.screen_width // 2 - self.popup_width // 6 + (self.popup_width // 3) * position,
                        self.screen_height // 2 + self.popup_height // 6)))

        self.direction_key = list(self.direction.keys())

    def draw_sub_menu(self):
        while self.is_running:
            parts.popup_rect(self.screen, self.screen_width // 2, self.screen_height // 2, self.popup_width,
                             self.popup_height)
            self.screen.blit(self.text, self.text_position)
            if self.popup_op.square_x == 0:
                self.screen.blit(self.bold_font_buttons[0], self.buttons_position[0])
                self.screen.blit(self.buttons[1], self.buttons_position[1])
            elif self.popup_op.square_x == 1:
                self.screen.blit(self.buttons[0], self.buttons_position[0])
                self.screen.blit(self.bold_font_buttons[1], self.buttons_position[1])

            pygame.display.update()

            self.popup_op.popup_operation(True)
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

            if command == "start":
                self.is_running = False
                self.is_game_start = True
                
            try:
                command = int(command)
                if 21 <= command <= 23:
                    self.write.keep_command(command=command-20)
                    self.is_running = False

                if command == 31:
                    self.load_popup.load_option()
                    self.write.change_option("option.csv", "FULL SCREEN")
                    self.load_popup.load_option()
                    if self.load_popup.options["FULL SCREEN"]:
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                    self.running = False
            except ValueError:
                pass
            except TypeError:
                pass
            
            

        except FileNotFoundError:
            pass
        self.popup_op.command = None


class ExceedError(Exception):
    pass
