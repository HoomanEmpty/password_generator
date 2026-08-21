from random import randint as ri
from input_handler import input_handler
import encrypt
from pathlib import Path

# Password include these
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+-={[}]\\/:;|,.<>?'"
numbers = "0123456789"
uppercase_letters = letters.upper()
similar_letters = ["o", "O", "0", "I", "l", "C", "X", "Z", "V", "M", "S", "K", "W", "U", "P"]

def password_generator(items, lenght, probabilities = -1):
    '''
    Generate password with custom lenght and 
    custom probabilities and 
    choose include symbols & numbers or not.
    this function return string var 
    '''

    password = ""

    if probabilities == -1: # Give same chance for every character in item
        probabilities = []
        for i in items:
            probabilities.append(10)
    
    total = sum(probabilities) # Sum chance from every character

    for i in range(lenght): # Generate password with choose character with it's chance
        random = ri(0, total)

        for j in range(len(items)):# Choose character with it's chance
            random -= probabilities[j]

            if random <= 0:
                password += items[j]
                break

    return password

def mixer(include_symbols, include_numbers, have_uppercase_letters, remove_similar):
    '''
    It mixes symbols, numbers, and letters (include uppercase & lowercase by user choose) based on our choice of which ones to mix

    this function return string var that name is mixed and include mix of words that custom by user
    '''

    global letters, symbols, numbers, uppercase_letters, similar_letters

    mixed = letters
    mixed = mixed + symbols if include_symbols else letters
    mixed = mixed + numbers if include_numbers else mixed
    mixed = mixed + uppercase_letters if have_uppercase_letters else mixed

    if remove_similar:
        for i in similar_letters: # Remove similar words
            mixed = mixed.replace(i, "")

    return mixed

def save_password(want_save, password, path):
    '''
    save passwords in json file where program is running

    for now this program save key and encrypted passwords and it's not safe

    this function doesn't return anythings
    '''
    save = []
    if want_save == password: # Save all passwords that are created
        save = password

    else: # Save passwords that user choose 
        want_save = want_save.replace(",", " ")
        want_save = want_save.split()
        for i in want_save:
            save.append(password[int(i) - 1])

    password_list = []
    for item in save: # Encrypt password for saving (with saving their keys)
        password_list.append(encrypt.encoding(item))

    with open(path, "a") as file: # Save encrypted passwords & keys where path
        for item in password_list:
            
            file.write(item)

def show_password(path):
    '''
    Show passwords that save
    this function doesn't return anythings
    '''
    with open(path, "r") as file: # Go to the path that you tell it (or default path) and reads file
        info_reader = file.read()# Turn json file to dict in python

    passwords = encrypt.decoding(info_reader)
    for i in range(len(passwords)):
        print(f"{i + 1}_ {passwords[i]}")
        
# Choose between create new passwords or show previous passwords
option = input_handler("[C]reate new password or [s]how past password(C/s)", options=["c", "s"], default="c")

if option == "c":
    # Settings for create passwords
    lenght = input_handler("Password Lenght(8)", low = 1, Type = "int", default = 8) # Lenght of passwords
    include_symbols = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y") # Have symbols or not
    include_numbers = input_handler("Include number(Y/n)", options=["y", "n"], default = "y") # Have numbers or not
    have_uppercase_letters = input_handler("Passwords have uppercase letters(Y/n)", options=["y", "n"], default="y") # Have uppercase letters or not
    remove_similar = input_handler("Do you want remove similar word(y/N)", options=["y", "n"], default="n") # Remove similar words or not
    how_many_repeat = input_handler("How many passwords do you want(10)", low = 1, Type = "int", default = 10) # How many password you want

    include_symbols = False if include_symbols == "n" else True # Check symbol
    include_numbers = False if include_numbers == "n" else True # Check number
    have_uppercase_letters = False if have_uppercase_letters == "n" else True # Check uppercase
    remove_similar = False if remove_similar == "n" else True #Check remove similar

    items = mixer(include_symbols, include_numbers, have_uppercase_letters, remove_similar)

    print() # For ui.
    password = []

    for i in range(how_many_repeat): # Create passwords with setting that we choose and show.
        password.append(password_generator(items, lenght = lenght))
        print(f"{i + 1}- {password[i]}")

    print() #For ui.

    if remove_similar: # More explain for password if user want remove similar things.
        if have_uppercase_letters and include_symbols:
            print("All uppercase and lowercase letters are considered lowercase, and all symbols, and letters that are similar in lowercase are removed.")

        elif have_uppercase_letters:
            print("All uppercase and lowercase letters are considered lowercase.")

        elif include_symbols:
            print("All similar symbols, and letters have been removed.")

        else:
            print("All similar symbols, numbers, and letters have been removed.")

    print("\nCopy any passwords you want because they will be encrypted after saving.")

    # Saving section.
    want_save = input_handler("\nWrite the number of things you want to save with a space(everything = Enter, nothing = 0)", low=0, high=len(password), default=password, automate=False)

    if want_save == "0":
        print("I hope you have a better password next time!!!!")

    else:
        path = Path(input_handler("Enter path where you want save passwords", default=Path.cwd(), automate=False)).joinpath("output.Jaraare")
        save_password(want_save, password, path)
        print("Your voice save in: ", Path(path).joinpath("output.Jaraare"))

else:
    # Showing section.
    path = Path(input_handler("Enter path your save password or contintue default", default=Path.cwd(), automate=False)).joinpath("output.Jaraare")
    show_password(path)
