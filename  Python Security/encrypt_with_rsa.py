'''
   @author:         Donald Chinhuru
   @project:        Encrypt data to file with RSA keys
                    Using OOP (left working flawlessly)
   @created:        18 Jan 2019
   @modified:       19 Jan 2019
'''

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from random import randint
import os

# test run for 1000 encrypted files
from time import sleep
from faker import Faker

class Encrypt(object):
    '''
        Encrypt data passed in
        each encrypted data is saved to a seperate file with a random name
    '''
    _FOLDER = "encrypted"
    _FILE = "receiver.pem"
    _SESSION_KEY = get_random_bytes(16)
    ROOT_DIR = os.path.dirname(__file__)
    ENCRYPTED_DATA_FOLDER = os.path.join(ROOT_DIR, _FOLDER)

    def rec_key(self):
        ''' check receiver.pem file existence'''
        if os.path.isfile(self._FILE):
            pass

        else:
            raise Exception("Receiver key file is missing!")

    def data_folder(self):
        # create folder with encrypted data files
        if os.path.exists(self.ENCRYPTED_DATA_FOLDER):
            print("[INFO] Encrypted data folder exists")

        else:
            print("[ALERT] Did not find encrypted data folder, creating..")
            os.mkdir(self.ENCRYPTED_DATA_FOLDER)
            print("[INFO] Folder created")

    def get_recipient_key(self):
        ''' check if file exists and return the key'''
        self.rec_key()
        recipient_key = RSA.import_key(open(self._FILE).read())
        return recipient_key

    def encrypt_data(self, data):
        '''
        encrypt data with AES session key
        :return: encrypted data
        '''
        data = data.encode("utf-8")

        recipient_key = self.get_recipient_key()

        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        self.file_out(esk=enc_session_key, can=cipher_aes, t=tag, ct=ciphertext)

        print("[INFO] Data Encrypted")

    def file_out(self, esk, can, t, ct):
        '''
            write encrypted data to file
        '''

        file = os.path.join(self.ENCRYPTED_DATA_FOLDER, "encrypted_data_{}.bin".format(randint(100, 999999)))
        f_out = open(file, 'wb')
        [f_out.write(x) for x in (esk, can.nonce, t, ct)]

        # debug
        print("[INFO] Data Encrypted to file '{}'".format(file))

running  = True
while running:
    print("_" * 50)
    print("  Welcome to encrypting testing program   ")

    text = input("Enter text to encrypt (type 'exit' to quit): ")

    if text == "exit":
        running = False

    else:
        enc = Encrypt()
        enc.encrypt_data(text)
