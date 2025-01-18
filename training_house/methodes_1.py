def sauvegarder():
    with open('resultats.txt','w') as f:
        f.write(nj1.text() + ' - ' + pj1.text() + '\n')
        f.write(nj2.text() + ' - ' + pj1.text() + '\n')
        f.write(nj3.text() + ' - ' + pj3.text() + '\n')
        f.write(nj4.text() + ' - ' + pj4.text())
    return

def charger():
    f = open('resultats','r')
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




