from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

def analyse():
    tab = [int(x.text()) for x in l2]
    tp.setText("Total des points : " + str(sum(tab)))
    moyenne.setText(("Moyenne : " + str(sum(tab)/len(tab))))
    for x in tab:
        if x == max(tab):
            ig = tab.index(x)     #index du gagnant
            gagnant.setText("Gagnant : " + l1[ig].text())

def sauvegarde():

    #fen1.setWindowTitle("Sauvegarde reussie")
    with open('Resultats.txt', 'w') as f:
        for x in l1:
            f.write(x.text()+'\n')
        for x in l2:
            f.write(x.text() + '\n')



def charger():
    with open('Resultats.txt', 'r') as f:
        for i in range(len(l1)):
            ligne = f.readline().strip()
            l1[i].setText(ligne)
        for i in range(len(l2)):
            ligne = f.readline().strip()
            l2[i].setText(ligne)








app = QApplication([])
fen = QWidget()

grid = QGridLayout()
fen.setLayout(grid)

#Qlabel
l_j = QLabel("LISTE DES JOUEURS")
grid.addWidget(l_j, 0, 2)
nj = QLabel("Nom du joueur")
grid.addWidget(nj,1, 1 )
pa = QLabel("Points accumules")
grid.addWidget(pa, 1, 2)

l = [QLabel("joueur #"+ str(i+1)) for i in range(4)]

grid.addWidget(l[0], 2, 0)
grid.addWidget(l[1], 3, 0)
grid.addWidget(l[2], 4, 0)
grid.addWidget(l[3], 5, 0)
#Qlineedit
l1 = [QLineEdit() for i in range(4)]
grid.addWidget(l1[0],2, 1)
grid.addWidget(l1[1],3, 1)
grid.addWidget(l1[2],4, 1)
grid.addWidget(l1[3],5, 1)
#Qlinedit
l2 = [QLineEdit() for i in range(4)]
grid.addWidget(l2[0],2, 2)
grid.addWidget(l2[1],3, 2)
grid.addWidget(l2[2],4, 2)
grid.addWidget(l2[3],5, 2)
#Qlabel
tp = QLabel("Total des points")
grid.addWidget(tp, 6, 0)
moyenne = QLabel("Moyenne")
grid.addWidget(moyenne, 6, 2)
gagnant = QLabel("Gagnant")
grid.addWidget(gagnant, 7, 0 )

#QPushButton
Chr = QPushButton("Charger resultats")
grid.addWidget(Chr, 8, 0)
Chr.clicked.connect(charger)
save = QPushButton("Sauvegarder resultats")
grid.addWidget(save, 8, 1 )
save.clicked.connect(sauvegarde)
anal = QPushButton("Analyser resultats")
grid.addWidget(anal, 8, 2)
anal.clicked.connect(analyse)





fen.show()
app.exec()