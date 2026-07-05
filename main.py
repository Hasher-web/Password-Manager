import sqlite3

def main():
    welcome_message = "Welcome to Password Manager!"

    print(welcome_message)

    connection = sqlite3.connect("passwords.db")
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
            

    while True:
            print("1. Add Password")
            print("2. View Password")
            print("3. Update Password")
            print("4. Delete Password")
            print("5. Exit")

            try:
                choice = int(input("Choose: "))
            except:
                return None
            if choice == 1:
                website = input("Enter the name of the website:")
                username = input("Enter username:")
                password = input("Enter passowrd:")

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

            elif choice == 2:
                cursor.execute(
                """SELECT * FROM passwords
                """
                )

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            elif choice == 3:
                cursor.execute(
                """SELECT * FROM passwords
                """
                )

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                new_website = input("Enter the new website name: ")
                new_username = input("Enter the new username: ")
                new_password = input("Enter the new password: ")
                update_id = int(input("Enter the new id:  "))                

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

            elif choice == 4:
                cursor.execute(
                """SELECT * FROM passwords
                """
                )

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                delete_id = int(input("Enter the id: "))

                cursor.execute(
                """DELETE FROM passwords
                WHERE id = ?
                """,
                (delete_id,)
                )
                connection.commit()

            elif choice == 5:
                break

    connection.close()

if __name__ == "__main__":
    main()

    