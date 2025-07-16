import sqlite3  

mydb = sqlite3.connect("mydb.db") 

mycursor =  mydb.cursor()

mycursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
mydb.commit()

# mycursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
# mycursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
mydb.commit()

mycursor.execute("SELECT * FROM users")
# rows = mycursor.fetchall()
# for row in rows:
#     print(row)

mycursor.close()