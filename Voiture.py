class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherinformation(self):
        print(f"matricule: {self.matricule}, marque:{self.marque}, couleur:{self.couleur}")
