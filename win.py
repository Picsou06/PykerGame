import pygame
from pygame import *
from time import sleep
import homescreen

def win(screen):
    
    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/win.jpg"), (screen_width,screen_height))
    
    x=0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                homescreen.homescreen(screen)

        screen.blit(background_image, (0, 0))
        if x==1:
            sleep(5)
            homescreen.homescreen(screen)
        x=1

        pygame.display.flip()

    pygame.quit()
