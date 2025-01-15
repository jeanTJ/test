import hashlib

def calculer_hashage(fichier, algorithme="sha256"):
    try:
        h = hashlib.new(algorithme) #creation d'un objet de hashage avec algorithme specifier
        with open(fichier, 'rb') as f:    # while block := f.read(8192)
            while block := f.read(8192):
                h.update(block)
        return h.hexdigest()
    except FileNotFoundError:
        #Gestion d'erreur si le fichier specifie n'est pas trouve
        print(f"Le fichier {fichier} est introuvable")
        return None
    except Exception as e:
        # Gestion d'autres erreurs imprevues
        print(f"Erreur lor du calcul du hashage : {e}")
        return None








text = "c:/temp/Notes.csv"

hashage_sha1 = hashlib.sha1(text.encode()).hexdigest()
#print("le sha1 de notes.csv est :", hashage_sha1)

# sha-256

hashage_sha256 = hashlib.sha256(text.encode()).hexdigest()
#print("Le hashage sha_256 de notes.csv est : ", hashage_sha256)

