from phe import paillier
from faker import Faker

def save_key(key_obj):
    '''
    save key obj to file
    '''

    try:
        with open("paillier_key.bin", "wb") as f:
            f.write(key_obj)

        print("[INFO] Keys successfully saved to file!")

    except Exception as e:
        print("[ERROR] There was a problem saving key to file!. ", e)

def gen_numbers(numbers):
    fake = Faker()

    for x in range(5):
        numbers.append(int(fake.numerify()))

    return numbers

def gen_keys():
    public_key, private_key = paillier.generate_paillier_keypair()
    return public_key, private_key

def numbers(x):
    print("********** RAW NUMBERS ********")
    for i in x:
        print(i)

def encrypt_numbers(key, raw_nums):
    encrypted = []
    enc = []
    encrypted_number_list = [key.encrypt(x) for x in raw_nums]
    enc.append([d.ciphertext() for d in encrypted_number_list])

    print("[INFO] Encrypted numbers: ", [n for n in enc], sep="\n")
    return encrypted_number_list, enc

def obfscate(raw):
    '''
    obfuscate encrypted data so that it becomes too hard to trace and crack
    without the provided key
    :param raw:
    :return obfuscated data x 2:
    '''
    print("[INFO] Before obfuscating: ", [f.ciphertext() for f in raw])
    for x in range(1, 3):
        c = [f.obfuscate() for f in raw]

    print("[INFO] After obfuscating: ", [f.ciphertext() for f in raw])

def decrypt_numbers(key, _encrypted):
    data = []
    for numbers in _encrypted:
        data.append(key.decrypt(numbers))

    print("[INFO] Decrypted numbers: ", data)

def run():
    nums = []
    num = gen_numbers(nums)
    pub, priv = gen_keys()

    numbers(num)
    enc_nums, enc = encrypt_numbers(pub, nums)
    obfscate(enc_nums)

    print("[INFO] After MAIN Obfuscating: ", [f.ciphertext() for f in enc_nums])

    decrypt_numbers(priv, enc_nums)

if __name__ == "__main__":
    run()

print("Hello donald")
