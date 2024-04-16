import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def aes_encrypt(plaintext):
    with open("../.keys/public-rsa-key.pem", "rb") as f:
        public_key = RSA.import_key(f.read())
    encryptor = PKCS1_OAEP.new(public_key)
    return encryptor.encrypt(plaintext.encode())


def aes_decrypt(ciphertext):
    with open("../.keys/private-rsa-key.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(ciphertext).decode()


if __name__ == "__main__":
    plaintext = "Goodbye, world."
    ciphertext = aes_encrypt(plaintext)

    assert plaintext == aes_decrypt(ciphertext)
