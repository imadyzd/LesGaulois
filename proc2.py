from creerMatrice import *
import os
def proc2(mat):
    c0 = 0 
    c1 =0
    c2= 0
    c3 = 0
    
    for ligne in mat:
        pid = os.fork()
        if pid == 0:
            sys.exit(traiterLigne(ligne,v1,v2))
        
    for ligne in mat :
        pid,stat = os.wait()
        code_rep = os.WEXITSTATUS(stat)
        if code_rep == 0:
            c0+=1
        elif code_rep == 1:
            c1+=1
        elif code_rep == 2:
            c2+=1
        elif code_rep == 3:
            c3+=1

    print("total : ",c0,c1,c2,c3)
proc2(mat)
