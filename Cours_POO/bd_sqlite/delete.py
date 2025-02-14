import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

req7 = """delete from livres where id_livre = 3 ;"""

c.execute(req7)
conn.commit()