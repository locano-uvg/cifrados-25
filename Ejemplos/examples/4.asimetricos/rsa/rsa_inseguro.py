from Crypto.PublicKey import RSA

# Generación de clave RSA insegura (sin padding adecuado)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

def cifrar_inseguro(mensaje):
    key_pub = RSA.import_key(public_key)
    return pow(int.from_bytes(mensaje.encode(), 'big'), key_pub.e, key_pub.n)  # Cifrado directo, sin padding

def descifrar_inseguro(mensaje_cifrado):
    key_priv = RSA.import_key(private_key)
    return pow(mensaje_cifrado, key_priv.d, key_priv.n).to_bytes((key_priv.n.bit_length() + 7) // 8, 'big').decode()

mensaje = "Hola Mundo"
mensaje_cifrado = cifrar_inseguro(mensaje)
mensaje_descifrado = descifrar_inseguro(mensaje_cifrado)

print("Mensaje cifrado (sin padding seguro):", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)