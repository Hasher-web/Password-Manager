import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt(plain_text: str, session_key: bytes):
    
    plain_textbytes = plain_text.encode("UTF-8")

    nonce = os.urandom(12)

    aes = AESGCM(session_key)
    
    cipher_text = aes.encrypt(
        nonce,
        plain_textbytes,
        None
    )

    return nonce + cipher_text

def decrypt(blob: bytes, session_key: bytes):

    nonce = blob[:12]
    cipher_text = blob[12:]

    aes = AESGCM(session_key)

    plain_textbytes = aes.decrypt(
        nonce,
        cipher_text,
        None
    )

    plain_text = plain_textbytes.decode("UTF-8")

    return plain_text