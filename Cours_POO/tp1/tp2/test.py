
import sqlite3
conn = sqlite3.connect('bibliotheque')
c = conn.cursor()
c.execute("""select ISBN from livre""")
l = c.fetchall()
print(l)
tab = [x[0] for x in l]
print(tab)