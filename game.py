import pygame
from pygame import *
import homescreen

def board_card(screen, n):
    card=pygame.transform.scale(pygame.image.load("images/cartes/2_coeur.png"), (130,200))
    if n==0:
        screen.blit(card, (100, 30))
    elif n==1:
        screen.blit(card, (250, 30))
    elif n==2:
        screen.blit(card, (400, 30))
    elif n==3:
        screen.blit(card, (550, 30))

def played_card(screen, n):
    card=pygame.transform.scale(pygame.image.load("images/cartes/2_coeur.png"), (130,200))
    if n==0:
        screen.blit(card, (250, 400))
    elif n==1:
        screen.blit(card, (400, 400))

def game(screen):
    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (screen_width,screen_height))
    enemycard = pygame.transform.scale(pygame.image.load("images/cartes/test.png"), (200,300))
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(enemycard, (700, 10))
        screen.blit(enemycard, (700, 60))
        screen.blit(pygame.transform.rotate(enemycard,90), (-150, 60))
        screen.blit(pygame.transform.rotate(enemycard,90), (-150, 10))
        board_card(screen, 0)
        board_card(screen, 1)
        board_card(screen, 2)
        board_card(screen, 3)
        played_card(screen, 0)
        played_card(screen, 1)


        pygame.display.flip()

    pygame.quit()

# screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
# pygame.display.set_caption("UnJeuDePoker")
# game(screen)
