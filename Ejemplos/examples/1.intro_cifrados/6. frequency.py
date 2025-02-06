def calcular_frecuencia(texto_cifrado):
    # Inicializar un diccionario para almacenar las frecuencias
    frecuencias = {}

    # Recorrer cada caracter en el texto cifrado
    for caracter in texto_cifrado:
        # Verificar si el caracter es una letra
        if caracter.isalpha():
            # Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
            caracter = caracter.lower()

            # Incrementar la frecuencia del caracter en el diccionario
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    # Calcular la frecuencia relativa
    total_caracteres = sum(frecuencias.values())
    frecuencia_relativa = {letra: frecuencia / total_caracteres for letra, frecuencia in frecuencias.items()}

    return frecuencia_relativa

# Ejemplo de uso:
texto_cifrado = "Gwc uivioml bw nqvl bpm zqopb apqnb"
frecuencias = calcular_frecuencia(texto_cifrado)
print("Frecuencia de letras:", frecuencias)
