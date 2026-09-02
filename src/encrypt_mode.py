from cryptography.fernet import Fernet
from PIL import Image
import numpy as np
from pathlib import Path
import os
import magic

class Encrypt:
    def __init__(self, mode, path, data_list = []):
        self.path = path.joinpath("output.Jaraare") if path.is_dir() else path
        self.mode = mode
        self.data_list = data_list
        self.length = len(data_list)
        self.WIDTH = 7680
        self.HEIGHT = 4320

        self.key_first_section = ""
        self.key_second_section = ""

        self.to_bin = ""
        self.encrypted = ""

        self.number_collector = ""
        self.word = ""
        self.passwords = []
        self.show_passwords = []

    def run_mode(self):
        match self.mode:
            case "text" | "t":
                return self.text_mode()
            
            case "image" | "i":
                return self.image_mode()
            
            case "voice" | "v":
                return self.voice_mode()
            
            case "morse" | "m":
                return self.morse_mode()

class Encoding(Encrypt):
    def __init__(self, mode, path, data_list=[]):
        super().__init__(mode, path, data_list)

        self.encrypted_password = []

        for i in range(self.length):
            key = Fernet.generate_key()
            cipher = Fernet(key)

            self.encrypted = cipher.encrypt(self.data_list[i].encode())
            key = key.decode()
            self.encrypted = self.encrypted.decode()

            match self.mode:
                case "text" | "t":
                    self.key_first_section = key[:23]
                    self.key_second_section = key[23:]
                    self.encrypted_password.append(self.key_first_section + self.encrypted + self.key_second_section)

                case "image" | "i":
                    entry = key + "SPLIT" + self.encrypted
                    self.encrypted_password.append(entry.encode("utf-8"))

         
    def text_mode(self):
        for password in self.encrypted_password:
            for character in password:
                self.to_bin += str(ord(character)) + "#"

            self.to_bin += "|"

        return self.to_bin

    def image_mode(self):
        combined = b"||".join(self.encrypted_password) + b"||END"
        data = np.frombuffer(combined, dtype=np.uint8)

        total_capacity = self.WIDTH * self.HEIGHT * 4
        if len(data) + 8 > total_capacity:
            raise ValueError("Data is too large to fit in the image.")

        pixels = np.random.randint(0, 256, total_capacity, dtype=np.uint8)

        data_length = len(data)
        for i in range(8):
            pixels[i] = (data_length >> (i * 8)) & 0xFF

        pixels[8:8 + len(data)] = data

        pixels = pixels.reshape((self.HEIGHT, self.WIDTH, 4))
        image = Image.fromarray(pixels, mode="RGBA")

        return image
    
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
        image = Image.open(self.path).convert("RGBA")
        pixels = np.array(image, dtype=np.uint8).flatten()

        # Read header
        data_length = 0
        for i in range(8):
            data_length |= int(pixels[i]) << (i * 8)

        # Extract bytes
        raw = pixels[8:8 + data_length].tobytes()

        # Split and decrypt
        entries = raw.split(b"||")
        entries = [e for e in entries if e and e != b"END"]

        for entry in entries:
            entry_str = entry.decode("utf-8")
            key_str, encrypted_str = entry_str.split("SPLIT", 1)

            cipher = Fernet(key_str.encode())
            decrypted = cipher.decrypt(encrypted_str.encode())
            self.show_passwords.append(decrypted.decode())

        return self.show_passwords

    def voice_mode(self):
        pass

    def morse_mode(self):
        pass

def save(mode, path, passwords):
    match mode:
        case "text" | "t":
            with open(path.joinpath("output.Jaraare"), "a") as file: # Save encrypted passwords & keys in the choosen path
                file.write(passwords)

        case "image" | "i":
            passwords.save(path.joinpath("output.png")) # Save encrypted passwords & keys in the choosen path
            os.rename(path.joinpath("output.png"), path.joinpath("output.Jaraare")) # Rename the file to output.Jaraare


        case "voice" | "v":
            pass

        case "morse" | "m":
            pass

def get_file_type(path):
    mime = magic.from_file(path, mime=True)

    if mime.startswith("image/"):
        return "image"
    elif mime.startswith("text/"):
        return "text"
    else:
        return "other"