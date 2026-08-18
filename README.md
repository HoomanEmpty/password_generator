# 🔐 Password Generator

A simple and lightweight **password generator and password saver** written in Python.

This project allows you to generate multiple random passwords with a customizable length and character set. You can choose whether generated passwords should contain **uppercase letters, numbers, and symbols**, and optionally save selected passwords for later use.

> ⚠️ **Security Notice:** The current password-saving implementation is intended for learning and personal use. It should **not be considered a secure password manager** for storing highly sensitive credentials. See the [Security](#security) section for more information.

## ✨ Features

* 🔑 Generate random passwords
* 📏 Choose the password length
* 🔠 Enable or disable uppercase letters
* 🔢 Enable or disable numbers
* 🔣 Enable or disable symbols
* 🔄 Generate multiple passwords at once
* 💾 Save selected generated passwords
* 🔓 Read previously saved passwords
* 🔐 Encrypt saved passwords using [Fernet](https://cryptography.io/en/latest/fernet/)
* 🧩 Simple command-line interface
* 📦 Lightweight and easy to run

## 🛠️ Requirements

* Python **3.8+**
* `cryptography==49.0.0`

The project has been tested with `cryptography` version **49.0.0**.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone git@github.com:HoomanEmpty/password_generator.git
cd password_generator
```

### 2. Install dependencies

The recommended way is to use the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or, if your system uses `pip3`:

```bash
pip3 install -r requirements.txt
```

You can also install the dependency directly:

```bash
pip install cryptography==49.0.0
```

Or with `pip3`:

```bash
pip3 install cryptography==49.0.0
```

## ▶️ How to Run

Run the main program from the project root:

```bash
python src/main.py
```

On systems where Python 3 is accessed through `python3`:

```bash
python3 src/main.py
```

The program will then ask whether you want to create new passwords or show previously saved passwords:

```text
[C]reate new password or [s]how past password(C/s)
```

## 🔑 Generate Passwords

When creating passwords, you can configure:

* Password length
* Whether to include symbols
* Whether to include numbers
* Whether to include uppercase letters
* Number of passwords to generate

For example:

```text
Password Lenght(8): 16
Include symbols(Y/n): y
Include symbols(Y/n): y
Passwords have uppercase letters(Y/n): y
How many passwords do you want(10): 5
```

The generated passwords can contain:

* Lowercase English letters
* Uppercase English letters
* Numbers
* Symbols

The character types used in the generated passwords depend on the options selected by the user.

## 💾 Saving Passwords

After generating passwords, you can choose which passwords to save.

You can:

* Press **Enter** to save all generated passwords
* Enter `0` to save nothing
* Enter password numbers separated by spaces to save specific passwords

For example:

```text
Write the number of things you want to save with a space(everything = Enter, nothing = 0): 1 3 5
```

The selected passwords are encrypted before being written to the save file.

By default, the program uses:

```text
output.Jaraare
```

as the save file name.

The file is created inside the directory specified by the user.

> ⚠️ The generated `output.Jaraare` file should not be committed to the repository if it contains your personal passwords.

## 🔓 Showing Saved Passwords

To display previously saved passwords, choose:

```text
s
```

when starting the program.

Then enter the directory containing the saved `output.Jaraare` file.

The program will read the saved data, decrypt the passwords, and display them in the terminal.

## 🔐 Encryption

Saved passwords are encrypted using **Fernet symmetric encryption** from the `cryptography` package.

The project generates a Fernet key and uses it to encrypt each password before saving it.

When saved data is loaded, the program reconstructs the key and decrypts the stored passwords.

For more information about Fernet:

https://cryptography.io/en/latest/fernet/

## ⚠️ Security

This project is primarily a **learning/personal project** and should not currently be treated as a production-grade password manager.

The current implementation stores the encryption key together with the encrypted password data. This means that the current storage design does **not provide strong protection** if someone obtains the saved file.

Therefore:

> **Do not use the current version to store highly sensitive passwords, banking credentials, recovery codes, API secrets, or other critical information.**

The project is intended primarily for **learning, experimentation, and demonstrating Python programming concepts**.

### Possible Future Improvements

Some possible improvements for future versions include:

* Secure key derivation from a master password
* Separate and protected key storage
* Better file permissions
* A safer storage format
* Password strength estimation
* Secure memory handling
* Better error handling
* Input validation improvements
* Unit tests
* A proper password-manager architecture
* Customizable character sets
* More advanced password-generation options

## 📁 Project Structure

```text
password_generator/
├── src/
│   ├── encrypt.py
│   ├── input_handler.py
│   └── main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### `src/main.py`

Contains the main application logic, password generation, saving/loading functionality, and command-line interface.

### `src/encrypt.py`

Contains the encryption and decryption functions based on Fernet.

### `src/input_handler.py`

Provides a reusable input-validation function supporting strings, integers, floats, booleans, ranges, defaults, and predefined options.

### `requirements.txt`

Contains the project's Python dependencies.

The current dependency is:

```text
cryptography==49.0.0
```

## 🧪 Example

A typical workflow looks like this:

```text
$ python src/main.py

[C]reate new password or [s]how past password(C/s): c

Password Lenght(8): 16
Include symbols(Y/n): y
Include symbols(Y/n): y
Passwords have uppercase letters(Y/n): y
How many passwords do you want(10): 3

1- xxxxxxxxxxxxxxxx
2- xxxxxxxxxxxxxxxx
3- xxxxxxxxxxxxxxxx

Copy any passwords you want because they will be encrypted after saving.
```

The actual generated passwords will of course be different each time.

## 🤝 Contributing

Contributions are welcome!

If you have an idea for improving the project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your changes
5. Open a Pull Request

Bug reports, suggestions, and improvements are also welcome.

## 📜 License

This project is licensed under the **MIT License**.

The MIT License allows you to:

* Use the software
* Copy the software
* Modify the software
* Distribute the software
* Use it commercially

The main requirement is that the original copyright notice and MIT License text are retained with copies or substantial portions of the software.

See the [`LICENSE`](LICENSE) file for the complete license text.

## 👤 Author

**Hooman (Jaraare) Karimi Shad**

GitHub: [@HoomanEmpty](https://github.com/HoomanEmpty)

---

⭐ If you find this project useful, consider giving it a star!
