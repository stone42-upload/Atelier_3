from Voiture import Voiture
class Parc:
    def __init__(self, capacite,):
        self.capacite = capacite
        self.voitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.voitures:
            print("Cette voiture est déja dans le parc")
        elif len(self.voitures) < self.capacite:
            self.voitures.append(voiture)
            print("Cette voiture a été ajouter au parc")
        else:
            print("Désolé il n'y a pas assez de place dans ce parc")


