from card import Carte


class Deck:
    def __init__(self):
        self.L=[]

    def ajoute(self,valeur,couleur):
        #self.L=t
        c=Carte(valeur,couleur)
        self.L.append(c.image)

    def nombre(self):
        print(len(self.L))

    def supprime(self):
        #a=(len(self.L)-1)
        del(self.L[-1])

    def voir(self):
         print(self.L[-1])
