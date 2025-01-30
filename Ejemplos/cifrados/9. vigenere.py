
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
def clearText(text):
    # remove áéíóúü
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')


    return ''.join([c for c in text if c in alfabeto])

def cifrar_vigenere(texto, clave):
    m = len(alfabeto)

    # Convertir el texto y la clave a minúsculas para evitar problemas con mayúsculas
    texto = texto.lower()
    texto = clearText(texto)
    clave = clave.lower()

    texto_cifrado = ""
    clave_extendida = ""
    if len(clave) < len(texto):
        # Extender la clave para que tenga la misma longitud que el texto
        for i in range(len(texto)):
            clave_extendida += clave[i % len(clave)]
    else:
        clave_extendida = clave[:len(texto)]

    for caracter, clave_caracter in zip(texto, clave_extendida):
        if caracter.isalpha():
            es_mayuscula = caracter.isupper()
            caracter = caracter.lower()
            clave_caracter = clave_caracter.lower()

            # Calcular la posición cifrada
            posicion_cifrado = (alfabeto.index(caracter) + alfabeto.index(clave_caracter)) % m

            # Obtener el caracter cifrado
            caracter_cifrado = alfabeto[posicion_cifrado]

            # Mantener la mayúscula si el caracter original es mayúscula
            if es_mayuscula:
                caracter_cifrado = caracter_cifrado.upper()

            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter

    return texto_cifrado

def descifrar_vigenere(texto, clave):
    m = len(alfabeto)

    # Convertir el texto cifrado y la clave a minúsculas para evitar problemas con mayúsculas
    texto_cifrado = texto.lower()
    clave = clave.lower()

    texto_descifrado = ""
    clave_extendida = ""
    if len(clave) < len(texto):
        # Extender la clave para que tenga la misma longitud que el texto
        for i in range(len(texto)):
            clave_extendida += clave[i % len(clave)]
    else:
        clave_extendida = clave[:len(texto)]

    for caracter_cifrado, clave_caracter in zip(texto_cifrado, clave_extendida):
        if caracter_cifrado.isalpha():
            es_mayuscula = caracter_cifrado.isupper()
            caracter_cifrado = caracter_cifrado.lower()
            clave_caracter = clave_caracter.lower()

            # Calcular la posición descifrada
            posicion_descifrado = (alfabeto.index(caracter_cifrado) - alfabeto.index(clave_caracter)) % m

            # Obtener el caracter descifrado
            caracter_descifrado = alfabeto[posicion_descifrado]

            # Mantener la mayúscula si el caracter cifrado es mayúscula
            if es_mayuscula:
                caracter_descifrado = caracter_descifrado.upper()

            texto_descifrado += caracter_descifrado
        else:
            texto_descifrado += caracter_cifrado

    return texto_descifrado


# Ejemplo de uso:
texto_original = input("Introduce el texto a cifrar: ")
clave = input("Introduce la clave: ")

texto_cifrado = cifrar_vigenere(texto_original, clave)
print("Texto cifrado:", texto_cifrado)



# # Ejemplo de uso:
texto_cifrado = input("Introduce el texto cifrado: ")
clave = input("Introduce la clave: ")

texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)