# simple incremental game to test out pygame
# may add more unique click sounds in the future

import pygame
import sys

# Setup
pygame.init()

screenWidth = 1000
screenHeight = 500
maxFPS = 60
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Clicker')

# Core part that actually runs everything
def main():

    # music
    ost = pygame.mixer.music
    ost.load('xDeviruchi - Title Theme .wav')
    ost.play(-1) # loop set to true

    # entire game runs inside this endless loop, keeps the code running forever
    while True:
        for event in pygame.event.get():
            # break loop when player quits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()
        pygame.time.Clock().tick(maxFPS)


main()