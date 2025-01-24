'''f = open('monfichier.txt', 'w')
f.write("Bonjour :)")
f.write("\t")  #\t  ajoute tabulation a la fin
f.writelines(['\na\n','b\n','c\n','d\n'])  # Pour ecrire plusieurs caractere a la fois
f.close()

f = open('monfichier.txt', 'a')
f.write('deuxieme bonjour')'''

f = open('monfichier.txt', 'r')
list = []
while ligne := f.readline():
    list.append(ligne.strip())
f.close()
print(list)

f = open('monfichier.txt', 'r')

tab = f.readlines()
tab1 = [tab[i].strip() for i in range(len(tab))]
print(tab1)

tab[1].split()