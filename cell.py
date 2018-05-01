import pygame
from constants import *
from random import randint


class Cell:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.w = width
        # Cells currently have 50% chance of having a bomb
        if randint(0, 2) == 1:
            self.bomb = True
        else:
            self.bomb = False
        self.revealed = False
        self.flagged = False

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
    
    def check(self):
        pass
