import csv
with open('journal.csv', 'r', newline='') as f:
    w = csv.DictReader(f, delimiter=';')
    tab = list(w)

print(tab)