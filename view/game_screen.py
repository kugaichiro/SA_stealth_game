import pygame
from pygame.locals import *

from prototype.operation.operation_user import Operation


class GameScreen(object):

    def __init__(self, screen_width, screen_height):
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction_key = None
        pygame.init()
        self.direction = {}
        self.screen = None
        self.menu_op = Operation(0, 0)

    def expand_game_screen(self, caption_title):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        pygame.display.set_caption(caption_title)

    def setup_game_screen(self):
        self.menu_op.square_y = 0
        self.menu_op.screen_address = None
        self.direction = {}
        self.direction_key = list(self.direction.keys())

    def draw_game_screen(self):
        self.setup_game_screen()
        while self.menu_op.is_running:
            self.screen.fill((0, 0, 0))

            pygame.display.update()
            self.menu_op.menu_operation(len(self.buttons))
            self.change_menu_screen()

