import math


class Rectangle:
    def __init__(self,largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def perimetre(self):
        return 2*(self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur

    #getters
    def get_largeur(self):
        return self.largeur
    def get_longueur(self):
        return self.longueur

    #setters
    def set_largeur(self, largeur):
        self.largeur = largeur
    def set_hauteur(self, longueur):
        self.longueur = longueur

class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        self.hauteur = hauteur

    def volume(self):
        return super().surface() * self.hauteur

class CompteBancaire:
    def __init__(self, numcompte, nom, solde):
        self.numcompte = numcompte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        self.solde += montant

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Retrait reussi")
        else:
            print('Retrait impossible car le solde est insuffisant')

    def agios(self):
        return self.solde - self.solde * 0.05

    def afficher(self):
        print(f"Numero du compte : {self.numcompte} \nDetenteur du compte : {self.nom} \nSolde : {self.solde}")


class Cercle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def surface(self):
        return math.pi * (self.r)**2

    def perimetre(self):
        return 2 * math.pi * self.r

    def testAppartenance(self, x, y):
        if (self.r)**2 == (self.a-x)**2 + (self.b-y)**2:
            print("Ce point est situe sur le cercle")
        else:
            print("Ce point n'appartient pas au cercle")

class Calcul:
    def __init__(self,nbre):
        self.nbre = nbre

    def factorielle(self, ):
        f = 1
        for i in range(1, self.nbre+1):
            f *= i
        return f

    def somme(self):
        s = 0
        for i in range(1, self.nbre+1):
            s += i
        return s

    def testPrim(self):
        for i in range(2, (self.nbre//2)+1):
            if self.nbre//i == 0:
                print("Ce nombre n'est pas premier")
            else:
                print("C'est un nombre primier")

    def testprimduo(self, nbre1):
        if math.gcd(self.nbre, nbre1) == 1:
            print("premier entre eux")

    def tableMult(self):
        for i in range(1, 13):
            print(f"{self.nbre} x {i} = {self.nbre * i}")

    def allTableMult(self):
        for i in range(1, 10):
            x = Calcul(i)
            x.tableMult()

    def listDiv(self):
        list = [x for x in range(1,self.nbre//2 +1) if self.nbre/x == 0]
        return list

    def listDivPrim(self):
        tab = self.listDiv()
        tab1 = []
        for x in tab:
            x1 = Calcul(x)
            if x1.testPrim():
                tab1.append(x)
        return tab1