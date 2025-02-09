with open('myFile1.txt', 'w') as f:
    f.write("learning to program in phyton is easier than learning to program java")

with open('myFile1.txt', 'r') as f:
    tab = f.readline().strip().split()

for x in tab:
    print(f"La frequence de repetition de '{x}' est ", tab.count(x))