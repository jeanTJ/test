#https://waytolearnx.com/2024/10/exercice-corrige-les-classes-poo-python-partie-5.html
#Exo1
class FeuDeCirculation:
    def __init__(self,couleur, duree):
        self.couleur = couleur
        self.duree = duree

    def changer_couleur(self):
        import time
        countdown = self.duree
        while True:
            for i in range(2):
                color = self.couleur[i]
                print(f'Feu {color}')
                time.sleep(self.duree)

c1 = FeuDeCirculation(['rouge', 'vert'], 6)
#c1.changer_couleur()


class Employee:
    def __init__(self,nom, salaire, date_dembauche):
        self.nom = nom
        self.salaire = salaire
        self.date_dembauche = date_dembauche

    def annee_service(self):
        from datetime import datetime, timedelta
        date = datetime.now()
        return date - self.date_dembauche
class Etudiant:
    liste_etud = []
    def __init__(self, nom, note, cours):
        self.nom = nom
        self.note = note
        self.cours = cours


  #  @classmethod
  #  def liste_des_etudiants(cls,obj):
  #      cls.liste_etud.append(obj)
    def __str__(self):
        return f"nom: {self.nom} \nNote: {self.note} \nListe de cours {self.cours}"

    @classmethod
    def liste_des_etuds(cls,obj):
        if type(obj) == list:
            for x in obj:
                Etudiant.liste_etud.append(x)
        else:
            Etudiant.liste_etud.append(obj)



    def ajouter_cours(self, cour):
        if type(cour) == list:
            for x in cour :
                self.cours.append(x)
        else:
            self.cours.append(cour)

    def retrait_cour(self,cour):
        if len(self.cours) != 0:
            try:
                self.cours.remove(cour)
                print(f"le cour {cour} a ete retirer de la liste des cours de {self.nom}")
            except:
                print(f"Impossible de retirer {cour} car il n'est pas dans la liste des cours de {self.nom}")
        else:
            print(f"L'etudiant {self.nom} n'a aucun cour assigne")

    def infos_etud(self):
        return f"nom: {self.nom} \nNote: {self.note} \nListe de cours {self.cours}"

    def recherche_etud(self,nom_etud):
        for eut in Etudiant.liste_etud:
            if self.nom == 'nom_etud':
                print(eut)
                break

e1 = Etudiant('Felix', 89,['prog', 'reseau'])
e2 = Etudiant('alex', 95, ['prog', 'reseau'])
e3 = Etudiant('Vincent', 92,['prog', 'reseau'])
Etudiant.liste_des_etuds([e1,e2,e3])
print(e1)
print(Etudiant.liste_etud)
for x in Etudiant.liste_etud:
    print('Etudiant')
    print(x)
    print()







