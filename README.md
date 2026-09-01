# 🔐 Password Generator & Manager

A lightweight **password generator and encrypted password manager** written in Python — built for learning, experimentation, and personal use.

Generate strong random passwords with a fully customizable character set, then encrypt and save them locally using Fernet symmetric encryption.

> ⚠️ **Security Notice:** The encryption key is stored alongside the encrypted data. This project is **not a production-grade password manager**. See [Security](#️-security) for details.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 Password Generation | Random passwords with a configurable length |
| 🔠 Character Control | Toggle uppercase letters, numbers, and symbols |
| 🚫 Similarity Filter | Optionally avoid visually similar characters (e.g. `O`, `0`, `I`, `l`) |
| 🔢 Batch Generation | Generate multiple passwords in one run |
| 💾 Encrypted Saving | Save selected passwords encrypted with Fernet |
| 🔓 Password Recovery | Read and decrypt previously saved passwords |
| 🖼️ Multiple Modes | Save via Text file or embed inside an Image (PNG) |
| 🧩 Clean CLI | Simple, guided command-line interface |

---

## 🛠️ Requirements

- Python **3.10+** (required for `match`/`case` syntax)
- `cryptography == 49.0.0`
- `Pillow`
- `numpy`

Install all dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install cryptography==49.0.0 Pillow numpy
```

---

## 📁 Project Structure

```
password_generator/
├── src/
│   ├── main.py            # Entry point — CLI, generation, save/load logic
│   ├── encrypt_mode.py    # Encryption & decryption (Text and Image modes)
│   └── input_handler.py   # Reusable input validation utility
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:HoomanEmpty/password_generator.git
cd password_generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
python src/main.py
```

---

## ▶️ Usage

When the program starts, it asks:

```
[G]enerate new password or [s]how previously made passwords? ([G]/s):
```

---

### 🔑 Generate Passwords

Choose `G` (or press Enter) to enter the generation flow.

```
Password Length [8]: 20
Include symbols ([Y]/n): y
Include numbers ([Y]/n): y
Include uppercase letters ([Y]/n): y
Should similar looking letters be avoided? (e.g w and W) (y/[N]): n
How many passwords do you want to generate? [10]: 5
```

The program will display all generated passwords:

```
1- Xk#9mP@qL2!vTz&nJwR
2- bY$3eK*8uAf!xQi^mNcV
3- ...
```

---

### 💾 Save Passwords

After generation, you'll be prompted:

```
Write the index of password(s) you want to save with a space (everything: Enter, None: = 0):
```

- Press **Enter** → save all
- Enter `0` → save nothing
- Enter indices like `1 3 5` → save specific passwords

Then choose an **encryption mode**:

```
Choose the mode of encryption: [T]ext, [I]mage, [V]oice, [M]orse ([T]/i/v/m):
```

And a **save location**:

```
Enter the path where you want the password(s) to be saved:
```

Passwords are saved to a file named `output.Jaraare` (text mode) or `output_image.png` (image mode) at the chosen location.

> ⚠️ Never commit your `output.Jaraare` or `output_image.png` files if they contain real passwords.

---

### 🔓 View Saved Passwords

Choose `s` at the start:

```
[G]enerate new password or [s]how previously made passwords? ([G]/s): s
Enter path to your saved passwords or continue with default:
```

The program reads, decrypts, and displays all saved passwords in the terminal.

---

## 🔐 Encryption Modes

### Text Mode (`t`) — Default

Passwords are encrypted with a Fernet key. The key is split and embedded around the ciphertext, then each character is converted to its ASCII code and written to `output.Jaraare`.

**Format per password:**
```
key_part_1 + encrypted_data + key_part_2 (stored as ASCII codes separated by #, entries separated by |)
```

### Image Mode (`i`)

Passwords are encrypted and the raw bytes are embedded into the pixel data of a PNG image (`output_image.png`).

- The first 8 bytes of the image store the data length as a header.
- The encrypted password bytes follow, embedded into the red channel of the image pixels.
- The rest of the image is white noise-free (solid white background for deterministic decoding).
- Decoding reads the header, extracts the exact byte count, and decrypts.

> This mode hides data inside an image file — a basic form of **steganography**.

### Voice & Morse Modes

These modes are planned for future development.

---

## ⚙️ How Password Generation Works

`password_generator()` builds a password character by character using a **weighted random selection**:

1. A character pool is assembled based on the user's choices (letters, uppercase, numbers, symbols).
2. Optionally, visually similar characters are removed (e.g. `O`, `0`, `I`, `l`, `S`, `5`).
3. Each character in the pool is assigned equal weight (by default).
4. For each position, a random number is rolled against the cumulative weights to pick a character.

This approach allows future support for **custom per-character probabilities**.

---

## 🔒 Security

This project is designed for **learning and personal experimentation**, not for production use.

### Current limitations:

- The Fernet encryption key is split and stored together with the ciphertext — anyone with the output file can decrypt the passwords.
- No master password or key derivation function (KDF) is used.
- File permissions are not hardened.

### Planned improvements:

- [ ] Master password with PBKDF2 / Argon2 key derivation
- [ ] Separate key storage
- [ ] Password strength estimator
- [ ] Secure memory handling (zeroing secrets after use)
- [ ] Full implementation of Image, Voice, and Morse modes
- [ ] Unit tests
- [ ] Input validation hardening
- [ ] Configurable character weights for generation

---

## 🤝 Contributing

Contributions, bug reports, and ideas are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make and test your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — you're free to use, copy, modify, and distribute it, as long as the original copyright notice is kept.

See [`LICENSE`](LICENSE) for the full text.

---

## 👤 Author

**Hooman (Jaraare) Karimi Shad**
GitHub: [@HoomanEmpty](https://github.com/HoomanEmpty)

---

⭐ If this project helped you learn something, consider leaving a star!