from random import randint as ri
from input_handler import input_handler
import encrypt

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

def saving(what_save, password):
    save = []
    if want_save == password:
        save = password

    elif want_save == "0":
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

    with open("output.txt", "a") as file:
        for i in save:
            file.write(f"{encrypt.encoding(i)}")


lenght = input_handler("Password Lenght(8)", low = 1, Type = "int", default = 8)
include_symbols = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
include_numbers = input_handler("Include symbols(Y/n)", options=["y", "n"], default = "y")
how_many_repeat = input_handler("How many passwords do you want(1)", low = 1, Type = "int", default = 1)

include_symbols = False if include_symbols == "n" else True
include_numbers = False if include_numbers == "n" else True

items = mixer(include_symbols, include_numbers)

print()
password = []

for i in range(how_many_repeat):
    password.append(password_generator(items, lenght = lenght))
    print(f"{i + 1}- {password[i]}")

print("\nCopy any passwords you want because they will be encrypted after saving.")

want_save = input_handler("\nWrite the number of things you want to save with a space(everything = Enter, nothing = 0)", low=0, high=len(password), default=password)
saving(0, password) if want_save == 0 else saving(want_save, password)
