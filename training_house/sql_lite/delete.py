import sqlite3
conn = sqlite3.connect('mydb')

c = conn.cursor()

req = """delete from bandeD
where id = 3
       and auteur = 'superman 2'
       and dessinateur = 'Bob Tree';"""

c.execute(req)
conn.commit()