import pygame
from pygame.locals import *

from prototype.operation.operation_user import Operation
from prototype.model.load_data import LoadData
import parts


class GameScreen(object):

    def __init__(self, screen_width, screen_height):
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction_key = None
        pygame.init()
        self.direction = {}
        self.screen = None
        self.game_op = Operation(0, 0)
        self.load_data = LoadData()

    def expand_game_screen(self, caption_title):
        self.load_data.load_option("option.csv")
        if self.load_data.options["FULL SCREEN"]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(caption_title)

    def setup_game_screen(self):
        self.game_op.y = 0
        self.game_op.x = 0
        self.direction = {}
        self.direction_key = list(self.direction.keys())

    def draw_game_screen(self):
        self.setup_game_screen()
        while self.game_op.is_running:
            self.screen.fill((255, 255, 255))
            parts.human(self.screen, self.game_op.x, self.game_op.y)
            pygame.display.update()
            self.game_op.game_operation(self.screen_width, self.screen_height, True)

    def draw_map(self, screen, map_info: list):
        pass

"""G = GameScreen(800, 600)
G.expand_game_screen("S")
G.draw_game_screen()"""

class SubGamePupUp(object):

    pass