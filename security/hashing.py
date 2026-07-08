import hashlib
import os


def hash_password(password):
    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt.hex(), password_hash.hex()


def verify_password(password, stored_salt, stored_hash):
    salt = bytes.fromhex(stored_salt)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return password_hash.hex() == stored_hash