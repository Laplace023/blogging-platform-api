import sqlite3

blogID = 1

conn = sqlite3.connect('blogs.db')
c = conn.cursor()
c.execute(f"SELECT * FROM posts WHERE id='{blogID}'")
data = c.fetchall()
print(data)
for x in c.description:
    print(x[0])
for y in data[0]:
    print(y)

data = dict(zip([c[0] for c in c.description], data[0]))
print(data)