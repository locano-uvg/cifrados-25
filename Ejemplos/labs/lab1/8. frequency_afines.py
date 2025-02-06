from sympy import mod_inverse

alfabeto = "abcdefghijklmnñopqrstuvwxyz"


def calcular_frecuencia(texto):
    frecuencias = {}
    for caracter in texto:
        if caracter.isalpha():
            caracter = caracter.lower()
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    total_caracteres = sum(frecuencias.values())
    frecuencia_relativa = {
        letra: frecuencia / total_caracteres
        for letra, frecuencia in frecuencias.items()
    }
    return frecuencia_relativa


def ataque_afin(texto_cifrado):
    m = len(alfabeto)

    # Calcular la frecuencia de letras en el texto cifrado
    frecuencias_cifrado = calcular_frecuencia(texto_cifrado)
    letras_ordenadas_cifrado = sorted(
        frecuencias_cifrado, key=frecuencias_cifrado.get, reverse=True
    )

    # Paso 1: Convertir letras a números
    X_f = alfabeto.index("e")   # Letra más común en el texto español
    C_f = alfabeto.index(letras_ordenadas_cifrado[0])  # Letra más común en el texto cifrado

    # Otra suposición: usamos 'a' en claro y su equivalente en cifrado
    X_s = alfabeto.index('a')  # 'a' es la segunda letra más común en español
    C_s = alfabeto.index(letras_ordenadas_cifrado[1])  # Suponemos la primera letra del cifrado

    # Paso 2: Resolver el sistema de ecuaciones para encontrar 'a'
    # Calcular la diferencia entre los valores de X y C
    diff_X = (X_f - X_s) % 27 
    # diff_X = (X_f - X_s) % 27
    diff_C = (C_f - C_s) % 27
    
    # Encontrar el inverso modular de diff_X
    a = (diff_C * mod_inverse(diff_X, 27)) % 27

    # Paso 3: Encontrar 'b'
    b = (C_f - a * X_f) % 27

    # Paso 4: Encontrar el inverso de 'a'
    a_inv = mod_inverse(a, 27)

    # Paso 5: Descifrar el texto
    decrypted_text = ""
    for char in texto_cifrado:
        if char in alfabeto:
            C = alfabeto.index(char)
            X = (a_inv * (C - b)) % 27
            decrypted_text += alfabeto[X]
        else:
            decrypted_text += char  # Mantener caracteres desconocidos (espacios, signos, etc.)

    return decrypted_text
# Ejemplo de uso:
texto_cifrado_afin = input("Ingrese el texto cifrado: ").lower()
test = ataque_afin(texto_cifrado_afin)
print(test)
# ataque_fuerza_bruta_afin2(texto_cifrado_afin)


# # Ejemplo de uso:
# texto_cifrado_afin = "vldi fwhñl"
# ataque_fuerza_bruta_afin(texto_cifrado_afin)
