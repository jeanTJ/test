with open("myfile.txt", 'w') as f:
    for i in range(5):
        f.write("Ligne numero" + ' ' + str(i+1) + '\n')

with open('myfile.txt', 'r') as f:
    tab = f.readlines()

tab[2] = "desole! Le contenu de cette ligne a ete change!\n"
with open("myfile.txt", 'w') as f:
    f.writelines(tab)

with open("myfile.txt", 'r') as f:
    print(f.read())
with open('myfile.txt', 'a') as f:
    f.write('Python est le meilleur langage de programmation')

with open('myfile.txt', 'r') as f:
    tab1 = f.readlines()
tab15 = tab1[5].split()
tab15.pop(4)
ch = ''
for x in tab15:
    ch += x+' '
tab1[5] = ch
with open('myfile.txt', 'w') as f:
    f.writelines(tab1)
