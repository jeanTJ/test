from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit

app = QApplication([])
fen = QWidget()

# Créer un  Grid layout et l'associer a la fenetre
grid = QGridLayout()
fen.setLayout(grid)

grid.addWidget(QLabel("Nom_Joueur"),0,1)
grid.addWidget(QLabel("Points_Joueur"),0,2)

lbl1 = QLabel("joueur1")
grid.addWidget(lbl1, 1, 0)
lbl2 = QLabel("joueur2")
grid.addWidget(lbl2, 2, 0)
lbl3 = QLabel("joueur3")
grid.addWidget(lbl3, 3, 0)
lbl4 = QLabel("joueur4")
grid.addWidget(lbl4, 4, 0)

input1 = QLineEdit()
grid.addWidget(input1, 1, 1)
input2 = QLineEdit()
grid.addWidget(input2, 2, 1)
input3 = QLineEdit()
grid.addWidget(input3, 3, 1)
input4 = QLineEdit()
grid.addWidget(input4, 4, 1)

input12 = QLineEdit()
grid.addWidget(input12, 1, 2)
input22 = QLineEdit()
grid.addWidget(input22, 2, 2)
input32 = QLineEdit()
grid.addWidget(input32, 3, 2)
input42 = QLineEdit()
grid.addWidget(input42, 4, 2)

lbl_totalPoint = QLabel("total_point : 0")
grid.addWidget(lbl_totalPoint, 5, 1)
lbl_moyenne = QLabel("moyenne : 0")
grid.addWidget(lbl_moyenne, 5, 2)
lbl_gagnant = QLabel("gagnant : x")
grid.addWidget(lbl_gagnant, 6, 1)


btn_charger = QPushButton("Charger")
grid.addWidget(btn_charger, 7, 0)
btn_sauvegarde = QPushButton("Sauvegarde")
grid.addWidget(btn_sauvegarde, 7, 1)
btn_analyse = QPushButton("Analyser")
grid.addWidget(btn_analyse, 7, 2)


fen.show()
app.exec()