import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("../.keys/public-rsa-key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())
encryptor = PKCS1_OAEP.new(public_key)

# Encrypt a message
message = 'Hello World'
encrypted_msg = encryptor.encrypt(message.encode())
print("Encrypted:", binascii.hexlify(encrypted_msg))

with open("../.keys/private-rsa-key.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Decrypt the message
decryptor = PKCS1_OAEP.new(private_key)
decrypted_msg = decryptor.decrypt(encrypted_msg)
print("Decrypted:", decrypted_msg.decode())
