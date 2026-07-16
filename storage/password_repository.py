import sqlite3
from security import encryption
from .database import get_connection

def add_password(website, username, password, session_key):
    connection = get_connection()
    cursor = connection.cursor()
    blob = encryption.encrypt(password, session_key)

    cursor.execute(
        """INSERT INTO passwords(
            website,
            username,
            password
        )
        VALUES(?, ?, ?)
        """,
        (website, username, blob)
        )
    

    connection.commit()
    connection.close()

def get_passwords(session_key):
    connection = get_connection()
    cursor = connection.cursor()
    

    cursor.execute(
        """SELECT * FROM passwords
        """
        )
    
    rows = cursor.fetchall()

    results = []

    for row in rows:
        decrypted_row = list(row)
        blob = decrypted_row[3]
        plain_text = encryption.decrypt(blob, session_key)

        decrypted_row[3] = plain_text
        results.append(decrypted_row)

    connection.close()
    return results

def update_password(new_website, new_username, new_password, update_id, session_key):
    connection = get_connection()
    cursor = connection.cursor()
    blob = encryption.encrypt(new_password,session_key)
    
    cursor.execute(
        """UPDATE passwords
        SET website = ?,
            username = ?,
            password = ?
        WHERE id = ?
        """,
        (new_website, new_username, blob, update_id)
        )

    connection.commit()
    connection.close()

def delete_password(delete_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """DELETE FROM passwords
        WHERE id = ?
        """,
        (delete_id,)
        )
    connection.commit()
    connection.close()