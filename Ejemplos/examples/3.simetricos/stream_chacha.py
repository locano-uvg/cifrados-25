import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def create_nonce():
    return os.urandom(16)

def create_keystream(nonce):
    return nonce

def cypher_text(text, keystream):
    ciphertext = encryptor.update(data)
    with open("archivo_cifrado.txt", "wb") as f:
        f.write(ciphertext)

    return ciphertext


file_path = r"Ejemplos/examples/3.simetricos/informacion.txt"

# Crear la clave
key = urandom(32) 
nonce = create_nonce()
keystream = create_keystream(nonce)

# key = 'ab108b4292497216930a0a14867d777c512626affd94aecd0af19be032a98425'
# key = bytes.fromhex(key)
# print(f"Clave: {key.hex()}")
# # Crear el nonce
# nonce = '568920136e7a7bf5a813f5afea41c379'
# nonce = bytes.fromhex(nonce)
# print(f"Nonce: {nonce.hex()}")

print(f"-"*50)

# Crear el cifrador
cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
encryptor = cipher.encryptor()

ciphertext = encryptor.update(read_file(file_path).encode())

print(f"Texto cifrado: {ciphertext.hex()}")
print(f"-"*50)

# Descifrar el mensaje
decryptor = cipher.decryptor()
decrypted_text = decryptor.update(ciphertext)

print(f"Texto descifrado: {decrypted_text.decode()}")
