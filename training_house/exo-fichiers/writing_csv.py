import csv

# Données à écrire dans le CSV
donnees = [
    {'nom': 'Alice', 'age': 25, 'ville': 'Paris'},
    {'nom': 'Bob', 'age': 30, 'ville': 'Lyon'},
    {'nom': 'Charlie', 'age': 35, 'ville': 'Marseille'},
]

# Noms des colonnes (en-têtes)
noms_des_colonnes = ['nom', 'age', 'ville']

# Ouvrir le fichier CSV en mode écriture
with open('personnes.csv', mode='w', newline='', encoding='utf-8') as fichier:
    writer = csv.DictWriter(fichier, fieldnames=noms_des_colonnes)

    # Écrire la ligne d'en-tête
    writer.writeheader()

    # Écrire les lignes de données
    writer.writerows(donnees)