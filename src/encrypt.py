from cryptography.fernet import Fernet

def encoding(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(password.encode())
    key = key.decode()
    encrypted = encrypted.decode()
    key_first_section = ""
    key_second_section = ""

    for i in range(len(key)):
        if i <= 22:
            key_first_section += key[i]

        else:
            key_second_section += key[i]

    encrypted_password = key_first_section + encrypted + key_second_section
    to_bin = ""

    for letter in encrypted_password:
        to_bin += str(ord(letter)) + "#"
    to_bin += "|"

    return to_bin

def decoding(encrypted_passwords):
    number_collector = ""
    word = ""
    passwords = []
    show_passwords = []

    for letter in encrypted_passwords:
        if letter == "#":
            word += chr(int(number_collector))
            number_collector = ""

        elif letter == "|":
            passwords.append(word)
            word = ""

        else:
            number_collector += letter

    for element in passwords:
        key_first_section = ""
        key_second_section = ""
        encrypted = ""

        key_first_section = element[:23]
        encrypted = element[23:-21]
        key_second_section = element[-21:]

        key = (key_first_section + key_second_section).encode()
        encrypted = encrypted.encode()

        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted)

        show_passwords.append(decrypted.decode())

    return show_passwords
