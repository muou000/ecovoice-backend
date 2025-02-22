import sqlite3
import database.select

def deleteUser(uid):
    userExist = database.select.selectUser(uid)
    if userExist == "User not found!":
        return "User not found!"
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  DELETE FROM users WHERE id=?""", (uid,))
    con.commit()
    con.close()
    return "User deleted successfully!"

def deleteFile(file_id):
    fileExist = database.select.selectFileByFid(file_id)
    if fileExist == "File not found!":
        return "File not found!"
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("""
                  DELETE FROM files WHERE id=?""", (file_id,))
    con.commit()
    con.close()
    return "File deleted successfully!"