from sympy import mod_inverse
alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Encript: E(a,b,x) = (ax + b) mod m
#  x = valor numérico de la letra
#  m = length of the alphabet
# Decript: E(a,b,x) = (a-1 * (x - b)) mod m
# 

# get index of a letter in the alphabet
# alphabet.index('a') # 0

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

def clearText(text):
    # remove áéíóúü
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')

    return ''.join([c for c in text if c in alphabet])
def cifrar_afin(texto, a, b):
    texto = clearText(texto)
    m = len(alfabeto)

    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            es_mayuscula = caracter.isupper()
            caracter = caracter.lower()
            posicion = (a * alfabeto.index(caracter) + b) % m
            letra_cifrada = alfabeto[posicion]
            if es_mayuscula:
                letra_cifrada = letra_cifrada.upper()
            texto_cifrado += letra_cifrada
        else:
            texto_cifrado += caracter

    return texto_cifrado

def descifrar_afin(texto_cifrado, a, b):
    m = len(alfabeto)
    try:
        a_inverso = mod_inverse(a, m)
    except ValueError:
        return "El valor de a no tiene inverso modular"

    texto_descifrado = ""
    for caracter in texto_cifrado:
        if caracter.isalpha():
            es_mayuscula = caracter.isupper()
            caracter = caracter.lower()
            posicion = (a_inverso * (alfabeto.index(caracter) - b)) % m
            letra_descifrada = alfabeto[posicion]
            if es_mayuscula:
                letra_descifrada = letra_descifrada.upper()
            texto_descifrado += letra_descifrada
        else:
            texto_descifrado += caracter

    return texto_descifrado

# Ejemplo de uso:
texto_original = "hello world"
a = 5
b = 8



plain_text = input("Ingrese el texto a cifrar: ")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
encrypted_text = cifrar_afin(plain_text, a, b)
print("Texto cifrado:", encrypted_text)

print("___________________\n")

encrypted_text = input("Ingrese el texto cifrado: ")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
decrypted_text = descifrar_afin(encrypted_text, a, b)
print("Texto descifrado:", decrypted_text)
