import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE user = '%s' AND password = '%s'" % (username, password)
    print("Executing:", query)
    c.execute(query)
    result = c.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")

login("admin", "1234")