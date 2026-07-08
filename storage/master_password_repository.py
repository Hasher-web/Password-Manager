from .database import get_connection

def master_password_exists():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT 1 FROM master_password LIMIT 1")
    exists = cursor.fetchone() is not None

    connection.close()

    return exists

def save_master_password(salt, password_hash):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO master_password (salt, password_hash) VALUES (?, ?)",
    (salt, password_hash),
    )

    connection.commit()
    connection.close()

def get_master_password():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT salt, password_hash FROM master_password LIMIT 1"
    )
    
    row = cursor.fetchone()
    connection.close()

    return row