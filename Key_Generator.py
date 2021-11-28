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
    print(key)