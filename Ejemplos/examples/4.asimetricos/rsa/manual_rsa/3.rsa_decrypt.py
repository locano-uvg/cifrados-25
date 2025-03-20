def rsa_decrypt(encrypted_message, private_key):
    # Desempaqueta la clave privada (n, d)
    n, d = private_key
    
    # Descifra cada valor cifrado usando la fórmula m ≡ c^d (mod n)
    decrypted_message_ascii = [pow(char, d, n) for char in encrypted_message]
    
    # Convierte cada valor ASCII a su carácter correspondiente
    decrypted_message = ''.join([chr(char) for char in decrypted_message_ascii])
    
    return decrypted_message

# Ejemplo de uso
encrypted_message_to_decrypt = [116017, 66240, 22672, 22672, 47860]
private_key = (138953, 29749)
decrypted_message = rsa_decrypt(encrypted_message_to_decrypt, private_key)

# Muestra los resultados
print(f"Mensaje Cifrado: {encrypted_message_to_decrypt}")
print(f"Mensaje Descifrado: {decrypted_message}")
