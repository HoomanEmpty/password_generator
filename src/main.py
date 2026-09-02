from random import randint as ri
from input_handler import input_handler
from pathlib import Path
import encrypt_mode

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

    if probabilities == -1: # Give the same chance to every character in item
        probabilities = []
        for i in items:
            probabilities.append(10)
    
    total = sum(probabilities) # The sum of chances of every character

    for i in range(lenght): # Generate the password with the choose character's chance
        random = ri(0, total)

        for j in range(len(items)): # Choose a character based on it's chance
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
        for i in similar_letters: # Avoid similar letters
            mixed = mixed.replace(i, "")

    return mixed

def save_password(want_save, password, path, mode):
    '''
    save passwords in json file where program is running

    for now this program save key and encrypted passwords and it's not safe

    this function doesn't return anythings
    '''
    save = []
    if want_save == password: # Save all of the generated passwords
        save = password

    else: # Save the password(s) that user has choosen
        want_save = want_save.replace(",", " ")
        want_save = want_save.split()
        for i in want_save:
            save.append(password[int(i) - 1])

    passwords = encrypt_mode.Encoding(mode, path, save).run_mode()
    encrypt_mode.save(mode, path, passwords) # Save the mode of encryption in the choosen path

def show_password(path):
    '''
    Show passwords that save
    this function doesn't return anythings
    '''
    mode = encrypt_mode.get_file_type(path.joinpath("output.Jaraare"))
    passwords = encrypt_mode.Decoding(mode, path).run_mode()
    
    for i in range(len(passwords)):
        print(f"{i + 1}_ {passwords[i]}")

def main():

    while(True):

        try:
            # The option to choose between creating new passwords or showing previously made passwords
            option = input_handler("\n[G]enerate new password or [s]how previously made passwords? ([G]/s)", options=["g", "s"], default="g")

            if option == "g":
                # Settings for password creation
                lenght = input_handler("Password Lenght [8]", low = 1, Type = "int", default = 8) # The lenght of the password(s)
                include_symbols = input_handler("Include symbols ([Y]/n)", options=["y", "n"], default = "y") # Include symbols or not
                include_numbers = input_handler("Include number ([Y]/n)", options=["y", "n"], default = "y") # Include numbers or not
                have_uppercase_letters = input_handler("Include uppercase letters ([Y]/n)", options=["y", "n"], default="y") # Include uppercase letters or not
                remove_similar = input_handler("Should similiar looking letters be avoided? (e.g w and W) (y/[N])", options=["y", "n"], default="n") # Avoid similar letters or not
                how_many_repeat = input_handler("How many password(s) do you want to generate? [10]", low = 1, Type = "int", default = 10) # How many passwords to generate

                include_symbols = False if include_symbols == "n" else True # Checks symbol
                include_numbers = False if include_numbers == "n" else True # Checks number
                have_uppercase_letters = False if have_uppercase_letters == "n" else True # Checks uppercase
                remove_similar = False if remove_similar == "n" else True #Checks avoiding similar letters

                items = mixer(include_symbols, include_numbers, have_uppercase_letters, remove_similar)

                print() # For indentation purposes.

                password = []

                for i in range(how_many_repeat): # Generates the passwords with the specified settings and show those settings.
                    password.append(password_generator(items, lenght = lenght))
                    print(f"{i + 1}- {password[i]}")

                print() # For indentation purposes.

                if remove_similar: # Gives detailed explanation about the options if user want similiar letters to be avoided.
                    if have_uppercase_letters and include_symbols:
                        print("All uppercase and lowercase letters are considered lowercase, and all symbols, and letters that are similar in lowercase were avoided.")

                    elif have_uppercase_letters:
                        print("All uppercase and lowercase letters are considered lowercase.")

                    elif include_symbols:
                        print("All similar symbols, and letters were avoided.")

                    else:
                        print("All similar symbols, numbers, and letters were avoided.")

                print("\nCopy any passwords you want to keep as plain text because they will be encrypted after saving.")

                # Saving section.
                want_save = input_handler("\nWrite the index of password(s) you want to save with a space (everything: Enter, None: = 0)", low=0, high=len(password), default=password, automate=False)

                if want_save == "0":
                    print("\nI hope I can provide better passwords next time!!!")

                else:
                    mode = input_handler("Choose the mode of encryption: [T]ext, [I]mage, [V]oice, [M]orse ([T]/i/v/m)", options=["t", "i", "v", "m"], default="t")
                    path = Path(input_handler("Enter the path where you want the password(s) to be saved", default=Path.cwd(), automate=False))
                    save_password(want_save, password, path, mode)
                    print("Your password(s) have been saved in: ", Path(path))

            else:
                # Showing section.
                path = Path(input_handler("Enter path your save password or contintue default", default=Path.cwd(), automate=False))
                show_password(path)

            reuse_status = input_handler("\nWould you like to [c]ontinue using the program or [e]xit it? (c/[e])",options=["c","e"])

            if reuse_status == "c":
                continue
            else:
                print("\nThank you for using this program!")
                return 0 # 0 The default exit code
        except:
            print("\n\nEither an error has occured or the user terminated the program! exiting now...\n")
            return 1 # exit with an error status code
        
if __name__ == "__main__":
    main()
