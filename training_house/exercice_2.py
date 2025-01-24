from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit

app = QApplication([])
fen = QWidget()

grid = QGridLayout()
fen.setLayout(grid)
titre = fen.setWindowTitle('Nom du fichier')
list = []
for i in range(10):
    x = QLineEdit()
    grid.addWidget(x, i, 0)









fen.show()
app.exec()