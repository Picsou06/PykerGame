import pygame
from pygame import *
import class_JeuDeCartes
import class_EnemyHand
import class_PlayerHand
import class_Cartes
import homescreen
from compte_points import*
from random import*

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


        #Mise
        
        if phase == 0:
            mise = 0
            action_confirme = False #Verification pour voir si les 3 joueurs on pris une descision
            mise_joueur = 0
            mise_adversaire1 = 0
            mise_adversaire2 = 0 
            mise_du_tour = 0
            action_definitive_joueur = False
            action_definitive_adversaire1 = False
            action_definitive_adversaire2 = False
            compteur_check = 0
            while action_confirme == False: #Tant que les 3 joueurs ont pas fait une quelquonque chose permettant de passer à la phase suivante
                
                #Joueur
                
                choix_joueur = False #Action joueur
                joueur_en_lice = 3
                if action_definitive_joueur == False: # Verification pour voir si le joueur a pris une action de type passer (par exemple) ou bien Tapis etc
                    while choix_joueur == False:

                        action = str(input())

                        if action == "p": #Passe
                            print ("Joueur /Passe")
                            joueur_en_lice = joueur_en_lice - 1                          
                            action_definitive_joueur = True
                            choix_joueur = True

                        if action == "c": #Check
                            print ("Joueur /Check")
                            compteur_check = compteur_check + 1
                            choix_joueur = True

                        if action == "s" and mise_du_tour != 0: #Suivre
                            print ("Joueur /Suivre")
                            if mise_du_tour < player_hand.affiche_total_monnaie():
                                mise_joueur = mise_joueur + mise_du_tour
                                choix_joueur = True
                            else:
                                print ("Tapis (fond insufisant pour suivre)")
                                mise_joueur = player_hand.affiche_total_monnaie()
                                choix_joueur = True
                                action_definitive_joueur = True

                        if action == "m" and mise_du_tour == 0: #Mise
                            print ("Joueur /Mise")
                            budget_suffisant = False
                            while budget_suffisant == False:
                                backup = mise_du_tour
                                mise_du_tour = int(input("Combien ?"))
                                while mise_du_tour % 25 != 0:
                                    print ("Incompatible avec les jetons")
                                    mise_du_tour = int(input("Combien ?"))
                                if mise_du_tour + mise_joueur < player_hand.affiche_total_monnaie():
                                    budget_suffisant = True
                                    choix_joueur = True
                                elif mise_du_tour + mise_joueur == player_hand.affiche_total_monnaie():
                                    print ("Tapis !")
                                    action_definitive_joueur = True
                                    choix_joueur = True
                                    budget_suffisant = True
                                elif mise_du_tour + mise_joueur > player_hand.affiche_total_monnaie():
                                    print ("budget insufisant")
                                    mise_du_tour = backup
                            mise_joueur = mise_joueur + mise_du_tour
                            compteur_check = 0

                        if action == "r" and mise_du_tour != 0: #Remise
                            print ("Joueur /Remise")
                            budget_suffisant = False
                            while budget_suffisant == False:
                                backup = mise_du_tour
                                mise_du_tour = int(input("Combien ?"))
                                while mise_du_tour % 25 != 0:
                                    print ("Incompatible avec les jetons")
                                    mise_du_tour = int(input("Combien ?"))
                                if mise_du_tour + mise_joueur < player_hand.affiche_total_monnaie() and mise_du_tour >= backup:
                                    budget_suffisant = True
                                    choix_joueur = True
                                elif mise_du_tour +  mise_joueur == player_hand.affiche_total_monnaie():
                                    print ("Tapis !")
                                    action_definitive_joueur = True
                                    choix_joueur = True
                                    budget_suffisant = True
                                elif mise_du_tour + mise_joueur > player_hand.affiche_total_monnaie():
                                    print ("budget insufisant")
                                    mise_du_tour = backup
                            mise_joueur = mise_joueur + mise_du_tour
                            compteur_check = 0

                        if action == "t": #Tapis (All-in)
                            print ("Joueur /Tapis (all-in)")
                            print ("Tapis !!!")
                            mise_joueur = player_hand.affiche_total_monnaie()
                            mise_du_tour = mise_joueur
                            action_definitive_joueur = True
                            choix_joueur = True 
                            compteur_check = 1

                #Adversaire 1
                if phase == 0:
                    bo_phase = []
                if action_definitive_adversaire1 == False:    
                    choix_adversaire1 = False
                    while choix_adversaire1 == False:
                        if phase == 0:
                            if 29 <= nbr_pts(en1,bo_phase) <= 41 or 46 <= nbr_pts(en1,bo_phase) <= 68:
                                print ("ca marche")
                            else:
                                if nbr_pts(en1,bo_phase) <= 12: #si le jeu fait moins de 12 points
                                    plouf_plouf = randint (1, 10)
                                    if plouf_plouf != 1: #Passe (9 chance sur 10)
                                        print ("Adversaire 1 /Passe")
                                        joueur_en_lice = joueur_en_lice - 1                          
                                        action_definitive_adversaire1 = True
                                        choix_adversaire1 = True
                                    else: # "Bluff" (mise malgrès une main pas folichonne)
                                        if mise_du_tour == 0:
                                            print("Adversaire 1 /mise")
                                            budget_suffisant = False
                                            while budget_suffisant == False:
                                                backup = mise_du_tour
                                                mise_du_tour = randint(25, adversaire1_hand.affiche_total_monnaie() % 10)
                                                while mise_du_tour % 25 != 0:
                                                    print ("Incompatible avec les jetons")
                                                    mise_du_tour = randint(25, adversaire1_hand.affiche_total_monnaie() % 10)
                                                if mise_du_tour + mise_adversaire1 < adversaire1_hand.affiche_total_monnaie():
                                                    budget_suffisant = True
                                                    choix_adversaire1 = True
                                                elif mise_du_tour + mise_adversaire1 == adversaire1_hand.affiche_total_monnaie():
                                                    print ("Tapis !")
                                                    action_definitive_adversaire1 = True
                                                    choix_adversaire1 = True
                                                    budget_suffisant = True
                                                elif mise_du_tour + mise_adversaire1 > adversaire1_hand.affiche_total_monnaie():
                                                    print ("budget insufisant")
                                                    mise_du_tour = backup
                                            mise_adversaire1 = mise_adversaire1 + mise_du_tour
                                            compteur_check = 0
                                        else:
                                            plouf_plouf = randint (1,10)
                                            if plouf_plouf == 1: #L'adversaire 1 remise avec sa main foireuse donc du gros bluff
                                                print ("Adversaire 1 /Remise")
                                                budget_suffisant = False
                                                while budget_suffisant == False:
                                                    backup = mise_du_tour
                                                    mise_du_tour = randint(25, adversaire1_hand.affiche_total_monnaie() % 10)
                                                    while mise_du_tour % 25 != 0:
                                                        print ("Incompatible avec les jetons")
                                                        mise_du_tour = randint(25, adversaire1_hand.affiche_total_monnaie() % 10)
                                                    if mise_du_tour + mise_adversaire1 < adversaire1_hand.affiche_total_monnaie() and mise_du_tour >= backup:
                                                        budget_suffisant = True
                                                        choix_adversaire1 = True
                                                    elif mise_du_tour +  mise_adversaire1 == adversaire1_hand.affiche_total_monnaie():
                                                        print ("Tapis !")
                                                        action_definitive_adversaire1 = True
                                                        choix_adversaire1 = True
                                                        budget_suffisant = True
                                                    elif mise_du_tour + mise_adversaire1 > adversaire1_hand.affiche_total_monnaie():
                                                        print ("budget insufisant")
                                                        mise_du_tour = backup
                                                mise_adversaire1 = mise_adversaire1 + mise_du_tour
                                                compteur_check = 0
                                            else: #L'adversaire 1 suit
                                                print ("Adversaire 1 /Suivre")
                                                if mise_du_tour < adversaire1_hand.affiche_total_monnaie():
                                                    mise_adversaire1 = mise_adversaire1 + mise_du_tour
                                                    choix_adversaire1 = True
                                                else:
                                                    print ("Tapis (fond insufisant pour suivre)")
                                                    mise_adversaire1 = adversaire1_hand.affiche_total_monnaie()
                                                    choix_adversaire1 = True
                                                    action_definitive_adversaire1 = True



            mise = mise_joueur + mise_adversaire1 + mise_adversaire2 #Mise en dehors du reste pour eviter dupli (Jcrois)
            print (mise)

                    

        #Plus mise

    #if phase == 4:

    pygame.quit()
