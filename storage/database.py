import sqlite3


def get_connection():
    connection = sqlite3.connect("passwords.db")
    return connection  

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
            """CREATE TABLE IF NOT EXISTS passwords
            (
                id INTEGER PRIMARY KEY,
                website TEXT,
                username TEXT,
                password TEXT
            )"""
        )
    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS master_password
        (
            id INTEGER PRIMARY KEY,
            salt TEXT,
            password_hash TEXT
        )"""
    )

    connection.commit()
    connection.close()