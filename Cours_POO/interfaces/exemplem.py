import sys
import PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
fen = QWidget()
fen.setWindowTitle('My first window')
fen.setGeometry(50, 50, 350, 200)
qlabel = QLabel(fen)
qlabel.setText('HAPPY DAY!')
qlabel.setGeometry(50,50,250,50)
qlabel.setStyleSheet("background: darkblue; border: 2px solid red; color:yellow; font:broadway; font-size:36px;")

fen.show()
app.exec()


