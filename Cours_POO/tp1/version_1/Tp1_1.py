from datetime import datetime

from Cours_POO.tp1.mehode import valider_date
from Cours_POO.tp1.version_1.methode_1 import extrait_txt, ecrire_txt


class Document:
    def __init__(self,titre):
        self.titre = titre
#Sous classe de Document

class Journal(Document):
    def __init__(self, titre, date):
        self.date = date
        super().__init__(titre)

    def ajout_journal(self):
        tab = extrait_txt('journal.txt')
        tab.append(f'{self.titre}, {self.date}\n')
        #Updater la base de donnee
        ecrire_txt('journal.txt', tab)
        print('Journal ajoute avec succes')

    def enlever_journal(self):
        tab = extrait_txt('journal.txt')
        for x in tab:
            y = x.strip().split(',')
            if y[0] == self.titre and y[1] == self.date:
                tab.remove(x)
                break
        print('Journal suprime avec succes')

class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur


class Bande_dessine(Volume):
    def __init__(self,titre, auteur, dessinateur):
        self.dessinateur = dessinateur
        super().__init__(titre,auteur)

    def ajout_bd(self):
        tab = extrait_txt('BD.txt')
        tab.append(f'{self.titre}, {self.auteur}, {self.dessinateur}\n')
        #update la base de donnee
        ecrire_txt('BD.txt', tab)

    def enlever_bd(self):
        tab = extrait_txt('BD.txt')
        for x in tab:
            y = x.strip().split(',')
            if y[0] == self.titre and y[1] == self.auteur and y[2] == self.dessinateur:
                tab.remove(f'{self.titre}, {self.auteur}, {self.dessinateur}\n')
                print('Bande dessinner enleve avec succes')
                break




class Livre(Volume):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)
    def __str__(self):
        return f"{self.titre} de {self.auteur}"

    def est_disponible(self):
        tab = extrait_txt('livre.txt')
        y = f'{self.titre}, {self.auteur}\n'
        for x in tab:
            if y == x:
                return True
        return False
    def ajout_livre(self):
        liste = extrait_txt('livre.txt')
        l1 = f'{self.titre}, {self.auteur}\n'
        liste.append(l1)
        ecrire_txt('livre.txt', liste)
        print('Ajout reussi')


    def enlever_livre(self):
        tab = extrait_txt('livre.txt')
        try:
            tab.remove(f'{self.titre}, {self.auteur}\n')
            ecrire_txt('livre.txt', tab)
            print('Livre supprime')
        except FileNotFoundError:
            print("Ce livre n'est pas dans la bibliotheque")



class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def nom_prenom(self):
        return f"{self.nom} {self.prenom}"



class Emprunter:
    def __init__(self, adherent, livre, date):
        self.adherent = adherent
        self.livre = livre
        self.date_initial = datetime.now()
        self.date_return = date

    def enr_emprunt(self):
        time_i = self.date_initial
        time_r = self.date_return
        adh = self.adherent.nom +' '+ self.adherent.prenom +',' +  self.livre.titre +','+  self.livre.auteur +','+str(time_i)+','+str(time_r)

        with open('emprunt.txt','a') as f:
            f.write('\n'+adh)


class Bibliotheque:
    #def __init__(self):


    def ajout_adherent(self,Adherent):
        tab = extrait_txt('adherent.txt')
        adh = f'{Adherent.nom_prenom()}\n'
        if adh in tab:
            print(f"impossible d'ajouter {adh.strip()} car il est deja adherent")
        else:
            tab.append(adh)
            ecrire_txt('adherent.txt', tab)
            print(f"{adh.strip()} a ete ajoute avec succes")


    def enlever_adherent(self, Adherent):
        tab = extrait_txt('adherent.txt')
        try:
            tab.remove(Adherent.nom_prenom()+'\n')
            ecrire_txt('adherent.txt', tab)
            print(f"{Adherent.nom_prenom()} a ete Supprimer de la liste")
        except FileNotFoundError:
            print("Erreur, cet individu ne figure pas dans la liste des adherents")


    def ajout_emprunt(self):
        nom = input("Entrez le nom de l'adherent : ")
        prenom = input("Entrez le prenom de l'adherent: ")
        ind = nom + ' ' + prenom+'\n'
        tab = extrait_txt('adherent.txt')
       # tab_emp = extrait_txt('emprunt.txt')
        if ind in tab:
          #  if ind not in tab_emp:
                titre = input("Entrez le titre du livre solicite: ")
                auteur = input("Entrez l'auteur du livre solicite: ")
                livre = Livre(titre, auteur)
                if livre.est_disponible() == True:
                    emp = Emprunter(Adherent(nom, prenom), livre, valider_date()).enr_emprunt()
                    livre.enlever_livre()
                    print('Emprunt valide et enregistre avec succes')
                else:
                    print("Desole ce livre n'est pas disponible")

            #else:
                #print("Emprunt impossible, veuillez retourner les precedents documents")
        else:
            print("Emprunt impossible; n'est pas adherent")

    def retour_emprunt(self,Adherent,Livre):
        tab = extrait_txt('emprunt.txt')
        for x in tab:
            y = x.strip().split(',')
            if y[0] == Adherent.nom_prenom() and y[1] == Livre.titre and y[2] == Livre.auteur:
                tab.remove(x)
                ecrire_txt('emprunt.txt', tab)
                Livre.ajout_livre()
                return print("Document retourner.")
        print("Erreur livre non reconnu")


    def afficher_docs(self):

        liste = extrait_txt('journal.txt')
        print("LISTE DES JOURNAUX")
        for x in liste:
            y = x.strip().split(',')
            print(f"{y[0]    |y[1]    }")
    def afficher_adh(self):
        liste_ad = extrait_txt('adherent.txt')
        print("LISTE DES ADHERENTS")
        print()
        for x in liste_ad:
            print(x.strip())

    def afficher_emp(self):
        emp = extrait_txt('emprunt.txt')
        print("LISTE DES emprunts")
        print()
        for x in emp:
            y = x.strip().split(',')
            print(f"{y[0]} | {y[1]}   |{y[2]}    |{y[3]}   |{y[4]}")




b1 = Bibliotheque()
#b1.ajout_adherent(Adherent('Paul', 'Mathieu'))
#b1.enlever_adherent(Adherent('Paul', 'Mathieu'))
#b1.ajout_emprunt()
#b1.retour_emprunt(Adherent('Pierre', 'Alain'), Livre('Pierre Prince le malin', 'Julien Timuss'))
#b1.afficher_adh()
#b1.afficher_emp()