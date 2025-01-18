from cryptography.fernet import Fernet
#premiere etape generation de la cle de chiffrement
#cle sysmetrique utilise pour chiffrer

cle = Fernet.generate_key()
#on va creer un objet de la classe Fernet avec la cle genere
cipher = Fernet(cle)

message = 'Bonjour tout le monde'.encode()
message_chiffre = cipher.encrypt(message)
print(cle)
print(message_chiffre)

#dechiffrer message
message_decrypter = cipher.decrypt(message_chiffre)
print(f"Message en clair {message_decrypter}")