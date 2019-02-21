from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from uuid import uuid4

# using pycryptodome module for saving encrypted data to file
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

data = "im going to encrypt this file for now!".encode("utf-8")
data1 = uuid4().bytes
ciphertext, tag = cipher.encrypt_and_digest(data1)

file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

print("Key: ", key)
print("Cipher: ", cipher)
print("Data: ", data)
print("Data1: ", data1)
print("Ciphertext: ", ciphertext)
