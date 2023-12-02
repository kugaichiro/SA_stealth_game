from pygame.locals import *
import pygame
import sys


class BasicOperation(object):

    def __init__(self, first_square_x=0, first_square_y=0, first_x=0, first_y=0):
        self.event = None
        self.is_running = True
        self.square_x = first_square_x
        self.square_y = first_square_y
        self.x = first_x
        self.y = first_y
        self.screen_address = None
        self.command = None

    def move_square_y(self, event, last_y=100, first_y=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_w, K_UP]:
                if first_y < self.square_y:
                    self.square_y -= 1
                else:
                    self.square_y = last_y
            if self.event.key in [K_s, K_DOWN]:
                if self.square_y < last_y:
                    self.square_y += 1
                else:
                    self.square_y = first_y

    def move_square_x(self, event, last_x=100, first_x=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_a, K_LEFT]:
                if first_x < self.square_x:
                    self.square_x -= 1
                else:
                    self.square_x = last_x
            if self.event.key in [K_d, K_RIGHT]:
                if self.square_x < last_x:
                    self.square_x += 1
                else:
                    self.square_x = first_x

    def move_y(self, event, last_y=100, first_y=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_w, K_UP]:
                if first_y < self.y:
                    self.y -= 10
                    return None
                else:
                    self.y = last_y
                    return 0
            if self.event.key in [K_s, K_DOWN]:
                if self.y < last_y:
                    self.y += 10
                    return None
                else:
                    self.y = first_y
                    return 1

    def move_x(self, event, last_x=100, first_x=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_a, K_LEFT]:
                if first_x < self.x:
                    self.x -= 10
                    return None
                else:
                    self.x = last_x
                    return 3
            if self.event.key in [K_d, K_RIGHT]:
                if self.x < last_x:
                    self.x += 10
                    return None
                else:
                    self.x = first_x
                    return 1

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

    def menu_operation(self, last_y, can_operate: bool):

        if can_operate:
            pygame.key.set_repeat(400, 100)
            for event in pygame.event.get():
                # キーが押されたとき
                self.command = super().get_command(event, self.square_y)
                super().move_square_y(event, last_y-1)

                # 右上の×ボタンが押されたとき
                super().delete_screen(event)

    def popup_operation(self, can_operate: bool):
        pygame.key.set_repeat(400, 100)
        for event in pygame.event.get():
            # キーが押されたとき
            self.command = super().get_command(event, self.square_x)
            super().move_square_x(event, 1)

            # 右上の×ボタンが押されたとき
            super().delete_screen(event)

    def game_operation(self, width, height, can_operate: bool):

        if can_operate:
            pygame.key.set_repeat(200, 50)
            for event in pygame.event.get():
                super().move_y(event, height)
                super().move_x(event, width)

                # 右上の×ボタンが押されたとき
                super().delete_screen(event)

