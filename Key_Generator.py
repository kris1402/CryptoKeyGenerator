from cryptography.fernet import Fernet

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