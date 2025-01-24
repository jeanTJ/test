import os
from os import chdir
import shutil
user = os.getlogin()
with open("c:/users/"+user+"/OneDrive - Collège de Bois-de-Boulogne/bureau/myFile1.txt",'w') as f:
    f.write("Voici le fichier cree myFile1.txt")

def creationDos(new):
    try:
        path = "c:/users/"+user+"/OneDrive - Collège de Bois-de-Boulogne/bureau/"+str(new)
        os.mkdir(path)
    except FileNotFoundError:
        print("le dossier existe deja")

source = "c:/users/"+os.getlogin()+"/OneDrive - Collège de Bois-de-Boulogne/bureau/myFile1.txt"
dest = "c:/users/"+os.getlogin()+"/OneDrive - Collège de Bois-de-Boulogne/bureau/new"
shutil.move(source, dest)
