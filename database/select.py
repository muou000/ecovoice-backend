import sqlite3

def selectUser(uid):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  SELECT * FROM users WHERE id=?""", (uid,))
    user = cursor.fetchone()
    con.close()
    return user

def selectFile(uid):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  SELECT * FROM files WHERE user_id=?""", (uid,))
    files = cursor.fetchall()
    con.close()
    return files