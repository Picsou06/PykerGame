class Carte:
    def __init__(self, signe, couleur, valeur, image):
        self.signe = signe
        self.couleur = couleur
        self.valeur = valeur
        self.image = image

    def get_signe(self):
        return self.signe
    def get_couleur(self):
        return self.couleur
    def get_valeur(self):
        return self.valeur
    def get_image(self):
        return self.image

    def set_signe(self,i):
        self.signe = i
    def set_couleur(self,i):
        self.signe = i
    def set_valeur(self,i):
        self.valeur = i
    def set_image(self,i):
        self.image = i

    def afficher_carte(self):
        print(self.signe,"de",self.couleur)

    def est_superieure_a(self, carte2):
        return self.valeur > carte2.get_valeur()

    def est_inferieure_a(self,carte2):
        return self.valeur < carte2.get_valeur()

    def est_egal_a(self,carte2):
        return self.valeur == carte2.get_valeur()
