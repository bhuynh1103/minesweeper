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
                pygame.draw.ellipse(window, gray(25), (self.x + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.y + (self.w - (self.w * .75)) - (self.w * .125),
                                                    self.w * .75, self.w * .75))

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
                    i = self.i + x
                    j = self.j + y
                    if not(i < 0 or j < 0 or i > gridLength - 1 or j > gridLength - 1):
                        if grid[i][j].bomb:
                            count += 1

            self.neighbors = count

    def reveal(self, grid):
        self.revealed = True
        if self.neighbors == 0 and not self.flagged:
            self.revealNeighbors(grid)

    def revealNeighbors(self, grid):
        for x in range(-1, 2):
            for y in range(-1, 2):
                i = self.i + x
                j = self.j + y
                if not(i < 0 or j < 0 or i > gridLength - 1 or j > gridLength - 1):
                    if not grid[i][j].bomb and not grid[i][j].revealed:
                        grid[i][j].reveal(grid)

    def writeNeighbors(self, window):
        if self.revealed and not self.bomb and not self.neighbors == 0:
            font = pygame.font.Font(None, int((boardSide // gridLength) * .9))
            text = font.render(str(self.neighbors), 1, color[self.neighbors - 1])
            textpos = text.get_rect()
            textpos.centerx = self.x + self.w * .5
            textpos.centery = self.y + self.w * .5
            window.blit(text, textpos)
            return (textpos)
