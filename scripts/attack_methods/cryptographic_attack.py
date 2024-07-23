from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

# Target parameters
ENCRYPTION_KEY = b'Sixteen byte key'  # 16 bytes key for AES-128
IV = b'Sixteen byte iv '  # 16 bytes IV for AES
ENCRYPTED_MESSAGE = b'Encrypted message here'  # This should be replaced with actual encrypted data

def decrypt_message(ciphertext, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted
    except (ValueError, KeyError) as e:
        print("Decryption failed:", e)
        return None

def perform_cryptographic_attack():
    # Decrypt the encrypted message
    decrypted_message = decrypt_message(ENCRYPTED_MESSAGE, ENCRYPTION_KEY, IV)
    if decrypted_message:
        print("Decrypted message:", decrypted_message.decode())
    else:
        print("Failed to decrypt the message.")

    # Hash collision attack simulation
    def hash_function(data):
        # Example with MD5, which is vulnerable to collisions
        return hashlib.md5(data).hexdigest()

    original_data = b'original data'
    collision_data = b'original data' + b'collision'
    
    original_hash = hash_function(original_data)
    collision_hash = hash_function(collision_data)
    
    print("Original hash:", original_hash)
    print("Collision hash:", collision_hash)
    
    if original_hash == collision_hash:
        print("Hash collision detected.")
    else:
        print("No hash collision detected.")

    # Hash function collision attack with stronger hash (for demonstration)
    def strong_hash_function(data):
        # Example with SHA-256, more resistant to collisions
        return hashlib.sha256(data).hexdigest()
    
    strong_original_hash = strong_hash_function(original_data)
    strong_collision_hash = strong_hash_function(collision_data)
    
    print("Strong original hash:", strong_original_hash)
    print("Strong collision hash:", strong_collision_hash)
    
    if strong_original_hash == strong_collision_hash:
        print("Collision detected in strong hash function (unlikely).")
    else:
        print("No collision in strong hash function.")

if __name__ == "__main__":
    perform_cryptographic_attack()
