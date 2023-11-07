import pygame
from pygame import *
import class_JeuDeCartes
import class_EnemyHand
import class_PlayerHand
import lose
from time import sleep
from compte_points import *
from random import *
import win

def board_card(screen, cartes, phase):

    """
    Fonction qui permet d'afficher les cartes au millieu de la table en fonction de la phase de jeu
    Parametre d'entree : Le screen qui est un pygame.display
                         Les cartes qui sont des images
                         Les phase en int qui servent a faire afficher les cartes au fur et a mesure    
    """
    if phase<=5:
        x=-10*1.25
        for i in range(0,phase):
            card=pygame.transform.scale(pygame.image.load(cartes[i].get_image()), (130,200))
            x=x+110*1.25
            if i==0:
                screen.blit(card, (x, 30*1.25))
            elif i==1:
                screen.blit(card, (x, 30*1.25))
            elif i==2:
                screen.blit(card, (x, 30*1.25))
            elif i==3:
                screen.blit(card, (x, 30*1.25))
            elif i==4:
                screen.blit(card, (x, 30*1.25))

def played_card(player, screen, cartes, n):

    """
    Fonction qui permet d'afficher les carte du joueur 
    Paramètres d'entree : Le screen qui est un pygame.display
                          Les cartes qui sont des images
                          Le n en int qui permet de selectionner la carte

    """

    #print("Debug, affichage cartes tournée")
    card=pygame.transform.scale(pygame.image.load(cartes.get_image()), (130,200))
    if n==0:
        screen.blit(card, (screen.get_width()/2-135, screen.get_height()-200))
    elif n==1:
        screen.blit(card, (screen.get_width()/2+5, screen.get_height()-200))

# def affichage_enemy_card():

def affichermessage(screen, message):
    """
    Fonction qui permet d'afficher le message au centre
    Parametre d'entre : Le screen qui est un pygame.display
                        Le message (str) à afficher
    """
    TextPolice = pygame.font.SysFont("bold",25)
    texteInfo = TextPolice.render(message, 1 ,(150,0,0))
    screen.blit(texteInfo,(270*1.25,300*1.25))


def choix_adversaire(adversaire,phase,score,lbet,player_action):
    """
    Fonction qui permet a l'adversaire de faire un choix ( sacrément utile)
    """
    #print("Debug, choix adversaire")
    if player_action=="All-In":
        if score>=82:
            return "Suivre"
        elif score >= 64:
            plouf_plouf = randint(1,5)
            if plouf_plouf == 1:
                return "Suivre"
        else:
            return "Coucher"
    if 25 <= score <= 40:
        plouf_plouf = randint(1,5)
        if plouf_plouf != 1:
            return "Suivre"  # Si le score correspond à une paire basse, le bot suit
        else:
            return ("Bet",randint(20,score)*5)
    elif score < 8:
        plouf_plouf = randint (1,10)
        if plouf_plouf == 1 or plouf_plouf == 2 or plouf_plouf == 3 or plouf_plouf == 4:
            return ("Bet",randint(10,score)*5)
        elif plouf_plouf == 5 or plouf_plouf == 6 or plouf_plouf == 7 or plouf_plouf == 8:
            return "Suivre"
        else:
            return "Coucher"
    elif 50 <= score <= 80:
        plouf_plouf = randint (1,10)
        if plouf_plouf <= 5:
            return ("Bet",randint(5,score)*5)  # Si le score correspond à un brelan, le bot mise
        else:
            if lbet >= 600:
                plouf_plouf = (1,4)
                if plouf_plouf != 1:
                    return "Suivre"
                else:
                    return "Coucher"
            else:
                return "Suivre"
    elif score > 500:
        plouf_plouf = randint (1,10)
        if plouf_plouf == 1 or plouf_plouf == 2 or plouf_plouf == 3 or plouf_plouf == 4:
            return "All-In"  # Si le score est très élevé, le bot fait tapis
        else:
            return ("Bet",randint(75,score)*5)
    else:
        return "Suivre"

