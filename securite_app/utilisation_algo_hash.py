from hashage_new import calculer_hashage as calch

file = 'C:\\temp\\notes.csv'
empreinte = calch(file)
print(f"le hashage 256 de {file} est : {empreinte}")

empreinte1 = calch(file, 'sha512')

print(f"Le hashage 512 de {file} est : {empreinte1}")
