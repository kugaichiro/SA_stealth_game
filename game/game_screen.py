import pygame
from pygame.locals import *

from prototype.operation.operation_user import Operation
from prototype.model.load_data import LoadData
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

    def expand_game_screen(self, caption_title):
        self.load_data.load_option("option.csv")
        if self.load_data.options["FULL SCREEN"]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(caption_title)

    def setup_game_screen(self):
        self.load_data.load_charactor("guardman")

    def draw_game_screen(self):
        self.setup_game_screen()
        while self.game_op.is_running:
            # self.screen.fill((255, 255, 255))
            self.draw_map(0)
            #parts.human(self.screen, self.game_op.x, self.game_op.y)
            self.screen.blit(self.load_data.charactor["guardman"][self.game_op.charactor_direction["guardman"]],
                             (self.game_op.x, self.game_op.y))
            pygame.display.update()
            self.game_op.game_operation(self.screen_width, self.screen_height,
                                        self.load_data.map_info, True)

    def draw_map(self, map_address):
        self.load_data.load_map_file(map_address)
        for row in range(16):
            for column in range(12):
                self.screen.blit(self.load_data.maptips[int(self.load_data.map_info[column][row])], (row*50, column*50))


G = GameScreen(800, 600)
G.expand_game_screen("S")
G.draw_game_screen()


class SubGamePupUp(object):
    pass
