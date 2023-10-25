class EnemyHand:
    def __init__(self):
        self.cartes = []

#Getters

    def get_cartes(self):
        return self.cartes

#Setters

    def add_cartes(self,card):
        self.cartes.append(card)