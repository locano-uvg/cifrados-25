def calcular_frecuencia(texto):
    # Inicializar un diccionario para almacenar las frecuencias
    frecuencias = {}

    # Recorrer cada caracter en el texto cifrado
    for caracter in texto:
        # Verificar si el caracter es una letra
        if caracter.isalpha():
            # Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
            caracter = caracter.lower()

            # Incrementar la frecuencia del caracter en el diccionario
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
        else:
            frecuencias[caracter] = 0

    # Calcular la frecuencia relativa
    total_caracteres = sum(frecuencias.values())
    frecuencia_relativa = {
        letra: frecuencia / total_caracteres
        for letra, frecuencia in frecuencias.items()
    }

    # Tambien pueden hacerlo con un ciclo for
    # frecuencia_relativa = {}
    # for letra, frecuencia in frecuencias.items():
    #     frecuencia_relativa[letra] = frecuencia / total_caracteres


    return frecuencia_relativa

def fuerza_bruta_ceasar(texto):
    frecuencias = calcular_frecuencia(texto)

    # Calcular la frecuencia de las letras en español
    # Obtenemos la letra que mas se repite y con eso podemos asumir que es la letra mas comun por lo cual tomaremos su posición e iniciaremos hacer un
    # desplazamiento de 1 en 1 hasta llegar a la letra z

def fuerza_bruta_afines(texto):
    frecuencias = calcular_frecuencia(texto)

    # Calcular la frecuencia de las letras en español
    # Recordemos que Afines se basa en la formula ax + b mod 27, donde a y b son las claves
    # Donde a debe ser primo de 27
    # por lo tanto a puede ser solamente a: 1,3,5,7,9,15,17,19,21,23,25
    # y b puede ser cualquier numero de 1-27
    
     # Paso 1: Convertir letras a números
    # X_f = alfabeto.index("e")   # Letra más común en el texto español
    # C_f = alfabeto.index(letras_ordenadas_cifrado[0])  # Letra más común en el texto cifrado

    # # Otra suposición: usamos 'a' en claro y su equivalente en cifrado
    # X_s = alfabeto.index('a')  # 'a' es la segunda letra más común en español
    # C_s = alfabeto.index(letras_ordenadas_cifrado[1])  # Suponemos la primera letra del cifrado

    # # Paso 2: Resolver el sistema de ecuaciones para encontrar 'a'
    # # Calcular la diferencia entre los valores de X y C
    # diff_X = (X_f - X_s) % 27 
    # # diff_X = (X_f - X_s) % 27
    # diff_C = (C_f - C_s) % 27
    
    # # Encontrar el inverso modular de diff_X
    # a = (diff_C * mod_inverse(diff_X, 27)) % 27

    # # Paso 3: Encontrar 'b'
    # b = (C_f - a * X_f) % 27

    # # Paso 4: Encontrar el inverso de 'a'
    # a_inv = mod_inverse(a, 27)




def fuerza_bruta_vigenere(texto):
    frecuencias = calcular_frecuencia(texto)

    # Calcular la frecuencia de las letras en español
    # Recordemos que Vigenere se basa en la formula xi = (yi - ki) mod 27, donde xi es la letra cifrada, yi es la letra original y ki es la clave
    # asi que buscamos la letra mas comun y hacemos el desplazamiento de su posición en el alfabeto para encontrar la clave
    


texto = input("Ingrese el texto cifrado: ")
frecuencias = calcular_frecuencia(texto)
print(frecuencias)