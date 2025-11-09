from cryptography.fernet import Fernet


def generate_key():
    
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved to secret.key")

def load_key():
    
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key file not found. Generating a new one.")
        generate_key()
        return open("secret.key", "rb").read()



def encrypt_message(message, key):
    
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message


if __name__ == "__main__":
    generate_key()