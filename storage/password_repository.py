import sqlite3
from .database import get_connection

def add_password(website, username, password):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO passwords(
            website,
            username,
            password
        )
        VALUES(?, ?, ?)
        """,
        (website, username, password)
        )
    connection.commit()
    connection.close()

def get_passwords():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """SELECT * FROM passwords
        """
        )

    rows = cursor.fetchall()
    connection.close()
    return rows

def update_password(new_website, new_username, new_password, update_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """UPDATE passwords
        SET website = ?,
            username = ?,
            password = ?
        WHERE id = ?
        """,
        (new_website, new_username, new_password, update_id)
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