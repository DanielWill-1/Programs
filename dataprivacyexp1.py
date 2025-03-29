# -*- coding: utf-8 -*-
"""dataprivacyexp1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hyHGwWu2ae8TDxR-42sqhtG1fnaf18ui
"""

# Caesar Cipher for Confidentiality

# Function to encrypt plaintext using Caesar Cipher
def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase letters
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters (like spaces or punctuation) are not changed
    return encrypted_text

# Function to decrypt Caesar Cipher
def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)  # Decrypt by shifting in the opposite direction

# Example usage
plain_text = "Hello, Confidential World!"
shift = 3  # Number of positions to shift for encryption

# Encrypt the plain text
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
# Decrypt the encrypted text
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

# Output
print("Plaintext: ", plain_text)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)

import hashlib

# Function to calculate the hash of a given text (using SHA-256)
def calculate_hash(text):
    # Use SHA-256 hashing algorithm
    hash_object = hashlib.sha256(text.encode())  # Encode the string into bytes
    hash_hex = hash_object.hexdigest()  # Get the hexadecimal representation of the hash
    return hash_hex

# Function to check if the integrity of the data has been preserved
def check_integrity(original_text, received_text):
    # Calculate the hash of both the original text and the received text
    original_hash = calculate_hash(original_text)
    received_hash = calculate_hash(received_text) # This line was indented incorrectly, causing the error.

    # If the hashes are the same, integrity is preserved
    if original_hash == received_hash:
        return True  # Integrity is intact
    else:
        return False  # Integrity has been compromised

# Example usage
original_text = "This is the original message."
modified_text = "This is the modified message."  # Modified version

# Calculate hash for the original message
original_hash = calculate_hash(original_text)

# Check integrity of the original text and the modified text
is_integrity_preserved = check_integrity(original_text, modified_text)

# Output
print("Original Text Hash:", original_hash)
print("Modified Text Hash:", calculate_hash(modified_text))
print("Is integrity preserved?", is_integrity_preserved)

import hashlib
def hash_password(password):
  sha256_hash = hashlib.sha256()
  sha256_hash.update(password.encode('utf-8'))
  return sha256_hash.hexdigest()

stored_password_hash = hash_password("123")
print(f"Stored password hash: (stored_password_hash)")

entered_password = "1234"
entered_password_hash = hash_password(entered_password)

if entered_password_hash == stored_password_hash:
  print("Password is valid!")
else:
  print("Invalid password!")