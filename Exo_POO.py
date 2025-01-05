class Employee:
    def __init__(self,emp_id, emp_name, emp_salary, emp_departement):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_departement = emp_departement

    def emp_affecter(self,new_departement):
        self.emp_departement = new_departement

    def afficher_emplyee(self):
        print("Employee : ", self.emp_name, "\nNumero d'identification : ", self.emp_id, "\nSalairre : ", self.emp_salary, "\nDepartement: ",self.emp_departement)

    def calculer_emp_salary(self,salaires,heures):
        heures_sup = 0
        if heures > 50:
            heures_sup = heures-50
        self.emp_salary = salaires*50 + heures_sup*(salaires/50)

class Restaurant:
    def __init__(self):
        self.menu_plat = {}
        self.reserver_table = []
        self.commandes_clients = []


    def ajouter_plat_au_menu(self,plat,prix):
        self.menu_plat[plat] = prix

    def afficher_menu(self):
        print('----MENU DU JOUR----')
        for m, p in self.menu_plat.items():
            print('\n', m,'---', p, )

    def reserverTable(self,numero_table):
        self.reserver_table.append(numero_table)

    def commandesClients(self, numero_table, cmd_client):
        cmd = {numero_table: cmd_client}
        self.commandes_clients.append(cmd)

    def afficher_cmdClient(self):
        print("Commandes clients")
        for x in self.commandes_clients:
            print(x,'\n')

#main
r1 = Restaurant()
r1.ajouter_plat_au_menu('Pizzas',9.99)
r1.ajouter_plat_au_menu('salade', 8)
r1.ajouter_plat_au_menu('crepe', 19.99)
r1.ajouter_plat_au_menu('Sandwichs', 3.99)
r1.ajouter_plat_au_menu('Fish & Chips', 15)
r1.reserverTable(1)
r1.reserverTable(2)
r1.reserverTable(3)
r1.commandesClients(1, 'Pizzas')
r1.commandesClients(2, 'Crepe', )
r1.commandesClients(3, 'Sandwichs', )
r1.commandesClients(3, 'Pizzas', )

class Bankaccount:
    def __init__(self,numero_compte, solde,date_ouverture,nom_client):
        self.numero_compte = numero_compte
        self.solde = solde
        self.date_ouverture = date_ouverture
        self.nom_client = nom_client

    def versement(self,montant):
        self.solde += montant
        print(f"{montant} a ete depose sur votre compte ")

    def retrait(self, montant):
        if self.montant < montant:
            print(f"Retrait impossible votre balance n'est pas suffiante")
        else:
            self.montant -= montant
            print(f"Retrait reussi, vous avez retire {montant} de votre compte")

    def verificationsolde(self):
        print(f"le compte {self.numero_compte} de {self.nom} cree le {self.date_ouverture} detient la somme de {self.solde}")

class Vehicule:
    def __init__(self, nom,  vitessemax, kilometrage):
        self.nom = nom
        self.vitessemax = vitessemax
        self.kilometrage = kilometrage

    def __str__(self):
        return f"Vitesse maximum: {self.vitessemax} \nkilometrage: {self.kilometrage}"

    def nombres_de_place(self,capacite):
        return f"la capacite de {self.nom} est {capacite} passagers"


class Bus(Vehicule):
    def __init__(self):
        pass

    def nombres_de_place(self, capacite):
        return super().nombres_de_place(50)


class Etudiant:
    def __init__(self, nom, numero_matricule, note1,note2):
        self.nom = ''
        self.numero_matricule = ''
        self.note1 = note1
        self.note2 = note2




    def display(self):
        print(f"nom de l'etudiant: {self.nom} \nNumero de matricule: {self.numero_matricule} \nNote1: {self.note1} \nNote2: {self.note2}")



#exo3
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimetre(self):
        return 2*(self.width + self.length)

    def surface(self):
        return self.width*self.length
    def affichege(self):
        print(f"le perimetre de ce rectangle est de {self.perimetre()}, et sa surface est de {self.surface()}")

class Polyedre(Rectangle):
    def __init__(self, width, length, heigth):
        self.heigth = heigth
        Rectangle.__init__(self,width, length)

    def volume(self):
        return self.surface()*self.heigth

#exo5
class Personne:
    def __init__(self, nom, pays, date_naissance):
        self.nom = nom
        self.pays = pays
        self.date_naissance = date_naissance

    def Age(self):
        print(f"l'age de cette personne est de {2025-self.date_naissance}")

class Panier:
    def __init__(self):
        self.article = []

    def ajouter_produits(self,produits, prix):
        t = (produits, prix)
        self.article.append(t)
    def retirer_produitss(self,produit):
        for ele in self.article:
            if produit == ele[0]:
                self.article.remove(ele)
                break

    def prix_total(self):
        som = 0
        for achat in self.article:
            som += achat[1]
        print(f"La somme des achat du panier vaut {som}")



p1 = Panier()
p1.ajouter_produits('riz', 10)
p1.ajouter_produits('mais',5)
p1.ajouter_produits('jus',1.5)
p1.ajouter_produits('bonbon',5)
p1.prix_total()
p1.retirer_produitss('riz')
p1.prix_total()




