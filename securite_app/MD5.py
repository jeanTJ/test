import hashlib

text = 'hello'
text1 = 'world'


hashage_md5 = hashlib.md5(text.encode()).hexdigest()
hashage1_md5 = hashlib.md5(text1.encode()).hexdigest()

#hashlib est une classe python pour creer les hashage md5,sha-256 etc
#text.encode() convertit une chaine de caractere en format binaire car hashlib ne s'applique que sur des valeurs binaires
#hexdigest() methode qui retourne une empreinte md5 sous forme de chaine hexadecimale
print('MD5 : ', hashage_md5)
print('MD5 : ', hashage1_md5)