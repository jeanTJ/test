import os
from os import chdir

chdir("c:/users/" + os.getlogin() + '/OneDrive - Collège de Bois-de-Boulogne/bureau')
f = open('monFichier2.txt', 'w')
f.write("Je suis entrain d'apprendre python au college-bois-de Boulogne" )
f.close()