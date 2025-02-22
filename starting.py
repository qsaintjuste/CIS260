from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates and saves a key for encryption and decryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'")

def load_key():
    """Loads the encryption key from file."""
    return open("secret.key", "rb").read()

def encrypt_image(image_path, encrypted_path):
    """Encrypts an image file."""
    key = load_key()
    cipher = Fernet(key)
    
    with open(image_path, "rb") as file:
        image_data = file.read()
    
    encrypted_data = cipher.encrypt(image_data)
    
    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)
    
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt_image(encrypted_path, decrypted_path):
    """Decrypts an encrypted image file."""
    key = load_key()
    cipher = Fernet(key)
    
    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)
    
    print(f"Image decrypted and saved as {decrypted_path}")

# Example Usage
if __name__ == "__main__":
    if not os.path.exists("secret.key"):
        generate_key()
    
    image_path = "example.jpg"  # Change to your image file
    encrypted_path = "encrypted.img"
    decrypted_path = "decrypted.jpg"
    
    encrypt_image(image_path, encrypted_path)
    decrypt_image(encrypted_path, decrypted_path)

