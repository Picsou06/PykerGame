from pygame import *
import pygame
import homescreen

# Définissez une taille initiale pour la fenêtre
initial_width = 800
initial_height = 600

pygame.init()
screen = pygame.display.set_mode((initial_width, initial_height), pygame.NOFRAME)
pygame.display.set_caption("UnJeuDePoker")
homescreen.homescreen(screen)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    pygame.display.flip()
