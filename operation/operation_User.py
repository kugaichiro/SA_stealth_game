from pygame.locals import *
import pygame
import sys


class BasicOperation(object):

    def __init__(self, first_x=0, first_y=0):
        self.event = None
        self.is_running = True
        self.square_x = first_x
        self.square_y = first_y
        self.screen_address = None
        self.command = None

    def move_y(self, event, last_y=100, first_y=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_w, K_UP] and first_y < self.square_y:
                self.square_y -= 1
            if self.event.key in [K_s, K_DOWN] and self.square_y < last_y:
                self.square_y += 1

    def move_x(self, event, last_x=100, first_x=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.type in [K_a, K_LEFT] and first_x < self.square_x:
                self.square_x -= 1
            if self.event.type in [K_d, K_RIGHT] and self.square_x < last_x:
                self.square_x += 1

    def get_command(self, event, resource):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == K_RETURN:
                return resource

    def delete_screen(self, event):
        self.event = event
        if self.event.type == QUIT:
            self.is_running = False
            pygame.quit()
            sys.exit()


class Operation(BasicOperation):

    def __init__(self, first_x=0, first_y=0):
        super().__init__(first_x, first_y)

    def menu_operation(self, last_y):
        pygame.key.set_repeat(200, 50)
        for event in pygame.event.get():
            # キーが押されたとき
            self.screen_address = super().get_command(event, self.square_y)
            super().move_y(event, last_y-1)

            # 右上の×ボタンが押されたとき
            super().delete_screen(event)

    def game_operation(self):
        pass