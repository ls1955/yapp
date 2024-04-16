from os import path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(plaintext):
    base_path = path.dirname(__file__)
    with open(path.abspath(path.join(base_path, "..", ".keys", "public-rsa-key.pem")), "rb") as f:
        public_key = RSA.import_key(f.read())
    encryptor = PKCS1_OAEP.new(public_key)
    return encryptor.encrypt(plaintext.encode())


def rsa_decrypt(ciphertext):
    base_path = path.dirname(__file__)
    with open(path.abspath(path.join(base_path, "..", ".keys", "private-rsa-key.pem")), "rb") as f:
        private_key = RSA.import_key(f.read())
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(ciphertext).decode()


if __name__ == "__main__":
    plaintext = "Goodbye, world."
    ciphertext = rsa_encrypt(plaintext)

    assert plaintext == rsa_decrypt(ciphertext)

