from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

from Cours_POO.tp1.TP1 import Bibliotheque



app = QApplication([])
fen = QWidget()

grid = QGridLayout()
fen.setLayout(grid)

b2 = Bibliotheque()

b = QLabel("BIBLIOTHEQUE")
grid.addWidget(b, 0, 3)
af = QLabel("Affichage")
grid.addWidget(af, 0, 8)
#qPushbutton
aj = QPushButton("Ajouter adherent")
tab = ['Ajouter adherent', 'Supprimer adherent', 'Afficher tous les adherents', 'Ajouter documents', 'Supprimer documents', 'Ajouter emprunt', 'Retour emprunt', 'Afficher tous les emprunts', 'Quitter']
button = [QPushButton(x) for x in tab]
for i in range(len(button)):
    position = [grid.addWidget(button[i], i+1, 1) ]

button[2].clicked.connect(b2.Afficher_adherent)
af.setText(b2.Afficher_adherent())




fen.show()
app.exec()