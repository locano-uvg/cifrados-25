# IMPORTAMOS AES DE LA LIBRERIA Crypto.Cipher
from Crypto.Cipher import AES
# PODEMOS USAR COMO ALTERNATIVA DE OS URANDOM LA LIBRERIA Crypto.Random PARA GENERAR BYTES ALEATORIOS
from Crypto.Random import get_random_bytes
# PODEMOS USAR LA LIBRERIA BINASCII PARA CONVERTIR BYTES A HEXADECIMAL
import binascii
from Crypto.Util.Padding import pad, unpad

# CREAMOS UNA LLAVE DE 256 BITS
key = get_random_bytes(32)
# CREAMOS UN VECTOR DE INICIALIZACIÓN ALEATORIO DE 16 BYTES
iv = get_random_bytes(16) 

cipher = AES.new(key, AES.MODE_CBC, iv)
# EL MENSAJE DEBE SER MULTIPLO DE 16 BYTES
plaintext = b"Mensaje de AES-256" 
# RELLENAMOS EL MENSAJE CON BYTES DE RELLENO
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print(f"AES Cifrado: {binascii.hexlify(ciphertext)}")

# Descifrado
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print(f"AES Descifrado: {decrypted}")