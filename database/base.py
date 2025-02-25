import sqlite3

def initDatabase():
    with sqlite3.connect('database.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        username TEXT NOT NULL,
                                                        password TEXT NOT NULL,
                                                        email TEXT NOT NULL)""")
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        user_id INTEGER NOT NULL,
                                                        file_name TEXT NOT NULL,
                                                        upload_time TIMESTAMP)""")
        con.commit()