import sqlite3
conn = sqlite3.connect('example.db')

def getUsers():
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    users = c.fetchall()
    print(users)

getUsers()