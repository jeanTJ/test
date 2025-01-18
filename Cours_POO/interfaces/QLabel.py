from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

def action_ok():
    print('ok')
    print(f"Bonjour {input1.text()} {input2.text()}")
    label3.setText(f"Bonjour {input1.text()}  {input2.text()}")

def action_cancel():
    input1.setText('')
    input2.setText('')
    label3.setText("Message : ")

app = QApplication([])
fen = QWidget()

#Parametre de fenetre
fen.setWindowTitle("Titre de la fenetre")
fen.setGeometry(300, 300, 450, 350)
#QLabel
label1 = QLabel(fen)
label1.setText("nom : ")
label1.setGeometry(10,10,200,50)

label2 = QLabel(fen)
label2.setText("prenom :")
label2.setGeometry(10,150,200,50)

label3 = QLabel(fen)
label3.setText("Message")
label3.setGeometry(10, 300, 200, 50)

#QLineEdit
input1 = QLineEdit(fen)
input1.setGeometry(150,10,200,50)
input2 = QLineEdit(fen)
input2.setGeometry(150,150,200,50)

# QPushbutton
but_ok = QPushButton(fen)
but_ok.setText("Press me")
but_ok.setGeometry(200,250,150,50)
but_ok.clicked.connect(action_ok)
but_cancel = QPushButton(fen)
but_cancel.setText('Cancel')
but_cancel.setGeometry(10,250,100,50)
but_cancel.clicked.connect(action_cancel)




fen.show()
app.exec()