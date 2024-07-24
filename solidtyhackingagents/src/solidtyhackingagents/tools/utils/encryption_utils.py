# encryption_utils.py

from cryptography.fernet import Fernet

def generate_key() -> bytes:
    """
    Generate a new encryption key.
    """
    return Fernet.generate_key()

def encrypt_message(message: str, key: bytes) -> bytes:
    """
    Encrypt a message with the given key.
    """
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    """
    Decrypt a message with the given key.
    """
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message
