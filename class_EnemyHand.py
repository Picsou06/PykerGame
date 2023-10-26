from random import *
class EnemyHand:
    def __init__(self, monnaie = randint(100,500)):
        self.cartes = []

#Getters

    def get_cartes(self):
        return self.cartes
    
    def get_monnaie(self):
        return self.monnaie

#Setters

    def add_cartes(self,card):
        self.cartes.append(card)

    def set_monnaie(self,new_moula):
        self.monnaie = new_moula
