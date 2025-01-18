from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
# generation de clefs privee et publique

cle_prive = rsa.generate_private_key(public_exponent=65537, key_size=2048)
## standard pour exposant RSA
# plus la taille est grande plus c'est difficile de la trouver

cle_public = cle_prive.public_key()  #calculer la cle publique qui va servir pour crypter
#saisie du message a chiffrer
message = input ("introduire le message a crypter (asymetrique ) : ").encode()
#chiffrement du message
#message_chiffre=cle_public.encrypt(message,padding.AEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithme=hashes.SHA256(),label=None))
message_chiffre = cle_public.encrypt( message, # le message a crypter
 padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None ))
print(f"message chiffree est : {message_chiffre}")