from random import * 
from class_Cartes import *
class JeuDeCartes:
    def __init__(self):
        self.cartes = []

    def creer_jeu_52_cartes(self):
        couleurs = ['coeur', 'trefle', 'pique', 'carreau']
        signes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'reine', 'roi', 'as']
        valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'valet': 11, 'reine': 12,'roi': 13, 'as': 14}
        self.cartes = []
        for couleur in couleurs:
            for signe in signes:
                self.cartes.append(Carte(signe, couleur, valeurs, f"images/cartes/{signe}_{couleur}.png"))

#Getters

    def get_cartes(self):
        return self.cartes

    def pioche_carte(self):
        return self.cartes.pop()

#Setters

    def set_cartes(self,i):
        self.cartes = i

#Autres fonctions

    def afficher_jeu(self):
        for i in self.cartes:
             i.afficher_carte()

    def ajt_carte(self,carte):
        self.cartes.append(carte)

    def melange(self):
        shuffle(self.cartes)