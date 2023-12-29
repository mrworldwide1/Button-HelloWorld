## simple incremental game to test out pygame
## may add more unique click sounds in the future

import pygame
import sys

# Setup
pygame.init()

screenWidth = 1000
screenHeight = 500
maxFPS = 60
buttonColour = "tomato"
pygame.display.set_caption('Clicker')
screen = pygame.display.set_mode((screenWidth, screenHeight))

# surfaces are like layers in photoshop! you fill each layer with stuff like text/color/images
# then put the layers on the canvas
button = pygame.Surface((200, 200))
button.fill(buttonColour)

# Core part that actually runs everything
def main():

    # music
    ost = pygame.mixer.music
    ost.load('xDeviruchi - Title Theme .wav')
    ost.play(-1) # loops

    # entire game runs inside this loop, keeps the code running forever
    while True:
        for event in pygame.event.get():
            # break loop when player quits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(button, (0,0))

        pygame.display.update()
        pygame.time.Clock().tick(maxFPS)


main()