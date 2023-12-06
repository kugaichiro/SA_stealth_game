from pygame.locals import *
import pygame
import math


def cursor_triangle(screen, x, y, length):
    pygame.draw.polygon(screen, (255, 255, 255),
                        [[x - length / (2 * math.sqrt(3)), y + length / 2],
                         [x - length / (2 * math.sqrt(3)), y - length / 2],
                         [x + length / math.sqrt(3), y]])


def popup_rect(screen, x, y, width, height, bold=5):
    pygame.draw.rect(screen, (255, 255, 255), (x - width // 2 - bold, y - height // 2 - bold
                                               , width + 2 * bold, height + 2 * bold))
    pygame.draw.rect(screen, (0, 0, 0), (x - width // 2, y - height // 2
                                               , width, height))


def human(screen, x, y):
    img_file_path = r"C:\Users\irhi8\PycharmProjects\pythonProject\SA_project\prototype\system-data\picture\human.jpg"
    human = pygame.image.load(img_file_path).convert()
    color_transparent = human.get_at((0, 0))
    human.set_colorkey(color_transparent, RLEACCEL)

    screen.blit(human, (x - 25, y- 25))
