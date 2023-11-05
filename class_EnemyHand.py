class EnemyHand:
    def __init__(self, monnaie):
        self.cartes = []
        self.monnaie = monnaie
        self.ingame = True

#Getters

    def get_cartes(self):
        return self.cartes
    
    def get_monnaie(self):
        return self.monnaie

    def get_ingame(self):
        return self.ingame

#Setters

    def add_cartes(self,card):
        self.cartes.append(card)

    def set_cartes(self,cards):
        self.cartes = cards
    
    def set_monnaie(self,new_moula):
        self.monnaie = new_moula

    def set_ingame(self,var):
        self.ingame=var
