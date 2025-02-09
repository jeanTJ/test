tab = []
while len(tab) < 3:
    n = input("Entrer 10 nombre entier: ")
    try:
        n = int(n)
        tab.append(n)
    except:
        n = input("Erreur, svp entrer uniquement des nombres entiers: ")
print(tab)
max = tab[0]
min = tab[0]
for i in range(len(tab)-1):
    if tab[i] < min:
        min = tab[i]
    if tab[i] > max:
        max = tab[i]
print("min = ", min)
print('max = ',max)

for i in range(len(tab)):
    for j in range(i+1, len(tab)):
        if tab[i] > tab[j]:
            temp = tab[i]
            tab[i] = tab[j]
            tab[j] = temp
print(tab)

