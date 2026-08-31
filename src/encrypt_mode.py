from turtle import mode

from cryptography.fernet import Fernet
from pathlib import Path

class Encrypt:
    def __init__(self, path, data_list = []):
        self.path = path
        self.data_list = data_list
        self.length = len(data_list)

        self.key_first_section = ""
        self.key_second_section = ""

        self.key = []
        self.cipher = []
        self.to_bin = ""
        self.encrypted = ""

        self.number_collector = ""
        self.word = ""
        self.passwords = []
        self.show_passwords = []

    def run_mode(self, mode):
        match mode:
            case "text" | "t":
                return self.text_mode()
            case "image" | "i":
                return self.image_mode()
            case "voice" | "v":
                return self.voice_mode()
            case "morse" | "m":
                return self.morse_mode()

class Encoding(Encrypt):
    def __init__(self, path, data_list = []):
        super().__init__(path, data_list)

        for i in range(self.length):
            self.key.append(Fernet.generate_key())
            self.cipher.append(Fernet(self.key[i]))

            
    def text_mode(self):
        for i in range(self.length):
            self.encrypted = self.cipher[i].encrypt(self.data_list[i].encode())
            key = self.key[i].decode()
            self.encrypted = self.encrypted.decode()

            self.key_first_section = key[:23]
            self.key_second_section = key[23:]

            encrypted_password = self.key_first_section + self.encrypted + self.key_second_section

            for character in encrypted_password:
                self.to_bin += str(ord(character)) + "#"
            self.to_bin += "|"

        return self.to_bin

    def image_mode(self):
        pass

    def voice_mode(self):
        pass

    def morse_mode(self):
        pass

class Decoding(Encrypt):
    def text_mode(self):
        with open(self.path, "r") as file:
            self.encrypted_passwords = file.read()
            
        for character in self.encrypted_passwords:
            if character == "#":
                self.word += chr(int(self.number_collector))
                self.number_collector = ""

            elif character == "|":
                self.passwords.append(self.word)
                self.word = ""

            else:
                self.number_collector += character

        for password in self.passwords:
            self.key_first_section = password[:23]
            self.encrypted = password[23:-21]
            self.key_second_section = password[-21:]

            key = (self.key_first_section + self.key_second_section).encode()
            self.encrypted = self.encrypted.encode()

            cipher = Fernet(key)
            decrypted = cipher.decrypt(self.encrypted)

            self.show_passwords.append(decrypted.decode())

        return self.show_passwords
    
    def image_mode(self):
        pass

    def voice_mode(self):
        pass

    def morse_mode(self):
        pass
