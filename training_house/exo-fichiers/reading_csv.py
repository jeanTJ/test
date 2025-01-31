import csv

with open("c:/temp/notes.csv", mode="r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    #for ligne in lecteur:
     #   print(ligne)

#csv.DictReader(fichier) : Lit le fichier CSV et associe chaque colonne à son en-tête.
#for ligne in lecteur: : Boucle sur chaque ligne qui est représentée sous forme de dictionnaire.

# Convertir en liste de dictionnaires

with open("c:/temp/moyenne.csv", mode="r") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=';')
    data = list(lecteur)
print(data)


