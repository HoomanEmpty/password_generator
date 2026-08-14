from random import randint as ri
from input_handler import input_handler
import encrypt
from pathlib import Path
import json

letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+-={[}]\\/:;|,.<>?'"
numbers = "0123456789"

def password_generator(items, lenght, probabilities = -1):
    password = ""

    if probabilities == -1:
        probabilities = []
        for i in items:
            probabilities.append(10)
    
    total = sum(probabilities)

    for i in range(lenght):
        random = ri(0, total)

        for j in range(len(items)):
            random -= probabilities[j]

            if random <= 0:
                password += items[j]
                break

    return password

def mixer(include_symbols, include_numbers):
    global letters, symbols, numbers

    mixed = letters
    mixed = mixed + symbols if include_symbols == True else letters
    mixed = mixed + numbers if include_numbers == True else mixed

    return mixed

def save_password(want_save, password):
    save = []
    if want_save == password:
        save = password

    elif want_save == 0:
        return 0
    
    elif want_save:
        number_saver = ""

        for i in range(len(want_save)):
            if want_save[i] != " ":
                number_saver += want_save[i]

                if i + 1 >= len(want_save):
                    save.append(password[int(number_saver) - 1])

            else:
                save.append(password[int(number_saver) - 1])
                number_saver = ""

    password_dict = {"encrypted_password" : [],
                     "key" : []
                    } 
    
    for item in save:
        key, encrypted_password = encrypt.encoding(item)
        password_dict["encrypted_password"].append(encrypted_password.decode())
        password_dict["key"].append(key.decode())
        
    with open("output.Jaraare", "a") as file:
        file.write(json.dumps(password_dict))

def show_password(path):
    with open(path, "r") as file:
        info_reader = file.read()

    info_reader = json.loads(info_reader)

    for i in range(len(info_reader["encrypted_password"])):
        key = info_reader["key"][i].encode()
        encrypted = info_reader["encrypted_password"][i].encode()
        password = encrypt.decoding(key, encrypted)
        print(f"{i + 1}_ {password}")


option = input_handler("[C]reate new password or [s]how past password(C/s)", options=["c", "s"], default="c")

if option == "c":
    lenght = input_handler("Password Lenght(8)", low = 1, Type = "int", default = 8)
    include_symbols = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
    include_numbers = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
    how_many_repeat = input_handler("How many passwords do you want(10)", low = 1, Type = "int", default = 10)

    include_symbols = False if include_symbols == "n" else True
    include_numbers = False if include_numbers == "n" else True

    items = mixer(include_symbols, include_numbers)

    print()
    password = []

    for i in range(how_many_repeat):
        password.append(password_generator(items, lenght = lenght))
        print(f"{i + 1}- {password[i]}")

    print("\nCopy any passwords you want because they will be encrypted after saving.")

    want_save = input_handler("\nWrite the number of things you want to save with a space(everything = Enter, nothing = 0)", low=0, high=len(password), default=password, automate=False)
    save_password(0, password) if want_save == 0 else save_password(want_save, password)
    print("Your voice save in: ", Path.cwd().joinpath("output.Jaraare"))

else:
    path = input_handler("Enter path your save password or contintue default", default=Path.cwd().joinpath("output.Jaraare"), automate=False)
    show_password(path)
