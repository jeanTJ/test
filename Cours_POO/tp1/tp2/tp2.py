import sqlite3

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit, QLabel, QPushButton

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
req6 = """create table emprunts(
                       id primary key autoincrement,
                       adherent text,
                       titre text,
                       auteurtext,
                       ISBN text,)"""
#c.execute(req4)
#conn.commit()
#conn.close()



class Adherent:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    @classmethod
    def lire_clavier(cls):
        prenom = input("Entrez le prenom: ")
        nom = input("Entrez le nom:")
        return Adherent(prenom, nom)

    def est_adherent(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from adherent")  # recuperer la liste des adherents
        ad = c.fetchall()
        for x in ad:
            if x[1] == self.prenom and x[2] == self.nom:  # Verifier si l'adherent est dans la liste
                conn.close()
                return True   #s'il est dans la liste
        conn.close()
        return False    #sinon

    def ajout_adherent(self):
        Adherent.lire_clavier()
        if self.est_adherent():
            print(f"Ajout impossible car --{self.prenom} {self.nom}-- est deja adherent")
        else:
            conn = sqlite3.connect('bibliotheque')
            c = conn.cursor()
            c.execute("insert into adherent (prenom, nom) values (?, ?)", (self.prenom, self.nom))
            conn.commit()
            conn.close()
            print(f"--{self.prenom} {self.nom}-- a ete ajoute a la liste des adherent de la bibliotheque")

    def supprimer_adherent(self):
        Adherent.lire_clavier()
        if self.est_adherent():
            conn = sqlite3.connect('bibliotheque')
            c = conn.cursor()
            c.execute("delete from adherent where prenom =? and nom = ?", (self.prenom, self.nom))
            conn.commit()
            conn.close()
            print(f"-{self.prenom} {self.nom}- a ete supprime de la liste des adherent de la bibliotheque")
        else:
            print(f"Suppression impossible car -{self.prenom} {self.nom}- n'est pas un adherent de la bibliotheque")

    #@classmethod
    #def ajout_adherent(cls):

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
        c.execute("delete from dictionnaire where titre = ? and auteur = ?",
                  (d.titre, d.auteur))
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
            c.execute("delete from livre where ISBN = ?", (ele,))
            print(f"({l.titre} de {l.auteur} a ete supprime de la bibliotheque")
        else:
            print(f"Erreur {l.titre} de {'.auteur'} ne peut pas etre supprimer car n'existe pas dans la bibliotheque")
        conn.commit()
        conn.close()

    def est_disponible(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from livre")
        li = c.fetchall()
        for x in li:
            if x[1] == self.titre and x[2] == self.auteur:
                conn.close()
                return True
        conn.close()
        return False

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
            c.execute("delete from bandeD where auteur = ? and titre = ? and dessinateur = ? ",
                       (b.auteur, b.titre, b.dessinateur))
            print(f"La bande dessinee {b.titre} a ete supprimer de la bibliotheque")
        else:
            print("Suppression impossible. Cette bande dessinee n'existe pas dans la bibliotheque")
        conn.commit()
        conn.close()

class Emprunt:
    def __init__(self, adh, livre):
        self.adh = adh
        self.livre = livre

    @classmethod
    def lire_clavier(cls):
        adh = Adherent.lire_clavier()  #creer un object adherent
        if not adh.est_adherent:
            print(f"Emprunt impossible car --{adh.prenom} {adh.nom}-- n'est pas adherent")
            return
        else:
            livre = Livre.lire_clavier() # creer le livre a emprunter
        return  Emprunt(adh, livre)     #retourne un object emprunt

    def enregistrer(self):
        if not self.livre.est_disponible():
            print(f"Emprunt impossible --{self.livre.titre}-- de --{self.livre.auteur}-- est indisponible")
            return   # Si le livre n'est pas disponible
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into emprunt (adherent, titre, auteur, ISBN)
                values (?, ?, ?, ?)"""
        c.execute(req, (f'{self.adh.prenom} {self.adh.nom}', self.livre.titre, self.livre.auteur, self.livre.ISBN))
        c.execute("delete from livre where ISBN = ?", (self.livre.ISBN,))
        conn.commit()
        conn.close()
        print(f"--{self.livre.titre}-- de --{self.livre.auteur}-- a ete emprunter par -{self.adh.prenom} {self.adh.nom}-")

    def retour_emprunt(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = "delete from emprunt where adherent = ? and titre = ? and auteur = ?"
        #supprimer l'emprunt
        c.execute(req, (f'{self.adh.prenom} {self.adh.nom}', self.livre.titre, self.livre.auteur))
        #remettre le livre en etagere afin qu'il soit disponible
        reql = "insert into livre (titre, auteur, ISBN) values (?, ?, ?)"
        c.execute(reql, (self.livre.titre, self.livre.auteur, self.livre.ISBN))
        conn.commit()
        conn.close()
        print(f"--{self.livre.titre}-- de --{self.livre.auteur}-- a ete retourne par -{self.adh.prenom} {self.adh.nom}-")




class Bibliotheque:

    def ajout_adherent(self):
        Adherent.lire_clavier().ajout_adherent()

    def supprimer_adherent(self):
        Adherent.lire_clavier().supprimer_adherent()

    def afficher_adherent(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from adherent")
        ad = c.fetchall()
        print(("LISTE DES ADHERENT DE LA BIBLIOTHEQUE"))
        for a in ad:
            print(f"{a[0]} --{a[1]} {a[2]}--" )
        conn.close()


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

    def ajout_emprunt(self):
        Emprunt.lire_clavier().enregistrer()

    def retour_emprunt(self):
        Emprunt.lire_clavier().retour_emprunt()

    def afficher_emprunt(self):
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute('select * from emprunt')
        empl = c.fetchall()
        print("LISTE DES EMPRUNTS DE LA BIBLIOTHEQUE")
        for x in empl:
            print(f"   {x[0]}   |   {x[1]}    |    {x[2]}    |   {x[3]}")





b = Bibliotheque()
#b.ajout_document()
#b.afficher_doc()

app = QApplication([])
fen = QWidget()
grid = QGridLayout()
fen.setLayout(grid)

#Qlabel
acceuil = QLabel("BIENVENUE DANS LA BIBLIOTHE DE ALEXANDRE ET TJ")
grid.addWidget(acceuil, 0, 3)

#buton = QPushButton("ajouter adherent")
#grid.addWidget(buton, 1, 1)
tab = ['Ajouter adherent', 'Supprimer adherent', 'Afficher tous les adherents', 'Ajouter documents', 'Supprimer documents', 'Ajouter emprunt', 'Retour emprunt', 'Afficher tous les emprunts', 'Quitter']
button = [QPushButton(x) for x in tab]
for i in range(len(button)):
    position = [grid.addWidget(button[i], i+1, 1) ]

#QTextedit
zonetext = QTextEdit()
grid.addWidget(zonetext, len(button), 3)





fen.show()
app.exec()