import csv

import pandas
def extrait(path):
    tab = []
    with open(path, 'r') as f:
        ligne = f.readline()
        while ligne != '':
            ligne = ligne.strip()
            tab.append(ligne)
            ligne = f.readline()
    return tab

def extrait_c1(path):
    with open(path, 'r') as f:
        tab = []
        while ligne := f.readline():
            ligne = ligne.strip().split(',')
            tab.append(ligne[0])
            ligne = f.readline()
    return tab
def extrait_csv(path):
    with open(path, 'r', newline='') as f:
        tab = []
        read = csv.reader(f, delimiter=';')
        for ligne in read:
            if any(ligne):
                tab.append(ligne)
        print(tab)
    return tab

def valider_date():
    date = input('Veuillez entrez la date de retour au format AAAA-MM-JJ')
    while True:
        try:
            date_cor = pandas.to_datetime(date, format='%Y-%m-%d')
            return date_cor
        except ValueError:
            print('Format date incorrect. Recommencez annee-mois-jour')
            date = input('Veuillez entrez la date au format AAAA-MM-JJ')
def ecrire_csv(path, tab):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerows(tab)

def csv_dictreader(path):
    with open(path, 'r', newline='') as f:
        w = csv.DictReader(f, delimiter=';')
        tab = list(w)
    return tab

def csv_dictwriter(path, tab, entete=[]):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, entete, delimiter=';')
        w.writeheader()
        w.writerows(tab)


