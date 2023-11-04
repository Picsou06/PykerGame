# Finallement un Protype....

# #Mise

#         if phase == 0:
#             mise = 0
#             action_confirme = False #Verification pour voir si les 3 joueurs on pris une descision
#             mise_joueur = 0
#             mise_adversaire1 = 0
#             mise_adversaire2 = 0 
#             mise_du_tour = 0
#             action_definitive_joueur = False
#             action_definitive_adversaire1 = False
#             action_definitive_adversaire2 = False
#             compteur_check = 0
            
#             while action_confirme == False: #Tant que les 3 joueurs ont pas fait une quelquonque chose permettant de passer à la phase suivante
                
#                 #Joueur
                
#                 choix_joueur = False #Action joueur
#                 joueur_en_lice = 3
#                 if action_definitive_joueur == False: # Verification pour voir si le joueur a pris une action de type passer (par exemple) ou bien Tapis etc
#                     while choix_joueur == False:

#                         action = str(input())

#                         if action == "p": #Passe
#                             print ("Joueur /Passe")
#                             joueur_en_lice = joueur_en_lice - 1                          
#                             action_definitive_joueur = True
#                             choix_joueur = True

#                         if action == "c": #Check
#                             print ("Joueur /Check")
#                             compteur_check = compteur_check + 1
#                             choix_joueur = True

#                         if action == "s" and mise_du_tour != 0: #Suivre
#                             print ("Joueur /Suivre")
#                             if mise_du_tour < player_hand.get_monnaie():
#                                 mise_joueur = mise_joueur + mise_du_tour
#                                 choix_joueur = True
#                             else:
#                                 print ("Tapis (fond insufisant pour suivre)")
#                                 mise_joueur = player_hand.get_monnaie()
#                                 choix_joueur = True
#                                 action_definitive_joueur = True

#                         if action == "m" and mise_du_tour == 0: #Mise
#                             print ("Joueur /Mise")
#                             budget_suffisant = False
#                             while budget_suffisant == False:
#                                 backup = mise_du_tour
#                                 mise_du_tour = int(input("Combien ?"))
#                                 while mise_du_tour % 25 != 0:
#                                     print ("Incompatible avec les jetons")
#                                     mise_du_tour = int(input("Combien ?"))
#                                 if mise_du_tour + mise_joueur < player_hand.get_monnaie():
#                                     budget_suffisant = True
#                                     choix_joueur = True
#                                 elif mise_du_tour + mise_joueur == player_hand.get_monnaie():
#                                     print ("Tapis !")
#                                     action_definitive_joueur = True
#                                     choix_joueur = True
#                                     budget_suffisant = True
#                                 elif mise_du_tour + mise_joueur > player_hand.get_monnaie():
#                                     print ("budget insufisant")
#                                     mise_du_tour = backup
#                             mise_joueur = mise_joueur + mise_du_tour
#                             compteur_check = 0

#                         if action == "r" and mise_du_tour != 0: #Remise
#                             print ("Joueur /Remise")
#                             budget_suffisant = False
#                             while budget_suffisant == False:
#                                 backup = mise_du_tour
#                                 mise_du_tour = int(input("Combien ?"))
#                                 while mise_du_tour % 25 != 0:
#                                     print ("Incompatible avec les jetons")
#                                     mise_du_tour = int(input("Combien ?"))
#                                 if mise_du_tour + mise_joueur < player_hand.get_monnaie() and mise_du_tour >= backup:
#                                     budget_suffisant = True
#                                     choix_joueur = True
#                                 elif mise_du_tour +  mise_joueur == player_hand.get_monnaie():
#                                     print ("Tapis !")
#                                     action_definitive_joueur = True
#                                     choix_joueur = True
#                                     budget_suffisant = True
#                                 elif mise_du_tour + mise_joueur > player_hand.get_monnaie():
#                                     print ("budget insufisant")
#                                     mise_du_tour = backup
#                             mise_joueur = mise_joueur + mise_du_tour
#                             compteur_check = 0

#                         if action == "t": #Tapis (All-in)
#                             print ("Joueur /Tapis (all-in)")
#                             print ("Tapis !!!")
#                             mise_joueur = player_hand.get_monnaie()
#                             mise_du_tour = mise_joueur
#                             action_definitive_joueur = True
#                             choix_joueur = True 
#                             compteur_check = 1

