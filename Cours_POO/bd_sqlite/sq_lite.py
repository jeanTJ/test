#importer le package
import sqlite3
#creer
conn = sqlite3.connect('test.db')

curseur = conn.cursor()

req3 = """create table emprunts
(
    id  interger,
    id_utilisateur TEXT,
    id_livre TEXT
);    """

#curseur.execute(req3)

req4 = """insert into livres (id_livre, id_titre, id_auteur)
VALUES (2, 'le miserables', 'Victor');"""

curseur.execute(req4)
conn.commit()