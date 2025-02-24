import sqlite3

#INFO: This is a function to generate the ID for new posts

def id():

    conn = sqlite3.connect('blogs.db')
    cursor = conn.cursor()

    #INFO: ID generated is max ID + 1
    cursor.execute("SELECT MAX(id) FROM posts")
    data = cursor.fetchone()
    dataInt = int(data[0])
    newId = dataInt + 1
    strId = str(newId)
    conn.close()

    return strId

if __name__ == "__main__":
    ID = id()
    print(ID)
    print(type(ID))