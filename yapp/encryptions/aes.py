import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open("../.keys/aes-key", "rb") as f:
    key = f.read()
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt a message
pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
message = 'Hello World'
padded_message = pad(message)
encrypted_msg = cipher.encrypt(padded_message.encode())
print("Encrypted:", binascii.hexlify(encrypted_msg))

# Decrypt the message
decrypted_msg = cipher.decrypt(encrypted_msg).decode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
print("Decrypted:", unpad(decrypted_msg))

