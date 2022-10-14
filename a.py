import sys,  os
def is_dir(dossier):    
    
    for direc in os.listdir(dossier):
        
        path =  dossier+ "/" +direc 
        if os.path.isdir(path):
            print("|",direc)
            is_dir(path)
is_dir("TEST" )
