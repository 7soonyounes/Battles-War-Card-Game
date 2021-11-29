from appJar import gui
from deck import Deck

from card import Carte

app = gui()


app.addLabelOptionBox("couleur", ["\u2660", "\u2665", "\u2666", "\u2663"], 0, 0)
app.addLabelOptionBox("valeur", [str(i) for i in range(1, 14)], 0, 2)


def on_click(button):
    couleur = app.getOptionBox("couleur")
    valeur = app.getOptionBox("valeur")
    if couleur == "\u2660":
        app.setImage("Carte_image", Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":
        app.setImage("Carte_image", Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":
        app.setImage("Carte_image", Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":
        app.setImage("Carte_image", Carte(int(valeur), Carte.TREFLE).image())

app.addButton("affiche carte", on_click, 0, 1)
app.addImage("Carte_image", "src/empty.gif", 1, 0, 2)

user1 = Deck()
couleur = app.getOptionBox("couleur")
valeur = app.getOptionBox("valeur")

def button_user1():
    if on_click:
        user1.ajoute(valeur, couleur)
        user1.voir()
        user1.nombre()

app.addButton("user1", button_user1, 1, 2)

user2 = Deck()

def button_user2():
    if on_click:
        #print('=>>', user1.L[-1])
        user2.L.append(user1.L[-1])
        user2.voir()
        user2.nombre()        
app.addButton("user2", button_user2, 2, 2)


app.go()