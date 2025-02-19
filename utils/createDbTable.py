import sqlite3 #sqlite library


def setup(databaseName, tableName):
    conn = sqlite3.connect(f"{databaseName}.db") #creates the database as per name
    cursor = conn.cursor() #position the cursor

    #table creation
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {tableName} 
        (id, title, content, category, tags, createdAt, updatedAt)
                   ''')


if __name__ == "__main__":
    import sys
    setup(str(sys.argv[1]), str(sys.argv[2]))
#making it usable for testing