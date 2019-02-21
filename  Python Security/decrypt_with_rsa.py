from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import os

class Decrypt(object):
    '''
        decrypt data file passed in
        with private key
    '''
    _FOLDER = "encrypted"
    _FILE = "private.pem"
    ROOT_DIR = os.path.dirname(__file__)
    PEM_FILE_PATH = os.path.join(ROOT_DIR, _FILE)
    ENCRYPTED_DATA_FOLDER = os.path.join(ROOT_DIR, _FOLDER)

    def pri_key(self):
        ''' check private file existence'''
        if os.path.isfile(self.PEM_FILE_PATH):
            pass

        else:
            raise Exception("Private key file is missing!")

    def data_folder(self):
        if os.path.exists(self.ENCRYPTED_DATA_FOLDER):
            print("[INFO] Encrypted data folder exists")

        else:
            raise Exception("Could not find encrypted data folder")

    def get_private_key(self):
        ''' check if file exists and return the key'''
        self.pri_key()
        private_key = RSA.import_key(open(self.PEM_FILE_PATH).read())
        return private_key

    def decrypt(self, data_file, num):
        '''
        decrypt data with AES session key
        :return: decrypted data
        '''
        file_path = os.path.join(self.ENCRYPTED_DATA_FOLDER, data_file)
        file_in = open(file_path, 'rb')
        private_key = self.get_private_key()

        enc_session_key, nonce, tag, ciphertext = [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        print("[DATA] File name #{}: {} \t\t\t\t Decrypted data: {}".format(num, data_file, data.decode("utf-8")))

    def decrypt_(self):
        '''
            extract data from encrypted file
            cycle through all the encrypted files in the folder
        '''
        self.data_folder()
        bin_files = os.listdir(self.ENCRYPTED_DATA_FOLDER)

        print("[INFO] Found {} encrypted files".format(len(bin_files)))
        print("[INFO] Decrypting files...")

        count = 1
        for enc_file in bin_files:
            if enc_file.endswith(".bin"):
                # in case we encounter another bin file
                try:
                    self.decrypt(enc_file, count)

                except Exception as e:
                    print("[ALERT] Could not decrypt file '{}'. {}".format(enc_file, e))

            count += 1

        print("[INFO] Done decrypting {} files".format(count))

# testing
dec = Decrypt()
dec.decrypt_()