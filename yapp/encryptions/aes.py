from os import path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

base_path = path.dirname(__file__)
key_path = path.abspath(path.join(base_path, "..", ".keys", "aes-key"))


def pad(string):
    # QUESTION: What is the purpose of this function?
    return string + (16 - len(string) % 16) * chr(16 - len(string) % 16)


def aes_encrypt(plaintext):
    with open(key_path, "rb") as f:
        key = f.read()
    encrypter = AES.new(key, AES.MODE_ECB)
    return encrypter.encrypt(pad(plaintext).encode())


def unpad(string):
    # QUESTION: What is the purpose of this function?
    return string[:-ord(string[len(string) - 1:])]


def aes_decrypt(ciphertext):
    base_path = path.dirname(__file__)
    with open(key_path, "rb") as f:
        key = f.read()
    decrypter = AES.new(key, AES.MODE_ECB)
    return unpad(decrypter.decrypt(ciphertext).decode())


if __name__ == "__main__":
    plaintext = "Goodbye, world."
    ciphertext = aes_encrypt(plaintext)

    assert plaintext == aes_decrypt(ciphertext)

