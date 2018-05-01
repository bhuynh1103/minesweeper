import pygame
from constants import *
from random import randint


class Cell:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.w = width
        if randint(0, 2) == 1:
            self.bomb = True
        else:
            self.bomb = False
        # self.bomb = True
        self.revealed = True

    def draw(self, window):
        pygame.draw.rect(window, white, (self.x, self.y, self.w, self.w))
        pygame.draw.rect(window, gray(40), (self.x, self.y, self.w, self.w), 1)

        if self.revealed:
            if self.bomb:
                pygame.draw.ellipse(window, black, (self.x + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.y + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.w * .75, self.w * .75), 1)
