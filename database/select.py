import sqlite3

def selectUserByUid(uid):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      SELECT * FROM users WHERE id=?""", (uid,))
        user = cursor.fetchone()

    if user is None:
        return "User not found!"
    return user

def selectUserByUsername(username):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      SELECT * FROM users WHERE username=?""", (username,))
        user = cursor.fetchone()

    if user is None:
        return "User not found!"
    return user

def selectFileByUid(uid):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      SELECT * FROM files WHERE user_id=?""", (uid,))
        files = cursor.fetchall()

    if not files:
        return "No file found!"
    return files

def selectFileByFid(file_id):
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      SELECT * FROM files WHERE id=?""", (file_id,))
        file = cursor.fetchone()

    if file is None:
        return "File not found!"
    return file