from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
def double():
    try:
        result = 2 * float(input1.text())
        input2.setText(str(result))
    except:
        input2.setText("Erreur, veuillez saisir un nombre")


app = QApplication([])
fen = QWidget()

fen.setWindowTitle("boubleur")
fen.setGeometry(100,100,400,200)

label1 = QLabel(fen)
label1.setText("Entrez la valeur de N ")
label1.setGeometry(20,0,250,100)
label2 = QLabel(fen)
label2.setText("Voici le double : ")
label2.setGeometry(20,40,250,100)

input1 = QLineEdit(fen)
input1.setGeometry(150,25,150,40)
input1.setText('')
input2 = QLabel(fen)
input2.setGeometry(150,75,180,40)
input2.setText('')

buton = QPushButton(fen)
buton.setGeometry(150,105,150,40)
buton.setText("Validez l'operation")

buton.clicked.connect(double)





fen.show()
app.exec()