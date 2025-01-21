from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit

from Cours_POO.interfaces.cour_grid_layout import lbl_gagnant
def sauvegarder():
    with open('resultats.txt', 'w') as f:
        for i in range(4):
            f.write(l[i].text() + '\n')
            f.write(l1[i].text() + '\n')

def stats():
    tab = []
    for i in range(4):
        tab.append(int(l1[i].text()))
    for i in range(4):
        if max(tab) == tab[i]:
            lbl_gagnant.setText('Gagnant : ' + l[i].text())
    lbl_total.setText('Total de points: ' + str(sum(tab)))
    lbl_moyen.setText('Moyenne : ' + str(sum(tab)/len(tab)))

def charger():
    with open('resultats.txt', 'r') as f:
        for i in range(4):
            l[i].setText(f.readline().strip())
            l1[i].setText(f.readline().strip())



app =QApplication([])
fen = QWidget()

#Creer un grid layout et l;associer a ala fenetre

grid = QGridLayout()
fen.setLayout(grid)

#Qlabel
grid.addWidget(QLabel("Nom_Joueur"),0,1)
grid.addWidget(QLabel("Points_Joueur"),0,2)

l_lbl1 = [grid.addWidget(QLabel("joueur" + str(i+1)), i+1, 0) for i in range(4)]

'''lbl1 = QLabel("joueur1")
grid.addWidget(lbl1, 1, 0)
lbl2 = QLabel("joueur2")
grid.addWidget(lbl2, 2, 0)
lbl3 = QLabel("joueur3")
grid.addWidget(lbl3, 3, 0)
lbl4 = QLabel("joueur4")
grid.addWidget(lbl4, 4, 0)'''

#QLine edit
##    input[i] = QLineEdit()
 #   grid.addWidget(input[i], i, 1)
l = [QLineEdit() for i in range(4)]

l_n = [grid.addWidget(l[i], i+1, 1) for i in range(4)]

'''input1 = QLineEdit()
grid.addWidget(input1, 1, 1)
input2 = QLineEdit()
grid.addWidget(input2, 2, 1)
input3 = QLineEdit()
grid.addWidget(input3, 3, 1)
input4 = QLineEdit()
grid.addWidget(input4, 4, 1)'''
l1 = [QLineEdit() for i in range(4)]
l_score = [grid.addWidget(l1[i], i+1, 2) for i in range(4)]

'''input5 = QLineEdit()
grid.addWidget(input5, 1, 2)
input6 = QLineEdit()
grid.addWidget(input6, 2, 2)
input7 = QLineEdit()
grid.addWidget(input7, 3, 2)
input8 = QLineEdit()
grid.addWidget(input8, 4, 2)'''

lbl_total = QLabel('Total des points : 0')
grid.addWidget(lbl_total, 6, 0)
lbl_moyen = QLabel('Moyenne : 0')
grid.addWidget(lbl_moyen, 7, 0)
lbl_gagnant = QLabel('Gagnant : x')
grid.addWidget(lbl_gagnant, 6, 2)




btn_charger = QPushButton('Charger')
grid.addWidget(btn_charger, 8, 0)
btn_charger.clicked.connect(charger)
btn_save = QPushButton('Sauvegarder')
grid.addWidget(btn_save, 8, 1)
btn_save.clicked.connect(sauvegarder)
btn_analyser = QPushButton('Analyser')
grid.addWidget(btn_analyser, 8, 2)
btn_analyser.clicked.connect(stats)

print(type(l_n[1]))
print(type(l_n))


fen.show()
app.exec()