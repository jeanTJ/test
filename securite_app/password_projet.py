from hashage_new import calculer_hashage as calh

with open("passe.txt", 'w') as f:
    f.write("Be4freedom")
passe = "passe.txt"
hash_pass = calh(passe,'md5')
print(hash_pass)