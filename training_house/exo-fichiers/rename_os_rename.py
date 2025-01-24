import os
from os import getlogin

user = os.getlogin()

with open("c:/users/"+user+"/OneDrive - Collège de Bois-de-Boulogne/bureau/monFichier3.txt", 'w') as f:
    f.write("Voici le fichier a renomer")

source = "c:/users/"+user+"/OneDrive - Collège de Bois-de-Boulogne/bureau/monFichier3.txt"
dest = "c:/users/"+user+"/OneDrive - Collège de Bois-de-Boulogne/bureau/myFile.txt"

os.rename(source, dest)