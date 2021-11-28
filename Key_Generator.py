from cryptography.fernet import Fernet

def test_fun():
    key = Fernet.generate_key()
    print(key)
    file = open ('key.key', 'wb')
    file.write(key) # Type Bytes
    file.close()