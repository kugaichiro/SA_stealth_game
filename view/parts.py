import pygame
import math


def cursor_triangle(screen, x, y, length):
    pygame.draw.polygon(screen, (255, 255, 255),
                        [[x - length/(2*math.sqrt(3)), y + length/2],
                         [x - length/(2*math.sqrt(3)), y - length/2],
                         [x + length/math.sqrt(3), y]])
