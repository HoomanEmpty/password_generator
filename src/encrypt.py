from cryptography.fernet import Fernet

def encoding(password):      
    key = Fernet.generate_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(password.encode())

    return cipher, encrypted

def decoding(cipher, encrypted):
    decrypted = cipher.decrypt(encrypted)

    return decrypted.decode()
