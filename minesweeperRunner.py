import pygame, sys
from pygame.locals import *
from cell import *
from constants import *


pygame.init()
screen = pygame.display.set_mode((boardSide, boardSide))


# Creates grid which holds all cells
grid = []
for i in range(gridLength):
    grid.append([])
    for j in range(gridLength):
        grid[i].append(Cell(i, j, boardSide // gridLength))

for x in range(gridLength):
    for y in range(gridLength):
        grid[x][y].count(grid)
        print(grid[x][y].neighbors)

leftClicked = False
rightClicked = False
spacePressed = False


while True:
    screen.fill(white)

    mousePos = pygame.mouse.get_pos()

    for x in range(gridLength):
        for y in range(gridLength):
            grid[x][y].draw(screen)

            if grid[x][y].has(mousePos) and leftClicked:
                grid[x][y].revealed = True
            elif grid[x][y].has(mousePos) and rightClicked and not grid[x][y].flagged:
                grid[x][y].flagged = True
            elif grid[x][y].has(mousePos) and grid[x][y].flagged and spacePressed:
                grid[x][y].flagged = False

            # DEBUG
            # if grid[x][y].has(mousePos):
            #     print(grid[x][y].neighbors)

    pygame.display.update()

    # DEBUG
    # print(pygame.mouse.get_pressed())


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        mouseStates = pygame.mouse.get_pressed()

        # Checks which mouse buttons are pressed

        # Left mouse button
        if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
            leftClicked = True
        else:
            leftClicked = False

        # Right mouse button
        if event.type == MOUSEBUTTONDOWN and mouseStates[2] == 1:
            rightClicked = True
        else:
            rightClicked = False

        if event.type == KEYDOWN and event.key == K_SPACE:
            spacePressed = True
        else:
            spacePressed = False
