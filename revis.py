fich=open('c:/temp/notes.csv', 'r')
print(fich.read())

fich.close()
fich = open('c:/temp/notes.csv', 'r')
ligne  = fich.readline()
ligne  = fich.readline()
tab=[]
while ligne != "":
    ligne = ligne.strip().split(';')
    tab.append(ligne)
    ligne = fich.readline()
print(tab)
fich.close()

fich = open('c:/temp/notes.csv', 'r')
fich2 = open('c:/temp/moyen.csv', 'w')
ligne = fich.readline()
ligne = ligne.split(';')
fich2.write(ligne[0] + ';' + ligne[1] + ';' + ligne[2] + ';' + 'moyenne' + '\n')
ligne = fich.readline()
while ligne != '':
    ligne = ligne.strip().split(';')
    moy = (int(ligne[3])+int(ligne[4])+int(ligne[5])+int(ligne[6])+int(ligne[7]))/5
    fich2.write(ligne[0] + ';' + ligne[1] + ';' + ligne[2] + ';' + str(moy) + '\n')
    ligne = fich.readline()
fich.close()
fich2.close()
fich = open ('c:/temp/moyen.csv', 'r')
print(fich.read())

# EXO banque
def soldeDepot():
    sD = 0
    sR = 0
    fiche = open('c:/temp/banque.txt','r')
    lign = fich.readline()
    while lign != '':
        lign = lign.strip()
        if int(lign) > 0:
            sD += int(lign)
        else:
            sR += int(lign)
        lign = fiche.readline()
    return (sD, sR)

fich = open('c:/temp/banque.txt', 'r')
fich1 = open('c:/temp/banqueRetrait.txt', 'w')
fich2 = open('c:/temp/banqueDepot.txt', 'w')
fich1.write('Liste des depot:' + '\n')
fich2.write('liste des retrait :' + '\n')
r = []
d = []
ligne = fich.readline()
print('le strip() produit un fichier de tipe', type(ligne.strip()))
while ligne != '':
    if int(ligne) < 0:
        fich1.write(ligne + '\n')
        r.append(ligne)
    else:
        fich2.write(ligne + '\n')
        d.append(ligne)
    ligne = fich.readline()
fich.close()
fich1.close()
fich2.close()
fich1 = open('c:/temp/banqueDepot.txt', 'r')
fich2 = open('c:/temp/banqueRetrait.txt', 'r')
print(fich1.read())
print(fich2.read())



