class Stock:
    def __init__(self,produits):
        self.produits = {}

    def ajouter(self, elements, quantite):
        if elements in self.produits:
            self.produits[elements] += quantite
        else:
            self.produits = quantite

    def supprimer(self,element):
        if element in self.produits:
            self.produits.pop(element)
        else:
            print("Ce produit n'est pas dans le stock")

    def verifierStock(self, element,quant):
        if element in self.produits:
            if self.produits[element] < quant:
                print('Quantite insufisante')
            else:
                print("Quantite suffisante")
        else:
            print("Ce Produit n'est pas en stock")




