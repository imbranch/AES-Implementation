from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def keyVerification():
    key = input('Enter cryptographic key:').encode("utf8")
    try:
        cipher1 = AES.new(key, AES.MODE_CBC, "asdfasdfasdfasdf".encode("utf8"))
    except:
        print('Wrong Key or Error with key, Goodbye.')
        exit()
    try:
        cipher2 = AES.new(key, AES.MODE_CBC, iv=cipher1.iv)
    except:
        print('Wrong Key or Error with key, Goodbye.')
        exit()
    cipherObjects = [cipher1, cipher2] 
    return cipherObjects
   

def encryption(cipher):
    f = open('database.txt', 'r')
    plaintext = f.read()
    f.close
    with open('database.txt', 'wb') as f:
        ciphertext = cipher.encrypt(pad(plaintext.encode("utf8"), AES.block_size))
        f.write(ciphertext)
        print('Database Encrypted.')
    f.close


def decryption(cipher):
    plaintext = ""
    with open('database.txt', 'rb') as f:
        ciphertext = f.read()
        try:
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        except:
            print('Wrong Key, Goodbye.')
            exit()
        print('Database Opened.')
    f.close
    with open("database.txt", 'w') as f:
        f.write(plaintext.decode("utf8"))
    f.close