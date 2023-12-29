import pygame
import sys

pygame.init()

screenWidth = 1000
screenHeight = 500
buttonWidth = 200
buttonHeight = 200
maxFPS = 60
ostName = "xDeviruchi - Title Theme .wav"
bgColour = "linen"
buttonName = "button.png"
pygame.display.set_caption('Clicker')
display = pygame.display.set_mode((screenWidth, screenHeight))


# surfaces are like layers in photoshop! you fill each layer with stuff like text/color/images
# then put the layers on the canvas
# here, layers are called Surfaces
# creates instance of Surface and fills it
bg = pygame.Surface((screenWidth, screenHeight))
bg.fill(bgColour)

buttonSurface = pygame.image.load(buttonName)


# Core part that actually runs everything
def main():

    ost = pygame.mixer.music
    ost.load(ostName)
    ost.play(-1) # loops

    # entire game runs inside this loop, keeps the code running forever
    while True:
        # check each frame for events that occur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # place bg surface onto display surface, at this point
        display.blit(bg, (0,0))
        display.blit(button, (0,0))

        pygame.display.update()
        pygame.time.Clock().tick(maxFPS)


main()