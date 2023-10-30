from random import*
class EnemyHand:
    def __init__(self, monnaie = [randint(3, 15),randint(2, 12),randint(1, 8),randint(0, 5),randint(0, 3),randint(0, 10)]):
        self.cartes = []
        self.monnaie = monnaie

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

#Autres

    def affiche_total_monnaie(self):
        return self.monnaie[0]*25 + self.monnaie[1]*50 + self.monnaie[2]*100 + self.monnaie[3]*200 + self.monnaie[4]*500 + self.monnaie[5]*1000
