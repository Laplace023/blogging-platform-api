import sqlite3

conn = sqlite3.connect('blogs.db')
cursor = conn.cursor()

cursor.execute("SELECT MAX(id) FROM posts")
data = cursor.fetchone()
print(data[0])
print(type(data[0]))