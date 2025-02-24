import sqlite3

conn = sqlite3.connect('blogs.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO posts VALUES ('2', 'test', 'test', 'test', 'test', 'test', 'test')")

conn.commit()
conn.close()