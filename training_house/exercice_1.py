from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
def sauvegarder():
    with open('resultats.txt','w') as f:
        f.write(nj1.text() + ' - ' + pj1.text() + '\n')
        f.write(nj2.text() + ' - ' + pj1.text() + '\n')
        f.write(nj3.text() + ' - ' + pj3.text() + '\n')
        f.write(nj4.text() + ' - ' + pj4.text())
    return

def charger():
    f = open('resultats.txt', 'r')
    line = f.readline()
    line = line.split('-')
    nj1.setText(line[0])
    pj1.setText(line[1])
    line = f.readline()
    line = line.split('-')
    nj2.setText(line[0])
    pj2.setText(line[1])
    line = f.readline()
    line = line.split('-')
    nj3.setText(line[0])
    pj3.setText(line[1])
    line = f.readline()
    line = line.split('-')
    nj4.setText(line[0])
    pj4.setText(line[1])
    f.close()


def statis():
    list = [int(pj1.text()), int(pj2.text()), int(pj3.text()), int(pj4.text())]
    if  max(list) == int(pj1.text()):
        inp_gagnant.setText(nj1.text())
    elif max(list) == int(pj2.text()):
        inp_gagnant.setText(nj2.text())
    elif max(list) == int(pj3.text()):
        inp_gagnant.setText(nj3.text())
    elif max(list) == int(pj4.text()):
        inp_gagnant.setText(nj4.text())
    itp.setText(str(sum(list)))
    inp_m.setText(str(sum(list)/4))





app = QApplication([])
fen =QWidget()

fen.setGeometry(500,500,600,400)

label1 = QLabel(fen)
label1.setText('Liste des joueurs')
label1.setGeometry(300,10,200,160)
label2 = QLabel(fen)
label2.setText("Nom du joueur")
label2.setGeometry(200,20,200,160)
label3 = QLabel(fen)
label3.setText("Point acculumules")
label3.setGeometry(400,20,200,160)
l_j1 = QLabel(fen)
l_j1.setText("Joueur #1")
l_j1.setGeometry(100,40,200,160)
l_j2 = QLabel(fen)
l_j2.setText("joueur #2")
l_j2.setGeometry(100,70,200,160)
l_j3 = QLabel(fen)
l_j3.setText("joueur #3")
l_j3.setGeometry(100,100,200,160)
l_j4 = QLabel(fen)
l_j4.setText("joueur #4")
l_j4.setGeometry(100,140,200,160)
tp = QLabel(fen)
tp.setText("Total des points :")
tp.setGeometry(100,180,120,160)
l_m = QLabel(fen)
l_m.setText('Moyenne')
l_m.setGeometry(350,250,80,20)
l_gagnant = QLabel(fen)
l_gagnant.setText('Gagnant')
l_gagnant.setGeometry(100,230,120,160)

#nom des joueurs
nj1 = QLineEdit(fen)
nj1.setText('')
nj1.setGeometry(200,110,100,20)
nj2 = QLineEdit(fen)
nj2.setText('')
nj2.setGeometry(200,140,100,20)
nj3 = QLineEdit(fen)
nj3.setText('')
nj3.setGeometry(200,170,100,20)
nj4 = QLineEdit(fen)
nj4.setText('')
nj4.setGeometry(200,210,100,20)
#point acumules
pj1 = QLineEdit(fen)
pj1.setText('')
pj1.setGeometry(320,110,100,20)
pj2 = QLineEdit(fen)
pj2.setText('')
pj2.setGeometry(320,140,100,20)
pj3 = QLineEdit(fen)
pj3.setText('')
pj3.setGeometry(320,170,100,20)
pj4 = QLineEdit(fen)
pj4.setText('')
pj4.setGeometry(320,210,100,20)
#total des points
itp = QLineEdit(fen)
itp.setText('')
itp.setGeometry(250,250,80,20)
inp_m = QLineEdit(fen)
inp_m.setText("")
inp_m.setGeometry(450,250,80,20)
inp_gagnant = QLineEdit(fen)
inp_gagnant.setText('')
inp_gagnant.setGeometry(200,300,100,20)

#buttons charger et save
char_r = QPushButton(fen)
char_r.setText('Charger resultats')
char_r.setGeometry(100,350,120,30)
char_r.clicked.connect(charger)
save_r = QPushButton(fen)
save_r.setText('Sauvegarder resultats')
save_r.setGeometry(250,350,120,30)
save_r.clicked.connect(sauvegarder)
stat = QPushButton(fen)
stat.setText('Statistiques')
stat.setGeometry(380,350,120,30)
stat.clicked.connect(statis)





fen.show()
app.exec()