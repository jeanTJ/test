import sqlite3
conn = sqlite3.connect('mydb')

c = conn.cursor()

id = input('Enter ID: ')
auteur = input('Enter auteur: ')
dessinateur = input('Enter dessinateur: ')


req = """insert into bandeD (id, auteur, dessinateur)
values (?, ?, ?)"""

c.execute(req, (id, auteur, dessinateur))
conn.commit()
conn.close()