from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


#Write to File
def test_fun():
    key = Fernet.generate_key()
    print("Read Key is:")
    print(key)
    file = open ('key.key', 'wb')
    file.write(key) # Type Bytes
    file.close()
#Read from File
def test_fun_read():
    file = open('key.key', 'rb')  # read
    key = file.read()  # Type Bytes
    file.close()
    print("Read Key is:")
    print(key)

#passsword
def test_fun_pass():
    password_provided = "password" # input from string
    password = password_provided.encode() #conversion to bytes
    salt = b"'\xab\x1a\x8do\x8c\xed\xa6\xec]\x90@24y\xff"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key=base64.urlsafe_b64encode(kdf.derive(password))# password
    file = open('key.key', 'rb')  # read
    key = file.read()  # Type Bytes
    file.close()
    print(key)

def testMain():
    # Get the key from the file
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    #Encode the message
    message = "My deep message"
    encode = message.encode()

    # encrypt the message
    f = Fernet(key)
    encrypted = f.encrypt(encode)

    #Get the key (Demonstration purpose)
    file = open('key.key','rb')
    key = file.read()#key bytes
    file.close()

    #Decrypt the encypted message
    f2 = Fernet(key)
    decrypted = f2.decrypt(encrypted)

    # Decode the message
    original_message = decrypted.decode()
    print(original_message)



def testEncr():
    # Get the key from the file
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

    # open the file to encrypt
    with open('ReadableMessage.txt', 'rb', ) as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    # Write to encrypted file
    with open('EncodeMessage.txt.encrypted', 'wb') as f:
        f.write(encrypted)
    print("Message Crypted")

def testDecr():
    # Get the key from the file
    file = open('key.key', 'rb')
    key = file.read()
    file.close()


    # Open file to decrypt
    with open('EncodeMessage.txt.encrypted', 'rb', ) as f:
        data = f.read()

    #Decrypt the encypted message
    fernet = Fernet(key)

    decrypted = fernet.decrypt(data)

    with open('DecodeMessage.txt', 'wb') as f:
        f.write(decrypted)
    print("Message Decrypted")


