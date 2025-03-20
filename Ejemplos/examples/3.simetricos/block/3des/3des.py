# EJERCICIO PARA MOSTRAR COMO USAR DES
# USTILIZAR LIBRERIA pycryptodome
# pip install pycryptodome

# IMPORTAR DES
from Crypto.Cipher import DES3
# IOMPORTAR OS RANDOM PARA GENERAR CLAVE
# ES POSIBLE USAR EL RANDOM DE CRYPTO.RANDOM PARA MAYOR SEGURIDAD
import os
from os import urandom
from Crypto.Util.Padding import pad, unpad

# GENERAMOS UNA CLAVE ALEATORIA
# RECUERDEN QUE 3des USA CLAVES DE 16 o 24 BYTES (128 o 192 BITS)
key = os.urandom(16)

# UTILIZAMOS DES Y SELECCIONAMOS UN MODO DE OPERACIÓN PARA ESTE EJEMPLO ES EL ECB
cipher = DES3.new(key, DES3.MODE_CBC)

plaintext = b"PRUEBA ALGOTIMO 3DES"
# UTILIZAMOS UNA LIBRERIA PARA QUE NOS BRINDE EL TEXTO RELLENADO EN LUGAR DE HACERLO NOSOTROS
# DEBE SER MULTIPLO DE 8 BYTES O DEL TAMAÑO DEL BLOQUE
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
print(f"3DES Cifrado: {ciphertext}")

# DESCIFRAMOS CON LA MISMA LLAVE Y EL MISMO MODO DE OPERACIÓN
decipher = DES3.new(key, DES3.MODE_CBC)
decrypted = decipher.decrypt(ciphertext)
print(f"DES3 Descifrado: {decrypted}")