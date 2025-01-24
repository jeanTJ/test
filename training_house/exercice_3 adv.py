from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

def double():
    try:
        list[1].setText(str(2* float(list[0].text())))
    except:
        list[1].setText('Erreur, entrez un nombre ')



app = QApplication([])
fen = QWidget()

grid = QGridLayout()
fen.setLayout(grid)

fen.setWindowTitle('TJ')
#QLabel
l1 = QLabel('Enter la valeur de N ')
grid.addWidget(l1, 0, 0)
l2 = QLabel('Voici le double ')
grid.addWidget(l2, 1, 0)
list = []
for i in range(2):
    x = QLineEdit()
    grid.addWidget(x, i, 1)
    list.append(x)
print(list)

btn = QPushButton("Valider l'operation")
grid.addWidget(btn, 2, 1)
btn.clicked.connect(double)

fen.show()
app.exec()