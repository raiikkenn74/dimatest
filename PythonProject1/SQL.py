import sqlite3


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                     (id INTEGER PRIMARY KEY, login TEXT, password TEXT)''')
    cursor.execute("INSERT INTO users (login, password) VALUES ('admin', 'secret')")
    cursor.execute("INSERT INTO users (login, password) VALUES ('user', 'qwerty')")
    conn.commit()
    conn.close()


def vulnerable_login():
    login = input("Логин: ")
    password = input("Пароль: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    return result is not None

# def safe_login():
#     login = input("Логин: ")
#     password = input("Пароль: ")
#
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#
#     query = "SELECT * FROM users WHERE login = ? AND password = ?"
#     cursor.execute(query, (login, password))
#
#     result = cursor.fetchone()
#     conn.close()
#
#     return result is not None

if __name__ == "__main__":
    init_db()
    if vulnerable_login():
        print("Доступ предоставлен")
    else:
        print("Досуп отклонен")





# Логин: admin
# Пароль: secret
# Доступ предоставлен!

# Логин: ' OR 1=1 --
# Пароль: anything
# Доступ предоставлен!