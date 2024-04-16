import binascii
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

with open("../.keys/des-key", "rb") as f:
    key = f.read()
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt a message
pad = lambda s: s + (8 - len(s) % 8) * chr(8 - len(s) % 8)
message = 'Hello World'
padded_message = pad(message)
encrypted_msg = cipher.encrypt(padded_message.encode())
print("Encrypted:", binascii.hexlify(encrypted_msg))

# Decrypt the message
decrypted_msg = cipher.decrypt(encrypted_msg).decode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
print("Decrypted:", unpad(decrypted_msg))

