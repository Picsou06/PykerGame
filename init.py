<<<<<<< HEAD
from tkinter import * #Importer tkinter
from JeuDeCartes import * #Importer JeuDeCartes.py (et ses fonctions)
from homescreen import *

Jeu=JeuDeCartes() #Definir la variable Jeu
Jeu.creer_jeu_52_cartes() #Creation du jeu de cartes avec la fonction 
print(Jeu.afficher_jeu()) #Affichage du paquet de cartes
homescreen()

=======
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
>>>>>>> 89d54f8 (Evan: Début d'idée, base screen et placement carte)
