from abc import ABC, abstractmethod


class Personne(ABC):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    @abstractmethod
    def envoyerMail(self):
        print(f"== Mail : bonjour {self.nom} {self.prenom}")


#classe enfant
class Employee(Personne):
    def __init__(self,nom, prenom, numEmployee): # constructeur new
        super().__init__(nom, prenom) #appeler le constructeur du parent
        self.numEmployee = numEmployee

    def __str__(self):
        return super().__str__() + str(self.numEmployee)

    def envoyerMail(self):
        print(f"== Mail Employee bonjour {self.nom} {self.prenom}" )

class Enseignant(Employee):
    def __init__(self,nom, prenom, numEmployee, departement):
        super().__init__(nom, prenom, numEmployee)
        self.departement = departement

    def __str__(self):
        return super().__str__() + ' ' +str(self.departement)

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass

class Rectangle(Forme):
    def __init__(self,largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2*(self.hauteur + self.largeur)

r1 = Rectangle(4,6)
print(r1.aire())



#p1 = Personne('jean', 'alain')
em1 = Employee('Isaac', 'pierre', '452ERU')

#list = [p1, em1]
#for e in list:
#    e.envoyerMail()