#                 #Adversaire 1
#                 if phase == 0:
#                     bo_phase = []
#                 if action_definitive_adversaire1 == False:    
#                     choix_adversaire1 = False
#                     while choix_adversaire1 == False:
#                         if phase == 0:
#                             if 29 <= nbr_pts(en1,bo_phase) <= 41 or 46 <= nbr_pts(en1,bo_phase) <= 68:
#                                 print ("ca marche")
#                             else:
#                                 if nbr_pts(en1,bo_phase) <= 12: #si le jeu fait moins de 12 points
#                                     plouf_plouf = randint (1, 10)
#                                     if plouf_plouf != 1: #Passe (9 chance sur 10)
#                                         print ("Adversaire 1 /Passe")
#                                         joueur_en_lice = joueur_en_lice - 1                          
#                                         action_definitive_adversaire1 = True
#                                         choix_adversaire1 = True
#                                     else: # "Bluff" (mise malgrès une main pas folichonne)
#                                         if mise_du_tour == 0:
#                                             print("Adversaire 1 /mise")
#                                             budget_suffisant = False
#                                             while budget_suffisant == False:
#                                                 backup = mise_du_tour
#                                                 mise_du_tour = randint(25, adversaire1_hand.get_monnaie() % 10)
#                                                 while mise_du_tour % 25 != 0:
#                                                     print ("Incompatible avec les jetons")
#                                                     mise_du_tour = randint(25, adversaire1_hand.get_monnaie() % 10)
#                                                 if mise_du_tour + mise_adversaire1 < adversaire1_hand.get_monnaie():
#                                                     budget_suffisant = True
#                                                     choix_adversaire1 = True
#                                                 elif mise_du_tour + mise_adversaire1 == adversaire1_hand.get_monnaie():
#                                                     print ("Tapis !")
#                                                     action_definitive_adversaire1 = True
#                                                     choix_adversaire1 = True
#                                                     budget_suffisant = True
#                                                 elif mise_du_tour + mise_adversaire1 > adversaire1_hand.get_monnaie():
#                                                     print ("budget insufisant")
#                                                     mise_du_tour = backup
#                                             mise_adversaire1 = mise_adversaire1 + mise_du_tour
#                                             compteur_check = 0
#                                         else:
#                                             plouf_plouf = randint (1,10)
#                                             if plouf_plouf == 1: #L'adversaire 1 remise avec sa main foireuse donc du gros bluff
#                                                 print ("Adversaire 1 /Remise")
#                                                 budget_suffisant = False
#                                                 while budget_suffisant == False:
#                                                     backup = mise_du_tour
#                                                     mise_du_tour = randint(25, adversaire1_hand.get_monnaie() % 10)
#                                                     while mise_du_tour % 25 != 0:
#                                                         print ("Incompatible avec les jetons")
#                                                         mise_du_tour = randint(25, adversaire1_hand.get_monnaie() % 10)
#                                                     if mise_du_tour + mise_adversaire1 < adversaire1_hand.get_monnaie() and mise_du_tour >= backup:
#                                                         budget_suffisant = True
#                                                         choix_adversaire1 = True
#                                                     elif mise_du_tour +  mise_adversaire1 == adversaire1_hand.get_monnaie():
#                                                         print ("Tapis !")
#                                                         action_definitive_adversaire1 = True
#                                                         choix_adversaire1 = True
#                                                         budget_suffisant = True
#                                                     elif mise_du_tour + mise_adversaire1 > adversaire1_hand.get_monnaie():
#                                                         print ("budget insufisant")
#                                                         mise_du_tour = backup
#                                                 mise_adversaire1 = mise_adversaire1 + mise_du_tour
#                                                 compteur_check = 0
#                                             else: #L'adversaire 1 suit
#                                                 print ("Adversaire 1 /Suivre")
#                                                 if mise_du_tour < adversaire1_hand.get_monnaie():
#                                                     mise_adversaire1 = mise_adversaire1 + mise_du_tour
#                                                     choix_adversaire1 = True
#                                                 else:
#                                                     print ("Tapis (fond insufisant pour suivre)")
#                                                     mise_adversaire1 = adversaire1_hand.get_monnaie()
#                                                     choix_adversaire1 = True
#                                                     action_definitive_adversaire1 = True



#             mise = mise_joueur + mise_adversaire1 + mise_adversaire2 #Mise en dehors du reste pour eviter dupli (Jcrois)
#             print (mise)

                    

#         Plus mise
