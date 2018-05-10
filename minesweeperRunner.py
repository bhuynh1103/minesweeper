import pygame, sys
from pygame.locals import *
from cell import *
from constants import *
from random import randint as rand

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize + (screenSize // gridLength) * 2))
pygame.display.set_caption("Minesweeper")

while True:
    # Setup/game generation processes

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


    # Game control variables
    leftClicked = False # reveal cell
    rightClicked = False # flag cell
    fPressed = False # unflag cells

    gameOver = False
    setup = True

    winCount = 0
    flagCount = 0
    correct = 0

    # Game loop and game-over loop
    while setup:
        # Game loop
        while not (gameOver) and (winCount != bombCount):
            screen.fill(gray(150))
            mousePos = pygame.mouse.get_pos()

            # Loops through each cell and calls methods for each cell
            for i in range(gridLength):
                for j in range(gridLength):
                    cell = grid[i][j]
                    cell.draw(screen)

                    # Revealing
                    if cell.has(mousePos) and leftClicked and not cell.revealed and not cell.flagged:
                        cell.revealed = True
                        if cell.bomb:
                            gameOver = True
                        if cell.neighbors == 0 and not cell.bomb:
                            cell.revealNeighbors(grid)

                    # Flagging and unflagging
                    if cell.has(mousePos) and rightClicked and not cell.flagged and not cell.revealed:
                        cell.flagged = True
                        flagCount += 1
                        if cell.bomb:
                            winCount += 1
                            correct += 1
                    elif cell.has(mousePos) and fPressed and cell.flagged and not cell.revealed:
                        cell.flagged = False
                        flagCount -= 1
                        if cell.bomb:
                            winCount -= 1
                            correct -= 1

                    # Win condition
                    if winCount == bombCount:
                        gameOver = True

            # GUI

            # Writes number of flags placed / total bombs
            writeText(screen, "Flags : " + str(flagCount) + "/" + str(bombCount), black,
            screenSize * .25 , screenSize // gridLength, (screenSize // gridLength) * 2 * .9)

            # Timer (needs to be added)

            pygame.display.update()


            # End program and check input loop
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

                # Check 'F' key is pressed
                if event.type == KEYDOWN and event.key == K_f:
                    fPressed = True
                else:
                    fPressed = False


        # Game-over loop

        screen.fill(gray(150))

        # Draws each cell
        for i in range(gridLength):
            for j in range(gridLength):
                cell = grid[i][j]
                cell.revealed = True
                cell.draw(screen)
                # Draws 'X' for incorrectly flagged cells and green box for correctly flagged cells
                cell.drawCorrect(screen)


        # Writes a lot of text

        # If won, write 'You Won!'; else, write 'You Lost!'
        if winCount == bombCount:
            writeText(screen, "You Won!", green, screenSize * .75,
            screenSize // gridLength * 2 * .25, (screenSize // gridLength) * .9)
        else:
            writeText(screen, "You Lost!", red, screenSize * .75,
            screenSize // gridLength * 2 * .25, (screenSize // gridLength) * .9)

        # Writes "Press 'Enter' to play again."
        writeText(screen, "Press 'Enter' to play again.", white,
        screenSize * .75, screenSize // gridLength * 2 * .8, (screenSize // gridLength) * .9)

        # Writes flags placed
        writeText(screen, "Flags : " + str(flagCount) + "/" + str(bombCount), black,
        screenSize * .25 , screenSize // gridLength * 2 * .25, (screenSize // gridLength) * .9)

        # Writes correct and wrong flags
        writeText(screen, "Correct flags : " + str(correct), (0, 200, 0),
        screenSize * (1/8), screenSize // gridLength * 2 * .75, (screenSize // gridLength) * .75)

        writeText(screen, "Incorrect flags : " + str(flagCount - correct), red,
        screenSize * (3/8), screenSize // gridLength * 2 * .75, (screenSize // gridLength) * .75)

        pygame.display.update()

        # End program loop and checks if 'RETURN' key is pressed to reset game
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                setup = False
            else:
                setup = True
