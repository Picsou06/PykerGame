import pygame
from pygame import *
import class_JeuDeCartes
import class_EnemyHand
import class_PlayerHand
import class_Cartes
import homescreen

def board_card(screen, cartes, phase):
    for i in range(0,phase):
        card=pygame.transform.scale(pygame.image.load(cartes[i].get_image()), (130,200))
        if i==0:
            screen.blit(card, (100, 30))
        elif i==1:
            screen.blit(card, (250, 30))
        elif i==2:
            screen.blit(card, (400, 30))
        elif i==3:
            screen.blit(card, (550, 30))

def played_card(player, screen, cartes, n):
    player.add_cartes(cartes)
    card=pygame.transform.scale(pygame.image.load(cartes.get_image()), (130,200))
    if n==0:
        screen.blit(card, (250, 400))
    elif n==1:
        screen.blit(card, (400, 400))

def adversaire_card(adversaire, cartes):
    adversaire.add_cartes(cartes)

def game(screen):
    adversaire1_hand=class_EnemyHand.EnemyHand()
    adversaire2_hand=class_EnemyHand.EnemyHand()
    player_hand=class_PlayerHand.PlayerHand()
    pioche=class_JeuDeCartes.JeuDeCartes()
    pioche.creer_jeu_52_cartes()
    pioche.melange()
    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (screen_width,screen_height))
    enemycard = pygame.transform.scale(pygame.image.load("images/cartes/test.png"), (200,300))
    pl=[pioche.pioche_carte(),pioche.pioche_carte()]
    en1=[pioche.pioche_carte(),pioche.pioche_carte()]
    en2=[pioche.pioche_carte(),pioche.pioche_carte()]
    bo=[pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte()]

    running = True
    phase=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if phase<4:
                    phase=phase+1


        screen.blit(background_image, (0, 0))
        screen.blit(enemycard, (700, 10))
        screen.blit(enemycard, (700, 60))
        screen.blit(pygame.transform.rotate(enemycard,90), (-150, 60))
        screen.blit(pygame.transform.rotate(enemycard,90), (-150, 10))

        #Affichage differents textes (scores)

            #Mise en place des variables

        police = pygame.font.SysFont("monospace",20)

                #Pour le Joueur

        player_monnaie = str(player_hand.affiche_total_monnaie())
        texte_player = police.render ("Argent Joueur :", 1 ,(150,0,0)) #Le (150,0,0) est la couleur du texte en RGB, pareil pour les suivants
        player_texte = police.render (player_monnaie,1,(150,0,0))

                #Pour l'adversaire 1
        adversaire1_monnaie = str(adversaire1_hand.affiche_total_monnaie())
        texte_adversaire1 = police.render ("Argent Adversaire :", 1 ,(150,0,0))
        adversaire1_texte = police.render (adversaire1_monnaie, 1 ,(150,0,0))

                #Pour l'adversaire 2

        adversaire2_monnaie = str(adversaire2_hand.affiche_total_monnaie())
        texte_adversaire2 = police.render ("Argent Adversaire :", 1 ,(150,0,0))
        adversaire2_texte = police.render (adversaire2_monnaie, 1 ,(150,0,0))


            # Placement

        screen.blit(texte_player,(25,500))
        screen.blit(player_texte,(50,525))
        screen.blit(texte_adversaire1,(75,25))
        screen.blit(adversaire1_texte,(75,50))
        screen.blit(texte_adversaire2,(550,25))
        screen.blit(adversaire2_texte,(700,50))

        played_card(player_hand, screen, pl[0], 0)
        played_card(player_hand, screen, pl[1], 1)
        adversaire_card(adversaire1_hand, en1[0])
        adversaire_card(adversaire1_hand, en1[1])
        adversaire_card(adversaire2_hand, en2[0])
        adversaire_card(adversaire2_hand, en2[1])
        board_card(screen, bo, phase)

        #Replacement texte

        screen.blit(texte_adversaire1,(75,25))
        screen.blit(adversaire1_texte,(75,50))
        screen.blit(texte_adversaire2,(550,25))
        screen.blit(adversaire2_texte,(700,50))

        pygame.display.flip()
    pygame.quit()
