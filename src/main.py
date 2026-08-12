from random import randint as ri
from input_handler import input_handler

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

lenght = input_handler("Password Lenght(8) ", low = 1, Type = "int", default = 8)
include_symbols = input_handler("Include symbols(Y/n) ", options=["y", "n"], default = "y")
include_numbers = input_handler("Include symbols(Y/n) ", options=["y", "n"], default = "y")
how_many_repeat = input_handler("How many passwords do you want(1) ", low = 1, Type = "int", default = 1)

include_symbols = False if include_symbols == "n" else True
include_numbers = False if include_numbers == "n" else True

items = mixer(include_symbols, include_numbers)

print()
for i in range(how_many_repeat):
    print(password_generator(items, lenght = lenght))

