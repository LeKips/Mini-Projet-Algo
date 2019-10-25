from dico import villes #on importe notre librairie

#On initialise

def depart():

    listeVilles = []
    choixVille = None
    compteur = 1
    tempsTotal = 0 
    trajetTotal = 0

#On demande le trajet que l'on souhaite effectuer

start = input("Choisissez votre ville de départ : ")
end = input("Choisissez votre ville d'arrivée : ")

#Dans le cas où on est pas très malin

if start == end :
    print("Ben t'es déjà arrivé ! GG !")

#

    while choixVille != '' :
        