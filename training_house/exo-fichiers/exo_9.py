with open('myfile1.txt', 'w') as f:
    f.write('Python Programming' + '\nJava Programming' + '\nC++ Programming')
with open('myfile1.txt', 'r') as f:
    tab = f.readlines()
temp = tab[1]
tab[1] = tab[2]+'\n'
tab[2] = temp
with open('myfile1.txt', 'w') as f:
    f.writelines(tab)