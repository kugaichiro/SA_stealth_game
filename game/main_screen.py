#import game_screen
import menu_screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MainScreen(object):

    def __init__(self):
        self.menu = menu_screen.MenuScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
        # self.game = game_screen.GameScreen()

    def draw_screen(self):
        self.menu.expand_screen("Stealth Game")
        self.menu.draw_menu_screen()



MainScreen().draw_screen()
