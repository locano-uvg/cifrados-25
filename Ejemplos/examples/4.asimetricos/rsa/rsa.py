from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generar_llaves():
    # Generamos una clave RSA de 2048 bits
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    print("LLAVE PRIVADA:\n", private_key.decode())
    print("LLAVE PÚBLICA:\n", public_key.decode())

    return private_key, public_key

def guardar_llaves(private_key, public_key):
    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key)

def cifrar_mensaje(public_key, mensaje):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)  # Usamos OAEP para mayor seguridad
    mensaje_cifrado = cipher.encrypt(mensaje.encode())
    return mensaje_cifrado
    # return base64.b64encode(mensaje_cifrado).decode() 

def descifrar_mensaje(private_key, mensaje_cifrado):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    # mensaje_cifrado_bytes = base64.b64decode(mensaje_cifrado)
    mensaje_descifrado = cipher.decrypt(mensaje_cifrado)
    return mensaje_descifrado.decode()

# Prueba del código
private_key, public_key = generar_llaves()
guardar_llaves(private_key, public_key)

mensaje = "Hola Mundo"
mensaje_cifrado = cifrar_mensaje(public_key, mensaje)
print("\nMensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_mensaje(private_key, mensaje_cifrado)
print("\nMensaje descifrado:", mensaje_descifrado)