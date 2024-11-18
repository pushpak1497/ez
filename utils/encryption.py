from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def generate_secure_url(data: str):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_secure_url(token: str):
    try:
        return cipher_suite.decrypt(token.encode()).decode()
    except:
        return None
