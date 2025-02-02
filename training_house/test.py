import csv
from datetime import datetime

from Cours_POO.tp1.TP1  import Journal
from Cours_POO.tp1.TP1  import csv_dictreader

with open('adherent.txt', 'r') as f:
    tab = f.readlines()
#print(tab)

l = [2,5,6]
#if 2 in l:
 #   print('yes')

tab = []

'''with open('livre.csv', 'r') as f:
    tab = []
    while ligne := f.readline():
        tab.append(ligne.strip().split(','))
print(tab)
y = ['le solitaire', 'Rouseau']
if y in tab:
    print('yes')

t= datetime.now()
strt = str(t)
print(type (strt))'''
def test():
    with open('emprunt.csv', 'r', newline='') as f:
        tab = []
        read = csv.reader(f, delimiter=';')
        for ligne in read:
            if any(ligne):
                tab.append(ligne)

j1 = Journal('La guerre est declare', '2025-02-02')
#j1.ajout_journal()
#tab = csv_dictreader('journal.csv')
#print(tab)
j1.enlenver_journal()

