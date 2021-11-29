class Carte:
    PIQUE = "spade"
    COEUR = "heart"
    CARREAU = "diamond"
    TREFLE = "club"
    

    def __init__(self, valeur, couleur):
        self._valeur = valeur
        self._couleur = couleur

    def image(self):
        return "resources/Playing_card_" + self._couleur + "_" + str(self._valeur) + ".gif"

