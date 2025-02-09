n = input("Entrez un nombre entier non nul: ")
while True:
    try:
        n = int(n)
        if n > 0:
            for i in range(1, n+1):
                print("*"*i)
            break
        else:
            n = input("Entrez un nombre entier naturel: ")


    except:
        print("Erreur de saisi, Vous ne devez entrez que des chiffres entier naturel")
        n = input("Entrez un nombre entier naturel: ")


        