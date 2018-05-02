import pygame
from constants import *
from random import randint


class Cell:
    def __init__(self, i, j, width):
        self.i = i
        self.j = j
        self.x = i * (boardSide // gridLength)
        self.y = j * (boardSide // gridLength)
        self.w = width
        # Cells currently have 50% chance of having a bomb
        if randint(0, 2) == 1:
            self.bomb = True
        else:
            self.bomb = False
        self.revealed = False
        self.flagged = False
        self.neighbors = 0

    def draw(self, window):
        pygame.draw.rect(window, white, (self.x, self.y, self.w, self.w))
        pygame.draw.rect(window, black, (self.x, self.y, self.w, self.w), 1)

        # Draws flag if the cell is flagged
        if self.flagged and not self.revealed:
            pygame.draw.rect(window, gray(100), (self.x, self.y, self.w, self.w))
            pygame.draw.rect(window, black, (self.x, self.y, self.w, self.w), 1)
        # If revealed draw its contents (bomb or no bomb)
        elif self.revealed:
            pygame.draw.rect(window, gray(200), (self.x, self.y, self.w, self.w))
            pygame.draw.rect(window, black, (self.x, self.y, self.w, self.w), 1)
            if self.bomb:
                pygame.draw.ellipse(window, black, (self.x + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.y + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.w * .75, self.w * .75), 1)

    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)

    def count(self, grid):
        if not self.bomb:            
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if grid[self.i + x][self.j + y].bomb:
                        count += 1

            self.neighbors = count
