import pygame
import sys

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)

def run():
    pygame.init()
    screen_width=500
    screen_height=500
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Test gaming")
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        screen.fill(green)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

run()