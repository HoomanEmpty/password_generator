from cryptography.fernet import Fernet

def encoding(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(password.encode())
    return key, encrypted

def decoding(key, encrypted):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted)

    return decrypted.decode()
