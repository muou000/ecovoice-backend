import sqlite3

def insertUser(username, password, email):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                    INSERT INTO users (username, password, email) VALUES (?, ?, ?)""", (username, password, email))
        con.commit()

def insertFile(user_id, file_name, upload_time):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                        INSERT INTO files (user_id, file_name, upload_time) VALUES (?, ?, ?)""", (user_id, file_name, upload_time))
        con.commit()
    