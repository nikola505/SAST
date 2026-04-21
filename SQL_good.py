import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE user = ? AND password = ?"
    print("Executing parameterized query")
    c.execute(query, (username, password))
    result = c.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")

login("admin", "1234")
