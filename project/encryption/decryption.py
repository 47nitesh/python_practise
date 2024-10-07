from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt(data: bytes, key: bytes) -> (bytes, bytes):
    """Encrypts the given data using AES GCM."""
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(12)  # 12 bytes for GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the data
    ciphertext = encryptor.update(data) + encryptor.finalize()
    tag = encryptor.tag

    return iv + tag + ciphertext


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypts the given data using AES GCM."""
    # Extract the IV, tag, and ciphertext
    iv = encrypted_data[:12]
    tag = encrypted_data[12:28]
    ciphertext = encrypted_data[28:]

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    return decryptor.update(ciphertext) + decryptor.finalize()


# Example usage
if __name__ == '__main__':
    # Define a 256-bit (32 bytes) AES key
    key = os.urandom(32)

    # Data to encrypt
    original_data = b"Hello, this is a secret message!"
    print(f"Original Data: {original_data}")

    # Encrypt the data
    encrypted_data = encrypt(original_data, key)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypt the data
    decrypted_data = decrypt(encrypted_data, key)
    print(f"Decrypted Data: {decrypted_data}")
