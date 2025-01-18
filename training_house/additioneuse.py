from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton
def add():
    try:
        print(f"la somme de x et y est : {float(input1.text()) + float(input2.text())}")
        s = float(input1.text())+float(input2.text())
        label2.setText(f"Resultat : {s}")
    except:
        None

def reset():
    input1.setText("")
    input2.setText("")

app = QApplication([])
fen = QWidget()

fen.setWindowTitle("Additionneuse")
fen.setGeometry(100,200,300,150)

input1 = QLineEdit(fen)
input1.setText(" ")
input1.setGeometry(10,10,80,30)

input2 = QLineEdit(fen)
input2.setText(" ")
input2.setGeometry(80,10,80,30)

label = QLabel(fen)
label.setText('+')
label.setGeometry(65,10,50,30)
label1 = QLabel(fen)
label1.setText('=')
label1.setGeometry(130,10,50,30)
label2 = QLabel(fen)
label2.setText("Resutat : ")
label2.setGeometry(10,80,150,30)

but_can = QPushButton(fen)
but_can.setText('Cancel')
but_can.setGeometry(150,80,50,30)
but_can.clicked.connect(reset)

but_cal = QPushButton(fen)
but_cal.setText("Calc")
but_cal.setGeometry(150,10,50,30)
but_cal.clicked.connect(add)

















fen.show()
app.exec()