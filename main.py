# simple incremental game to test out pygame
# may add more unique click sounds in the future

import pygame, sys

def setup():
    pygame.init()

    # constants / variables
    screenWidth = 1280
    screenHeight = 720

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Clicker')

setup()

# Core part of code that runs everything
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

setup()