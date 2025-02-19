import sqlite3

from PyQt6.QtWidgets import QApplication, QPushButton, QTextEdit, QLabel, QGridLayout, QWidget, QLineEdit, QTableWidget, \
    QTableWidgetItem

from Cours_POO.tp1.tp2.tp2 import zonetext


class Adherent:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

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

        zonetext.clear()
        if self.est_adherent():
            zonetext.setText(f"Ajout impossible car --{self.prenom} {self.nom}-- est deja adherent")
        else:
            conn = sqlite3.connect('bibliotheque')
            c = conn.cursor()
            c.execute("insert into adherent (prenom, nom) values (?, ?)", (self.prenom, self.nom))
            conn.commit()
            conn.close()
            zonetext.setText(f"--{self.prenom} {self.nom}-- a ete ajoute a la liste des adherent de la bibliotheque")

    def supprimer_adherent(self):
        zonetext.clear()
        if self.est_adherent():
            conn = sqlite3.connect('bibliotheque')
            c = conn.cursor()
            c.execute("delete from adherent where prenom =? and nom = ?", (self.prenom, self.nom))
            conn.commit()
            conn.close()
            zonetext.setText(f"-{self.prenom} {self.nom}- a ete supprime de la liste des adherents de la bibliotheque")
        else:
            zonetext.setText(f"Suppression impossible car -{self.prenom} {self.nom}- n'est pas un adherent de la bibliotheque")

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
        ql = [QLabel(x) for x in ('Entrez le titre', 'Entrez le date')]
        qle = []
        for i in range(2):
            grid.addWidget(ql[i], 4, 2+i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2+i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)
        def valider():
            titre = qle[0].text()
            date = qle[1].text()
            if titre and date:
                j1 = Journal(titre, date)
                j1.ajout_journal()
            for i in range(2):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()
        but.clicked.connect(valider)

    @classmethod
    def lire_clavier_sup(cls):
        ql = [QLabel(x) for x in ('Entrez le titre', 'Entrez le date')]
        qle = []
        for i in range(2):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            date = qle[1].text()
            if titre and date:
                j1 = Journal(titre, date)
                j1.supprimer_journal()
            for i in range(2):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)


    def ajout_journal(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into journal (titre, date) values (?, ?)"""
        c.execute(req, (self.titre, self.date))
        zonetext.setText(f"Le journal --{self.titre}-- du --{self.date}-- a été ajouté ")
        conn.commit()
        conn.close()


    def supprimer_journal(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("""select * from journal""")
        ele = (self.titre, self.date)
        tab = [x for x in c.fetchall()]
        if ele in tab:
            c.execute("delete from journal where titre = ? and date = ?", (self.titre, self.date))
            zonetext.setText(f"Le journal --{self.titre}-- du --{self.date}-- a ete supprimer")
        else:
            zonetext.setText(f"Suppression impossible car {self.titre} du {self.date} n'est pas dans la bibliotheque")
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
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur")]
        qle = []
        for i in range(2):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            if titre and auteur:
                d1 = Dictionnaire(titre, auteur)
                d1.ajout_dictionnaire()
            for i in range(2):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)

    @classmethod
    def lire_clavier_sup(cls):
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur")]
        qle = []
        for i in range(2):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            if titre and auteur:
                d1 = Dictionnaire(titre, auteur)
                d1.supprimer_dictionnaire()
            for i in range(2):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)


    def ajout_dictionnaire(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into dictionnaire (titre, auteur) values (?, ?)"""
        c.execute(req, (self.titre, self.auteur))
        conn.commit()
        conn.close()
        zonetext.setText(f"--{self.titre}-- de --{self.auteur}-- a été ajoute a la bibliotheque")


    def supprimer_dictionnaire(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("delete from dictionnaire where titre = ? and auteur = ?",
                  (self.titre, self.auteur))
        conn.commit()
        conn.close()
        zonetext.setText(f"--{self.titre}-- de --{self.auteur}-- a été supprime de la bibliotheque")

class Livre(Volume):
    def __init__(self, titre, auteur, ISBN):
        super().__init__(titre, auteur)
        self.ISBN = ISBN
    @classmethod
    def lire_clavier(cls):
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur", "Entrez l'ISBN" )]
        qle = []
        for i in range(3):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            ISBN = qle[2].text()
            if titre and auteur:
                l1 = Livre(titre, auteur, ISBN)
                l1.ajout_livre()
            for i in range(3):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)

    @classmethod
    def lire_clavier_sup(cls):
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur", "Entrez l'ISBN")]
        qle = []
        for i in range(3):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            ISBN = qle[2].text()
            if titre and auteur:
                l1 = Livre(titre, auteur, ISBN)
                l1.supprimer_livre()
            for i in range(3):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)

    def ajout_livre(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into livre (titre, auteur, ISBN)
        values (?, ?, ?)"""
        c.execute(req, (self.titre, self.auteur, self.ISBN))
        conn.commit()
        conn.close()
        zonetext.setText(f"--{self.titre}-- de --{self.auteur}-- a été ajoute a la bibliotheque")
    #@classmethod
    def supprimer_livre(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("""select ISBN from livre""")
        tab = [x[0] for x in c.fetchall()]
        ele = self.ISBN
        if ele in tab:
            c.execute("delete from livre where ISBN = ?", (ele,))
            zonetext.setText(f"({self.titre} de {self.auteur} a ete supprime de la bibliotheque")
        else:
            zonetext.setText(f"Erreur {self.titre} de {self.auteur} ne peut pas etre supprimer car n'existe pas dans la bibliotheque")
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
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur", "Entrez le dessinateur")]
        qle = []
        for i in range(3):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            dessinateur = qle[2].text()
            if titre and auteur:
                b1 = BandeD(titre, auteur, dessinateur)
                b1.ajout_bandeD()
            for i in range(3):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)

    @classmethod
    def lire_clavier_sup(cls):
        ql = [QLabel(x) for x in ('Entrez le titre', "Entrez l'auteur", "Entrez le dessinateur")]
        qle = []
        for i in range(3):
            grid.addWidget(ql[i], 4, 2 + i)
            qle.append(QLineEdit())
            grid.addWidget(qle[i], 5, 2 + i)
        but = QPushButton('Valider')
        grid.addWidget(but, 6, 2)

        def valider():
            titre = qle[0].text()
            auteur = qle[1].text()
            dessinateur = qle[2].text()
            if titre and auteur:
                b1 = BandeD(titre, auteur, dessinateur)
                b1.supprimer_bandeD()
            for i in range(3):
                ql[i].deleteLater()
                qle[i].deleteLater()
            but.deleteLater()

        but.clicked.connect(valider)

    def ajout_bandeD(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        req = """insert into bandeD (titre, auteur, dessinateur)
        values (?, ?, ?)"""
        c.execute(req, (self.titre, self.auteur, self.dessinateur))
        conn.commit()
        conn.close()
        zonetext.setText(f"La bande dessinée --{self.titre}-- de --{self.auteur} a été ajoute a la bibliotheque")


    def supprimer_bandeD(self):
        zonetext.clear()
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from bandeD")
        ele = (b.titre, b.auteur, b.dessinateur)
        tab = [x for x in c.fetchall()]
        if ele in tab:
            c.execute("delete from bandeD where auteur = ? and titre = ? and dessinateur = ? ",
                       (self.auteur, self.titre, self.dessinateur))
            zonetext.setText(f"La bande dessinee {self.titre} a ete supprimer de la bibliotheque")
        else:
            zonetext.setText("Suppression impossible. Cette bande dessinee n'existe pas dans la bibliotheque")
        conn.commit()
        conn.close()

class Bibliotheque:
    def __init__(self):
        self.adherent = []

    def ajout_adherent(self):

        q = [QLabel(x) for x in ('Entrez le prenom', 'Entrez le nom')]  #ajouter les champs qLabel
        g = [grid.addWidget(q[i], 4, 2 + i) for i in range(2)]
        q1e = [QLineEdit(), QLineEdit()]
        g1 = [grid.addWidget(q1e[i], 5, 2 + i) for i in range(2)]  # Ajouter les champs QLineEdit
        but_valider = QPushButton('Valider')    #boutton valider
        grid.addWidget(but_valider, 6, 2)
        def valider():       #fonction de boutton valider
            prenom = q1e[0].text()
            nom = q1e[1].text()
            if prenom and nom:
                adh = Adherent(prenom, nom)
                adh.ajout_adherent()   #enregistrer l'adherent dans la base de donnee
                for i in range(2):
                    q[i].deleteLater()       #effacer le boutons utiliser
                    q1e[i].deleteLater()
                but_valider.deleteLater()

        but_valider.clicked.connect(valider)

    def supprimer_adherent(self):

        q = [QLabel(x) for x in ('Entrez le prenom', 'Entrez le nom')]  # ajouter les champs qLabel
        g = [grid.addWidget(q[i], 4, 2 + i) for i in range(2)]
        q1e = [QLineEdit(), QLineEdit()]
        g1 = [grid.addWidget(q1e[i], 5, 2 + i) for i in range(2)]  # Ajouter les champs QLineEdit
        but_valider = QPushButton('Valider')  # boutton valider
        grid.addWidget(but_valider, 6, 2)

        def valider():  # fonction de boutton valider
            prenom = q1e[0].text()
            nom = q1e[1].text()
            if prenom and nom:
                adh = Adherent(prenom, nom)
                adh.supprimer_adherent()  # supprimer l'adherent dans la base de donnee
                for i in range(2):
                    q[i].deleteLater()  # effacer le boutons utiliser
                    q1e[i].deleteLater()
                but_valider.deleteLater()

        but_valider.clicked.connect(valider)

    def afficher_adherent(self):
        #zonetext.deleteLater()
        zone = QTableWidget()
        grid.addWidget(zone, len(button), 3)


        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from adherent")
        ad = c.fetchall()
        zone.setRowCount(len(ad))
        zone.setColumnCount(2)
        zone.setHorizontalHeaderLabels(['PRENOM', 'NOM'])

        #zonetext.clear()
        #zonetext.setText("LISTE DES ADHERENT DE LA BIBLIOTHEQUE\n\n")
        #for a in ad:
            #zonetext.setText(f"{a[0]} --{a[1]} {a[2]}--" )
            #zonetext.append(f"{a[0]} --{a[1]} {a[2]}--\n")
        for i in range(len(ad)):
            zone.setItem(i, 0, QTableWidgetItem(ad[i][1]))
            zone.setItem(i, 1, QTableWidgetItem(ad[i][2]))
        conn.close()

        but = QPushButton('Clear')
        grid.addWidget(but, len(button)+1, 3)
        def clear():
            zone.deleteLater()
            but.deleteLater()

        but.clicked.connect(clear)



    def ajout_document(self):
        zonetext.clear()
        ql = QLabel("Selectionnez le document a ajouter")
        grid.addWidget(ql,1, 2)
        ql1 = QLabel("1-JOURNAL \n2- LIVRE \n3- BANDE DESSINE \n4- DICTIONNAIRE")
        grid.addWidget(ql1, 2, 2)
        ql2 = QLabel("Entrez un chiffre parmi les suivant selon votre choix 1,2,3,4")
        grid.addWidget(ql2, 6, 2)
        qle = QLineEdit()
        grid.addWidget(qle, 6, 3)
        but_valider = QPushButton('Valider')
        grid.addWidget(but_valider, 7, 3)
        def valider():
            choix = qle.text()   #Recuperer la saisie au clavier
            if choix not in ['1','2','3','4']:
                ql2.setText("Erreur : choix erroné. Recommencer juste les chiffres de 1 a 4 : ")
                qle.clear()   # effacer l'entree utilisateur
                return
            ql.deleteLater()
            ql1.deleteLater()
            ql2.deleteLater()
            qle.deleteLater()
            but_valider.deleteLater()
            # Journal.ajout_journal()
            if choix == '1':
                Journal.lire_clavier()
            elif choix == '2':
                Livre.lire_clavier()
            elif choix == '3':
                BandeD.lire_clavier()
            elif choix == '4':
                Dictionnaire.lire_clavier()
        but_valider.clicked.connect(valider)

    def supprimer_document(self):
        ql = QLabel("Selectionnez le document a supprimerr")
        grid.addWidget(ql, 1, 2)
        ql1 = QLabel("1-JOURNAL \n2- LIVRE \n3- BANDE DESSINE \n4- DICTIONNAIRE")
        grid.addWidget(ql1, 2, 2)
        ql2 = QLabel("Entrez un chiffre parmi les suivants selon votre choix 1,2,3,4")
        grid.addWidget(ql2, 6, 2)
        qle = QLineEdit()
        grid.addWidget(qle, 6, 3)
        but_valider = QPushButton('Valider')
        grid.addWidget(but_valider, 7, 3)

        def valider():
            choix = qle.text()  # Recuperer la saisie au clavier
            if choix not in ['1', '2', '3', '4']:
                ql2.setText("Erreur : choix erroné. Recommencer juste les chiffres de 1 a 4 : ")
                qle.clear()  # effacer l'entree utilisateur
                return
            ql.deleteLater()
            ql1.deleteLater()
            ql2.deleteLater()
            qle.deleteLater()
            but_valider.deleteLater()
            # Journal.ajout_journal()
            if choix == '1':
                Journal.lire_clavier_sup()
            elif choix == '2':
                Livre.lire_clavier_sup()
            elif choix == '3':
                BandeD.lire_clavier_sup()
            elif choix == '4':
                Dictionnaire.lire_clavier_sup()

        but_valider.clicked.connect(valider)

    def afficher_doc(self):
        #zonetext.deleteLater()
        titre = QLabel("LISTE DES LIVRES DISPONIBLES DANS LA BIBLIOTHEQUE")
        grid.addWidget(titre,len(button)-1, 3)
        zone = QTableWidget()
        grid.addWidget(zone, len(button), 3)
        conn = sqlite3.connect('bibliotheque')
        c = conn.cursor()
        c.execute("select * from livre")
        li = c.fetchall()
        zone.setRowCount(len(li))
        zone.setColumnCount(3)
        #zone.setHorizontalHeader("LISTE DES LIVRES DISPONIBLES LA BIBLIOTHEQUE")
        zone.setHorizontalHeaderLabels(['TITRE', 'AUTEUR', 'ISBN' ])
        for i in range(len(li)):
            zone.setItem(i, 0, QTableWidgetItem(li[i][1]))
            zone.setItem(i, 1, QTableWidgetItem(li[i][2]))
            zone.setItem(i, 2, QTableWidgetItem(li[i][3]))

        titre1 = QLabel("LISTE DES JOURNAUX DE LA BIBLIOTHEQUE")
        grid.addWidget(titre1,len(button)-1, 5)
        zone1 = QTableWidget()
        grid.addWidget(zone1, len(button), 5)
        c.execute("select * from journal")
        jourl = c.fetchall()
        zone1.setRowCount(len(jourl))
        zone1.setColumnCount(2)
        zone1.setHorizontalHeaderLabels(['TITRE', 'DATE'])
        for i in range(len(jourl)):
            zone1.setItem(i, 0, QTableWidgetItem(jourl[i][1]))
            zone1.setItem(i, 1, QTableWidgetItem(jourl[i][2]))

        titre3 = QLabel("LISTE DES BANDES DESSINNEES DE LA BIBLIOTHEQUE")
        grid.addWidget(titre3, 6, 3)
        zone3 = QTableWidget()
        grid.addWidget(zone3, 7, 3)
        c.execute("select * from bandeD")
        bd = c.fetchall()
        zone3.setRowCount(len(bd))
        zone3.setColumnCount(3)
        zone3.setHorizontalHeaderLabels(['TITRE', 'AUTEUR', 'DESSINATEUR'])
        for i in range(len(bd)):
            zone3.setItem(i, 0, QTableWidgetItem(bd[i][1]))
            zone3.setItem(i, 1, QTableWidgetItem(bd[i][2]))
            zone3.setItem(i, 2, QTableWidgetItem(bd[i][3]))

        titre4 = QLabel("LISTE DES DICTIONNAIRE DE LA BIBLIOTHEQUE")
        grid.addWidget(titre4, 6, 5)
        zone4 = QTableWidget()
        zone4 = QTableWidget()
        grid.addWidget(zone4, 7, 5)
        c.execute("select * from dictionnaire")
        dico = c.fetchall()
        zone4.setRowCount(len(dico))
        zone4.setColumnCount(2)
        zone4.setHorizontalHeaderLabels(['TITRE', 'AUTEUR'])
        for i in range(len(dico)):
            zone4.setItem(i, 0, QTableWidgetItem(dico[i][1]))
            zone4.setItem(i, 1, QTableWidgetItem(dico[i][2]))

        conn.close()
        but = QPushButton('clear')
        grid.addWidget(but, len(button)+2, 5)
        def clear():
            zone.deleteLater()
            zone1.deleteLater()
            zone3.deleteLater()
            zone4.deleteLater()
            titre.deleteLater()
            titre1.deleteLater()
            titre3.deleteLater()
            titre4.deleteLater()
            but.deleteLater()
        but.clicked.connect(clear)





app = QApplication([])
fen = QWidget()
grid = QGridLayout()
fen.setLayout(grid)

#Qlabel
acceuil = QLabel("BIENVENUE DANS LA BIBLIOTHE DE ALEXANDRE ET TJ")
grid.addWidget(acceuil, 0, 3)

#buton = QPushButton("ajouter adherent")
#grid.addWidget(buton, 1, 1)
tab = ['Ajouter adherent', 'Supprimer adherent', 'Afficher tous les adherents', 'Ajouter documents', 'Supprimer documents', 'Afficher documents', 'Ajouter emprunt', 'Retour emprunt', 'Afficher tous les emprunts', 'Quitter']
button = [QPushButton(x) for x in tab]
for i in range(len(button)):
    position = [grid.addWidget(button[i], i+1, 1) ]

#QTextedit
zonetext = QTextEdit()
grid.addWidget(zonetext, len(button), 3)
b = Bibliotheque()
#QLinedit
#QTableWidget





button[2].clicked.connect(b.afficher_adherent)
button[0].clicked.connect(b.ajout_adherent)
button[1].clicked.connect(b.supprimer_adherent)
button[3].clicked.connect(b.ajout_document)
button[4].clicked.connect(b.supprimer_document)
button[5].clicked.connect(b.afficher_doc)
#button[6].clicked.connect(b.ajout_emprunt)
#button[7].clicked.connect(b.retour_emprunt)


fen.show()
app.exec()