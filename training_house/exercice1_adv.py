from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

def analyse():
    tab = []
    try:
        for i in list2:
            tab.append(int(i.text()))
        l4.setText('Total des points : ' + str(sum(tab)))
        l5.setText('Moyenne : ' + str(sum(tab)/len(tab)))
        idg = tab.index(max(tab))
        l6.setText('Gagnant : ' + str(list1[idg].text()) )
    except:
        print('Erreur entrez des chiffres comme scores')

def save():
    try:
        with open('resultats.txt', 'w') as f:
            for i in range(4):
                f.write(str(list1[i].text()) + '\n')
            for i in range(4):
                f.write(str(list2[i].text()) + '\n')
    except:
        print('Rien a save')

def charger():
    try:
        with open('resultats.txt', 'r') as f:
            for i in range(4):
                list1[i].setText(f.readline().strip())
            for i in range(4):
                list2[i].setText(f.readline().strip())
    except FileNotFoundError:
        print('aucun fichier save')


app = QApplication([])
fen = QWidget()

grid = QGridLayout()
fen.setLayout(grid)

#Qlabel
l1 = QLabel('Liste des joueurs')
grid.addWidget(l1,0,1)
l2 = QLabel('Nom du joueur')
grid.addWidget(l2, 1, 1)
l3 = QLabel('Points accumules')
grid.addWidget(l3, 1, 2)

l_j1 = QLabel('Joueur #1')
grid.addWidget(l_j1, 2, 0 )
l_j2 = QLabel('Joueur #2')
grid.addWidget(l_j2, 3, 0 )
l_j3 = QLabel('joueur #3')
grid.addWidget(l_j3,4,0 )
l_j4 = QLabel('Joueur #4')
grid.addWidget(l_j4, 5 ,0)

# QLinedit nom
list1 = [QLineEdit() for i in range(4)]
list_1 = [grid.addWidget(list1[i], i+2, 1) for i in range(4)]

#Score
list2 = [QLineEdit() for i in range(4)]
list_2 = [grid.addWidget(list2[i], i+2, 2 ) for i in range(4)]

#QLabel
l4 = QLabel('Total des points :')
grid.addWidget(l4, 6, 0)
l5 = QLabel('Moyenne :')
grid.addWidget(l5, 6, 2)
l6 = QLabel('Gagnant :')
grid.addWidget(l6, 7, 0)

#QPushbutton
butn1 = QPushButton('Charger resultats')
grid.addWidget(butn1, 9, 0)
butn1.clicked.connect(charger)
butn2 = QPushButton('Sauvegarder')
grid.addWidget(butn2, 9, 1)
butn2.clicked.connect(save)
butn3 = QPushButton('Analyser resultats')
grid.addWidget(butn3, 9, 2)
butn3.clicked.connect(analyse)








fen.show()
app.exec()