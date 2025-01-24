import os
user = os.getlogin()


with open('C:\\Users\\jeank\\OneDrive - Collège de Bois-de-Boulogne\\Bureau\\monFichier.txt', 'w') as f:
    f.write('Python est un langage de programmation oriente object')

with open('C:\\Users\\'+user+'\\OneDrive - Collège de Bois-de-Boulogne\\Bureau\\monFichier.txt', 'r') as f:
    print(f.read())


    