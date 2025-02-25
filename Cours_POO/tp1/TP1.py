from datetime import datetime
import pandas
import csv

from Cours_POO.tp1.mehode import extrait, extrait_c1, extrait_csv, valider_date, ecrire_csv, csv_dictreader, \
    csv_dictwriter


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
        tab = extrait_csv('livre.csv')
        y = [self.titre, self.auteur]
        if y in tab:
            return True
        return False
    def ajout_livre(self):
        liste = extrait_csv('livre.csv')
        l1 = [self.titre,self.auteur]
        liste.append(l1)
        ecrire_csv('livre.csv', liste)
        print(f"{self.titre} de {self.auteur} a ete ajoute a la bibliotheque")
    def enlever_livre(self):
        tab = extrait_csv('livre.csv')
        try:
            tab.remove([self.titre,self.auteur])
            ecrire_csv('livre.csv', tab)
            print(f"{self.titre} de {self.auteur} a ete retire de la bibliotheque")
        except FileNotFoundError:
            print("Ce livre n'est pas dans la bibliotheque")




#Sous classe de Document et Volume

class Bande_dessine(Volume):
    def __init__(self,titre, auteur, dessinateur):
        self.dessinateur = dessinateur
        super().__init__(titre,auteur)

    def ajout_bd(self):
        with open('bande_d.csv','r', newline='') as f:
            w = csv.DictReader(f)
            tab = list(w)
        bool = False
        for x in tab:
            if x['Titre'] == self.titre and x['Auteur'] == self.date and x['Dessinateur'] == self.dessinateur:
                x['Quantite'] = int(x['Quantite'])+1
                bool = True
                break
        if bool == False:
            tab.append({'Titre':self.titre, "Auteur":self.auteur, 'Dessinateur':self.dessinateur, 'Quantite':1})
        #update la base de donnee
        with open('bande_d.csv','w') as f:
            w = csv.DictWriter(f,['Titre', 'Auteur','Dessinateur','Quantite'])
            w.writeheader()
            w.writerows(tab)

    def enlever_bd(self):
        tab = csv_dictreader('bande_d.csv')
        bool = False
        for x in tab:
            if x['Titre'] == self.titre and x['Auteur'] == self.date and x['Dessinateur'] == self.dessinateur and x['Quantite'] >1:
                x['Quantite'] = int(x['Quantite']) - 1
                bool = True
                break
        if bool == False:
            tab.remove({'Titre': self.titre, "Auteur": self.auteur, 'Dessinateur': self.dessinateur, 'Quantite': 1})






#Sous classe de Volume

class dictionnaire(Volume):
    def __init__(self, titre):
        super().__init__(titre)

#Sous classe de Document

