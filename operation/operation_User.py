from pygame.locals import *
import pygame
import sys


class BasicOperation(object):

    def __init__(self, first_square_x=0, first_square_y=0, first_x=0, first_y=0, name="guardman"):
        self.event = None
        self.is_running = True
        self.square_x = first_square_x
        self.square_y = first_square_y
        self.x = first_x
        self.y = first_y
        self.name = name
        self.screen_address = None
        self.command = None
        self.charactor_direction = {self.name: 0}

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

    def up_y(self, event, last_y=100, first_y=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_w, K_UP]:
                if first_y < self.y:
                    self.y -= 25
                    self.charactor_direction[self.name] = 0
                    return 0
                else:
                    self.y = last_y
                    self.charactor_direction[self.name] = 0
                    return -10

        return 0

    def down_y(self, event, last_y=100, first_y=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_s, K_DOWN]:
                if self.y < last_y:
                    self.y += 25
                    self.charactor_direction[self.name] = 2
                    return 0
                else:
                    self.y = first_y
                    self.charactor_direction[self.name] = 2
                    return 10

        return 0

    def left_x(self, event, last_x=100, first_x=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_a, K_LEFT]:
                if first_x < self.x:
                    self.x -= 25
                    self.charactor_direction[self.name] = 3
                    return 0
                else:
                    self.x = last_x
                    self.charactor_direction[self.name] = 3
                    return -1
        return 0

    def right_x(self, event, last_x=100, first_x=0):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key in [K_d, K_RIGHT]:
                if self.x < last_x:
                    self.x += 25
                    self.charactor_direction[self.name] = 1
                    return 0
                else:
                    self.x = first_x
                    self.charactor_direction[self.name] = 1
                    return 1

        return 0

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
        super().__init__(first_x, first_y, 400, 300)
        self.map_address = 0

    def menu_operation(self, last_y, can_operate: bool):

        if can_operate:
            pygame.key.set_repeat(400, 100)
            for event in pygame.event.get():
                # キーが押されたとき
                self.command = super().get_command(event, self.square_y)
                super().move_square_y(event, last_y - 1)

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

    def game_operation(self, width, height, map_info, can_operate: bool = True):
        if can_operate:
            pygame.key.set_repeat(200, 75)
            for event in pygame.event.get():
                self.square_y = self.y // 50
                self.square_x = self.x // 50
                try:
                    if not (int(map_info[self.square_y-1][self.square_x]) in [1]):
                        self.map_address += super().up_y(event, height)
                    if not (int(map_info[self.square_y + 1][self.square_x]) in [1]):
                        self.map_address += super().down_y(event, height)
                    if not (int(map_info[self.square_y][self.square_x+1]) in [1]):
                        self.map_address += super().right_x(event, width)
                    if not (int(map_info[self.square_y][self.square_x-1]) in [1]):
                        self.map_address += super().left_x(event, width)
                except IndexError:
                    self.map_address += super().up_y(event, height)
                    self.map_address += super().down_y(event, height)
                    self.map_address += super().right_x(event, width)
                    self.map_address += super().left_x(event, width)

                # 右上の×ボタンが押されたとき
                super().delete_screen(event)



