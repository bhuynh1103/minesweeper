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


leftClicked = False
rightClicked = False


while True:
    screen.fill(white)
    
    mousePos = pygame.mouse.get_pos()

    for i in range(gridLength):
        for j in range(gridLength):
            grid[i][j].draw(screen)
            
            if grid[i][j].has(mousePos) and leftClicked:
                grid[i][j].revealed = True
            elif grid[i][j].has(mousePos) and rightClicked:
                grid[i][j].flagged = True

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
            
            
            
        