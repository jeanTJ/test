import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
widget = QWidget()
widget.setGeometry(50, 50, 100, 100)
widget.setWindowTitle("Label exemple2")

qlabel1 = QLabel(widget)
qlabel1.setText("Hello world")

#define label1 dimension
qlabel1.setGeometry(50,50,250,50)

#Use QSS designe
qlabel1.setStyleSheet("background: darkblue; border: 2px solid red; color:yellow; font:broadway; font-size:36px;")

widget.show()
app.exec()

