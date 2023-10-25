import pygame
from pygame import *
import homescreen

def game(screen):
    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (screen_width,screen_height))
    enemycard = pygame.transform.scale(pygame.image.load("images/cartes/dos_carte.png"), (150,250))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(pygame.transform.rotate(enemycard, -116), (-150, 50))
        screen.blit(pygame.transform.rotate(enemycard, 116), (-150, 90))


        pygame.display.flip()

    pygame.quit()

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
pygame.display.set_caption("UnJeuDePoker")
game(screen)