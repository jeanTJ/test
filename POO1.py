# Questionnaire

class Question:
    def __init__(self, titre, choix, bon_reponse):
        self.titre = titre
        self.choix = choix
        self.bon_reponse = bon_reponse

    def poser(self):
        print(self.titre)
        print('--------')
        for i in range(len(self.choix)):
            print(i+1, ' ---- ', self.choix[i])
        print("Entrez votre choix de reponse entre 1 et ", len(self.choix))
        inp = input()
        while True:
            try:
                if int(inp) >= 1 and int(inp) <= 4:
                    if self.choix[int(inp)-1] == self.bon_reponse:
                        print('bonne reponse')
                        return True
                    else:
                        print('mauvaise reponse')
                        return False
                else:
                    print("ERREUR,Entrez votre choix de reponse entre 1 et ", len(self.choix))
                    inp = input()
            except:
                print("ERREUR,Entrez votre choix de reponse entre 1 et ", len(self.choix))
                inp = input()


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
            print("Score final : ", score, 'sur ', len(self.questions))







questions = (Question('quel est la capitale de la france?', ('Nante', 'Marseille','Paris','Evian'), 'Paris')
#q1.poser()
,Question("quelle est la capitale de l'italie", ('Venise', 'Rome', 'Turin','Naple'), 'Rome'))
#q2.poser()
q = Questionnaire(questions)
q.lancer()
