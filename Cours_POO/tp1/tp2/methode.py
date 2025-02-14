import pandas
def valider_date():
    date = input('Veuillez entrez la date au format AAAA-MM-JJ : ')
    while True:
        try:
            date_cor = pandas.to_datetime(date, format='%Y-%m-%d').date()
            return date_cor
        except ValueError:
            print('Format date incorrect. Recommencez annee-mois-jour')
            date = input('Veuillez entrez la format AAAA-MM-JJ : ')
