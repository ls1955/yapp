from os import path
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

base_path = path.dirname(__file__)
key_path = path.abspath(path.join(base_path, "..", ".keys", "des-key"))


def pad(string):
    return string + (8 - len(string) % 8) * chr(8 - len(string) % 8)


def des_encrypt(plaintext):
    base_path = path.dirname(__file__)
    with open(key_path, "rb") as f:
        key = f.read()
    encrypter = DES.new(key, DES.MODE_ECB)
    return encrypter.encrypt(pad(plaintext).encode())


def unpad(string):
    return string[:-ord(string[len(string) - 1:])]


def des_decrypt(ciphertext):
    base_path = path.dirname(__file__)
    with open(key_path, "rb") as f:
        key = f.read()
    decrypter = DES.new(key, DES.MODE_ECB)
    return unpad(decrypter.decrypt(ciphertext).decode())
