import pygame
from pygame import *
import class_JeuDeCartes
import class_EnemyHand
import class_PlayerHand
import lose
from time import sleep
from compte_points import *
from random import *

def board_card(screen, cartes, phase):
    print("Debug, affichage cartes table")
    if phase<=4:
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
    print("Debug, affichage cartes tournée")
    card=pygame.transform.scale(pygame.image.load(cartes.get_image()), (130,200))
    if n==0:
        screen.blit(card, (250, 400))
    elif n==1:
        screen.blit(card, (400, 400))

# def affichage_enemy_card():


def choix_adversaire(adversaire,phase,score,mise,canchoise):
    print("Debug, choix adversaire")
    if phase==0:
        return "Coucher"
    if 29 <= score <= 41:
        return "Suivre"  # Si le score correspond à une paire basse, le bot suit
    elif score < 20:
        plouf_plouf = randint (1,10)
        if plouf_plouf == 1 or plouf_plouf == 2 or plouf_plouf == 3:
            return "Coucher"
        else:
            return "Bet",randint(mise+10,mise+100)
    elif 70 <= score <= 82:
        return ("Bet",randint(mise+10,adversaire.get_monnaie()))  # Si le score correspond à un brelan, le bot mise
    elif score > 500:
        return "All-In"  # Si le score est très élevé, le bot fait tapis
    else:
        if canchoise:
            return "Check"
        else:
            return "Suivre"

