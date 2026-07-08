def show_main_menu():
    print("1. Add Password")
    print("2. View Password")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Exit")

def get_menu_choice():
    try:
        choice = int(input("Choose from the menu: "))
        return choice
    except ValueError:
        print("INVALID CHOICE")
        return None