def game(screen):
    #print("Debug, Game")
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
    board=[pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte()]
    player_en_lice={"Player":True,"Adversaire1":True,"Adversaire2":True}

    running = True
    phase=0
    messageinformation=None
    action_joueur=None
    
    mise=50
    bet=50
    lbet=50
    has_select=False
    #print("Debug, Fin Variable définitives")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2+200 <= mouse[0] <= width/2+340 and height-195 <= mouse[1] <= height-195+40:
                    if not has_select:
                        action_joueur="Bet"
                        has_select=True
                        #print("Debug, bet")

                elif width/2+200 <= mouse[0] <= width/2+340 and height-145 <= mouse[1] <= height-145+40:
                    if not has_select:
                        action_joueur="Coucher"
                        has_select=True
                        #print("Debug, Coucher")

                elif width/2+200 <= mouse[0] <= width/2+340 and height-95 <= mouse[1] <= height-95+40:
                    if not has_select:
                        action_joueur="Suivre"
                        has_select=True
                        #print("Debug, Suivre")

                elif width/2+45 <= mouse[0] <= width/2+340 and height-45 <= mouse[1] <= height-45+40:
                    if not has_select:
                        action_joueur="All-In"
                        has_select=True
                        #print("Debug, All-in")

                elif 147 <= mouse[0] <= 147+46 and 480 <= mouse[1] <= 480+46:
                    if bet<player_hand.get_monnaie():
                        bet=bet+5
                        #print("Debug, bet+5")
                elif 55 <= mouse[0] <= 55+46 and 480 <= mouse[1] <= 480+46:
                    if bet>lbet:
                        bet=bet-5
                        #print("Debug, bet-5")

        mouse = pygame.mouse.get_pos()
        screen.blit(background_image, (0, 0))
        if adversaire2_hand.get_ingame():
            screen.blit(enemycard, (700*1.25, 10*1.25))
            screen.blit(enemycard, (700*1.25, 60*1.25))
        if adversaire1_hand.get_ingame():
            screen.blit(pygame.transform.rotate(enemycard,90), (-150, 60*1.50))
            screen.blit(pygame.transform.rotate(enemycard,90), (-150, 10*1.50))

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
        textebet = TextPolice.render("Bet", 1 ,(0,0,0))
        texte_all_in = TextPolice.render("All-in",1,(0,0,0))
        textesuivre = TextPolice.render("Suivre / Call",1,(0,0,0))



        played_card(player_hand, screen, player_hand.get_cartes()[0], 0)
        played_card(player_hand, screen, player_hand.get_cartes()[1], 1)
        board_card(screen, board, phase)
        affichermessage(screen, messageinformation)

        #Replacement texte

        #print("Debug, affichage textes")
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-195,140,40]) #Coucher
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-145,140,40]) #Attendre
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-95,140,40]) #Relancer
        pygame.draw.rect(screen,(217,217,217),[width/2+200,height-45,140,40]) #Suivre
        pygame.draw.rect(screen,(240,0,32),[55,480,46,46]) #Bet+
        pygame.draw.rect(screen,(0,128,255),[147,480,46,46]) #Bet-
        pygame.draw.rect(screen,(255,255,255),[101,480,46,46]) #Bet level
        screen.blit(texte_adversaire1,(75*1.25,10*1.25))
        screen.blit(texte_adversaire2,(700*1.25,25*1.25))
        screen.blit(texte_player,(width/2+200,height-220))
        screen.blit(textecoucher,(width/2+200+10,height-195+10))
        screen.blit(textebet,(width/2+200,height-145))
        screen.blit(textesuivre,(width/2+200,height-95))
        screen.blit(texte_all_in,(width/2+200,height-45))
        screen.blit(textemonnaie,(105*1.25,490*1.25))
        screen.blit(textmise,(370*1.25,240*1.25))
        screen.blit(texteremove,(72*1.25,490*1.25))
        screen.blit(texteadd,(165*1.25,490*1.25))
        #print("Debug, fin affichage textes")


        if phase>=6:
            sleep(3)
            #print("Debug, Phase 6 passé!")
            #Determiner qui gagne le tour
            print(player_en_lice)
            if player_en_lice["Player"] == True: #Pour verif si il est toujours en lice (c con de faire gagner qqn qui s'est couché)
                male_alpha=[player_hand]
                male_alpha_score = nbr_pts(player_hand.get_cartes(), board)
            else:
                male_alpha=None
                male_alpha_score=0

            #Verif Adversaire 1 win
            if player_en_lice["Adversaire1"] == True: #Pour verif si il est toujours en lice (c con de faire gagner qqn qui s'est couché)
                constestants_1 = nbr_pts(adversaire1_hand.get_cartes(), board)
            else:
                constestants_1 = 0
            if constestants_1 > male_alpha_score:
                male_alpha = [adversaire1_hand]
                male_alpha_score = constestants_1
            if constestants_1 == male_alpha_score:
                male_alpha.append(adversaire1_hand)
                male_alpha_score = constestants_1

            #Verif Adversaire 2 win
            if player_en_lice["Adversaire2"] == True: #Pour verif si il est toujours en lice (c con de faire gagner qqn qui s'est couché)
                constestants_2 = nbr_pts(adversaire2_hand.get_cartes(), board)
            else:
                constestants_2 = 0
            if constestants_2 > male_alpha_score:
                male_alpha = [adversaire2_hand]
                male_alpha_score = constestants_2
            if constestants_2 == male_alpha_score:
                male_alpha.append(adversaire2_hand)
                male_alpha_score = constestants_1

            
            print("mise",mise)
            print("Player",player_hand.get_monnaie(),nbr_pts(player_hand.get_cartes(), board))
            print("Adversaire1",adversaire1_hand.get_monnaie(),constestants_1)
            print("Adversaire2",adversaire2_hand.get_monnaie(),constestants_2)
            mise=int(mise/len(male_alpha))
            if male_alpha!=None:
                for i in male_alpha:
                    i.set_monnaie(i.get_monnaie()+mise)
            if player_hand.get_monnaie()<=0:
                lose.lose(screen)
            if adversaire1_hand.get_monnaie()<=0 and adversaire2_hand.get_monnaie()<=0:
                win.win(screen)
            #print("Debug, Update Monnaie!")
            phase=0
            action_joueur=None
            mise=50
            bet=50
            messageinformation=None
            has_select=False
            pioche.creer_jeu_52_cartes()
            pioche.melange()
            player_hand.set_ingame(True)
            adversaire1_hand.set_ingame(True)
            adversaire2_hand.set_ingame(True)
            background_image = pygame.transform.scale(pygame.image.load("images/table.png"), (width,height))
            enemycard = pygame.transform.scale(pygame.image.load("images/cartes/test.png"), (200,300))
            pl_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            player_hand.set_cartes(pl_card)
            enemy1_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            adversaire1_hand.set_cartes(enemy1_card)
            enemy2_card=[pioche.pioche_carte(),pioche.pioche_carte()]
            adversaire2_hand.set_cartes(enemy2_card)
            board=[pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte(),pioche.pioche_carte()]
            #print("Debug, Update Variable!")
            player_en_lice={"Player":True,"Adversaire1":True,"Adversaire2":True}
            if adversaire1_hand.get_monnaie() == 0:
                adversaire1_hand.set_ingame(False)
                player_en_lice["Adversaire1"] = False
            if adversaire2_hand.get_monnaie() == 0:
                adversaire2_hand.set_ingame(False)
                player_en_lice["Adversaire2"] = False

        if phase==5:
            phase=6
        if player_hand.get_ingame()==False:
            has_select=True
            action_joueur=None
        if has_select:
            if phase !=6:
                if action_joueur=="Bet" or action_joueur=="Suivre":
                    temp = True
                    if lbet >= player_hand.get_monnaie():
                        action_joueur = "All-In"
                        temp = False
                    if temp == True:
                        player_hand.set_monnaie(player_hand.get_monnaie()-bet)
                        mise=mise+bet
                        lbet=bet
                        action_joueur=None
                        has_select=False
                        #print("Debug, Bet, Suivre 2")     

                if action_joueur=="All-In":
                    mise=player_hand.get_monnaie()
                    bet=player_hand.get_monnaie()
                    lbet=player_hand.get_monnaie()
                    player_hand.set_monnaie(0)
                    action_joueur=None
                    #print("Debug, All-In 2")

                if action_joueur=="Coucher":
                    player_hand.set_ingame(False)
                    action_joueur=None
                    has_select=False
                    player_en_lice["Player"] = False
                    #print("Debug, Coucher 2")

            board_temp_card=[] #Liste permettant à l'IA de ne pas tricher
            #print("Debug, List Temp Card avant")
            if phase<=5:
                for i in range(0,phase): #Procédé permettant à l'IA de voir les meme cartes que nous
                    board_temp_card.append(board[i])
            #print("Debug, Liste Temp Card après")
            botChoise=0
            while botChoise < 2:
                action_adversaire1="Waiting"
                action_adversaire2="Waiting"
                messageinformation="Adversaire 1 Absent"
                if adversaire1_hand.get_ingame() and action_adversaire1!=None:
                    action_adversaire1=choix_adversaire(adversaire1_hand,phase,nbr_pts(adversaire1_hand.get_cartes(),board),mise, action_joueur)
                    
                if adversaire1_hand.get_ingame():
                    if action_adversaire1==None:
                        botChoise=botChoise+1
                    if action_adversaire2==None:
                        botChoise=botChoise+1

                    if action_adversaire1=="Suivre": #Adversaire 1
                        if adversaire1_hand.get_monnaie()<=lbet:
                            action_adversaire1="All-In"
                        else:
                            mise=mise+lbet
                            adversaire1_hand.set_monnaie(adversaire1_hand.get_monnaie()-lbet)
                            botChoise=botChoise+1
                            messageinformation="Adversaire 1 suis"
                        
                        
                    elif type(action_adversaire1)==tuple: #Adversaire 1
                        if adversaire1_hand.get_monnaie()<=lbet+action_adversaire1[1]:
                            action_adversaire1="All-In"
                        else:
                            messageinformation=f"Adversaire 1 bet de {lbet+action_adversaire1[1]}"
                            adversaire1_hand.set_monnaie(adversaire1_hand.get_monnaie()-(lbet+action_adversaire1[1]))
                            mise=mise+lbet+action_adversaire1[1]
                            bet=lbet+action_adversaire1[1]
                            lbet=bet
                            botChoise=botChoise+1

                    elif action_adversaire1=="All-In": #Adversaire 1
                        messageinformation="Adversaire 1 All-In"
                        action_adversaire1=None
                        mise=mise+adversaire1_hand.get_monnaie()
                        if adversaire1_hand.get_monnaie() > lbet:
                            bet=adversaire1_hand.get_monnaie()
                            lbet=adversaire1_hand.get_monnaie()
                        adversaire1_hand.set_monnaie(0)
                        botChoise=botChoise+1

                    elif action_adversaire1=="Coucher": #Adversaire 1
                        messageinformation="Adversaire 1 se couche"
                        botChoise=botChoise+1
                        action_adversaire1==None
                        adversaire1_hand.set_ingame(False)
                        player_en_lice["Adversaire1"]=False
                else:
                    botChoise=botChoise+1
                    messageinformation="Adversaire 1 Absent"
                if adversaire2_hand.get_ingame() and not action_adversaire2==None:
                        action_adversaire2=choix_adversaire(adversaire2_hand,phase,nbr_pts(adversaire2_hand.get_cartes(),board),mise, action_joueur)
                if adversaire2_hand.get_ingame():
                    if action_adversaire2=="Suivre":
                        if adversaire2_hand.get_monnaie()<=lbet:
                            action_adversaire2="All-In"
                        else:
                            mise=mise+lbet
                            adversaire2_hand.set_monnaie(adversaire2_hand.get_monnaie()-lbet)
                            messageinformation=messageinformation+" | Adversaire 2 suis"
                        botChoise=botChoise+1
                        

                    if type(action_adversaire2)==tuple: #Adversaire 2
                        if adversaire2_hand.get_monnaie()<=lbet+action_adversaire2[1]:
                            action_adversaire2="All-In"
                        else:
                            messageinformation=messageinformation+" | "+f"Adversaire 2 bet de {lbet+action_adversaire2[1]}"
                            adversaire2_hand.set_monnaie(adversaire2_hand.get_monnaie()-(lbet+action_adversaire2[1]))
                            mise=mise+lbet+action_adversaire2[1]
                            bet=lbet+action_adversaire2[1]
                            lbet=bet
                            botChoise=botChoise+1

                    if action_adversaire2=="All-In": #Adversaire 2
                        messageinformation=messageinformation+" | Adversaire 2 All-In"
                        action_adversaire2=None
                        mise=mise+adversaire2_hand.get_monnaie()
                        if adversaire2_hand.get_monnaie() > lbet:
                            bet=adversaire2_hand.get_monnaie()
                            lbet=adversaire2_hand.get_monnaie()
                        adversaire2_hand.set_monnaie(0)
                        botChoise=botChoise+1
                
                    if action_adversaire2=="Coucher": #Adversaire 2
                        messageinformation=messageinformation+" | Adversaire 2 se couche"
                        affichermessage(screen, messageinformation)
                        botChoise=botChoise+1
                        adversaire2_hand.set_ingame(False)  
                        player_en_lice["Adversaire2"]=False
                else:
                    botChoise=botChoise+1
                    messageinformation=messageinformation+" | Adversaire 2 Absent"
            if player_en_lice["Player"]==True and player_en_lice["Adversaire1"]==False and player_en_lice["Adversaire2"]==False:
                phase=6
            if player_en_lice["Player"]==False and player_en_lice["Adversaire1"]==True and player_en_lice["Adversaire2"]==False:
                phase=6
            if player_en_lice["Player"]==False and player_en_lice["Adversaire1"]==False and player_en_lice["Adversaire2"]==True:
                phase=6

            phase=phase+1

        pygame.display.flip()