def game(screen):
    print("Debug, Game")
    width,height = screen.get_width(),screen.get_height()
    monnaie = randint(200, 1000)*5
    adversaire1_hand=class_EnemyHand.EnemyHand(monnaie)
    adversaire2_hand=class_EnemyHand.EnemyHand(monnaie)
    player_hand=class_PlayerHand.PlayerHand(monnaie)
    pioche=class_JeuDeCartes.JeuDeCartes()
    pioche.creer_jeu_52_cartes()
    pioche.melange()
    background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (width,height))
    enemycard = pygame.transform.scale(pygame.image.load("images/cartes/test.png"), (200,300))
    pl_card=[pioche.pioche_carte(),pioche.pioche_carte()]
    player_hand.set_cartes(pl_card)
    enemy1_card=[pioche.pioche_carte(),pioche.pioche_carte()]
    adversaire1_hand.set_cartes(enemy1_card)
    enemy2_card=[pioche.pioche_carte(),pioche.pioche_carte()]
    adversaire2_hand.set_cartes(enemy2_card)
    board=[pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte()]
    player_en_lice={"Player":True,"Adversaire1":True,"Adversaire2":True}

    running = True
    phase=0
    action_joueur=None
    player_en_liste=True
    
    mise=50
    bet=50
    lbet=50
    has_select=False
    print("Debug, Fin Variable définitives")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2+200 <= mouse[0] <= width/2+340 and height-195 <= mouse[1] <= height-195+40:
                    if not has_select:
                        action_joueur="Check"
                        has_select=True
                        print("Debug, Check")

                elif width/2+200 <= mouse[0] <= width/2+340 and height-145 <= mouse[1] <= height-145+40:
                    if not has_select:
                        action_joueur="Coucher"
                        has_select=True
                        print("Debug, Coucher")

                elif width/2+200 <= mouse[0] <= width/2+340 and height-95 <= mouse[1] <= height-95+40:
                    if not has_select:
                        action_joueur="Suivre"
                        has_select=True
                        print("Debug, Suivre")

                elif width/2+45 <= mouse[0] <= width/2+340 and height-45 <= mouse[1] <= height-45+40:
                    if not has_select:
                        action_joueur="All-In"
                        has_select=True
                        print("Debug, All-in")

                elif 55 <= mouse[0] <= 55+340 and height-120 <= mouse[1] <= height-120+40:
                    if not has_select:
                        action_joueur="Bet"
                        has_select=True
                        print("Debug, bet")

                elif 147 <= mouse[0] <= 147+46 and height-176 <= mouse[1] <= height-176+46:
                    if bet<player_hand.get_monnaie():
                        bet=bet+5
                        print("Debug, bet+5")
                elif 55 <= mouse[0] <= 55+46 and height-176 <= mouse[1] <= height-176+46:
                    if bet>lbet:
                        bet=bet-5
                        print("Debug, bet-5")

        mouse = pygame.mouse.get_pos()
        screen.blit(background_image, (0, 0))
        if adversaire1_hand.get_ingame:
            screen.blit(enemycard, (700, 10))
            screen.blit(enemycard, (700, 60))
        if adversaire2_hand.get_ingame:
            screen.blit(pygame.transform.rotate(enemycard,90), (-150, 60))
            screen.blit(pygame.transform.rotate(enemycard,90), (-150, 10))

        #Affichage differents textes (scores)

        #Mise en place des variables

        TextPolice = pygame.font.SysFont("bold",25)

        #Pour le Joueur

        texte_player = TextPolice.render("$"+str(player_hand.get_monnaie()), 1 ,(150,0,0)) #Le (150,0,0) est la couleur du texte en RGB, pareil pour les suivants

        #Pour l'Adversaire 1

        texte_adversaire1 = TextPolice.render("$"+str(adversaire1_hand.get_monnaie()), 1 ,(150,0,0))

        #Pour l'adversaire 2

        texte_adversaire2 = TextPolice.render("$"+str(adversaire2_hand.get_monnaie()), 1 ,(150,0,0))


        # Placement
                #Actions
        texteadd = TextPolice.render("+", 1 ,(0,0,0))
        textmise = TextPolice.render("$"+str(mise), 1 ,(0,0,0))
        textemonnaie = TextPolice.render(str(bet), 1, (0,0,0))
        texteremove = TextPolice.render("-", 1 ,(0,0,0))
        textecoucher = TextPolice.render("Coucher / Fold", 1 ,(0,0,0))    
        textecheck = TextPolice.render("Check / Check", 1 ,(0,0,0))
        textebet = TextPolice.render("Bet", 1 ,(0,0,0))  
        texte_all_in = TextPolice.render("All-in",1,(0,0,0))
        textesuivre = TextPolice.render("Suivre / Call",1,(0,0,0))



        played_card(player_hand, screen, player_hand.get_cartes()[0], 0)
        played_card(player_hand, screen, player_hand.get_cartes()[1], 1)
        board_card(screen, board, phase)

        #Replacement texte

        print("Debug, affichage textes")
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-195,140,40]) #Coucher
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-145,140,40]) #Attendre
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-95,140,40]) #Relancer
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-45,140,40]) #Suivre
        pygame.draw.rect(screen,(217,217,217),[55,height-120,140,40]) #Bet
        pygame.draw.rect(screen,(240,0,32),[55,height-176,46,46]) #Bet+
        pygame.draw.rect(screen,(0,128,255),[147,height-176,46,46]) #Bet-
        pygame.draw.rect(screen,(255,255,255),[101,height-176,46,46]) #Monnaie
        screen.blit(texte_adversaire1,(75,10))
        screen.blit(texte_adversaire2,(700,25))
        screen.blit(texte_player,(370,height-220))
        screen.blit(textecoucher,(605,465))        
        screen.blit(textecheck,(612,415))
        screen.blit(textebet,(110,490))
        screen.blit(textesuivre,(617,515))
        screen.blit(texte_all_in,(645,565))
        screen.blit(textemonnaie,(105,440))
        screen.blit(textmise,(370,240))
        screen.blit(texteremove,(72,440))
        screen.blit(texteadd,(165,440))
        print("Debug, fin affichage textes")


        if phase>=5:
            sleep(2)
            print("Debug, Phase 4 passé!")
            #Determiner qui gagne le tour

            #Pour verif si il est toujours en lice (c con de faire gagner qqn qui s'est couché)
            male_alpha=player_hand
            male_alpha_score = nbr_pts(player_hand.get_cartes(), board)
            constestants_1 = nbr_pts(adversaire1_hand.get_cartes(), board)
            if constestants_1 > male_alpha_score:
                male_alpha = adversaire1_hand
                male_alpha_score = constestants_1
            constestant_2 = nbr_pts(adversaire2_hand.get_cartes(), board)
            if constestant_2 > male_alpha_score:
                male_alpha = adversaire2_hand
                male_alpha_score = constestant_2
            male_alpha.set_monnaie(male_alpha.get_monnaie() + mise)
            if player_hand.get_monnaie()<=0:
                lose.lose(screen)
            print("Debug, Update Monnaie!")
            phase=0
            action_joueur=None
            mise=50
            bet=50
            has_select=False
            pioche.creer_jeu_52_cartes()
            pioche.melange()
            background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (width,height))
            enemycard = pygame.transform.scale(pygame.image.load("images/cartes/test.png"), (200,300))
            pl_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            player_hand.set_cartes(pl_card)
            enemy1_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            adversaire1_hand.set_cartes(enemy1_card)
            enemy2_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            adversaire2_hand.set_cartes(enemy2_card)
            board=[pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte()]
            print("Debug, Update Variable!")
            player_en_lice={"Player":True,"Adversaire1":True,"Adversaire2":True}

        notcheck=False
        checkpass=False
        choisewithoutcheck={"Player":True,"Adversaire1":False,"Adversaire2":False} #Verification très peu optimisé pour Check
        if has_select:
            while not checkpass:
                checkcounter=0
                if action_joueur=="All-In":
                    mise=player_hand.get_monnaie()
                    player_hand.set_monnaie(0)
                    action_joueur=None
                    choisewithoutcheck["Player"]=True
                    print("Debug, All-In 2")

                if action_joueur=="Bet" or action_joueur=="Suivre":
                    player_hand.set_monnaie(player_hand.get_monnaie()-bet)
                    mise=mise+bet
                    lbet=bet
                    action_joueur=None
                    has_select=False
                    choisewithoutcheck["Player"]=True
                    print("Debug, Bet, Suivre 2")

                if action_joueur=="Coucher":
                    player_hand.set_ingame(False)
                    action_joueur=None
                    has_select=False
                    choisewithoutcheck["Player"]=True
                    player_en_lice["Player"]= False
                    print("Debug, Coucher 2")

                if action_joueur=="Check":
                    action_joueur=None
                    has_select=False
                    choisewithoutcheck["Player"]=False
                    print("Debug, Check 2")

                board_temp_card=[] #Liste permettant à l'IA de ne pas tricher
                print("Debug, List Temp Card avant")
                if phase<=4:
                    for i in range(0,phase): #Procédé permettant à l'IA de voir les meme cartes que nous
                        board_temp_card.append(board[i])
                print(board_temp_card)
                print("Debug, Liste Temp Card après")
                print(nbr_pts(adversaire1_hand.get_cartes(),board))
                botChoise=0
                while botChoise < 2:
                    if not notcheck:
                        if adversaire1_hand.get_ingame():
                            action_adversaire1=choix_adversaire(adversaire1_hand,phase,nbr_pts(adversaire1_hand.get_cartes(),board),mise, True)
                        if adversaire2_hand.get_ingame():
                            action_adversaire1=choix_adversaire(adversaire1_hand,phase,nbr_pts(adversaire1_hand.get_cartes(),board),mise, True)
                    if adversaire1_hand.get_ingame():
                        if action_adversaire1=="Suivre": #Adversaire 1
                            adversaire1_hand.set_monnaie(adversaire1_hand.get_monnaie()-lbet)
                            mise=mise+lbet
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire1"]=True
                        if type(action_adversaire1)==tuple(): #Adversaire 1
                            adversaire1_hand.set_monnaie(adversaire1_hand.get_monnaie()-action_adversaire1(1))
                            mise=mise+action_adversaire1(1)
                            bet=action_adversaire1(1)
                            lbet=action_adversaire1(1)
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire1"]=True
                        if action_adversaire1=="Check": #Adversaire 1
                            checkcounter=checkcounter+1
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire1"]=True
                        if action_adversaire1=="All-In": #Adversaire 1
                            mise=mise+adversaire1_hand.get_monnaie()
                            adversaire1_hand.set_monnaie(0)
                            bet=adversaire1_hand.get_monnaie()
                            lbet=adversaire1_hand.get_monnaie()
                            choisewithoutcheck["Adversaire1"]=True
                            botChoise=botChoise+1
                        if action_adversaire1=="Coucher": #Adversaire 1
                            botChoise=botChoise+1
                            adversaire1_hand.set_ingame(False)
                            player_en_lice["Adversaire1"]= False
                            choisewithoutcheck["Adversaire2"]=True
                    else:
                        botChoise=botChoise+1
                    if adversaire2_hand.get_ingame():
                        if action_adversaire2=="Suivre": #Adversaire 2
                            adversaire2_hand.set_monnaie(adversaire2_hand.get_monnaie()-lbet)
                            mise=mise+lbet
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire2"]=True
                        if type(action_adversaire1)==tuple(): #Adversaire 2
                            adversaire2_hand.set_monnaie(adversaire2_hand.get_monnaie()-action_adversaire2(1))
                            mise=mise+action_adversaire2(1)
                            bet=action_adversaire2(1)
                            lbet=action_adversaire2(1)
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire2"]=True
                        if action_adversaire2=="Check": #Adversaire 2
                            checkcounter=checkcounter+1
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire2"]=True
                        if action_adversaire2=="All-In": #Adversaire 2
                            mise=mise+adversaire2_hand.get_monnaie()
                            adversaire2_hand.set_monnaie(0)
                            bet=adversaire2_hand.get_monnaie()
                            lbet=adversaire2_hand.get_monnaie()
                            botChoise=botChoise+1
                            choisewithoutcheck["Adversaire2"]=True
                        if action_adversaire2=="Coucher": #Adversaire 2
                            botChoise=botChoise+1
                            adversaire2_hand.set_ingame(False)
                            choisewithoutcheck["Adversaire2"]=True      
                            player_en_lice["Adversaire2"]=False                              
                    else:
                        botChoise=botChoise+1
                    if botChoise<2:
                        print("Error,",action_adversaire1,action_adversaire2)
                    if checkcounter==3:
                        checkpass=True
                    if choisewithoutcheck["Player"]==True and choisewithoutcheck["Adversaire1"]==True and choisewithoutcheck["Adversaire2"]==True:
                        checkpass=True
                    else:
                        notcheck=True
                        action_adversaire1=choix_adversaire(adversaire1_hand,phase,nbr_pts(adversaire1_hand.get_cartes(),board),mise, False)
                        action_adversaire2=choix_adversaire(adversaire2_hand,phase,nbr_pts(adversaire1_hand.get_cartes(),board),mise, False)
                        checkcounter=checkcounter-2
            if player_en_lice["Player"]==True and player_en_lice["Adversaire1"]==False and player_en_lice["Adversaire2"]==False:
                phase=5
                player_hand.set_monnaie(player_hand.get_monnaie()+mise)
                mise=0
                    
                    

                print("Adversaire 1:",action_adversaire1)
                print("Adversaire 2:",action_adversaire2)
                phase=phase+1

        pygame.display.flip()
