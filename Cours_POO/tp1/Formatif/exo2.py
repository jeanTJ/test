with open('myFile.txt','w') as f:
    f.write("python Programming\n"+"Java Programming\n"+"C++ Programming\n")

with open('myFile.txt', 'r') as f:
    tab = f.readlines()
print(tab)
temp = tab[1]
tab[1] = tab[2]
tab[2] = temp
with open('myFile.txt','w') as f:
    f.writelines(tab)
    