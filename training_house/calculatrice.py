from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

def operation():
    sender = fen.sender()

    try:
        x = float(input_x.text())
        y = float(input_y.text())
        match sender.text():
            case '+':
                result = x+y
            case '-':
                result = x-y
            case '*':
                result = x*y
            case '/':
                if y == 0:
                    label.setText('Erreur, division par 0')
                    return
                else:
                    result = x/y
        label.setText("resultat : "+ str(result))
    except:
        label.setText("Erreur, entrees invalides")
def cancel():
    input_x.setText('')
    input_y.setText('')

app = QApplication([])
fen = QWidget()
fen.setWindowTitle('calculatrice_v1')
fen.setGeometry(100,100,250,250)

input_x = QLineEdit(fen)
input_x.setText('')
input_x.setGeometry(10,10,60,60)
input_y = QLineEdit(fen)
input_y.setText('')
input_y.setGeometry(80,10,60,60)

label = QLabel(fen)
label.setGeometry(10,160,160,100)
label.setText('Resultat :')
label1 = QPushButton(fen)
label1.setText('reset')
label1.setGeometry(100,160,80,30)
label1.clicked.connect(cancel)

but_p = QPushButton(fen)
but_p.setText('*')
but_p.setGeometry(20,80,30,30)
but_m = QPushButton(fen)
but_m.setText('-')
but_m.setGeometry(40,80,30,30)
but_a = QPushButton(fen)
but_a.setText('+')
but_a.setGeometry(60,80,30,30)
but_d = QPushButton(fen)
but_d.setText('/')
but_d.setGeometry(80,80,30,30)

list =[ but_a, but_d, but_m, but_p]
for x in list:
    x.clicked.connect(operation)















fen.show()
app.exec()