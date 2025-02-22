import sqlite3

def selectUser(uid):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  SELECT * FROM users WHERE id=?""", (uid,))
    user = cursor.fetchone()
    con.close()
    if user is None:
        return "User not found!"
    return user

def selectFileByUid(uid):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  SELECT * FROM files WHERE user_id=?""", (uid,))
    files = cursor.fetchall()
    con.close()
    if not files:
        return "No file found!"
    return files

def selectFileByFid(file_id):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  SELECT * FROM files WHERE id=?""", (file_id,))
    file = cursor.fetchone()
    con.close()
    if file is None:
        return "File not found!"
    return file