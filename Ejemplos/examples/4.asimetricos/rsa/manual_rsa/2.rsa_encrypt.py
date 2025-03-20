def rsa_encrypt(message, public_key):
    # Desempaqueta la clave pública (n, e)
    n, e = public_key
    
    # Convierte cada carácter del mensaje a su valor ASCII
    message_ascii = [ord(char) for char in message]
    
    # Cifra cada valor ASCII usando la fórmula c ≡ m^e (mod n)
    encrypted_message = [pow(char, e, n) for char in message_ascii]
    
    return encrypted_message

# Ejemplo de uso
message_to_encrypt = "HELLO"
public_key = (138953, 98629)
encrypted_message = rsa_encrypt(message_to_encrypt, public_key)

# Muestra los resultados
print(f"Mensaje Original: {message_to_encrypt}")
print(f"Mensaje Cifrado: {encrypted_message}")
