import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

id_livre = input('Insert ID livre: ')
id_auteur = input('Insert ID auteur: ')
id_titre = input('Insert ID titre: ')

req6 = """insert into livres (id_livre, id_auteur, id_titre)
values ('"+ str(id_livre) +"', '" + id_auteur + "', '" + id_titre + "');"""
c.execute(req6)
conn.commit()
print(req6)
