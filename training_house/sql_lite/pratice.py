import sqlite3


def ajour_adh():
    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    id = int(input('Entrez id adherent: '))
    nom = input("entrez le nom de l'adherent: ")
    adresse = input("entrez l'adresse: ")
    req = """insert into Adherent (id, nom, adresse)
    values (?, ?, ?)"""
    c.execute(req, (id, nom, adresse))
    conn.commit()
    conn.close()
def afficher_adh():
    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    req = """select * from Adherent"""
    c.execute(req)
    data = c.fetchall()
    print(data)
    conn.close()
def supprimer_adh():
    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    id = int(input('Entrez id adherent: '))
    adh = input("entrez le nom de l'adherent: ")
    req = """delete from Adherent
    where id = ?
        and nom = ?"""
    c.execute(req,(id, adh))
    conn.commit()
    conn.close()

def ajout_bd():
    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    Auteur = input("entrez le nom de l'auteur: ")
    dessinateur = input("entrez le nom du dessinateur: ")
    Titre = input("entrez le titre: ")
    req = ("""insert into bandeD (Auteur, dessinateur, Titre)
    values (?, ?, ?)""")
    c.execute(req, (Auteur, dessinateur, Titre))
    conn.commit()
    conn.close()

ajout_bd()