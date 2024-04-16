import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open("../.keys/aes-key", "rb") as f:
    key = f.read()

def pad(string):
    # QUESTION: What is the purpose of this function?
    return string + (16 - len(string) % 16) * chr(16 - len(string) % 16)


def aes_encrypt(plaintext):
    encrypter = AES.new(key, AES.MODE_ECB)
    return encrypter.encrypt(pad(plaintext).encode())


def unpad(string):
    # QUESTION: What is the purpose of this function?
    return string[:-ord(string[len(string) - 1:])]


def aes_decrypt(ciphertext):
    decrypter = AES.new(key, AES.MODE_ECB)
    return unpad(decrypter.decrypt(ciphertext).decode())


if __name__ == "__main__":
    plaintext = "Goodbye, world."
    ciphertext = aes_encrypt(plaintext)

    assert plaintext == aes_decrypt(ciphertext)

