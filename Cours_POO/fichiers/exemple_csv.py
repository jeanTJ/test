import csv
import panda

f = open('c:/temp/moyen.csv')

reader = csv.DictReader(f, delimiter=',')
for r in reader:
    print(r)
print(type(reader))
