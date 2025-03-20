# EJERCICIO PARA MOSTRAR COMO USAR DES
# USTILIZAR LIBRERIA pycryptodome
# pip install pycryptodome

# IMPORTAR DES
from Crypto.Cipher import DES
# IOMPORTAR OS RANDOM PARA GENERAR CLAVE
# ES POSIBLE USAR EL RANDOM DE CRYPTO.RANDOM PARA MAYOR SEGURIDAD
import os
from os import urandom

# GENERAMOS UNA CLAVE ALEATORIA
# RECUERDEN QUE DES USA BLOQUES DE 8 BITS Y LLAVES DE 56 BITS DONDE 8 BITS SON DE PARIDAD
# UTILIZA 16 RONDAS PARA CIFRAR
key = os.urandom(8)

# UTILIZAMOS DES Y SELECCIONAMOS UN MODO DE OPERACIÓN PARA ESTE EJEMPLO ES EL ECB
cipher = DES.new(key, DES.MODE_ECB)

# UTILIZAMOS UN MENSAJE A CIFRAR
# EN ESTE PUNTO USTEDES DEBEN HACER SUS FUNCIONES PARA EXTRAER EL TEXTO DE UN ARCHIVO, EL CONTENIDO DE UNA IMAGEN, ETC.
# DEBE SER MULTIPLO DE 8 BYTES
plaintext = b"PRUEBA ALGOTIMO DES"  

# VALIDAR SI EL MENSAJE ES MULTIPLO DE 8 BYTES
if len(plaintext) % 8 != 0:
    print("El mensaje no es múltiplo de 8 bytes")
    print("Se debe rellenar con bytes de relleno")
    print("En este caso se usará el byte 0x00")
    # SE REL
    plaintext += b"\x00" * (8 - len(plaintext) % 8)

print("Mensaje a cifrar: ", plaintext)
ciphertext = cipher.encrypt(plaintext)
print(f"DES Cifrado: {ciphertext}")

# DESCIFRAMOS CON LA MISMA LLAVE Y EL MISMO MODO DE OPERACIÓN
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)

# EL MENSAJE DESCIFRADO PUEDE TENER BYTES DE RELLENO
# QUITAR LOS BYTES DE RELLENO
decrypted = decrypted.rstrip(b"\x00")
print(f"DES Descifrado: {decrypted}")