from appJar import gui
from deck import Deck

from card import Carte
from test_card import random_card_Nbr

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

#app.addButton("affiche carte", on_click, 1, 1)
app.addImage("Carte_image", "src/empty.gif", 0, 1)

user1 = Deck()
user2 = Deck()

def button_user1():
    if on_click:
        #print('=>>', user1.L[-1])
        user1.L.insert(0, user2.L[-1])
        user2.supprime()
        user1.voir()
        user1.nombre()
        print("User 1 =>>",len(user1.L))

app.addButton("Take card from player 2", button_user1, 1, 0, 1)

def button_user2():
    if on_click:
        #print('=>>', user1.L[-1])
        user2.L.insert(0, user1.L[-1])
        user1.supprime()
        user2.voir()
        user2.nombre()
        print("User 2 =>>", len(user2.L))

app.addButton("take card from player 1", button_user2, 1, 2, 1)


def button_user1_affichage():
    app.setImage("carte image user2","resources/Playing_card_" + str(user2.L[-1][1]) + "_" + str(user2.L[-1][0]) + ".gif")

app.addButton("afficher la carte a user1", button_user1_affichage, 2, 0)
app.addImage("carte image user1", "src/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif", 0,2)    

def button_user2_affichage():
    app.setImage("carte image user1","resources/Playing_card_" + str(user1.L[-1][1]) + "_" + str(user1.L[-1][0]) + ".gif")

app.addButton("afficher la carte a user2", button_user2_affichage, 2, 2)
app.addImage("carte image user2", "src/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif", 0, 0)



def distribute():
    if random_card_Nbr() not in user1.L and random_card_Nbr() not in user2.L:
        for i in range(53):
            if i%2==0 and len(user1.L) < 27:
                user1.L.append(random_card_Nbr())
            elif len(user2.L) < 27:
                user2.L.append(random_card_Nbr())
       
app.addButton("distribuer les cartes", distribute, 2, 1)
app.go()




