from Crypto.PublicKey import RSA

secret_code = "donald"
key = RSA.generate(2048)

encrypted_key = key.export_key(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")

file_out = open("rsa_key.bin", "wb")

file_out.write(encrypted_key)

print(key.publickey().export_key())