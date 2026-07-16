from storage import password_repository, master_password_repository, database
from system import menu
from security import hashing
from logic import authentication

def main():
    welcome_message = "Welcome to Password Manager!"

    print(welcome_message)

    database.create_tables()


    exists = master_password_repository.master_password_exists()
    print(f"[DEBUG] master password exists: {exists}")

    session_key = authentication.authenticate()

    if session_key:
        while True:
                menu.show_main_menu()
                choice = menu.get_menu_choice()

                if choice == 1:
                    website = input("Enter the name of the website:")
                    username = input("Enter username:")
                    password = input("Enter passowrd:")

                    password_repository.add_password(website, username, password, session_key)

                elif choice == 2:
                    rows = password_repository.get_passwords(session_key)

                    if not rows:
                        print(f"{'=' * 40}")
                        print("No passwords stored.")
                        print(f"{'=' * 40}")
                    else:
                        for row in rows:
                            print(row)

                elif choice == 3:
                    password_repository.get_passwords(session_key)

                    new_website = input("Enter the new website name: ")
                    new_username = input("Enter the new username: ")
                    new_password = input("Enter the new password: ")
                    update_id = int(input("Enter the new id:  "))

                    password_repository.update_password(new_website, new_username, new_password, update_id, session_key)

                elif choice == 4:
                    password_repository.get_passwords()

                    delete_id = int(input("Enter the id: "))

                    password_repository.delete_password(delete_id)

                elif choice == 5:
                    print("EXITING...")
                    break
                else:
                    print("Invalid Input")
    else:
        exit

if __name__ == "__main__":
    main()

    