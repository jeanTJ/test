import random
tab =[]
while len(tab) < 6:
    note = random.randint(1,19)
    try:
        note = int(note)
        if note > 0 and note < 20 :
            tab.append(note)
            #note = input("Entrez la note suivante : ")
        else:
            print("Erreur la note de l'eleve doit etre comprise entre 0 et 20: ")
    except:
        print("Erreur: les notes doivent etre des nombre entiers")
        #note = input("Entrez la note de l'eleve: ")
print(tab)

min = tab[0]
max = tab[0]
for i in range(len(tab)-1):
    if tab[i] > max:
        max = tab[i]
    if tab[i] < min:
        min = tab[i]
print("La somme des notes de l'eleve est : ", sum(tab))
print("La plus grande moyenne de l'eleve est : ", max)
print("La plus petite moyenne de l'eleve est : ", min)
print("La moyenne de l'eleve est de : ", sum(tab)/len(tab))
moy = sum(tab)/len(tab)
if moy >= 18:
    print('Excellent')
elif moy >= 16:
    print("Bon")
elif moy >= 12:
    print("Moyen")
elif moy >= 10:
    print("insuffisant")