class Journal(Document):
    def __init__(self, titre, date):
        self.date = date
        super().__init__(titre)
    def ajout_journal(self):
        tab = csv_dictreader('journal.csv')

        bool = False
        for x in tab:
            if x['Titre'] == self.titre and x['Date'] == self.date and int(x['Quantite']) >=1:
                x['Quantite'] = int(x['Quantite'])+1
                bool = True
                break
            else:
                tab.append({'Titre':self.titre, 'Date':self.date, 'Quantite':1})
                break
        #Updater la base de donnee
        with open('journal.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, ['Titre', 'Date', 'Quantite'], delimiter=';')
            w.writeheader()
            w.writerows(tab)
        print('Journal ajoute avec succes')

    def enlenver_journal(self):
        tab = []
        tab = csv_dictreader('journal.csv')
        bool = False
        for x in tab:
            if x['Titre'] == self.titre and x['Date'] == self.date and int(x['Quantite']) > 1:
                x['Quantite'] = int(x['Quantite'])-1
                bool = True
                break
            else:
                tab.remove({'Titre': self.titre, "Date": self.date, "Quantite": '1'})
                break
        #Updater la base de donnee
        ent = ['Titre', 'Date', 'Quantite']
        csv_dictwriter('journal.csv', tab, ent)
        print('Journal enlever avec succes')




class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def nom_prenom(self):
        return f"{self.nom} {self.prenom}"


class Emprunter:
    def __init__(self, adherent, livre,date):
        self.adherent = adherent
        self.livre = livre
        self.date_initial = datetime.now()
        self.date_return = date

    def enr_emprunt(self):
        time_i = self.date_initial
        time_r = self.date_return
        adh = [self.adherent.nom +' '+ self.adherent.prenom, self.livre.titre, self.livre.auteur, str(time_i), str(time_r)]
        tab = extrait_csv('emprunt.csv')
        tab.append(adh)
        ecrire_csv('emprunt.csv', tab)

class Bibliotheque:
    def __init__(self):
       self.emprunt = []

    def ajout_adherent(self, adherent):
        nom = adherent.nom
        prenom = adherent.prenom
        adherent = Adherent(nom, prenom)
        try:
            with open('adherent.csv', 'r') as f:
                tab = []
                reader = csv.reader(f)
                for x in reader:
                    if any(x):
                        tab.append(x)
            adh = [nom +' '+ prenom]
            if adh in tab:
                print(f"impossible d'ajouter {adherent.nom_prenom()} car il est deja adherent")
            else:
                tab.append(adh)
                print(f"{adherent.nom_prenom()} a ete ajoute avec succes")
                ecrire_csv('Adherent.csv', tab)
        except FileNotFoundError:
            print("fichier adherent.csv introuvable")

    def enlever_adherent(self, obj):
        tab = extrait_csv('adherent.csv')
        try:
            tab.remove([obj.nom+' '+obj.prenom])
            ecrire_csv('adherent.csv', tab)
            print("Supression reussie")
        except ValueError:
            print("Erreur, cet individu ne figure pas dans la liste des adherents")

    def ajout_emprunt(self):
        nom = input("Entrez le nom de l'adherent : ")
        prenom = input("Entrez le prenom de l'adherent: ")
        ind = [nom+' '+prenom]
        tab = extrait_csv('adherent.csv')
        tab_emp = extrait_c1('emprunt.csv')
        if ind in tab:
            if ind[0] not in tab_emp:
                titre = input("Entrez le titre du livre solicite: ")
                auteur = input("Entrez l'auteur du livre solicite: ")
                livre = Livre(titre, auteur)
                if livre.est_disponible() == True:
                    emp = Emprunter(Adherent(nom, prenom), livre, valider_date()).enr_emprunt()
                    livre.enlever_livre()
                    print('Emprunt valide et enregistre avec succes')
                else:
                    return print("Desole ce livre n'est pas disponible")

            else:
                return print("Emprunt impossible, veuillez retourner les precedents documents")
        else:
            print("Emprunt impossible; n'est pas adherent")

    def retour_emprunt(self,objadh,objli):
        tab = extrait_csv('emprunt.csv')
        for x in tab:
            if x[0] == objadh.nom_prenom() and x[1] == objli.titre and x[2] == objli.auteur:
                tab.remove(x)
                ecrire_csv('emprunt.csv', tab)
                objli.ajout_livre()
                return print("Document retourner.")
        print("Erreur livre non reconnu")

    def afficher_emprunt(self):
        liste = extrait_csv('emprunt.csv')
        print('LISTE DES EMPRUNTS')
        for x in liste:
            print(f"{x[0]}    |  {x[1]}      |{x[2]}       |{x[3]}    |{x[4]}  ")

    def Afficher_adherent(self):
        print("LISTE DES ADHERENTS")
        liste = extrait_csv('adherent.csv')
        for x in liste:
            print(x[0])

    def ajout_documents(self):
        print("Selectionner le document a ajouter")
        print("1--journal\n2--Livre\n3--Bande dessinnee\n")
        choix = input(": ")
        while choix in ['1', '2', '3']:
            if choix == '1':
                titre = input("Entrez le titre du journal:  ")
                date = valider_date()
                Journal(titre, date).ajout_journal()
            elif choix == '2':
                titre = input("Entrez le titre du livre: ")
                auteur = input("entrez l'auteur: ")
                Livre(titre, auteur).ajout_livre()
            elif choix  == '3':
                titre = input("Entrez le titre de la bande dessinee: ")
                auteur = input("entrez l'auteur: ")
                dess = input("Entrez le nom du dessinnateur:  ")
                Bande_dessine(titre, auteur, dess).ajout_bd()
            return

    def afficher_documents(self):
        tab1 = extrait_csv('journal.csv')
        tab2 = extrait_csv('livre.csv')
        tab3 = extrait_csv('bande_d.csv')
        print("LISTE DES JOURNAUX EN STOCK")
        for x in tab1:
            print(f"{x[0]}   |    {x[1]}    |{x[2]}")
        print()
        print("LISTE DES LIVRES EN STOCK")
        print(tab2)
        for x in tab2:
            print(f"{x[0]}   |    {x[1]}")
        print()
        print("LISTES DES BANDES DESSINNEES DISPONIBLE")
        for x in tab3:
            print(f"{x[0]}   |    {x[1]}     |{x[2]}   |{x[3]}")

    def supprimer_doc(self):
        print("Selectionner le document a supprimer")
        choix = input(" 1--journal\n2--Livre\n3--Bande dessinnee")
        while choix in ['1', '2', '3']:
            if choix == '1':
                titre = input("Entrez le titre du journal:  ")
                date = valider_date()
                Journal(titre, date).enlenver_journal()
            elif choix == '2':
                titre = input("Entrez le titre du livre: ")
                auteur = input("entrez l'auteur: ")
                Livre(titre, auteur).enlever_livre()
            elif choix == '3':
                titre = input("Entrez le titre de la bande dessinee: ")
                auteur = input("entrez l'auteur: ")
                dess = input("Entrez le nom du dessinnateur:  ")
                Bande_dessine(titre, auteur, dess).enlever_bd()
            return

    def lancer_biblio(self):
        while True:

            print("""
    Choix de l'operation:"
    1. Ajouter un adhérent
    2. Supprimer un adhérent
    3. Afficher tous les adhérents
    4. Ajouter un document
    5. Supprimer un document
    6. Afficher tous les documents
    7. Ajouter un emprunt
    8. Retour d'un emprunt
    9. Afficher tous les emprunts
    10. Quitter
    """)
            choix = input("Quelle operation vous sollicetez? : ")
            if choix == '1':
                nom = input("entrer le nom: ")
                prenom = input("entrer le prenom: ")
                obj = Adherent(nom, prenom)
                b1.ajout_adherent(obj)
            elif choix == '2':
                nom = input("entrer le nom: ")
                prenom = input("entrez le prenom : ")
                obj = Adherent(nom, prenom)
                b1.enlever_adherent(obj)
            elif choix == '3':
                b1.Afficher_adherent()
            elif choix =='4':
                b1.ajout_documents()
            elif choix == '5':
                b1.supprimer_doc()
            elif choix == '6':
                b1.afficher_documents()
            elif choix == '7':
                b1.ajout_emprunt()
            elif choix == '8':
                nom = input("Entrez le nom de l'adherent : ")
                prenom = input("Entrez le prenom de l'adherent: ")
                objadh = Adherent(nom, prenom)
                titre = input("Entrez le titre du livre solicite: ")
                auteur = input("Entrez l'auteur du livre solicite: ")
                objli = Livre(titre, auteur)
                b1.retour_emprunt(objadh, objli)
            elif choix == '9':
                b1.afficher_emprunt()
            elif choix == '10':
                break
            else:
                print("Erreur de saisie, les choix sont des nombres entiers de 1 a 10 ")




b1 = Bibliotheque()
b1.lancer_biblio()

#b1.enlever_adherent(Adherent('Emma', 'Richelieu'))
#b1.ajout_adherent(Adherent('Pierre','Alain'))
#b1.ajout_adherent(Adherent('Pierre','Gaston'))
#b1.ajout_adherent(Adherent('Bosco','Parping'))
#b1.ajout_emprunt()
#b1.enlever_adherent(Adherent('Bosco','Parping'))
#b1.retour_emprunt(Adherent('Pierre', 'Gaston'), Livre('le solitaire', 'Rouseau'))
#b1.afficher_emprunt()
#b1.Afficher_adherent()
#b1.ajout_documents()






