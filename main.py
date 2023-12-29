# simple incremental game to test out pygame
# may add more unique click sounds in the future

import pygame, sys

def setup():
    pygame.init()

    # Define constants, variables
    screenWidth = 500
    screenHeight = 400

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Clicker')

# Core part of code that runs everything
def main():
    while True:
        for event in pygame.event.get():
            # exit game when player quits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

setup()
main()