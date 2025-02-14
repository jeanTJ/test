import sqlite3
def ecrire_d():
    conn = sqlite3.connect('school')
    c = conn.cursor()

    c.execute("""create table if not exists students
              (id integer primary key autoincrement,
              name text,
              email text,
              phone integer,
              section text)""")
    conn.commit()
    conn.close()

def inserer():
    conn = sqlite3.connect('school')
    c = conn.cursor()
    name = input('Entrez le nom: ')
    email = input("Entrez l'email: ")
    phone = input("entrez le numero de telephone: ")
    section = input("entrez la section: ")
    req = ("""insert into students (name, email, phone, section)
    values  (?, ?, ?, ?)""")
    c.execute(req, (name, email, phone, section))
    conn.commit()
    conn.close()
def lire():
    conn = sqlite3.connect('school')
    c = conn.cursor()
    c.execute("""select * from students
              """)
    data = c.fetchall()
    conn.commit()
    conn.close()
    print(data)
    print(type(data))
lire()




