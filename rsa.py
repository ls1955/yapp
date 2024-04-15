
m Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
encryptor = PKCS1_OAEP.new(public_key)

# Encrypt a message
message = 'Hello World'
encrypted_msg = encryptor.encrypt(message.encode())
print("Encrypted:", binascii.hexlify(encrypted_msg))

# Decrypt the message
decryptor = PKCS1_OAEP.new(key)
decrypted_msg = decryptor.decrypt(encrypted_msg)
print("Decrypted:", decrypted_msg.decode())

