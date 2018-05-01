import pygame, sys
from pygame.locals import *
from cell import *
from constants import *


pygame.init()
screen = pygame.display.set_mode((boardSide, boardSide))


# Creates grid which holds all cells
grid = []
for x in range(gridLength):
    grid.append([])
    for y in range(gridLength):
        grid[x].append(Cell(x * (boardSide // gridLength), y * (boardSide // gridLength), boardSide // gridLength))




while True:
    screen.fill(white)

    for i in range(gridLength):
        for j in range(gridLength):
            grid[i][j].draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
