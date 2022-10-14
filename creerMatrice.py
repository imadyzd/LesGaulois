import sys, os
from random import randint 
def creerMatrice(nbLignes, nbColonnes):
    mot = [[randint(0,20) for i in range (nbColonnes)]for i in range (nbLignes)]
    return mot 


def afficherMatrice(matrice):
    for ligne in matrice:
        print(ligne)

def traiterLigne(uneLigne, v1, v2):
    int1 = 0
    int2 =0
    for i in uneLigne:
        if i == int1:
            v1 = 1
        if i == int2:
            v2 = 1
    if v1 == 1 and v2 == 1:
        return 3
    elif v1 ==1 and v2 == 0:
        return 1
    elif v1 ==0 and v2 == 1:
        return 2
    else :
        return 0
v1 = 5
v2= 4
mat =creerMatrice(10,500000)

