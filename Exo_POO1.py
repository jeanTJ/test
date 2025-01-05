#https://waytolearnx.com/2024/09/exercice-corrige-les-classes-poo-python-partie-3.html

#exo1
class Book:
    def __init__(self,titre, nom_auteur, prix):
        self.titre = titre
        self.nom_auteur = nom_auteur
        self.prix = prix

class File:
    def __init__(self):
        self.data = []

    def inserer(self, element):
        if type(element) == list:
            for x in element:
                self.data.append(x)
        else:
            self.data.append(element)

    def retirer(self,ele):
        if len(self.data) != 0:
            try:
                self.data.remove(ele)
            except:
                print("cet element n'est pas dans la liste d'attente")

        else:
            print(f"Impossible de retirer d'ume file d'attente vide")
#Exo partie4
class Personne:
    def __init__(self,nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom} a {self.age} ans"


class Livre:
    tab = []
    def __init__(self,titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"{self.titre}: {self.auteur}, {self.isbn}"
        #self.collection(obj)
    @ classmethod
    def collection(cls,obj):
        if type(obj) == list:
            for x in obj:
                cls.tab.append(x)
        else:
            Livre.tab.append(obj)
    @ classmethod
    def retirer(cls,obj):
        if len(Livre.tab) != 0:
            try:
                Livre.tab.remove(obj)
            except:
                print("Ce livre ne fait pas partie de la collection")
        else:
            print("Supression impossible la collection est vide")

li1 = Livre('le marchand', 'jean couture', '5ed2')
li2 = Livre('Le solitaire', 'belmond','fg4d')
li3 = Livre('ops', 'Vilier', 'or44')
li4 = Livre('Afrique', 'Senghor', 'a12g')
Livre.collection([li1, li2, li3])
Livre.collection(li4)
Livre.retirer(li4)
print()
for x in Livre.tab:
    print(x)

class Employee:
    def __init__(self, nom, poste, salaire):
        self.__nom = nom
        self.__poste = poste
        self.__salaire = salaire

class Banque:
    list_compte = []
    def __init__(self,num_compte, nom, solde, ):
        self.num_compte = num_compte
        self.nom = nom
        self.solde = solde

    @ classmethod
    def addCompte(cls,obj):
        if type(obj) == list:
            for x in obj:
                cls.list_compte.append(x)
        else:
            cls.list_compte.append(obj)
    @classmethod
    def removeCompte(cls, obj):
        try:
            cls.list_compte.remove(obj)
            print("Supression de compte termine")
        except:
            print("Ce compte n'existe pas")

    def depot(self, montant):
        self.solde += montant

    def retirer(self,montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print(f"Retrait impossible du compte {self.num_compte} balance insuffisante")

    def info_client(self):
        print(f"Numero de compte: {self.num_compte}, \nproprietaire du compte: {self.nom}, \nSolde du compte: {self.solde}")

c1 = Banque('c101','Alex', 8000)
c2 = Banque("c102", "Ali Koris", 6500)
c3 = Banque("c103", "Bob Finor", 500)
Banque.addCompte([c1,c2,c3])
c1.depot(500)
c3.retirer(2000)

