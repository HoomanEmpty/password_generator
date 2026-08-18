from random import randint as ri
from input_handler import input_handler
import encrypt
from pathlib import Path

# password include these
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+-={[}]\\/:;|,.<>?'"
numbers = "0123456789"
uppercase_letters = letters.upper()

def password_generator(items, lenght, probabilities = -1):
    '''
    generate password with custom lenght and 
    custom probabilities and 
    choose include symbols & numbers or not.
    this function return string var 
    '''

    password = ""

    if probabilities == -1: # give same chance for every character in item
        probabilities = []
        for i in items:
            probabilities.append(10)
    
    total = sum(probabilities) # sum chance from every character

    for i in range(lenght): # generate password with choose character with it's chance
        random = ri(0, total)

        for j in range(len(items)):# choose character with it's chance
            random -= probabilities[j]

            if random <= 0:
                password += items[j]
                break

    return password

def mixer(include_symbols, include_numbers, have_uppercase_letters): # todo: can add items for customizable combine.
    '''
    it mixes symbols, numbers, and letters based on our choice of which ones to mix

    this function return string var
    '''

    global letters, symbols, numbers, uppercase_letters

    mixed = letters
    mixed = mixed + symbols if include_symbols else letters
    mixed = mixed + numbers if include_numbers else mixed
    mixed = mixed + uppercase_letters if have_uppercase_letters else mixed

    return mixed

def save_password(want_save, password, path):
    '''
    save passwords in json file where program is running

    for now this program save key and encrypted passwords and it's not safe

    this function doesn't return anythings
    '''
    save = []
    if want_save == password: # save all passwords that are created
        save = password

    elif want_save == 0: # save nothing
        return 0
    
    elif want_save: # save passwords that user choose 
        # todo , and more space handler for better feel
        number_saver = ""

        for i in range(len(want_save)): # understand what want user to save
            if want_save[i] != " ":
                number_saver += want_save[i]
                if i + 1 >= len(want_save):
                    save.append(password[int(number_saver) - 1])

            else:
                save.append(password[int(number_saver) - 1])
                number_saver = ""

    password_list = []
    for item in save: # encrypt password for saving (with saving their keys)
        password_list.append(encrypt.encoding(item))

    with open(path, "a") as file: # save encrypted passwords & keys where path
        for item in password_list:
            
            file.write(item)

def show_password(path):
    '''
    show passwords that save
    this function doesn't return anythings
    '''
    with open(path, "r") as file: # go to the path that you tell it (or default path) and reads file
        info_reader = file.read()# turn json file to dict in python

    passwords = encrypt.decoding(info_reader)
    for i in range(len(passwords)):
        print(f"{i + 1}_ {passwords[i]}")
        
#choose between create new passwords or show previous passwords
option = input_handler("[C]reate new password or [s]how past password(C/s)", options=["c", "s"], default="c")

if option == "c":
    # settings for create passwords
    lenght = input_handler("Password Lenght(8)", low = 1, Type = "int", default = 8)
    include_symbols = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
    include_numbers = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
    have_uppercase_letters = input_handler("Passwords have uppercase letters(Y/n)", options=["y", "n"], default="y")
    how_many_repeat = input_handler("How many passwords do you want(10)", low = 1, Type = "int", default = 10)

    include_symbols = False if include_symbols == "n" else True
    include_numbers = False if include_numbers == "n" else True
    have_uppercase_letters = False if have_uppercase_letters == "n" else True

    items = mixer(include_symbols, include_numbers, have_uppercase_letters)

    print() # for ui
    password = []

    for i in range(how_many_repeat): # create passwords with setting that we choose and show
        password.append(password_generator(items, lenght = lenght))
        print(f"{i + 1}- {password[i]}")

    print("\nCopy any passwords you want because they will be encrypted after saving.")

    # saving section
    want_save = input_handler("\nWrite the number of things you want to save with a space(everything = Enter, nothing = 0)", low=0, high=len(password), default=password, automate=False)
    path = Path(input_handler("Enter path where you want save passwords", default=Path.cwd(), automate=False)).joinpath("output.Jaraare")
    save_password(0, password, path) if want_save == 0 else save_password(want_save, password, path)
    print("Your voice save in: ", Path(path).joinpath("output.Jaraare"))

else:
    # showing section
    path = Path(input_handler("Enter path your save password or contintue default", default=Path.cwd(), automate=False)).joinpath("output.Jaraare")
    show_password(path)
