import sqlite3

from Cours_POO.tp1.tp2.methode import valider_date

#conn = sqlite3.connect('bibliotheque')
#c = conn.cursor()
req5 = """create table if not exists adherent(
        id integer primary key autoincrement,
        prenom text,
        nom text)"""
req1 = """create table livre(
        id integer primary key autoincrement,
        titre text,
        auteur text,
        ISBN text) """
req2 = """create table journal(
          id integer primary key autoincrement,
          titre text,
          date)"""
req3 = """create table bandeD(
          id integer primary key autoincrement,
          titre text,
          auteur text,
          dessinateur text)
          """
req4 = """create table dictionnaire(
          id integer primary key autoincrement,
          titre text,
          auteur text)"""
#c.execute(req4)
#conn.commit()
#conn.close()



class Adherent:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

class Document:
    def __init__(self, titre):
        self.titre = titre


class Journal(Document):
    def __init__(self, titre, date):
        super().__init__(titre)
        self.date = date

    @classmethod
    def lire_clavier(cls):
        titre = input("Titre du journal: ")
        date = str(valider_date())
        return Journal(titre, date)
    @classmethod
    def ajout_journal(cls):
        j = Journal.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into journal (titre, date) values (?, ?)"""
        c.execute(req, (j.titre, j.date))
        print(f"Le journal --{j.titre}-- du --{j.date}-- a été ajouté ")
        conn.commit()
        conn.close()

    @classmethod
    def supprimer_journal(cls):
        j = Journal.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("""select * from journal""")
        ele = (j.titre, j.date)
        tab = [x for x in c.fetchall()]
        if ele in tab:
            c.execute("delete from journal where titre = ? and date = ?", (j.titre, j.date))
            print(f"Le journal --{j.titre}-- du --{j.date}-- a ete supprimer")
        else:
            print(f"Suppression impossible car {j.titre} du {j.date} n'est pas dans la bibliotheque")
        conn.commit()
        conn.close()

class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

class Dictionnaire(Volume):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)

    @classmethod
    def lire_clavier(cls):
        titre = input("Titre du dictionnaire: ")
        auteur = input("Auteur du dictionnaire: ")
        return Dictionnaire(titre, auteur)

    @classmethod
    def ajout_dictionnaire(cls):
        d = Dictionnaire.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into dictionnaire (titre, auteur) values (?, ?)"""
        c.execute(req, (d.titre, d.auteur))
        conn.commit()
        conn.close()
        print(f"--{d.titre}-- de --{d.auteur}-- a été ajoute a la bibliotheque")

    @classmethod
    def supprimer_dictionnaire(cls):
        d = Dictionnaire.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("""delete from dictionnaire where titre = ? and auteur = ?, 
                  (d.titre, d.auteur)""")
        conn.commit()
        conn.close()

