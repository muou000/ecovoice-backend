import sqlite3

def insertUser(username, password, email):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  INSERT INTO users (username, password, email) VALUES (?, ?, ?)""", (username, password, email))
    con.commit()
    con.close()

def insertFile(user_id, file_name, upload_time):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  INSERT INTO files (user_id, file_name, upload_time) VALUES (?, ?, ?)""", (user_id, file_name, upload_time))
    con.commit()
    con.close()