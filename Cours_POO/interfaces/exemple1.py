from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
# De la bibliotheque PyQt6 on prent le package QtWidgets et importe les classes QApplication QWidget
app = QApplication([])

fen = QWidget()

#fen.show()

#app.exec()
fen.setGeometry(QRect(200,200,400,150))
fen.setWindowTitle("Mon app graphique")

#fen.show()

#app.exec()

class Mafenetre(QWidget):
    def __init__(self, fen):
        super().__init__()
        self.fen = fen

    def build(self):
        fen.setWindowTitle("hi")
        fen.setGeometry(100, 100, 400, 150)



