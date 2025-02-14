import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
req5 = """select * from livres"""
cursor.execute(req5)
data = cursor.fetchall()
print(data)




