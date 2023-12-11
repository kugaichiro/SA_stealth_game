import game_screen
import menu_screen
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MainScreen(object):

    def __init__(self):
        self.menu = menu_screen.MenuScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game = game_screen.GameScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw_screen(self, caption_title="Stealth Game"):
        while True:
            self.menu.__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.menu.expand_screen(caption_title)
            self.menu.draw_menu_screen()
            self.game.__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.game.expand_game_screen(caption_title)
            self.game.draw_game_screen()


MainScreen().draw_screen()
