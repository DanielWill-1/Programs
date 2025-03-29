# -*- coding: utf-8 -*-
"""dpslab4th.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MtCM7hVMJnaIjTDZREM7AH_BJSUYbGGu
"""

!pip install Crypto

!pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_decrypt():
    plaintext = b"This is a secret message to be encrypted." # Message to encrypt
    key = get_random_bytes(16) # AES-128 requires a 16-byte key

    padded_plaintext = pad(plaintext, AES.block_size)

    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)

    print("Original Plaintext:", plaintext.decode())
    print("Padded Plaintext:", padded_plaintext)
    print("Ciphertext (Hex):", ciphertext.hex())
    print("-" * 50)

    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv) # Use the same key and IV
    decrypted_data = cipher_decrypt.decrypt(ciphertext)

    decrypted_plaintext = unpad(decrypted_data, AES.block_size)
    print("Decrypted Plaintext:", decrypted_plaintext.decode())

if __name__ == "__main__":
    aes_encrypt_decrypt()