from card import Carte
from deck import Deck

a = Deck()

a.ajoute(1,"COEUR")
a.voir()
a.nombre()
a.supprime()
a.nombre()



import os 

folder = len(os.listdir("resources/"))
print(folder)