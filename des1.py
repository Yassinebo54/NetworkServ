from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(8)

def encrypt_ECB(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = text.encode('utf-8')
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

def encrypt_CBC(text, key):
    cipher = DES.new(key, DES.MODE_CBC)
    plaintext = text.encode('utf-8')
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

key = generate_key()
plaintext = "DES Systems and Network Security "
print("Original Text:", plaintext)

encrypted_text_ECB = encrypt_ECB(plaintext, key)
encrypted_text_CBC = encrypt_CBC(plaintext, key)

print("Encrypted Text ECB:", encrypted_text_ECB)
print("Encrypted Text CBC:", encrypted_text_CBC)