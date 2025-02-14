import sqlite3

conn = sqlite3.connect('mydb')
c = conn.cursor()

req = """create table bandeD
(
    id integer,
    auteur TEXT,
    dessinateur TEXT
);    """

c.execute(req)
conn.commit()