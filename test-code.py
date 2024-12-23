
inp = input("entrez un nombre :")
while True:
    try:
        inp = int(inp)
        if inp >= 0 and inp < 4:
            break
        else:
            print("erreur , veuillez saisir un nombre entre 1 et 4")
            inp = input("entrez un nombre :")
    except:
        print("Erreur, veuillez entrer un nombre entier entre 1 et 4")
        inp = input("entrez un nombre :")