import datetime
import csv
class Document:
    def __init__(self,titre):
        self.titre = titre

#Sous classe de Document

class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

#Sous classe de Document et Volume

class Livre(Volume):
    def __init__(self, titre, auteur):
        self.estdipo = True
        super().__init__(titre, auteur)
    def __str__(self):
        return f"{self.titre} de {self.auteur}"

    def est_disponible(self):
        pass

#Sous classe de Document et Volume

class Bande_dessine(Volume):
    def __init__(self,titre, auteur, dessinateur):
        self.dessinateur = dessinateur
        super().__init__(titre,auteur)

#Sous classe de Volume

class dictionnaire(Volume):
    def __init__(self, titre):
        super().__init__(titre)

#Sous classe de Document

class Journal(Document):
    def __init__(self, titre, date, nombre):
        self.date = date
        self.nombre = nombre
        super().__init__(titre)
    def ajout_journal(self):
        tab = []
        with open('journal.csv','r') as f:
            lig = f.readline()
            lig = f.readline()
            while lig != '':
                lig = lig.strip().split(';')
                dict = {'Titre': lig[0], 'Date': lig[1], 'Quantite': int(lig[2])}
                tab.append(dict)
                lig = f.readline()
        bool = False
        for x in tab:
            if x['Titre'] == self.titre and x['Date'] == self.date:
                x['Quantite'] += int(self.nombre)
                bool = True
                break
        if bool:
            tab.append({'Titre':self.titre, 'Date':self.date, 'Quantite':self.nombre})
        #Updater la base de donnee
        with open('journal.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, ['Titre', 'Date', 'Quantite'])
            w.writeheader()
            w.writerows(tab)










class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    def emprunt(self,livre):
        pass
    def nom_prenom(self):
        return self.nom + ' ' + self.prenom





class Emprunter:
    def __init__(self, adherent, livre):
        self.adherent = adherent
        self.livre = livre
        self.date_initial = datetime.now()
        self.date_return = input()
    def __str__(self):
        return f"{self.livre} emprunter par {self.adherent} "

    def enr_emprunt(self, adherent, livre):
        self.date_init = datetime.now()
        self.date_return = input()



class Bibliotheque:
    def __init__(self):
        self.adherent = []
        self.document = []
        self.emprunt = []

    def ajout_adherent(self,Adherent):
        tab = []
        with open('adherent.csv', 'r') as f:
            line = f.readline()
            line = f.readline()
            while line != '':
                line =line.strip().split(';')
                tab.append(line[0]+' '+line[1])
        if Adherent.nom_prenom() in tab:
            print("Cet individu est deja un adherent de la bibliotheque")
        else:
            tab.append(Adherent.nom_prenom())
        with open('adherent.csv','w') as f:
            f.writelines(tab)
    def enlever_adherent(self, Adherent):
        tab = []
        with open('adherent.csv', 'r') as f:
            line = f.readline()
            line = f.readline()
            while line != '':
                line = line.strip().split(';')
                tab.append(line[0] + ' ' + line[1])
            try:
                tab.remove(Adherent.nom_prenom())
            except FileNotFoundError:
                print("Erreur, cet individu ne figure pas dans la liste des adherents")
        with open('adherent.csv','w') as f:
            f.writelines(tab)

    def ajouter_document(self, Document):
        tipe = int(input('Selectionner le type de document' '\n1- Jounal' '\n2- Volume' ))
        #if tipe == 1:












