import pygame
from pygame import *
import game
import lose

def homescreen(screen):

    """
    Fonction qui affiche l'interface de jeu
    Paramètres d'entree : Le screen qui est un pygame.display    
    """

    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/background.gif"), (screen_width,screen_height))
    gif_image = pygame.image.load("images/play.gif")
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.game(screen)

        gif_x = (screen_width - gif_image.get_width()) / 2
        gif_y = screen_height - gif_image.get_height()
        screen.blit(background_image, (0, 0))
        screen.blit(gif_image, (gif_x, gif_y))

        pygame.display.flip()

    pygame.quit()
