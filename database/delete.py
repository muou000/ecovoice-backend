import sqlite3
import os

import globalVariables
import database.select

def deleteUser(uid):
    userExist = database.select.selectUserByUid(uid)
    if userExist == "User not found!":
        return userExist

    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      DELETE FROM users WHERE id=?""", (uid,))
        con.commit()
        con.close()
    return "User deleted successfully!"


def deleteFile(file_id):
    fileExist = database.select.selectFileByFid(file_id)
    if fileExist == "File not found!":
        return fileExist
    
    filePath = os.path.join(globalVariables.directory, fileExist[2])

    if os.path.exists(filePath):
        os.remove(filePath)
    
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                      DELETE FROM files WHERE id=?""", (file_id,))
        con.commit()
    return "File deleted successfully!"
    