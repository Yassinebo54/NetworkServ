import os
def generate_key(s):
# Function to generate the RC4 key based on the input key 's'
    key = bytearray(range(256)) # initializes a bytearray, used as the initial state for the RC4 algorithm
    j = 0
    for i in range(256): # Iterate through the range of 256, modifying the key based on the input key 's'
        j = (j + key[i] + s[i % len(s)]) % 256
        key[i], key[j] = key[j], key[i]
    return key

def rc4_crypt(data, key):
# Function to perform RC4 encryption/decryption on the input data using the generated key
    key = generate_key(key)
    output = bytearray()# Initialize an empty bytearray to store the encrypted/decrypted data
    i = j = 0
    for byte in data: # Main loop, iterate through each byte in the input data
        i = (i + 1) % 256
        j = (j + key[i]) % 256 # Update 'i' and 'j' based on the current state of the key
        key[i], key[j] = key[j], key[i] # Swap values in the key at positions 'i' and 'j'
        output.append(byte ^ key[(key[i] + key[j]) % 256]) # XOR the current byte with a pseudo-random byte from the key
    return bytes(output)

def encrypt_file(input_file, output_file, key): # Function to encrypt a file using RC4
    with open(input_file, 'rb') as file:
        data = file.read()
        encrypted_data = rc4_crypt(data, key)
        with open(output_file, 'wb') as output_file:
            output_file.write(encrypted_data)
        print(f"Encryption complete. Encrypted file saved as {output_file.name}")

def decrypt_file(input_file, output_file, key): # Function to decrypt a file using RC4    
    encrypt_file(input_file, output_file, key)
    print(f"Decryption complete. Decrypted file saved as {output_file.name}")

input_image = "/Users/yassin54/Desktop/audio.m4a"
encrypted_image = "/Users/yassin54/Desktop/encrypted audio"
decrypted_image = "decrypted_audio.mp4"
# Get a 16-character ASCII key from the user
#encryption_key = input("Enter a 16-character ASCII key: ").encode('utf-8')[:16]
encryption_key = "qwertyuiopasdfgh".encode('utf-8')[:16]
#encrypt_file(input_image, encrypted_image, encryption_key)
decrypt_file(encrypted_image, decrypted_image, encryption_key)
