from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
    
# Generación de clave RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Mensaje y firma
mensaje = b"Hola, este es un mensaje firmado."
hash_mensaje = SHA256.new(mensaje)
firma = pss.new(key).sign(hash_mensaje)
print(f"Firma: {firma}")

# Verificación de firma
hash_mensaje = SHA256.new(mensaje)
verifier = pss.new(key.publickey())
try:
    verifier.verify(hash_mensaje, firma)
    print("Firma válida.")
except (ValueError, TypeError):
    print("Firma inválida.")