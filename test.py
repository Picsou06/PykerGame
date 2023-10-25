import pygame
import os

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
screen = pygame.display.set_mode((400, 400))
screen_width, screen_height = screen.get_size()

# Charger l'image
background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (screen_width,screen_height))
enemycard = pygame.transform.scale(pygame.image.load("images/cartes/dos_carte.png"), (150,250))

# Définir l'angle de rotation
angle = 160

# Tourner l'image
rotated_image = pygame.transform.rotate(enemycard, angle)

# Récupérer le rectangle qui entoure l'image tournée
rect = rotated_image.get_rect()

# Mettre à jour la position pour centrer l'image
rect.center = screen.get_rect().center

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher l'image tournée
    screen.blit(rotated_image, rect.topleft)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
