import pandas


def extrait_txt(path):
    try:
        with open(path, 'r') as f:
            tab = []
            while line := f.readline():
                #line = line.strip()
                tab.append(line)
            return tab
    except FileNotFoundError:
        print(f'Erreur fichier {path} introuvable ')

def ecrire_txt(path, tab):
    try:
        with open(path, 'w') as f:
            f.writelines(tab)
    except Exception:
        print('Erreur')

def valider_date():
    date = input('Veuillez entrez la date de retour au format AAAA-MM-JJ')
    while True:
        try:
            date_cor = pandas.to_datetime(date, format='%Y-%m-%d')
            return date_cor
        except ValueError:
            print('Format date incorrect. Recommencez annee-mois-jour')
            date = input('Veuillez entrez la date au format AAAA-MM-JJ')


