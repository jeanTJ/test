import sqlite3
conn = sqlite3.connect('mydb')
c = conn.cursor()

req = """select * from bandeD"""
c.execute(req)
data = c.fetchall()
print(data)