from cryptography.fernet import Fernet
import os


def generate_key(key_path="secret.key"):
    # Generates and saves a key for encryption and decryption.
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved as '{key_path}'")


def load_key(key_path="secret.key"):
    # Loads the encryption key from file.
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file '{key_path}' not found.")
    return open(key_path, "rb").read()


def encrypt_image(image_path, encrypted_path, key_path="secret.key"):
    # Encrypts an image file.
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    key = load_key(key_path)
    cipher = Fernet(key)

    with open(image_path, "rb") as file:
        image_data = file.read()

    encrypted_data = cipher.encrypt(image_data)

    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)

    print(f"Image encrypted and saved as '{encrypted_path}'")


def decrypt_image(encrypted_path, decrypted_path, key_path="secret.key"):
    # Decrypts an encrypted image file.
    if not os.path.exists(encrypted_path):
        raise FileNotFoundError(f"Encrypted file '{encrypted_path}' not found.")

    key = load_key(key_path)
    cipher = Fernet(key)

    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError("Decryption failed. Possibly due to incorrect key or corrupted file.") from e

    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)

    print(f"Image decrypted and saved as '{decrypted_path}'")


def main_menu():
    print("\nImage Encryption/Decryption Tool")
    print("--------------------------------")
    print("1. Generate Key")
    print("2. Encrypt Image")
    print("3. Decrypt Image")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        generate_key()
    elif choice == '2':
        image_path = input("Enter the path to the image to encrypt: ")
        encrypted_path = input("Enter the output path for the encrypted file: ")
        try:
            encrypt_image(image_path, encrypted_path)
        except Exception as e:
            print(f"Encryption error: {e}")
    elif choice == '3':
        encrypted_path = input("Enter the path to the encrypted file: ")
        decrypted_path = input("Enter the output path for the decrypted image: ")
        try:
            decrypt_image(encrypted_path, decrypted_path)
        except Exception as e:
            print(f"Decryption error: {e}")
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please select again.")


if __name__ == "__main__":
    while True:
        main_menu()