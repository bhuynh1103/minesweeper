import pygame, sys
from pygame.locals import *
from cell import *
from constants import *
from random import randint as rand


pygame.init()
screen = pygame.display.set_mode((boardSide, boardSide))


# Creates grid which holds all cells
grid = []
for i in range(gridLength):
    grid.append([])
    for j in range(gridLength):
        grid[i].append(Cell(i, j, boardSide // gridLength))

# Generates bombs
countBombs = 0
while countBombs != bombCount:
    i = rand(0, gridLength - 1)
    j = rand(0, gridLength - 1)
    if not grid[i][j].bomb:
        grid[i][j].bomb = True
        countBombs += 1


# Counts neighboring bombs for each cell
for x in range(gridLength):
    for y in range(gridLength):
        grid[x][y].count(grid)
        # DEBUG
        # print(grid[x][y].neighbors)


leftClicked = False
rightClicked = False
spacePressed = False


while True:
    screen.fill(white)

    mousePos = pygame.mouse.get_pos()

    for i in range(gridLength):
        for j in range(gridLength):
            grid[i][j].draw(screen)
            grid[i][j].writeNeighbors(screen)

            if grid[i][j].has(mousePos) and leftClicked and not grid[i][j].revealed:
                grid[i][j].revealed = True
                if grid[i][j].neighbors == 0 and not grid[i][j].bomb and not grid[i][j].flagged:
                    grid[i][j].revealNeighbors(grid)

            if grid[i][j].has(mousePos) and leftClicked and grid[i][j].revealed:
                grid[i][j].revealNeighbors(grid)
                '''
                if grid[i][j].neighbors == 0 and not grid[i][j].bomb:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            a = grid[i][j].i + x
                            b = grid[i][j].j + y
                            if not(a < 0 or b < 0 or a > gridLength - 1 or b > gridLength - 1):
                                grid[a][b].revealed = True
                                if grid[a][b].neighbors == 0:
                '''
            elif grid[i][j].has(mousePos) and rightClicked and not grid[x][y].flagged:
                grid[i][j].flagged = True
            elif grid[i][j].has(mousePos) and grid[x][y].flagged and spacePressed:
                grid[i][j].flagged = False

            # DEBUG
            # if grid[x][y].has(mousePos):
                # print(grid[x][y].neighbors)

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
