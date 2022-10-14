from creerMatrice import *

def traite_mat(mat):
    c0 =0
    c1 =0
    c2= 0
    c3 = 0
    for ligne in mat:
        if traiterLigne(ligne,v1,v2) == 0:
            c0 +=1
        elif traiterLigne(ligne,v1,v2) == 1:
            c1+= 1
        elif traiterLigne(ligne,v1,v2) == 2:
            c2+= 1
        elif traiterLigne(ligne,v1,v2) == 3:
            c3+= 1
    print("total : ",c0,c1,c2,c3)
traite_mat(mat)