class Livre(Volume):
    def __init__(self, titre, auteur, ISBN):
        super().__init__(titre, auteur)
        self.ISBN = ISBN
    @classmethod
    def lire_clavier(cls):
        titre = input('Titre du livre: ')
        auteur = input("Auteur du livre: " )
        ISBN = input('ISBN du livre: ')
        return Livre(titre, auteur, ISBN)
    @classmethod
    def ajout_livre(cls):
        l = Livre.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into livre (titre, auteur, ISBN)
        values (?, ?, ?)"""
        c.execute(req, (l.titre, l.auteur, l.ISBN))
        conn.commit()
        conn.close()
        print(f"--{l.titre}-- de --{l.auteur}-- a été ajoute a la bibliotheque")
    @classmethod
    def supprimer_livre(cls):
        l = Livre.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("""select ISBN from livre""")
        tab = [x[0] for x in c.fetchall()]
        ele = l.ISBN
        if ele in tab:
            c.execute("""delete from livre where ISBN = ?, (ele,)""")
            print(f"({l.titre} de {l.auteur} a ete supprime de la bibliotheque")
        else:
            print(f"Erreur {l.titre} de {'.auteur'} ne peut pas etre supprimer car n'existe pas dans la bibliotheque")
        conn.commit()
        conn.close()

class BandeD(Volume):
    def __init__(self, titre, auteur, dessinateur):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur

    @classmethod
    def lire_clavier(cls):
        titre = input('Titre de la bande Dessinnée: ')
        auteur = input("Auteur de la bande Dessinnée: ")
        dessinateur = input("Dessinateur de la bande Dessinnée: ")
        return BandeD(titre, auteur, dessinateur)

    @classmethod
    def ajout_bandeD(cls):
        b = BandeD.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into bandeD (titre, auteur, dessinateur)
        values (?, ?, ?)"""
        c.execute(req, (b.titre, b.auteur, b.dessinateur))
        conn.commit()
        conn.close()
        print(f"La bande dessinée --{b.titre}-- de --{b.auteur} a été ajoute a la bibliotheque")

    @classmethod
    def supprimer_bandeD(cls):
        b = BandeD.lire_clavier()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from bandeD")
        ele = (b.titre, b.auteur, b.dessinateur)
        tab = [x for x in c.fetchall()]
        if ele in tab:
            c.execute("""delete from bandeD where auteur = ? and titre = ? and dessinateur = ?,
                       (b.auteur, b.titre, b.dessinateur)""")
            print(f"La bande dessinee {b.titre} a ete supprimer de la bibliotheque")
        else:
            print("Suppression impossible. Cette bande dessinee n'existe pas dans la bibliotheque")
        conn.commit()
        conn.close()

class emprunt:
    def __init__(self, adh, livre):
        self.adh = adh
        self.livre = livre




class Bibliotheque:
    pass

    def ajout_document(self):
        print("Selectionnez le document a ajouter")
        print("1-JOURNAL \n2- LIVRE \n3- BANDE DESSINE \n4- DICTIONNAIRE")
        choix = input("Entrez un chiffre parmi les suivant selon votre choix 1,2,3,4: ")
        while choix not in ['1','2','3','4']:
            choix = input("Erreur choix erroné. Recommencer: ")
        if choix == '1':
           Journal.ajout_journal()
        elif choix == '2':
            Livre.ajout_livre()
        elif choix == '3':
            BandeD.ajout_bandeD()
        elif choix == '4':
            Dictionnaire.ajout_dictionnaire()

    def supprimer_document(self):
        print("Selectionnez le document a supprimer")
        print("1-JOURNAL \n2- LIVRE \n3- BANDE DESSINE \n4- DICTIONNAIRE")
        choix = input("Entrez un chiffre parmi les suivant selon votre choix 1,2,3,4 : ")
        while choix not in ['1', '2', '3', '4']:
            choix = input("Erreur choix errone. Recommencer : ")
        if choix == '1':
            Journal.supprimer_journal()
        elif choix == '2':
            Livre.supprimer_livre()
        elif choix == '3':
            BandeD.supprimer_bandeD()
        elif choix == '4':
            Dictionnaire.supprimer_dictionnaire()

    def afficher_doc(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from livre")
        li = c.fetchall()
        print()
        print("LISTE DES LIVRES DISPONIBLES LA BIBLIOTHEQUE")
        for x in li:
            print(f"{x[0]} | {x[1]}  |  {x[2]}   | {x[3]}")
        c.execute("select * from journal")
        jourl = c.fetchall()
        print()
        print("LISTE DES JOURNAUX DE LA BIBLIOTHEQUE")
        for x in jourl:
            print(f"{x[0]}   |   {x[1]}   |    {x[2]}")
        c.execute("select * from bandeD")
        bd = c.fetchall()
        print()
        print("LISTE DES BANDES DESSINNEES DE LA BIBLIOTHEQUE")
        for x in bd:
            print(f"{x[0]}  |  {x[1]}    |   {x[2]}    |   {x[3]}")
        c.execute("select * from dictionnaire")
        dico = c.fetchall()
        print()
        print("LISTE DES DICTIONNAIRE DE LA BIBLIOTHEQUE")
        for x in dico:
            print(f"{x[0]}   |   {x[1]}    |   {x[2]}")
        conn.close()







b = Bibliotheque()
#b.ajout_document()
b.afficher_doc()