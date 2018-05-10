from pygame.font import Font

# Function for drawing text
def writeText(window, written, color, cenX, cenY, size):
    font = Font(None, int(size))
    text = font.render(written, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)


# Function for creating all gray-scale colors with one RGB argument
def gray(x):
    return (x, x, x)


# Colors
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 153, 0)
brightGreen = (0, 255, 0)
blue = (0, 0, 255)
purple = (127, 0, 255)
pink = (255, 0, 255)
maroon = (128, 0, 0)
turquoise = (0, 102, 204)
black = gray(0)
white = gray(255)

# Numbers' colors list
color = [blue, green, red, purple, maroon, turquoise, black, gray(90)]

# Constants
screenSize = 800
gridLength = 20
bombCount = 50
