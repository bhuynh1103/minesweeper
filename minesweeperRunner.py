import pygame, sys
from pygame.locals import *
from cell import *
from constants import *
from random import randint as rand

pygame.init()
screen = pygame.display.set_mode((boardSide, boardSide))
pygame.display.set_caption("Minesweeper")

# Generates grid which holds all cells
grid = []
for i in range(gridLength):
    grid.append([])
    for j in range(gridLength):
        grid[i].append(Cell(i, j))


# Generates "bombCount" bombs
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


# Function for drawing text
def writeText(window, written, color, cenX, cenY):
    font = pygame.font.Font(None, 75)
    text = font.render(written, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)

# Game control variables
leftClicked = False
rightClicked = False
fPressed = False
gameOver = False

winCount = 0

while True:
    while not (gameOver) and (winCount != bombCount):
        screen.fill(white)

        mousePos = pygame.mouse.get_pos()

        # For each cell in the grid, draws, checks if clicked or flagged, and if game has been won or lost
        for i in range(gridLength):
            for j in range(gridLength):
                cell = grid[i][j]
                cell.draw(screen)

                # Revealing
                if cell.has(mousePos) and leftClicked and not cell.revealed:
                    cell.revealed = True
                    if cell.bomb:
                        gameOver = True
                        break
                    if cell.neighbors == 0 and not cell.bomb:
                        cell.revealNeighbors(grid)

                # Flagging and unflagging
                if cell.has(mousePos) and rightClicked and not cell.flagged and not cell.revealed:
                    cell.flagged = True
                    if cell.bomb:
                        winCount += 1
                elif cell.has(mousePos) and fPressed and cell.flagged and not cell.revealed:
                    cell.flagged = False
                    if cell.bomb:
                        winCount -= 1

                # Win condition
                if winCount == bombCount:
                    gameOver = True

        pygame.display.update()

        # Kill program and check input loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            mouseStates = pygame.mouse.get_pressed()

            # Check left clicked
            if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
                leftClicked = True
            else:
                leftClicked = False

            # Check right clicked
            if event.type == MOUSEBUTTONDOWN and mouseStates[2] == 1:
                rightClicked = True
            else:
                rightClicked = False

            if event.type == KEYDOWN and event.key == K_f:
                fPressed = True
            else:
                fPressed = False

    # Game over loop
    for i in range(gridLength):
        for j in range(gridLength):
            cell = grid[i][j]
            cell.revealed = True
            cell.draw(screen)

    if winCount == bombCount:
        writeText(screen, "You Won!", white, boardSide // 2, boardSide // 2)
    else:
        writeText(screen, "You Lost!", white, boardSide // 2, boardSide // 2)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
