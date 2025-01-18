from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
def somme():
    print(float(input1.text()) + float(input2.text()))
    label3.setText(f"Resultat : {float(input1.text()) + float(input2.text())}")


app = QApplication([])
fen = QWidget()

fen.setWindowTitle("Calculateur")
fen.setGeometry(300, 300, 450, 350)

label1 = QLabel(fen)
label1.setText('x')
label1.setGeometry(10,10,200,50)
label2 = QLabel(fen)
label2.setText('Y')
label2.setGeometry(10,150,200,50)
label3 = QLabel(fen)
label3.setText("Resultat :")
label3.setGeometry(10, 300, 200, 50)

input1 = QLineEdit(fen)
input1.setGeometry(150,10,200,50)
input2 = QLineEdit(fen)
input2.setGeometry(150,150,200,50)

but_som = QPushButton(fen)
but_som.setText('x + y')
but_som.setGeometry(200,250,150,50)
but_som.clicked.connect(somme)




fen.show()
app.exec()