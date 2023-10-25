import pygame
from pygame import *
import class_JeuDeCartes
import Carte
import homescreen

def board_card(screen, pioche, n):
    cartes=pioche.pioche_carte()
    card=pygame.transform.scale(pygame.image.load(cartes.get_image()), (130,200))
    if n==0:
        screen.blit(card, (100, 30))
    elif n==1:
        screen.blit(card, (250, 30))
    elif n==2:
        screen.blit(card, (400, 30))
    elif n==3:
        screen.blit(card, (550, 30))

def played_card(screen, pioche, n):
    cartes=pioche.pioche_carte()
    card=pygame.transform.scale(pygame.image.load(cartes.get_image()), (130,200))
    if n==0:
        screen.blit(card, (250, 400))
    elif n==1:
        screen.blit(card, (400, 400))

def game(screen):
    pioche=class_JeuDeCartes.JeuDeCartes()
    pioche.creer_jeu_52_cartes()
    pioche.melange()
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
        board_card(screen, pioche, 0)
        board_card(screen, pioche, 1)
        board_card(screen, pioche, 2)
        board_card(screen, pioche, 3)
        played_card(screen, pioche, 0)
        played_card(screen, pioche, 1)


        pygame.display.flip()

    pygame.quit()
