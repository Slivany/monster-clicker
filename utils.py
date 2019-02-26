import pygame

pygame.init()

# Colors
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def getFont(name="Courier New", size=20, style=''):  # POST: Returns the font the Caller wants
    return pygame.font.SysFont(name, size, style)