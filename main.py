# simple incremental game to test out pygame
# may add more unique click sounds in the future

import pygame, sys

# Setup

pygame.init()

screenWidth = 1280
screenHeight = 720
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Clicker')

# Core part that actually runs everything
def main():

    pygame.mixer.music.load()
	pygame.mixer.music.play(-1)

    # endless loop
    while True:
        for event in pygame.event.get():
            # break loop when player quits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()
        clock.tick(maxFPS)

main()