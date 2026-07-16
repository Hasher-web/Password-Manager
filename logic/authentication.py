from security import hashing
from storage import master_password_repository


def setup_master_password():
    master_password = input("Create a master password: ")

    salt, password_hash = hashing.hash_password(master_password)

    master_password_repository.save_master_password(salt, password_hash)

    return hashing.derive_key(master_password, salt)


def login():
    stored_salt, stored_hash = (
        master_password_repository.get_master_password()
    )

    for attempt in range(3):
        entered = input("Enter master password: ")

        if hashing.verify_password(
            entered,
            stored_salt,
            stored_hash
        ):
            return hashing.derive_key(
                entered,
                stored_salt
            )

        print("Incorrect password.")

    print("Too many failed attempts.")
    return False


def authenticate():
    if not master_password_repository.master_password_exists():
        return setup_master_password()

    return login()